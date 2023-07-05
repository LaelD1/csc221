from random import randint
right = 0


question = "How many questions would you like to answer?"
print(question)
totalquestion = int(input("Enter a number: "))

for _ in range(totalquestion):
    num1= randint(1, 10)
    num2= randint(1, 10)
    
    question = "What is " + str(num1) + " times " + str(num2) + "?"
    print(question)
    user_input = int(input("Enter a number: "))
    answer = num1 * num2
        
    if user_input == answer:
        print("Correct")
        right = right + 1
    else:
        print("Wrong. The answer is:",answer)





print("I asked you", totalquestion,  "questions. You got " + str(right) + " of them right.")
if right < totalquestion:
    print("Better luck next time")
else:
    print("Great job!")


    

     



