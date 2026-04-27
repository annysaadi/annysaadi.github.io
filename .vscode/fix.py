import re
path = 'c:/Users/loany/Documents/annysaadi.github.io/annysaadi.github.io/training.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<div class=\"hero-bg-noise\"></div>\s*', '', content)
content = re.sub(r'<div class=\"hero-bg-grid\"></div>\s*', '', content)
content = re.sub(r'<div class=\"hero-bg-glow\"></div>\s*', '', content)
content = re.sub(r'<div class=\"hero-bg-glow-2\"></div>\s*', '', content)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Design simplificado com sucesso.')
