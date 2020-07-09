l = []
for i in range(1, 11):
    if i > 5:
        l.append(i ** 2)
print(l)
l2 = [i ** 2 for i in range(1, 11) if i > 5]
print(l2)
print('-----------------------------')

l = [str(i) + j for i in range (1, 6) for j in 'ABCDE']
print(l)
print('-----------------')

mydic = {'key1':'value1', 'key2':'value2'}
mylist = [key + ':' + value for key, value in mydic.items()]
print(mylist)
print('-----------------')

mydic = {i: i * i for i in (5, 6, 7)}
mydic2 = {value: key for key, value in mydic.items()}
print(mydic2)
print('-----------------')

myset = {i for i in 'HelloWorld' if i not in 'lo'}
print(myset)
print('-----------------')

mygenerator = {i for i in range(0, 11)}
print(mygenerator)
print(list(mygenerator))