import requests

'''
The outut of this program is a file with smaller size than that which was compressed. Use Datamuse API
to get a key for every word value, thereby converting it to number. (in this case output will look like
[123, 456, 789, \n]) with spetial notation to compute multi-line text and different capitalisations. 
Words that are not in the datamuse dataset will be saved without any changes, to preserve. Optionally 
encrypt the final output.

Alternatively, each letter can be assigned a value, and then that value can be mathematically manipulated 
(+,-,/,*,
**) to result in a smaller number.

The phrases can be used to train an Afry.

Need to implement json file with a dictionary of keyed words, appended everytime a new word is added (including 
gibberish and names)
'''
url = 'https://api.datamuse.com'

x = 0
data = []
inp = ' '
print('Enter input text, finish with a blank line:')
with open('tmpdir.txt', 'w') as f:
    while inp != '':
        x += 1
        inp = str(input(f'{x}│ '))
        data.append(inp)
    data.pop(-1)
    print(data)
    f.write(str(data))

for i in data:
    print(' '.join(i.split(' ')).split(' '))

    # print(str(i.split(' ')), end='')
    # print(str(i.split(' ')))
    # for j in i:
    #     print(j)

