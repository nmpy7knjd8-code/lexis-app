"""Overflow check + screenshots. Usage: python shot_mobile.py W H  (server: python3 -m http.server 8767 in repo root)"""
import sys,os
from playwright.sync_api import sync_playwright
W,H=int(sys.argv[1]),int(sys.argv[2]); O="/workspace/lexis-app/shots/";os.makedirs(O,exist_ok=True)
U="http://localhost:8767/cards/index.html"
HCHK="""[...document.querySelectorAll('.card')].filter(c=>{for(const f of c.querySelectorAll('.face')){const r=f.getBoundingClientRect();for(const e of f.querySelectorAll('*')){if(!e.offsetWidth)continue;const b=e.getBoundingClientRect();if(e.scrollWidth>e.clientWidth+1&&getComputedStyle(e).overflowX!=='hidden'&&!e.matches('img,.art,.art *,.tornwrap,.frame,.cut,.fine,.fine *'))return true;if(!e.closest('.art')&&(b.left<r.left-1||b.right>r.right+1))return true}}return false}).map(c=>c.dataset.id)"""
CHK="""[...document.querySelectorAll('.card')].map(c=>{const b=c.querySelector('.back'),f=c.querySelector('.front');return [c.dataset.id,b.style.overflowY==='auto'?0:b.scrollHeight-b.clientHeight,f.scrollHeight-f.clientHeight]}).filter(x=>x[1]>1||x[2]>1)"""
GLYPH="""document.fonts.load('30px "Gentium Book Plus"','ἀᾄῷὦ').then(f=>f.some(x=>x.unicodeRange.includes('1F00')))"""
SHOTS=os.environ.get("SHOTS")
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome"); pg=b.new_context(viewport={"width":W,"height":H},device_scale_factor=2,is_mobile=True,has_touch=True).new_page()
    pg.goto(U); pg.wait_for_timeout(1800)
    pg.evaluate("openSheet()"); pg.wait_for_timeout(300)
    invis=pg.evaluate("[...document.querySelectorAll('#path button')].filter(b=>{const s=getComputedStyle(b),r=b.getBoundingClientRect();return s.backgroundImage==='none'&&/rgba\\(0, 0, 0, 0\\)|transparent/.test(s.backgroundColor)||r.width<20||r.height<20}).map(b=>'section '+b.dataset.u)")
    print(W,H,"sections",pg.evaluate("document.querySelectorAll('#path button').length"),"invisible_sections",invis)
    pg.evaluate("document.getElementById('sheet').hidden=true")
    bad=[];tot=0;hbad=[];clamped=[]
    for u in range(1,pg.evaluate("UNITS.length")+1):
        pg.evaluate(f"setSec({u})"); pg.wait_for_timeout(300)
        tot+=pg.evaluate("document.querySelectorAll('.card').length"); bad+=pg.evaluate(CHK); hbad+=pg.evaluate(HCHK)
        clamped+=pg.evaluate("[...document.querySelectorAll('.ctx.clamp')].map(x=>x.closest('.card').dataset.id)")
    print(W,H,"cards",tot,"overflow",bad,"HORIZ",hbad,"clamped",len(clamped),"no_button",pg.evaluate("[...document.querySelectorAll('.ctx.clamp')].filter(c=>c.parentElement.querySelector('.more').hidden).length"),"pageScroll",pg.evaluate("document.documentElement.scrollHeight"),H,"polytonic font loaded",pg.evaluate(GLYPH))
    if SHOTS:
        for cid in SHOTS.split(","):
            sec=pg.evaluate(f"unitOf(CARDS.find(c=>c.id==='{cid}'))"); pg.evaluate(f"setSec({sec})"); pg.wait_for_timeout(300)
            i=pg.evaluate(f"VIS().findIndex(c=>c.id==='{cid}')")
            pg.evaluate(f"document.getElementById('card-{i}').scrollIntoView({{inline:'center'}})"); pg.wait_for_timeout(600)
            pg.screenshot(path=O+f"{W}x{H}-front-{cid}.png"); pg.evaluate(f"document.getElementById('card-{i}').click()"); pg.wait_for_timeout(180)
            pg.screenshot(path=O+f"{W}x{H}-midflip-{cid}.png"); pg.wait_for_timeout(700)
            pg.screenshot(path=O+f"{W}x{H}-back-{cid}.png")
        pg.click("#logo"); pg.wait_for_timeout(400); pg.screenshot(path=O+f"{W}x{H}-sections.png")
    b.close()
