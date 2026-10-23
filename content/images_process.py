import json,urllib.request,io,os
from PIL import Image
I=json.load(open("img_info.json")); os.makedirs("img/p",exist_ok=True)
for who,i in I.items():
    out=f"img/p/{who.lower().replace(' ','-')}.webp"
    if os.path.exists(out): continue
    im=Image.open(io.BytesIO(urllib.request.urlopen(urllib.request.Request(i["thumb"],headers={"User-Agent":"LexisCards/0.1"}),timeout=60).read())).convert("RGB")
    w,h=im.size; tw=min(w,int(h*3/4)); th=int(tw*4/3)
    top=max(0,min(h-th,int((h-th)*0.25))); im=im.crop(((w-tw)//2,top,(w-tw)//2+tw,top+th)).resize((600,800))
    im.save(out,"WEBP",quality=82); print(out)
