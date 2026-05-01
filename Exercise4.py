import random

#   Below is the Dictionary for the countries
def european_capitals_quizlet():
    questions = {
        "Belgium": "Brussels",
        "Austria": "Vienna",
        "Poland": "Warsaw",
        "France": "Paris",
        "Germany": "Berlin",
        "Denmark": "Copenhagen",
        "Finland": "Helsinki",
        "Greece": "Athens",
        "Portugal": "Lisbon",
        "Ireland": "Dublin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "United Kingdom": "London",   
        "Sweden": "Stockholm",
        "Norway": "Oslo",
    }
    #Here 10 countries are selected randomly
    countries = list(questions.keys())
    # It Reorganizes order of countries
    random.shuffle(countries)
    quiz_countries = countries[:10]

    #Keeps track of answers
    score = 0
    total_questions = 10
    print("Test Your Knowledge In The European Capital Quiz :)")
    print(f"You Will Be Asked {total_questions} Questions.")
    print("__" * 40)

    # It Loops through selected countries
    for i, country in enumerate(quiz_countries):
        correct_answer = questions[country]
        #Asks the user questions
        print(f"\nQuestion {i + 1}: What Is The Capital Of {country}?")
        #Removes all types of whitespace
        user_answer = input("Your Answer: ").strip().title()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {correct_answer}.\n")

    print("__" * 40)
    percentage = round((score / total_questions) * 100)
    print(f"Your Total Score Is {score} out of {total_questions} ({percentage}%).")

    if percentage >= 80:
        print("Great job! :)")
    elif percentage >= 50:
        print("Not bad, keep practicing!")
    else:
        print("Better luck next time!")
    print("Quiz Finished. Thank You For Playing")

if __name__ == "__main__":
    european_capitals_quizlet()