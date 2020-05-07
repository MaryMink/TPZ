class Formuls():
    def __init__(self, x):
        self.x = x
        
        
    def formul_1(self):
        y = self.x ** 4 * 3.75 + self.x ** 3 * 2.272 - self.x ** 2 * 5.351 + self.x * 4.653
        return y
    
    def formul_2(self):
        y = self.x ** 3 * 3.37 - self.x ** 2 * 3.336 + self.x * 5.42
        return y
    
    def formul_3(self):
        y = self.x ** 2 * 1.441 + self.x * 2.465
        return y

    def formul_4(self):
        y = self.x * 6.364
        return y
        

class NonPositiveError(Exception):
    pass
class WrongRangeX(Exception):
    pass
if __name__ == '__main__':
    
    try:
        x = float(input("Input a number:"))
        F = Formuls(x)
        
        if x <= 0:
            raise NonPositiveError('x should be positive')
        elif x >= 2.409 and x <= 57.59:
            raise WrongRangeX('Wrong range x')
        print(" formul 1:",F.formul_1(),"\n","formul 2:",F.formul_2(),"\n","formul 3:",F.formul_3(),"\n","formul 4:",F.formul_4())
    except ValueError:
        print ("Incorrect entry")
    
    #print(F.formul_1(), F.formul_2(), F.formul_3(), F.formul_4())
