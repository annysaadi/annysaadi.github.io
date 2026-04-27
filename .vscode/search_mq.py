import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = 'c:/Users/loany/Documents/annysaadi.github.io/annysaadi.github.io/training.css'
try:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        import re
        matches = re.findall(r'@media[^{]*\{[^\}]*\.hero-content[^{]*\{[^}]*\}[^\}]*\}', content)
        for m in matches:
            print(m)
        
        print("--- Mobile hero styles:")
        lines = content.split('\n')
        in_media = False
        for line in lines:
            if '@media' in line and 'max-width' in line:
                in_media = True
                print(line)
            elif in_media and line.startswith('    }'):
                in_media = False
                print(line)
            elif in_media and ('.hero' in line or 'font-size' in line or 'padding' in line or 'margin' in line):
                print(line)
except Exception as e:
    print('Erro ao ler CSS:', e)
