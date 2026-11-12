#!/usr/bin/env node
'use strict';
// Supplemental pixel evidence from the unmodified, exact GitHub host.
// This does not replace the canonical structural collector or human review.
const fs = require('node:fs');
const path = require('node:path');
const cp = require('node:child_process');
const crypto = require('node:crypto');
const collector = require('./capture_hosted_math.cjs');
const sha256 = value => crypto.createHash('sha256').update(value).digest('hex');
const TARGETS = {
  'science/capacity.md': [{kind:'label', text:'(C1)', name:'C1'}],
  'science/weighted-kernel.md': [{kind:'label', text:'(W2)', name:'W2'}],
  'science/operational-advantage.md': [{kind:'label', text:'(O2)', name:'O2'}],
  'science/robustness.md': [{kind:'label', text:'(R12)', name:'R12'}],
  'learning/milestones.md': [{kind:'heading', text:'M02.', name:'M02'}],
};

function parseArgs(argv) {
  const args = {};
  for (let i=0; i<argv.length; i+=2) {
    const key = argv[i];
    if (!['--root','--repository','--revision','--inventory','--output'].includes(key) || !argv[i+1])
      throw new Error('Unknown option or missing value: '+key);
    if (Object.hasOwn(args,key.slice(2))) throw new Error('Duplicate option: '+key);
    args[key.slice(2)] = argv[i+1];
  }
  for (const key of ['root','repository','revision','inventory','output'])
    if (!args[key]) throw new Error('Missing --'+key);
  // Reuse the canonical path/repository/revision validation without changing it.
  collector.argumentsFor(['--root',args.root,'--repository',args.repository,
    '--revision',args.revision,'--output',args.output]);
  return args;
}

function validateInventory(args) {
  const bytes = fs.readFileSync(args.inventory);
  const inventory = JSON.parse(bytes);
  const pinned = collector.pinnedPages({...args,pages:[]});
  if (inventory.schema_version!==1 || inventory.repository!==args.repository ||
      inventory.revision!==args.revision || inventory.renderer_profile!=='github' ||
      JSON.stringify(inventory.pages?.map(p=>p.path))!==JSON.stringify(pinned.pages))
    throw new Error('Inventory does not match the complete exact-source page set');
  for (const item of inventory.pages) {
    const source = cp.execFileSync('git',['--no-replace-objects','show',args.revision+':'+item.path],
      {cwd:args.root,maxBuffer:32*1024*1024});
    const url = 'https://github.com/'+args.repository+'/blob/'+args.revision+'/'+
      item.path.split('/').map(encodeURIComponent).join('/');
    if (sha256(source)!==item.source_sha256 || source.toString('utf8')!==item.source_text ||
        item.url!==url || !Array.isArray(item.expressions))
      throw new Error('Source/URL/hash mismatch: '+item.path);
    for (const target of TARGETS[item.path] || []) {
      if (!item.source_text.includes(target.text)) throw new Error('Target absent from source: '+target.name);
    }
  }
  return {inventory,tree:pinned.tree,inventory_sha256:sha256(bytes)};
}

// Executed in the real page. It only reads DOM geometry and visible text.
function targetGeometry(root, target) {
  const clean = value => value.replace(/\s+/g,' ').trim();
  const blockFor = el => el.closest('.markdown-heading') || el;
  const elements = [];
  if (target.kind==='label') {
    const labels = [...root.querySelectorAll('p')].filter(p=>clean(p.textContent)===target.text);
    if (labels.length!==1) throw new Error('Expected one exact label '+target.text+'; found '+labels.length);
    const label = labels[0];
    let hosts = [...root.querySelectorAll('math-renderer')];
    if (!hosts.length) hosts = [...root.querySelectorAll('math')]
      .filter(el=>!el.parentElement?.closest('math,annotation,annotation-xml'));
    const math = hosts.find(el=>label.compareDocumentPosition(el)&Node.DOCUMENT_POSITION_FOLLOWING);
    if (!math) throw new Error('No rendered math following '+target.text);
    elements.push({role:'label',el:label},{role:'following_math',el:math});
  } else {
    const headings = [...root.querySelectorAll('h1,h2,h3,h4,h5,h6')];
    const matches = target.kind==='lead' ? headings.slice(0,1) :
      headings.filter(el=>clean(el.textContent).startsWith(target.text));
    if (matches.length!==1) throw new Error('Expected one heading for '+target.name);
    const heading = matches[0];
    elements.push({role:'heading',el:heading});
    let sibling = blockFor(heading).nextElementSibling;
    const count = target.kind==='lead' ? 1 : 2;
    for (let i=0; sibling && i<count; i++,sibling=sibling.nextElementSibling) {
      if (sibling.matches('h1,h2,h3,h4,h5,h6,.markdown-heading')) break;
      elements.push({role:target.kind==='lead'?'navigation_or_lead':'following_content',el:sibling});
    }
  }
  const components = elements.map(({role,el})=>{
    let box = el.getBoundingClientRect();
    if (!box.width || !box.height) {
      const nested = el.querySelector('math');
      if (nested) box = nested.getBoundingClientRect();
    }
    if (!box.width || !box.height) throw new Error('Unmeasurable target component: '+role);
    const viewport = {x:box.x,y:box.y,width:box.width,height:box.height};
    const outside = box.left < -1 || box.right > innerWidth+1 || box.top < 0 || box.bottom > innerHeight;
    const obscured = [];
    if (!outside) {
      for (const x of [box.left+2,(box.left+box.right)/2,box.right-2]) {
        for (const y of [box.top+2,(box.top+box.bottom)/2,box.bottom-2]) {
          const top = document.elementFromPoint(x,y);
          if (!top || !(top===root || root.contains(top)))
            obscured.push({x,y,top_element:top?.tagName || null,top_class:top?.className || null});
        }
      }
    }
    return {role,text:clean(el.textContent),viewport,
      document:{...viewport,x:box.x+scrollX,y:box.y+scrollY},outside_viewport:outside,obscured_points:obscured};
  });
  const left = Math.min(...components.map(c=>c.viewport.x));
  const top = Math.min(...components.map(c=>c.viewport.y));
  const right = Math.max(...components.map(c=>c.viewport.x+c.viewport.width));
  const bottom = Math.max(...components.map(c=>c.viewport.y+c.viewport.height));
  return {name:target.name,kind:target.kind,components,
    bounding_box:{x:left,y:top,width:right-left,height:bottom-top},
    document_top:top+scrollY,scroll:{x:scrollX,y:scrollY},
    wholly_visible:components.every(c=>!c.outside_viewport && !c.obscured_points.length)};
}

async function scrollAndSettle(page, top) {
  await page.evaluate(async requested=>{
    window.scrollTo({left:0,top:Math.max(0,requested),behavior:'instant'});
    await new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)));
    await new Promise(resolve=>setTimeout(resolve,150));
  },top);
}

async function positionTarget(page, article, target) {
  let detail;
  // Native scrolling only: no style injection, element hiding or reconstruction.
  for (const safeTop of [240,340,140]) {
    detail = await article.evaluate(targetGeometry,target);
    await scrollAndSettle(page,detail.document_top-safeTop);
    detail = await article.evaluate(targetGeometry,target);
    if (detail.wholly_visible) return detail;
  }
  throw new Error('Target remains clipped or obscured: '+target.name+' '+JSON.stringify(detail));
}

async function saveShot(page, article, target, source, viewport, prefix, output, positioned) {
  const before = positioned ? await positionTarget(page,article,target) :
    await article.evaluate(targetGeometry,target);
  const filename = prefix+'-'+(positioned?target.name:'top')+'.png';
  await page.screenshot({path:path.join(output,filename),fullPage:false,timeout:30000});
  const after = await article.evaluate(targetGeometry,target);
  if (positioned && (!after.wholly_visible || Math.abs(before.scroll.y-after.scroll.y)>1 ||
      Math.abs(before.bounding_box.y-after.bounding_box.y)>1))
    throw new Error('Target moved or became obscured during screenshot: '+target.name);
  return {path:source.path,url:page.url(),source_sha256:source.source_sha256,viewport,
    target:positioned?target.name:'top',observed_at:new Date().toISOString(),
    screenshot:{path:filename,sha256:sha256(fs.readFileSync(path.join(output,filename)))},
    target_geometry_before:before,target_geometry_after:after,
    full_page:false,dom_or_css_modified:false,human_visual_review_required:true};
}

async function run(args) {
  const output = path.resolve(args.output);
  if (fs.existsSync(output) && (fs.lstatSync(output).isSymbolicLink() ||
      !fs.statSync(output).isDirectory() || fs.readdirSync(output).length))
    throw new Error('Use a new empty output directory; preserve prior evidence');
  const verified = validateInventory(args);
  fs.mkdirSync(output,{recursive:true});
  const report = {schema_version:1,kind:'hosted_visual_supplements',repository:args.repository,
    revision:args.revision,head:args.revision,tree:verified.tree,
    inventory_sha256:verified.inventory_sha256,script_sha256:sha256(fs.readFileSync(__filename)),
    canonical_collector_sha256:sha256(fs.readFileSync(path.join(__dirname,'capture_hosted_math.cjs'))),
    capture_method:'playwright-github-viewport',started_at:new Date().toISOString(),
    required_pages:verified.inventory.pages.map(p=>p.path),screenshots:[],failures:[],
    limits:'Unmodified actual-host viewport screenshots supplement the canonical structural report. Geometry and sampled occlusion checks do not establish pixel correctness; human source/display inspection is required.'};
  const reportPath = path.join(output,'visual-supplements.json');
  const save = ()=>fs.writeFileSync(reportPath,JSON.stringify(report,null,2)+'\n');
  const {chromium} = require('playwright');
  let browser;
  try {
    browser = await chromium.launch({headless:true});
    report.runtime = {node:process.version,playwright:require('playwright/package.json').version,browser:browser.version()};
    for (const viewport of collector.VIEWPORTS) {
      const context = await browser.newContext({viewport,deviceScaleFactor:1,colorScheme:'light'});
      try {
        for (const [index,source] of verified.inventory.pages.entries()) {
          const page = await context.newPage();
          const prefix = String(index+1).padStart(4,'0')+'-'+viewport.width;
          try {
            const response = await page.goto(source.url,{waitUntil:'domcontentloaded',timeout:60000});
            if (response?.status()!==200) throw new Error('HTTP '+response?.status());
            if (page.url()!==source.url) throw new Error('Browser redirected away from exact pinned source URL');
            const article = page.locator('article.markdown-body').first();
            await article.waitFor({state:'visible',timeout:30000});
            // Warm native lazy math exactly as the collector does, then await readiness.
            await page.evaluate(async()=>{
              for (let y=0,steps=0;y<document.body.scrollHeight && steps<200;y+=900,steps++) {
                window.scrollTo({left:0,top:y,behavior:'instant'});
                await new Promise(resolve=>setTimeout(resolve,50));
              }
            });
            await collector.waitForHostedMath(article,source.expressions.length);
            // Crucially reset after readiness, and capture viewports rather than full-page composites.
            await scrollAndSettle(page,0);
            const lead = {kind:'lead',name:'title-navigation'};
            report.screenshots.push(await saveShot(page,article,lead,source,viewport,prefix,output,false));
            report.screenshots.push(await saveShot(page,article,lead,source,viewport,prefix,output,true));
            for (const target of TARGETS[source.path] || [])
              report.screenshots.push(await saveShot(page,article,target,source,viewport,prefix,output,true));
            save();
          } catch (error) {
            report.failures.push({path:source.path,viewport,observed_at:new Date().toISOString(),
              category:collector.classifyFailure(error),reason:String(error)});
            save();
            throw error;
          } finally {await page.close();}
        }
      } finally {await context.close();}
    }
  } catch (error) {
    if (!report.failures.length) report.failures.push({category:collector.classifyFailure(error),reason:String(error)});
  } finally {
    if (browser) await browser.close();
    report.finished_at = new Date().toISOString();
    report.status = report.failures.length?'incomplete':'captured';
    report.human_visual_review_required = true;
    save();
  }
  console.log(JSON.stringify({status:report.status,report:reportPath,screenshots:report.screenshots.length,failures:report.failures.length}));
  return report.failures.length?1:0;
}

module.exports = {parseArgs,validateInventory,targetGeometry,positionTarget,run,TARGETS};
if (require.main===module) {
  run(parseArgs(process.argv.slice(2))).then(code=>{process.exitCode=code;})
    .catch(error=>{console.error(String(error));process.exitCode=2;});
}
