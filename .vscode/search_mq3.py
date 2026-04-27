import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = 'c:/Users/loany/Documents/annysaadi.github.io/annysaadi.github.io/training.css'
try:
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    in_media = False
    count = 0
    for line in lines:
        if '@media' in line:
            in_media = True
            print(line, end='')
            count = 1
        elif in_media:
            print(line, end='')
            if '{' in line:
                count += 1
            if '}' in line:
                count -= 1
            if count == 0:
                in_media = False
                print('---')
except Exception as e:
    print('Erro ao ler CSS:', e)
