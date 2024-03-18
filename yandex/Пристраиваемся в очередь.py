queue = []
for i in range(int(input())):
    string = input()
    if 'встал' in string:
        queue.append(string[:string.index('встал') - 1])
    elif 'будет за тобой.' in string:
        queue.insert(queue.index((string[7:string.index('!')]).strip()) + 1,
                     (string[string.find('! ') + 2:string.index('будет за тобой.')]).strip())
    else:
        del queue[queue.index(string[:string.index(', ')])]
for i in queue:
    print(i)
