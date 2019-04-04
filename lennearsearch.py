a=int(input('enter the no of trips.....'))
ice_prince={}
amount=[]
for i in range(a):
    aa=int(input('enter the no of ice cream avaliable in trip %d .......'%(i+1)))
    price=int(input('enter the amount that you have...'))
    amount.append(price)
    d=[]
    for j in range(aa):
        m=int(input('enter the price of ice cream %d '%(j+1)))
        d.append(m)
    else:
        ice_prince[i]=d[:]
for i in range(a):
    bs=ice_prince[i]
    best={}
    for ii in range(len(bs)):
        for j in range(len(bs)):
            if ii==j:
                continue
            if bs[ii]+bs[j]<=amount[i]:
                best[(bs[ii],bs[j])]=bs[ii]+bs[j]
    print(max(best))

                




