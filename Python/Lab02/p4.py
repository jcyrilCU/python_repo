import math

class Check:
    def __init__(self, number):
        self.number = number

    def isPrime(self):
        if self.number < 2:
            return False
        for i in range(2, int(math.sqrt(self.number)) + 1):
            if self.number % i == 0:
                return False
        return True
num = int(input("Enter a number: "))
checker = Check(num)

boolVal = checker.isPrime()
print(boolVal)
