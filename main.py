health = 0
def question(question, answer):
    global health
    ans2 = input(question+" >>> ").lower()
    if ans2==answer.lower():
        print("very well! that's correct")
    else:
        health -=1
        print("the answer was ",answer+". you now have", health, "health remaining")
        if health == 0:
            print("you lost, thanks for taking the trivia! you are always welcomed to try again")
            exit()


print("welcome to my first python project!")
name = input("what is your name? ")
age = int(input("what is your age? "))

print("hello", name + "," , "it's a very pretty name!")
ans = input("would you like to give a trivia? ")
if ans.lower() == "yes":
    health=3
    question("What's the capital of India","delhi")
    question("what's the capital of china","beijing")
    question("what's the capital of canada","toronto")
    question("what's the capital of russia","moscow")
    question("what's the capital of united kingdom","london")
    question("what's the capital of france","paris")
    question("what's the capital of USA","new york")
    question("what's the capital of brazil","rio de janerio")
    question("What's the capital of spain","madrid")
    question("what's the capital of australia","canberra")



