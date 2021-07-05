

class basicassignment_16:
    def question1(self,n):
        year_of_birth = n
        l = [year_of_birth+i for i in range(6)]
        return l
    def question2(self,n):
        third_birthday = basicassignment_16().question1(n)[3]
        return third_birthday
    def question3(self,n):
        oldest = max(basicassignment_16().question1(n))
        return oldest
    def question4(self,a,b,c):
        things = [a,b,c]
        return things
    def question5(self,l):
        things = [i.capitalize() for i in l]
        return things
    def question6(self,a,b,c):
        surprise = [a,b,c]
        return surprise
    def question7(self,l):
        l[-1] = l[-1].lower()[::-1].capitalize()
        return l
    def question8(self,d):
        e2f = d
        return e2f
    def question9(self,e2f,w):
        return e2f[w]
    def question10(self,e2f):
        f2e = dict([(value,key) for key, value in e2f.items()])
        return f2e
    def question11(self,f2e,w):
        return f2e[w]
    def question12(self,e2f):
        return list(e2f.keys())
    def question13(self,d):
        return d
    def question14(self,d):
        return list(d.keys())
    def question15(self,d,w):
        return list(d[w].keys())
    def question16(self,d,w1,w2):
        return d[w1][w2]
    def __str__(self):
        return """1. Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985].
                2. In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.
                3.In the years list, which year were you the oldest?
                4. Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
                5. Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?
                6. Make a surprise list with the elements "Groucho," "Chico," and "Harpo."
                7. Lowercase the last element of the surprise list, reverse it, and then capitalize it.
                8. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.
                9. Write the French word for walrus in your three-word dictionary e2f.
                10. Make a French-to-English dictionary called f2e from e2f. Use the items method.
                11. Print the English version of the French word chien using f2e.
                12. Make and print a set of English words from the keys in e2f.
                13. Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.
                14. Print the top-level keys of life.
                15. Print the keys for life['animals'].
                16. Print the values for life['animals']['cats']
                """
if __name__ == "__main__":
    a16 = basicassignment_16()
    print("first question: ", a16.question1(1998))
    print("second question: ", a16.question2(1998))
    print("third question: ", a16.question3(1998))
    things = a16.question4("mozzarella", "cinderella", "salmonella")
    print("fourth question: ", things)
    print("fifth question: ",a16.question5(things))
    surprise = a16.question6("Groucho","Chico","Harpo")
    print("sixth question: ", surprise)
    print("seventh question: ", a16.question7(surprise))
    e2f = a16.question8({"dog" : "chien", "cat": "chat", "walrus" : "morse"})
    print("eigth question: ", e2f)
    frenchwrdfor_walrus = a16.question9(e2f,"walrus")
    print("ninth question: ",frenchwrdfor_walrus)
    f2e = a16.question10(e2f)
    print("tenth question: ", f2e)
    Engwrdfor_walrus = a16.question9(f2e,"chien")
    print("eleventh question: ",Engwrdfor_walrus)
    print("twelth question:", a16.question12(e2f))
    life = a16.question13({"animals" : {"cats" : ["Henri", "Grumpy", "Luci"] , "octopi" : {},  "emus": {}}, "plants" : {}, "other" : {}})
    print("thirteenth question :",life)
    print("Fourteenth question: ",a16.question14(life))
    print("Fifteenth question:", a16.question15(life, "animals"))
    print("Sixteenth question:", a16.question16(life, "animals", "cats"))