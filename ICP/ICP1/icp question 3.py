str = input("Enter a string")
d=l=0
for c in str:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
print("Letters", l)
print("Digits", d)
