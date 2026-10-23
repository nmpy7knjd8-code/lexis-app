import json,sys,urllib.request,urllib.parse,re,os,io
UA={"User-Agent":"LexisCards/0.1 (educational; garrett)"}
def get(u):
    return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=40))
OVR=json.load(open("img_override.json")) if os.path.exists("img_override.json") else {}
def pick(who,art):
    if who in OVR: return "File:"+OVR[who]
    d=get("https://en.wikipedia.org/w/api.php?action=query&format=json&prop=pageimages&piprop=name&redirects=1&titles="+urllib.parse.quote(art))
    p=list(d["query"]["pages"].values())[0]; return "File:"+p.get("pageimage","")
def info(f):
    d=get("https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url|extmetadata&iiurlwidth=900&titles="+urllib.parse.quote(f))
    p=list(d["query"]["pages"].values())[0]
    if "imageinfo" not in p: return None
    ii=p["imageinfo"][0];m=ii["extmetadata"];g=lambda k:re.sub(r"<[^>]+>","",m.get(k,{}).get("value","")).strip()
    return dict(file=f,thumb=ii["thumburl"],page=ii["descriptionurl"],lic=g("LicenseShortName"),licurl=g("LicenseUrl"),artist=g("Artist")[:80],desc=g("ImageDescription")[:150])
if __name__=="__main__":
    arts=json.load(open("thinkers.json")); out={}
    for who,art in arts.items():
        f=pick(who,art); i=info(f) if f!="File:" else None; out[who]=i
        print(who,"|",i and (i["file"],i["lic"],i["artist"][:40]))
    json.dump(out,open("img_info.json","w"),ensure_ascii=False,indent=1)
