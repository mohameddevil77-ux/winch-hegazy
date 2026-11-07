import os
import re

with open(r'D:\winch-hegazy\index.html', 'r', encoding='utf-8') as f:
    c = f.read()

video_sources = re.findall(r'<source\s+src=[\"\'](.*?)[\"\']', c)
video_posters = re.findall(r'poster=[\"\'](.*?)[\"\']', c)

print('Video sources found:', video_sources)
for v in video_sources:
    p = os.path.join(r'D:\winch-hegazy', v.replace('/', os.sep))
    print(v, 'exists:', os.path.exists(p), 'size:', os.path.getsize(p) if os.path.exists(p) else 0)

print('Video posters found:', video_posters)
for poster in video_posters:
    p = os.path.join(r'D:\winch-hegazy', poster.replace('/', os.sep))
    print(poster, 'exists:', os.path.exists(p), 'size:', os.path.getsize(p) if os.path.exists(p) else 0)

print('Has VideoObject schema:', 'VideoObject' in c)
