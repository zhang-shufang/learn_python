- [5 if 语句](#5-if-语句)
  - [5.1 条件测试](#51-条件测试)
  - [5.2 if 语句](#52-if-语句)
# 5 if 语句
if 语句将通过检查条件语句，以选定执行对应的逻辑。
## 5.1 条件测试
- `==、!=`：用于判断两个值是否相等/不相等。
- `<、>=、<=、>`：用于数值间的大小比较。
- `and、or、not`关键字：用于布尔运算，分别表示和/或/非。
- `in`关键字：用于检查特定值是否在集合中。
- `not in`关键字：用于检查特定值是否 **不** 在集合中。

演示代码：
```python
condition1 = (100 == 100)               # True
condition2 = (100 != 100)               # False
condition3 = (100 < 200)                # True
condition4 = (100 >= 200)               # False
condition5 = ('a' in ['a'])             # True
condition6 = ('a' not in ['a'])         # False
condition7 = condition1 or condition2   # True
condition8 = condition1 and condition2  # False
```

## 5.2 if 语句
依次检查每个条件测试，选择执行首个为真或 `else` 中的子块代码。
- `elif`：可有零个或多个，当 `if` 的条件为假时，依次检查处理。
- `else`：可有零个或一个，处理 `if` 和 `elif` 的条件均为假的情况。

演示代码：
```python
age, vip = 12, False
if 0 <= age < 4 and vip:
    ticket_price = 0
elif age < 18:
    ticket_price = 25
elif age < 65:
    ticket_price = 40
else:
    ticket_price = 20
print(f"Ticket price is {ticket_price}.")

# 运行结果
Ticket price is 25.
```