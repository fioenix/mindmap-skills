// Offline source/state regression; does not emulate browser rendering or CSP.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync('skills/markmap/assets/template.html', 'utf8');
assert.match(source, /<html[^>]*data-theme="light"/, 'Default must be light even when OS is dark');
assert.doesNotMatch(source, /prefers-color-scheme/, 'Host and OS theme can disagree');
assert.match(source, /html \.markmap,\s*html\.markmap-dark \.markmap\s*\{[^}]*--markmap-text-color:\s*var\(--mm-fg\)/);
assert.match(source, /html \.mm-toolbar[^{]*\{[^}]*background[^:]*:\s*var\(--mm-panel\)/);
assert.match(source, /html \.mm-toolbar (?:a|button|svg)[^{]*\{[^}]*color:\s*var\(--mm-fg\)/);
assert.match(source, /toolbar\.setItems\(\["zoomIn", "zoomOut", "fit", "recurse"\]\)/, 'Library dark toggle must not bypass the theme state');
assert.match(source, /html \.mm-toolbar \.mm-toolbar-brand > span[^}]*color:\s*var\(--mm-fg\)/, "Brand span must override library gray");
const css = source.match(/<style>([\s\S]*?)<\/style>/)[1];
function palette(selector) {
  const block = css.slice(css.indexOf(selector)).match(/\{([^}]+)\}/)[1];
  return Object.fromEntries([...block.matchAll(/(--mm-[\w-]+):\s*(#[\da-f]{6})/g)].map(m => [m[1], m[2]]));
}
function luminance(hex) {
  const rgb = hex.slice(1).match(/../g).map(s => parseInt(s,16)/255).map(c => c <= .04045 ? c/12.92 : ((c+.055)/1.055)**2.4);
  return rgb[0]*.2126 + rgb[1]*.7152 + rgb[2]*.0722;
}
for (const selector of [':root', 'html.markmap-dark']) {
  const p = palette(selector);
  for (const surface of ['--mm-bg','--mm-panel','--mm-hover']) {
    const [hi,lo] = [luminance(p['--mm-fg']),luminance(p[surface])].sort((a,b)=>b-a);
    assert.ok((hi+.05)/(lo+.05) >= 4.5, `${selector} ${surface} contrast`);
  }
}
const script = source.match(/<script id="theme-controller">([\s\S]*?)<\/script>/)[1];
for (const initial of ['light','dark','invalid']) {
  const classes = new Set(); const attrs = {}; let click;
  const html = {dataset:{theme:initial},classList:{toggle:(k,v)=>v?classes.add(k):classes.delete(k)}};
  const button = {setAttribute:(k,v)=>attrs[k]=v,addEventListener:(event,fn)=>{assert.equal(event,'click');click=fn;}};
  vm.runInNewContext(script,{document:{documentElement:html,getElementById:id=>{assert.equal(id,'theme-toggle');return button;}}});
  const expected = initial === 'dark' ? 'dark' : 'light';
  for (let n=0;n<3;n++) {
    const dark = n%2 === 0 ? expected === 'dark' : expected !== 'dark';
    assert.equal(html.dataset.theme,dark?'dark':'light');
    assert.equal(classes.has('markmap-dark'),dark);
    assert.equal(attrs['aria-pressed'],String(dark));
    click();
  }
}
console.log('PASS: light default, dark state/toggle, label and toolbar CSS, >=4.5 text contrast (offline only)');
