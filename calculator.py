lst = input().split()
if len(lst) > 3:
    raise ValueError("Too many values to unpack")
if lst[1] in ("+", "-", "*", "/"):
    sign = lst[1]
else:
    raise ValueError("Invalid operation")
try:
    a, b = int(lst[0]), int(lst[2])
except ValueError:
    raise ValueError("Invalid literal for int()")
if 1 <= a <= 10 and 1 <= b <= 10:
    match sign:
        case "+":
            print(a + b)
        case "-":
            print(a - b)
        case "*":
            print(a * b)
        case "/":
            print(a // b)
else:
    raise ValueError("Invalid a or b for value [1, 10]")
