a = {'..-.': 'F', '-..-': 'X',
     '.--.': 'P', '-': 'T', '..---': '2',
     '....-': '4', '-----': '0', '--...': '7',
     '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
     '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
     '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
     '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
     '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
     '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}
a = {value: key for key, value in a.items()}
b = input().upper().split()
for i in b:
    count = 0
    for j in i:
        if count + 1 == len(i):
            print(a[j])
        else:
            print(a[j], end=' ')
        count += 1
