import re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = 'c:/Users/loany/Documents/annysaadi.github.io/annysaadi.github.io/training.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove o emoji intenso
content = content.replace('⚠️ Atenção:', 'Atenção:')

# Suaviza as cores dos indicadores
content = content.replace('background: var(--red-500);', 'background: var(--ink-3);')
content = content.replace('background: #10b981;', 'background: var(--line-2);')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Ajustes finais aplicados com sucesso.')
