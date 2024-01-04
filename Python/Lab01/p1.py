class Calc:
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
   
    def operate(self):
        pass

    def sum(self):
        print("The total sum: ", self._v1 + self._v2)
   
    def multiply(self):
        print("The Product of the two numbers: ", self._v1 * self._v2)
       
    def subtract(self):
        print("The value after subtraction: ", self._v1 - self._v2)
       
    def divide(self):
        if self._v2 != 0:
            print("The value after division is: ", self._v1 / self._v2)
        else:
            print("Error: Division by zero")

class AdvancedCalc(Calc):
    def operate(self):
        print(f"The result of {self._v1} raised to the power of {self._v2}: {self._v1 ** self._v2}")

x = float(input("Enter 1st value: "))
y = float(input("Enter 2nd value: "))
op = input("Enter an operator: ")

obj = Calc(x, y)
obj_advanced = AdvancedCalc(x, y)

if op == '+':
    obj.sum()
elif op == '-':
    obj.subtract()
elif op == '*':
    obj.multiply()
elif op == '/':
    obj.divide()
else:
    print("Error Occurred, try again")

obj.operate()
obj_advanced.operate()
