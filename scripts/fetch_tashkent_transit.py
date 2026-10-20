#!/usr/bin/env python3
"""Fetches Tashkent metro and bus routes from OpenStreetMap (Overpass) and writes data/tashkent-transit-raw.json.
Run on a GitHub runner (open internet). The compiled app data is built by scripts/build_transit.py."""
import requests, json, sys, time
BBOX = "41.15,69.05,41.45,69.45"
EPS = ["https://overpass-api.de/api/interpreter", "https://overpass.kumi.systems/api/interpreter", "https://overpass.private.coffee/api/interpreter"]
Q = {
 "metro": '[out:json][timeout:180];(rel["route"="subway"](%s);)->.r;(.r;node(r:"stop");node(r:"stop_entry_only");node(r:"stop_exit_only");node(r:"platform"););out body;' % BBOX,
 "bus": '[out:json][timeout:240];(rel["route"~"^(bus|trolleybus|share_taxi)$"](%s);)->.r;.r out body;(node(r.r:"stop");node(r.r:"stop_entry_only");node(r.r:"stop_exit_only");node(r.r:"platform");node(r.r:"platform_entry_only");node(r.r:"platform_exit_only"););out body;' % BBOX,
 "stations": '[out:json][timeout:120];(node["station"="subway"](%s);node["railway"="station"]["subway"="yes"](%s);node["railway"="subway_entrance"](%s););out body;' % (BBOX, BBOX, BBOX),
}
out = {}
for k, q in Q.items():
    for ep in EPS:
        try:
            r = requests.post(ep, data={"data": q}, timeout=300, headers={"User-Agent": "mreric16-lounge-transit/1.0"})
            if r.status_code == 200:
                out[k] = r.json().get("elements", []); print(k, ep, len(out[k])); break
            print(k, ep, r.status_code, r.text[:150])
        except Exception as e:
            print(k, ep, "ERR", str(e)[:120])
        time.sleep(5)
    else:
        print("FAILED", k); sys.exit(1)
json.dump(out, open("data/tashkent-transit-raw.json", "w", encoding="utf8"), ensure_ascii=False, separators=(",", ":"))
