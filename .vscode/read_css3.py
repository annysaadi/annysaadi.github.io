import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = 'c:/Users/loany/Documents/annysaadi.github.io/annysaadi.github.io/training.css'
try:
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[200:300]:
            print(line, end='')
except Exception as e:
    print('Erro ao ler CSS:', e)
