string="hello"
num=2

print("String is: ",string)
print("Num is",num)

tuples=[1,2,3]
print(tuples)
print("Last value of tuple: ",tuples[2])

# num = input("Enter a number: ")
num = int(input("Enter a number: "))
print(num)
num=num+5
print("new num: ",num," ,num+5: ",num+5)

array=[]
for i in range(5):
    array.append(int(input()))
print(array)