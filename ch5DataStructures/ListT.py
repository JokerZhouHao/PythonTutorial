from collections import deque


a = [1, 2, 3, 4, 5]



exit()


#del使用
a = [1, 2, 3, 4, 5]
del a[0]
del a[1:3]
del a[:]
#删除变量a
del a
print(a)



#嵌套使用List Comprehensions
matrix = [
        [1, 2, 3 ,4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
print([[row[i] for row in matrix] for i in range(4)])

#使用List Comprehensions
square = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
[x*2 for x in range(1, 4)]
[(x, x**2) for x in range(1, 4)]
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]
print(square)

#使用lambda表达式
square = list(map(lambda x:x**2, range(10)))
print(square)

#注意下面的i不是临时变量
square = []
for i in range(1, 5):
    square.append(i)
print(square)
print(i)

li = ['1', '2']
li.sort(key=1, reverse=False)
li = ['1', '2'];
li.extend(range(5, 10))
li.remove(5)
deque = deque(["Eric", "John", "Michael"])
deque.popleft()
print(deque)