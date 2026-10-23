#!/usr/bin/env python3
"""Validate content/*-cards.json: schema, unique ids, unique terms, NFC, image files exist, quotes carry citations; write cards/manifest.json."""
import json,os,glob,subprocess,sys,unicodedata as U,re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import jsonschema;V=jsonschema.Draft202012Validator(json.load(open("card-schema.json")))
bad=0;ids=set();terms={};n=0
norm=lambda t:re.sub(r'[^\w]','',''.join(c for c in U.normalize('NFD',t.lower()) if not U.combining(c)))
for f in sorted(glob.glob("content/*-cards.json")):
    for c in json.load(open(f)):
        n+=1;e=[x.message[:100] for x in V.iter_errors(c)]
        if c["id"] in ids: e.append("duplicate id")
        k=norm(c["greek"])
        if k in terms: e.append("duplicate term of "+terms[k])
        ids.add(c["id"]);terms[k]=c["id"]
        for fld in ("greek","translit","context"):
            if U.normalize("NFC",c.get(fld,""))!=c.get(fld,""): e.append(fld+" not NFC")
        if c.get("quote") and not (c["source"]["work"] and c["source"]["citation"] and c.get("attribution_confidence")=="verified"): e.append("quote without citation")
        if not c.get("quote") and c.get("attribution_confidence"): e.append("badge without quote")
        if "constructed" in json.dumps(c): e.append("constructed")
        if c["lang"] in ("grc","zh","sa","ar") and not c.get("translit"): e.append("non-Latin script needs translit")
        if not os.path.exists("content/"+c["image"]["src"]): e.append("missing image")
        if e: bad+=1;print(f"  {f}:{c['id']}: {e}")
print(f"schema+lint: {n-bad}/{n} cards valid")
files=subprocess.run(["git","ls-files","-co","--exclude-standard","cards","content"],capture_output=True,text=True).stdout.split()
json.dump(sorted(p for p in files if p.lower().endswith((".webp",".png",".jpg",".svg"))),open("cards/manifest.json","w"),indent=0)
sys.exit(1 if bad and "--strict" in sys.argv else 0)
