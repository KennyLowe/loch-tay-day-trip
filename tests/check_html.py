from html.parser import HTMLParser
from pathlib import Path
import os; os.chdir(Path(__file__).resolve().parent.parent)
class Check(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=set(); self.anchors=[]; self.stack=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, 'duplicate ID'
            self.ids.add(a['id'])
        if tag not in {'meta','link','br','input','img','hr'}: self.stack.append(tag)
        for key in ('src','href'):
            value=a.get(key,'')
            if value.startswith('#') and len(value)>1: self.anchors.append(value[1:])
            elif value and not value.startswith(('https:','#')): assert Path(value).is_file(),value
        if a.get('target')=='_blank': assert 'noopener' in a.get('rel',''), 'unsafe external link'
    def handle_endtag(self,tag):
        assert self.stack and self.stack[-1]==tag,(tag,self.stack[-3:])
        self.stack.pop()
p=Check();p.feed(Path('index.html').read_text());assert not p.stack,p.stack
assert all(a in p.ids for a in p.anchors)
assert Path('.nojekyll').exists()
print('PASS: HTML nesting, IDs, anchors, relative assets and external-link safety')
