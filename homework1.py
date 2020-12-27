print("Enter 5 values")
values=[]
types=[]
for i in range(5):
    a=input("Enter value: ")
    try:
        x=type(int(a))
    except:
        x=type(a)
    values.append(a)
    types.append(x)

for i in range(5):
    print("The Value: {}".format(values[i]), end="\t")
    print(f"Value's Type: {types[i]}", end="\n")