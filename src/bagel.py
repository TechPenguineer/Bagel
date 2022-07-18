import os

cwd = os.getcwd()
with open(cwd + '/__tests__/webpage.bagl', 'r') as f:
    print(f.read())