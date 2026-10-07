import re, json, requests, concurrent.futures as cf
H={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36","Accept-Language":"en-US,en;q=0.9","Cookie":"CONSENT=YES+1"}
rows=json.load(open("scripts/video_candidates.json"))
def pr(html):
    m=re.search(r"ytInitialPlayerResponse\s*=\s*(\{.*?\});\s*(?:var |</script>)",html,re.S)
    if not m: return None
    try: return json.loads(m.group(1))
    except Exception: return None
def one(r):
    v=r["id"]; o=dict(r)
    try:
        oe=requests.get("https://www.youtube.com/oembed",params={"url":f"https://www.youtube.com/watch?v={v}","format":"json"},headers=H,timeout=20)
        o["oembed"]=oe.status_code
        if oe.status_code==200:
            j=oe.json(); o["real_title"]=j.get("title"); o["channel"]=j.get("author_name")
    except Exception as e: o["oembed"]=type(e).__name__
    CL=[("ANDROID_VR",{"clientName":"ANDROID_VR","clientVersion":"1.57.29","deviceMake":"Oculus","deviceModel":"Quest 3","androidSdkVersion":32,"osName":"Android","osVersion":"12L","hl":"en"},"com.google.android.apps.youtube.vr.oculus/1.57.29 (Linux; U; Android 12L; eureka-user Build/SQ3A.220605.009.A1) gzip"),
        ("WEB_EMBEDDED_PLAYER",{"clientName":"WEB_EMBEDDED_PLAYER","clientVersion":"1.20240723.01.00","hl":"en"},H["User-Agent"]),
        ("IOS",{"clientName":"IOS","clientVersion":"19.45.4","deviceMake":"Apple","deviceModel":"iPhone16,2","osName":"iPhone","osVersion":"18.1.0.22B83","hl":"en"},"com.google.ios.youtube/19.45.4 (iPhone16,2; U; CPU iOS 18_1_0 like Mac OS X;)")]
    o["ib_tried"]=[]
    for nm,cl,ua in CL:
        try:
            ib=requests.post("https://www.youtube.com/youtubei/v1/player?prettyPrint=false",json={"videoId":v,"context":{"client":cl,"thirdParty":{"embedUrl":"https://mreric16.github.io/"}},"contentCheckOk":True,"racyCheckOk":True},headers={"User-Agent":ua,"Content-Type":"application/json","Accept-Language":"en"},timeout=25)
            j=ib.json(); vd=j.get("videoDetails",{}); pl=j.get("playabilityStatus",{})
            o["ib_tried"].append(nm+":"+str(pl.get("status")))
            if pl.get("status")=="OK" and vd:
                o["ib_status"]="OK"; o["ib_client"]=nm
                o["secs"]=int(vd.get("lengthSeconds",0) or 0); o["views"]=int(vd.get("viewCount",0) or 0); o["channel"]=vd.get("author") or o.get("channel"); o["live"]=vd.get("isLiveContent")
                mf=j.get("microformat",{}).get("playerMicroformatRenderer",{})
                o["pub"]=(mf.get("publishDate") or "")[:10]; o["cat"]=mf.get("category"); o["embed_ok"]=mf.get("embed") is not None
                break
            else: o["ib_status"]=pl.get("status"); o["ib_reason"]=(pl.get("reason") or "")[:60]
        except Exception as e: o["ib_tried"].append(nm+":"+type(e).__name__)
    try:
        w=requests.get(f"https://www.youtube.com/watch?v={v}",headers=H,timeout=25)
        p=pr(w.text)
        if p:
            vd=p.get("videoDetails",{}); pl=p.get("playabilityStatus",{})
            o["playable"]=pl.get("status"); o["reason"]=(pl.get("reason") or "")[:80]
            o["secs"]=int(vd.get("lengthSeconds",0) or 0); o["views"]=int(vd.get("viewCount",0) or 0)
            o["live"]=vd.get("isLiveContent"); o["channel"]=vd.get("author") or o.get("channel"); o["real_title"]=vd.get("title") or o.get("real_title")
            mf=p.get("microformat",{}).get("playerMicroformatRenderer",{})
            o["embed"]=mf.get("isUnlisted") is not True and mf.get("embed") is not None
            o["safe"]=mf.get("isFamilySafe"); o["cat"]=mf.get("category"); o["pub"]=(mf.get("publishDate") or "")[:10]
            o["lang_hint"]=mf.get("defaultAudioLanguage") if False else None
        else: o["playable"]="NOPARSE"
    except Exception as e: o["playable"]=type(e).__name__
    return o
with cf.ThreadPoolExecutor(10) as ex: out=list(ex.map(one,rows))
json.dump(out,open("scripts/video-audit.json","w"),indent=1)
from collections import Counter
print(Counter(o.get("ib_status") for o in out), Counter(o.get("playable") for o in out), Counter(o.get("oembed") for o in out))
