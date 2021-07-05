"""
1.	Write a Python Program to Display Fibonacci Sequence Using Recursion?
2.	Write a Python Program to Find Factorial of Number Using Recursion?
3.	Write a Python Program to calculate your Body Mass Index?
4.	Write a Python Program to calculate the natural logarithm of any number?
5.	Write a Python Program for cube sum of first n natural numbers?
"""
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
    def question(self,h,w):
        bmi = 
if __name__ == "__main__":
    a6 = basicprogram6()
    print("Question 1: ")
    for i in a6.question1(10):
        print(i)
    print("Question 2:", a6.question2(5))