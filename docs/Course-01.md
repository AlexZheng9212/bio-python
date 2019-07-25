# Course-01: Basic Data Struction & Algorithm
## Agenda
### Basice Data Struction
* String
* List
* Dictionary
* Tuple
* File
* Int, float...
* Boolean

### Algorithm
* leetcode 001: Two Sum

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
stringD = stringA - 'xyz'❌
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
* etc split(), join(), format() 比较简单就不一一展开
