- [7 用户输入和 while 循环](#7-用户输入和-while-循环)
  - [7.1 用户输入](#71-用户输入)
  - [7.2 字符串转换其他类型](#72-字符串转换其他类型)
  - [7.3 while 循环](#73-while-循环)

# 7 用户输入和 while 循环
## 7.1 用户输入
演示代码：
```python
name = input("Please enter your name:")
print(f"\nHello, {name})

# 运行结果
Please enter your name: Zhangshufang
Hello, Zhangshufang!
```

## 7.2 字符串转换其他类型
- `int(string)`：将字符串转换为整数值。
- `float(string)`：将字符串转换为浮点数（小数）值。

演示代码：
```python
age = input("How old are you?")
age = int(age)
print(type(age), type(int (age)))
pi = float(input("What's the value of pi?"))
```

## 7.3 while 循环
不断运行 while 语句块中的代码，直到给定的条件为假。
- `break` 关键字：退出整个循环语句块的执行。
- `continue` 关键字：跳过当前循环中余下代码的执行。
- 以上两个中断在 `for` 循环中也可以使用。

演示代码：
```python
current_number = 0
while True:
    current_number +=1
    if current_number > 5:
        break
    if current_number % 2 == 0:
        continue
    print(current_number)

# 运行结果
1
3
5
```
**注意**：
1. `for` 循环是一种遍历列表的有效方式，但一般不在 `for` 循环中修改列表，否则将导致 Python 难以跟踪其中的元素。
2. 要在遍历列表的同时修改它，通常使用 `while` 循环。（采用何种遍历方法？）