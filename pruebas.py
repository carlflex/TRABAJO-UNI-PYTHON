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

ar=[1,2,3,4,5,6,7,8,9,10,11,12]
c1=0
c2=1
c3=2
for i in range(4):
    print("+-"*4+"+")
    print(f"|{ar[c1]}||{ar[c2]}||{ar[c3]}|")

    if i <5:
        c1+=3
        c2+=3
        c3+=3
print("+-"*4+"+")
        