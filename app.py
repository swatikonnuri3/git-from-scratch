import math
def main():
    for i in range(5):
        print("swati")
    return
def make(a,b):
    return a+b
def squre(num):
    print(num**2)
    
main()
print(make(3,5))
squre(4)
print(int(math.sqrt(5)))
list=["swati","konnuri","python"]
print(list[0:3])
print(list[1][0])
list.append("hey")
list.remove("python")
print(list)
dict={0:1,1:2,2:4}
print(dict[0])
f=open("collaboration","r")
data=f.read()
print(type(data))