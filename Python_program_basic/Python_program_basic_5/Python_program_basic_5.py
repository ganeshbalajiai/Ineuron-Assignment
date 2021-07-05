class programbasic5:
    def question1(self,a,b):
        if a!=b:
            if a>b:
                greater = a
            else:
                greater = b
            while(True):
                if (greater%a == 0) and (greater%b == 0):
                    lcm = greater
                    break
                greater += 1
            return lcm
    def question2(self,a,b):
        while(b):
            a,b = b,a%b
        return a
    def question3(self,a):
        def to_binary(a):
            return bin(a)
        def to_octal(a):
            return oct(a)
        def to_hexadecimal(a):
            return hex(a)
        return to_binary(a), to_octal(a), to_hexadecimal(a)
    def question4(self,a):
        return ord(a)
    def question5(self,a,b):
        def add(a,b):
            return a+b
        def sub(a,b):
            return a-b
        def mul(a,b):
            return a*b
        def div(a,b):
            return a/b
        return add(a,b), sub(a,b), mul(a,b), div(a,b)
    def __str__(self):
        return """
                1.	Write a Python Program to Find LCM?
                2.	Write a Python Program to Find HCF?
                3.	Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
                4.	Write a Python Program To Find ASCII value of a character?
                5.	Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
                """

if __name__ == "__main__":
    a5 = programbasic5()
    print("Question 1 :", a5.question1(120,250))
    print("Question 2 :", a5.question2(44,234))
    bin,oct,hex = a5.question3(10)
    print("Question 3 : bin {}, oct {}, hex {}".format(bin,oct,hex) )
    print("Question 4 : ", a5.question4("a"))
    add,sub,mul,div = a5.question5(2,4)
    print("Question 5 : ", add,sub,mul,div)