

class basicassignment_15:
    def question_1(self):
        seconds_per_minute = 60
        minutes_per_hour = 60
        return seconds_per_minute*minutes_per_hour
    def question_2(self):
        seconds_per_hour = basicassignment_15().question_1()
        return seconds_per_hour
    def question_3(self):
        seconds_per_hour = basicassignment_15().question_2()
        return 24*seconds_per_hour
    def question_4(self):
        seconds_per_day = basicassignment_15().question_3()
        return seconds_per_day
    def question_5(self):
        float_div = basicassignment_15().question_4()/basicassignment_15().question_2()
        return "floating point division is {}".format(float_div)
    def question_6(self):
        int_div = basicassignment_15().question_4()//basicassignment_15().question_2()
        return "Integer point division is {}".format(int_div)
    def question_7(self,n):
        if n>=2:
            for i in range(1,n):
                for j in range(2,int(i//2+1)):
                    if i%j == 0:
                        break
                else:
                    yield i
        else:
            return "Enter the valid number"

    def __str__(self):
        return "\
        1.How many seconds are in an hour? Use the interactive interpreter as a calculator and multiply the number of seconds in a minute (60) by the number of minutes in an hour (also 60).\
        2. Assign the result from the previous task (seconds in an hour) to a variable called seconds_per_hour.\
        3. How many seconds do you think there are in a day? Make use of the variables seconds per hour and minutes per hour.\
        4. Calculate seconds per day again, but this time save the result in a variable called seconds_per_day\
        5. Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.\
        6. Divide seconds_per_day by seconds_per_hour, using integer (//) division. Did this number agree with the floating-point value from the previous question, aside from the final .0?\
        7. Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ..."


if __name__ == "__main__":
    a15 = basicassignment_15()
    print("First question:", a15.question_1())
    print("Second question:", a15.question_2())
    print("Third question:", a15.question_3())
    print("Fourth question:", a15.question_4())
    print("Fifth question:", a15.question_5())
    print("Sixth question:", a15.question_6()) #Yes the number agree with the floating-point value from the previous question, aside from the final .0
    val = a15.question_7(20)
    print("Seventh question:", )
    print(next(val))
    print(next(val))
    for i in val:
        print(i)