r = 1
while r <= 10:
    c = 1
    while c <= 10:
        ans = r*c
        print (ans)
        c += 1
        print()
        r += 1
def mult_table(num):
    print("multiplication table is:")
    for i in range(1,11):
        result=num*i
        print(f"{num}*{i}={result}")
    
