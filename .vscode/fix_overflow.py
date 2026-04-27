import re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = 'c:/Users/loany/Documents/annysaadi.github.io/annysaadi.github.io/training.css'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Ajuste do line-height do hero-title
content = re.sub(r'(\.hero-title\s*\{[^}]*line-height:\s*)1\.05', r'\g<1>1.2', content)

# Ajuste do hero-title em margin
content = re.sub(r'(\.hero-title\s*em\s*\{[^}]*margin-top:\s*)4px', r'\g<1>8px', content)

# Garantir que a max-width da hero-meta-item--wide não cause overflow
content = re.sub(r'(\.hero-meta-item--wide\s*\{[^}]*max-width:\s*)320px', r'\g<1>100%', content)

# Esconder o hero-scroll em telas menores onde ele poderia sobrepor o texto meta
if '.hero-scroll {' in content:
    # Adicionando um media query para esconder o scroll na versão mobile
    media_hide_scroll = "\n    @media (max-width: 768px) {\n      .hero-scroll {\n        display: none !important;\n      }\n    }\n"
    content += media_hide_scroll

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Ajustes de sobreposição e espaçamento de texto aplicados no CSS.')
