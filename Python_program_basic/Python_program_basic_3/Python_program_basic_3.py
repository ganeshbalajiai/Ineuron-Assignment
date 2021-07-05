class programbasic3:
    def question1(self,n):
        if type(n) == int:
            if n == 0:
                return "Number is zero"
            elif n > 0:
                return "Number is positive"
            else:
                return "Number is negative"
        else:
            return "Enter the integer to check"
    def question2(self,n):
        if type(n) == int:
            if n == 0:
                return "Number is zero"
            else:
                if n%2==0:
                    return "Number is even"
                else:
                    return "Number is odd"
        else:
            return "Enter the integer to check"
    def question3(self,n):
        if n%400 == 0:
            return "I am a leap year"
        elif n%100 == 0:
            return "I am not a leap year"
        elif n%4 == 0:
            return "I am a leap year"
        else:
            return "Not a leap year"
    def question4(self,n):
        if n>=1:
            if n == 1:
                return "prime"
            else:
                for i in range(2,int(n//2)+1):
                    if n%i == 0:
                        return "Not prime"
                else:
                    return "prime"
        else:
            return "Enter the valid number"
    def question5(self):
        l = []
        for i in range(1,10000):
            val = programbasic3().question4(i)
            if val == "prime":
                l.append(i)
        return l
    def __str__(self):
        return """
            1.	Write a Python Program to Check if a Number is Positive, Negative or Zero?
            2.	Write a Python Program to Check if a Number is Odd or Even?
            3.	Write a Python Program to Check Leap Year?
            4.	Write a Python Program to Check Prime Number?
            5.	Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
            """
if __name__ == "__main__":
    a3 = programbasic3()
    print("Question 1 :", a3.question1(4))
    print("Question 2 :", a3.question2(9))
    l = list(range(2000,2021))
    for i in l:
        print("Question 3 : {}".format(i), a3.question3(i))
    print("Question 4 : ", a3.question4(8))
    print("Question 5 : \n", a3.question5())