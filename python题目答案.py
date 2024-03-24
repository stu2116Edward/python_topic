# 期中卷，两个都无法输出
# range(开始，结束，步长)
for i in range(9,2):
    print(i)
for j in range(2,9,-2):
    print(j)


# 求1-100的阶乘
def jiecheng():
    chengji = 1
    for i in range(1,101):
        chengji *= i
    print(chengji)
if __name__ == '__main__':
    jiecheng()


# 第一题(列表内所有数字乘积的最后一个非零数字的奇偶性)
L = [1,7,7]
sum_L = 1
for i in L:
    sum_L *= i
suoyin = int(len(str(sum_L)) - 1)
new_sumL = []
for j in str(sum_L):
    new_sumL.append(j)
while new_sumL[suoyin] == '0':
    suoyin -= 1
# print(new_sumL[suoyin])
last_num = int(new_sumL[suoyin])
if last_num % 2 == 0:
    print('偶数输出0')
else:
    print('奇数输出1')


# 第二题
x = int(input("x="))
y = int(input("y="))
z = int(input("z="))
L = [x,y,z]
max_1 = max(L)
L.remove(max_1)
min_1 = min(L)
L.remove(min_1)
center = L[0]
print(min_1,center,max_1)


# 第三题
a = int(input('a='))
b = int(input('b='))
# 求公约数
def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
result1 = find_divisors(a)
result2 = find_divisors(b)
temp_L = []
for i in result1:
    if i in result2:
        temp_L.append(i)
print('公约数的个数为:',len(temp_L))


# 第四题
def fourth():
    a = input('请输入回文字符串:')
    n = int(input('请输入回文字符串的长度：'))
    new_a = a[::-1]
    if n != len(a):
        print('请输入正确的回文字符串个数!')
    else:
        if a == new_a:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    fourth()


# 第五题
# 方法1
def fifth(n):
    for i in range(1,n+1):
        temp = 1
        count = 0
        for j in range(1,i+1):
            temp *= j
            count += temp
    print(count)

if __name__ == '__main__':
    fifth(20)

# 方法2
def jiechen(n):
    temp = 1
    for i in range(1,n+1):
        temp *= i
    return temp
count = 0

n = int(input('n(1!+~n!)='))
for i in range(1,n+1):
    count += jiechen(i)
print(count)


# 方法3
import math
result = sum(math.factorial(i) for i in range(1, 21))
print("1! + 2! + 3! + ... + 20! 的和为:", result)


# 第六题
# 计算斐波那契数列的前20项
# 2/1 3/2 5/3 8/5 13/8
# 方法一
def fibonacci_sequence_sum(n):
    a, b = 2, 1
    total_sum = a / b
    for _ in range(2, n + 1):
        a, b = a + b, a
        total_sum += a / b
    return total_sum

result = fibonacci_sequence_sum(20)
print(result)

# 方法二
a, b = 2, 1
fenshu = a / b
# a, b = a + b, a需要执行19次
for i in range(1,20):
    a, b = a + b, a
    fenshu += a / b
print(fenshu) 


# 第七题(九九乘法表)
for i in range(1,10):
    for j in range(1,i+1):
        print(str(j) + '*' + str(i) + "=" + str(i*j),end='  ')
    print('')


# 第八题
num_1 = input("num=")
L = []
for i in num_1:
    # isdigit()如果字符串只包含数字则返回 True 否则返回 False
    if i.isdigit():
        L.append(int(i))
    else:
        continue
print(sum(L))


# 第九题
num_s = '1234'
L = []
for i in num_s:
    L.append((int(i) + 5) % 10)
new_L = [L[3],L[2],L[1],L[0]]
print(new_L)


# 第十题(列表全排列)
# 方法一
# 使用itertools.permutations函数获取全排列
import itertools
my_list = [1, 2, 3]
permutations = list(itertools.permutations(my_list))
new_L = []
for perm in permutations:
    new_L.append(list(perm))
print(new_L)


# 方法二
# enumerate用于获取列表的索引和值
# for i,ch in enumerate(nums):
#     print('索引',i,'值',ch)

nums = [1,2,3]
def pailie(arr):
    if len(arr) <= 1:
        return [arr]
    else:
        res = []
        for i,ch in enumerate(arr):
            for j in pailie(arr[:i] + arr[i+1:]): 
                res.append([ch] + j)
        return res
    
if __name__ == '__main__':
    print(pailie(nums))
