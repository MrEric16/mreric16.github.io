"""Shared HSK helpers: loads the complete-HSK list (drkameleon/complete-hsk-vocabulary, MIT; definitions from CC-CEDICT, CC BY-SA 4.0)
and maps words to levels. Level bands: a = HSK 2.0 levels 1-2 (A1-A2), b = 3-4 (B1-B2), c = 5-6 and beyond."""
import json, os, re, urllib.request

SRC = '/tmp/hsk.json'
URL = 'https://raw.githubusercontent.com/drkameleon/complete-hsk-vocabulary/main/complete.json'


def load():
    if not os.path.exists(SRC):
        urllib.request.urlretrieve(URL, SRC)
    return json.load(open(SRC, encoding='utf-8'))


def levels_of(e):
    old = new = None
    for t in e['level']:
        k, n = t.split('-')
        if k == 'old':
            old = int(n)
        elif k == 'new':
            new = int(n)
    return old, new


def band_of(old, new):
    if old is not None:
        return 'a' if old <= 2 else 'b' if old <= 4 else 'c'
    if new is not None:
        return 'a' if new <= 1 else 'b' if new <= 4 else 'c'
    return None


def index():
    d = load()
    W = {}
    for e in d:
        old, new = levels_of(e)
        W[e['simplified']] = {'old': old, 'new': new, 'band': band_of(old, new), 'freq': e.get('frequency') or 10**9, 'e': e}
    return W
