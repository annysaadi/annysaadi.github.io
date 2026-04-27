import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = 'c:/Users/loany/Documents/annysaadi.github.io/annysaadi.github.io/training.css'
try:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        import re
        matches = re.findall(r'@media\s*\(max-width:\s*900px\)\s*\{([^}]*(?:\{[^}]*\}[^}]*)*)\}', content)
        for m in matches:
            print(m)
            print("---")
except Exception as e:
    print('Erro ao ler CSS:', e)
