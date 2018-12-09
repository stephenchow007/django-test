'''
array = [1,4,6,8,3]

for j in range(0,len(array)-1):
    for i in range(0,len(array)-1-j):
        if array[i]>array[i+1]:
            array[i],array[i+1] = array[i+1],array[i]

print(array)


num = int(input("请输入一个数字："))
a = 1

if num < 0:
    print("抱歉，负数没有阶乘！")
elif num == 0:
    print("0的阶乘等于1")
else:
    for i in range(1,num+1):
        a = a*i
    print("%d 的阶乘为 %d" %(num,a))
'''

def A(n):
    if n <= 1:
        return n
    else:
        return (A(n-1) + A(n-2))

x = int(input("请输入一个数字"))

if x <= 0:
    print("请输入正数")
else:
    print("斐波那契数列：")
    for i in range(x):
        print(A(i))

























