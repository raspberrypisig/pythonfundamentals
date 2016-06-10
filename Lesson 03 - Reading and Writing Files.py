#The old-school way
f = open('test.txt','r')
for line in f.readlines():
    print(line)
f.close()

#The hipster's way (Pythonic)
with open('test.txt') as fp:
    for line in fp:
        print(line)

