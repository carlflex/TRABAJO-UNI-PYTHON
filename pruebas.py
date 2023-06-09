c1=23
c2=377
c3=45

ar=[
    [1,2,3],
    [2]
]



print(ar[0][0])

def ar_index(ar,e,largo):
    for i in range(largo):
        if ar[i]== e:
            return i
    return None

def ar_orden(ar,largo):

    for i in range(1,largo):
        print(i)
        for j in range(largo-i):
            print('h',j)
            if ar[j]>ar[j+1]:
                temp=ar[j]
                ar[j]=ar[j+1]
                ar[j+1]=temp
    return ar

ar_c=[c1,c2,c3]
ar_n=["CONTADOR 1","CONTADOR 2","CONTADOR 3"]

ar_copy=ar_c.copy()
ar_copy=ar_orden(ar_copy,3)

""" print(ar_n[ar_c.index(ar_copy[0])]) """

print(ar_n[ar_index(ar_c,ar_copy[-1],3)])