import subprocess as s

x = input('Vrei crearea fisierului Excel?')
x = int(x)
if x == 1:
    s.call('feature_extraction.py', shell=True)
s.call('modelling.py', shell=True)
