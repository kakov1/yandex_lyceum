from sys import stdin

print(*sorted(list(map(str.strip, stdin)),
              key=lambda x: (sum([ord(x[i].upper()) - ord('A') + 1 for i in range(len(x))]), x)),
      sep='\n')
