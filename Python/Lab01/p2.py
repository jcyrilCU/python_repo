try:
    x = 50
    y = "Run"
    z = int(x + y)
    print(z)
except TypeError as e:
    print(f"TypeError occurred ")

try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print(f"IndexError occurred ")

try:
    print(abc)
except NameError as e:
    print(f"NameError occurred ")
       
try:
    my_dict = {"key": "value"}
    print(my_dict["nonexistent_key"])
except KeyError as e:
    print(f"KeyError occurred ")


try:
    x = 5
    print(x.length)
except AttributeError as e:
    print(f"AttributeError occurred ")


try:
    result = 50 / 0
    print(result)
except ZeroDivisionError as e:
    print(f"ZeroDivisionError occurred ")

try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
        print(content)
except IOError as e:
    print(f"IOError occurred ")

try:
    import nonexistent_module
except ImportError as e:
    print(f"ImportError occurred ")
