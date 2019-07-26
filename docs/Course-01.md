# Course-01: Basic Data Struction & Algorithm
## Agenda
### Basice Data Struction
* String
* List
* Dictionary
* Tuple
* Int, float...
* Boolean

### Algorithm Test
* [leetcode 001: Two Sum](https://leetcode-cn.com/problems/two-sum/)

## Start
* BeforeAll `python3.X`的变量原则上是`不需指定类型`的。在开发过程中为了`代码可读性`可以适当为函数变量及返回值加上类型。

### String(字符串)
#### Basic Define
* Python 不区分单双引号

```
stringA = 'Abcde'
stringB = "School"
```
* String的索引
```
first_alpha = stringA[0]
last_alpha_0 = stringA[4]
last_alpha_1 = stringA[-1]

# 遍历stringA
for alpha in stringA:
    print(alpha)

for idx in range(len(stringA))：
    print('No.%s alpha is %s' % (idx, stringA[idx]))
```
* String的`替代与不可替代`
```
stringA[0] = 'xyz' ❌
# following anz which one will print 'xyzbcde'? Or Both?
stringA.replace(string[0], 'xyz')
print(stringA)
stringA = stringA.replace(string[0], 'xyz')
print(stringA)
```
* String的拼接
```
stringC = stringA + stringB
stringD = stringA - 'xyz' ❌
```
* String的subStr
```
No.2-4
subStr = stringA[1:5]
No.2-4
subStr = stringA[1:-1]
No.2-5
subStr = stringA[1:]
```

* iteration and iterator
```
strIter = iter(stringA)
next(strIter)
```
* etc split(), join(), format() 比较简单就不一一展开


### List(列表)
#### Basic Define
* List & numpy.array
```
# list中的元素类型可以随意组合，numpy.array()在不指定dtype时亦可随意组合，否则只能添加`指定类型元素`
list_a = [1,2,3,4,5]
list_b = [1,'23','xixi',2,45]
list_c = list([1,2,3])
array_b = np.array(list_b, dtype=int, ndmin=2) # error 'xixi' is not int()
```
* Mult-List & Mult-Array & Mult-Matrix (shape & reshape)

```
list_d = [[1,2,3],[4,5,6],[7,8,9]]
array_d = np.array(list_d)
matrix_d = np.matrix(list_d)

print(list_d.shape) ❌
print(array_d.shape) # (3,3)
print(matrix.shape) # (3,3)

array_d.shape = (1,9)
matrix_d.shape = (2,4) ❌

matrix_d.reshape(3,3)
matrix_d = matrix_d.reshape(3,3)
```

* iteration and iterator
```
for item in list:
for item in array:
```

* list append() and extend()
```
some different between append() and extend()
base_list = [12,11,10]
add_a = 1
add_b = [2,3]
base_list.append(add_a)
base_list.append(add_b)
base_list.extend(add_a)
base_list.extend(add_b)
```
* list remove() and clear()
* list insert() pop() count() reserve() sort() copy()

### Dictionary & Tuple
#### Basic Define
* Dictionary
```
字典是带索引<key,value>的数据结构，在结构内key具有唯一性。如果含有多个同名key时，以最后一个<k,v>为准。
也可以理解为Map映射
dict_a = {"name": "fat cat", "age":12, "name":"cai xixi"}
dict_a["name"] = "fat cat"
dict_a.get("name")
pop() -- remove
clear() and delete()

dict_b = dict(food="bread",drink:"cola")

元组
tuple_a = ("c", 12, [1,2,3])
print(tuple_a)
```

### Two Sum
#### Hint
* how do you use one loop to finish this issuse?
* what responsibility can you find between target and elements of list?