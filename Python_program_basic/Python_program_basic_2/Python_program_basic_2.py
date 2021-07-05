import calendar
import cmath
class programbasic2:
    def question1(self,km):
        mile = km/1.609
        return mile
    def question2(self,celcius):
        fahrenhiet = (celcius * (9/5)) + 32
        return fahrenhiet
    def question3(self,year):
        return calendar.calendar(year)
    def question4(self,a,b,c):
        d = b**2 - 4*a*c
        val = cmath.sqrt(d)
        sol1 = (-b+val)/(2*a)
        sol2 = (-b-val)/(2*a)
        return sol1, sol2
    def question5(self,a,b):
        return b,a
    def __str__(self):
        return """
                1.	Write a Python program to convert kilometers to miles?
                2.	Write a Python program to convert Celsius to Fahrenheit?
                3.	Write a Python program to display calendar?
                4.	Write a Python program to solve quadratic equation?
                5.	Write a Python program to swap two variables without temp variable?
                """
if __name__ == "__main__":
    a2 = programbasic1()
    print("Question 1:", a2.question1(1))
    print("Question 2 : ", a2.question2(35))
    print("Question 3 : ", a2.question3(2020))
    sol1,sol2 = a2.question4(1,4,5)
    print("Question 4 : ", sol1,sol2)
    a,b = a2.question5(1,2)
    print("Question 5 : a = {} , b = {}".format(a,b))
