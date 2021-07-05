"""
1.	Write a Python Program to Display Fibonacci Sequence Using Recursion?
2.	Write a Python Program to Find Factorial of Number Using Recursion?
3.	Write a Python Program to calculate your Body Mass Index?
4.	Write a Python Program to calculate the natural logarithm of any number?
5.	Write a Python Program for cube sum of first n natural numbers?
"""
from math import *
class basicprogram6:
    def question1(self,n):
        def fibo(n):
            if n <= 1:
                return 1
            else:
                return fibo(n-1) + fibo(n - 2)
        for i in range(n):
            yield fibo(i)
    def question2(self,n):
        def fact(n):
            if n == 1:
                return n
            else:
                return n*fact(n-1)
        return fact(n)
    def question3(self,h,w):
        bmi = w/(h*h)
        return bmi
    def question4(self,n):
        return log10(n)
    def question5(self,n):
        return (n*(n+1)/2)**2
if __name__ == "__main__":
    a6 = basicprogram6()
    print("Question 1: ")
    for i in a6.question1(10):
        print(i)
    print("Question 2:", a6.question2(5))
    print("Question 3:", a6.question3(1.8,72))
    print("Question 4:", a6.question4(8))
    print("Question 5:", a6.question5(10))
