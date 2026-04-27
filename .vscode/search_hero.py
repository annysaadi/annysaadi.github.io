import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = 'c:/Users/loany/Documents/annysaadi.github.io/annysaadi.github.io/training.css'
try:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        import re
        matches = re.findall(r'\.hero[^{]*\{[^}]*\}', content)
        for m in matches:
            if '100' in m or 'min-height' in m:
                print(m)
        print("---")
        matches = re.findall(r'@media[^{]*\{[^\}]*\.hero[^{]*\{[^}]*\}[^\}]*\}', content) # simplistic regex for media queries, better to just print lines
        lines = content.split('\n')
        for i, line in enumerate(lines):
             if '@media' in line:
                  for j in range(i, min(len(lines), i+30)):
                       if '.hero' in lines[j] and 'padding' in lines[j]:
                            print(lines[i], lines[j])
except Exception as e:
    print('Erro ao ler CSS:', e)
