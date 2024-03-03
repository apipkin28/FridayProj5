print("Welcome to The QuizBowl! Your questions start now.")
questionsList = {"What is the tallest animal in the world? ":"Giraffe",
                 "What is the anatomical term for the collarbone? ":"Clavicle",
                 "What does the deepest point in the ocean measure (in meters)? ":"10,935",
                 "When was the first computer invented? ":"1822",
                 "What types of letters will cost you in Wheel of Fortune? ":"Vowels"}
score = 0
for question, answer in questionsList.items():
    print(question)
    response = input("Your answer: ")
    if response == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

print("Quiz ended. Your score is "+str(score)+" out of 5.")