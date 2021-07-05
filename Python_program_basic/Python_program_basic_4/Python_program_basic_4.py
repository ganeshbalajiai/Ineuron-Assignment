class programbasic4:
    def question1(self,n):
        if n>=1:
            def fact(n):
                if n == 1:
                    return n
                else:
                    return n*fact(n-1)
        return fact(n)
    def question2(self,n):
        for i in range(1,11):
            yield "{} * {} = {}".format(i,n,i*n)
    def question3(self,n):
        a = 1
        b = 2
        if n == 1:
            yield n
        elif n == 2:
            yield "{} , {}".format(a,b)
        else:
            for i in range(2,n+1):
                yield a
                a,b = b,a+b  
    def question4(self,n):
        val = 0
        for i in str(n):
            val = val + int(i)**len(str(n))
        if val == n:
            return "Armstrong"
        else:
            return "None"
        
    def question5(self,a,b):
        for n in range(a,b):
            vals = programbasic4().question4(n)
            if vals == "Armstrong":
                yield n
            else:
                pass
    def question6(self,n):
        return (n*(n+1))/2
    def __str__(self):
        return """
                1.	Write a Python Program to Find the Factorial of a Number?
                2.	Write a Python Program to Display the multiplication Table?
                3.	Write a Python Program to Print the Fibonacci sequence?
                4.	Write a Python Program to Check Armstrong Number?
                5.	Write a Python Program to Find Armstrong Number in an Interval?
                6.	Write a Python Program to Find the Sum of Natural Numbers?
                """

if __name__ == "__main__":
    a4 = programbasic4()
    print("Question 1:", a4.question1(5))
    table = a4.question2(5)
    print("Question 2:")
    for i in table:
        print(i)
    fibo = a4.question3(10)
    print("Question 3:")
    for i in fibo:
        print(i)
    armstrong = a4.question4(153)
    print("Question 4 :", armstrong)
    armstrong_val = a4.question5(1,1000)
    print("Question 5 :")
    for i in armstrong_val:
        print(i)
    print("Question 6 :", a4.question6(9))
    
    
