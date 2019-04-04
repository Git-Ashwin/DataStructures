n=int(input('enter the number of elements.....'))
ls=[int(input('enter the %d elements..'%i)) for i in range(n)]
ls.sort()
key=int(input('enter the element to search......'))
b=len(ls)//2
while len(ls):
    if key == ls[b-1]:
        print('found')
        break
    elif key<ls[b]:
        ls=ls[:b]
    else:
        ls=ls[b+1:]
    b=b//2
else:
    print('Not found')