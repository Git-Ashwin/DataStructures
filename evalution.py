from postfix import *
m=stack()
a=input('enter the expression......')
for i in a:
    if i not in ['+','/','*','-']:
        if not i.isalpha():
           m.push(int(i))
        else:
            v=int(input('enter the value for %s.....'%i))
            m.push(v)
    else:
        f2=m.pop()
        f1=m.pop()
        if i=='+':
            m.push(f1+f2)
        elif i=='/':
            m.push(f1/f2)
        elif i=='*':
            m.push(f1*f2)
        elif i=='-':
            m.push(f1-f2)
print(m.ls)