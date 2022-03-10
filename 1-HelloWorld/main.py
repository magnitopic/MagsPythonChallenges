# method 1
print("Hola mundo")
# method 2
print('Hola mundo')
# method 3
print('Hola '+'mundo')
# method 4
print('Hola','mundo')
# method 5
print('{} {}'.format('Hola','mundo'))
# method 6
a="odnum aloH"
b=a[::-1]
print(b)
# method 7
str="odnum aloH"
print(''.join(reversed(str)))
# method 8
def main():
    print("Hola mundo")
main()
# method 9
from termcolor import colored
print(colored('Hola', 'red'), colored('mundo', 'green'))
# method 10
while True: print('Hola mundo'); break
# method 11
a='Hola'
b='Mundo'
print(f'{a} {b}')
# method 12
alguien='Mundo'
print(f'Hola {alguien}')
# method 12
print('\u0048\u006f\u006c\u0061\u0020\u006d\u0075\u006e\u0064\u006f')
# method 13
l=[111, 100, 110, 117, 77, 32, 97, 108, 111, 72]
while l:
    print(chr(l[-1]),end='')
    l.pop()
print()
