import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = 'c:/Users/loany/Documents/annysaadi.github.io/annysaadi.github.io/training.css'
try:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        import re
        matches = re.findall(r'\.hero-(actions|pills|pill-item|meta|meta-item|meta-divider)[^{]*\{[^}]*\}', content)
        for m in matches:
            # find full block
            pass
        
        # simpler way: just print lines containing these classes and next few lines
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if any(cls in line for cls in ['.hero-actions', '.hero-pills', '.hero-meta']):
                for j in range(max(0, i-1), min(len(lines), i+15)):
                    print(lines[j])
                print("---")
except Exception as e:
    print('Erro ao ler CSS:', e)
