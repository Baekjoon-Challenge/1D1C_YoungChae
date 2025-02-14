from sys import stdin

text = stdin.readline().strip()
for i in range(ord('a'), ord('z')+1):
    print(text.find(chr(i)), end=' ')