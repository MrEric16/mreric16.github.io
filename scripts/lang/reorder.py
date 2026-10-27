import re, sys
def reorder(path, order):
    s = open(path, encoding='utf-8').read()
    i = s.index('[grammar]'); head = s[:i]; g = s[i + len('[grammar]\n'):]
    parts = re.split(r'(?m)^(?=## )', g)
    blocks = {re.match(r'## (.+)', p).group(1).strip(): p if p.endswith('\n') else p + '\n' for p in parts if p.strip()}
    assert set(blocks) == set(order), (set(blocks) ^ set(order))
    open(path, 'w', encoding='utf-8').write(head + '[grammar]\n' + ''.join(blocks[h] for h in order))
if __name__ == '__main__':
    reorder(sys.argv[1], sys.argv[2].split(';'))
