a1=float(input())
a2=float(input())
a3=float(input())
tot=float(input())
p1=a1/(a1+a2+a3)
p2=a2/(a1+a2+a3)
p3=a3/(a1+a2+a3)
v1=p1*tot
v2=p2*tot
v3=p3*tot
print(f'{v1:.2f}')
print(f'{v2:.2f}')
print(f'{v3:.2f}')