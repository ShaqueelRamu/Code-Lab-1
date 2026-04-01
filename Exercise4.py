import random

def european_capitals_quizlet():
    questions = {
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "Unites Kingdom": "London",
        "Sweden": "Stockholm",
        "Norway": "Oslo",
        "Denmark": "Copenhagen",
        "Finland": "Helsinki",
        "Greece": "Athens",
        "Portugal": "Lisbon",
        "Ireland": "Dublin",
        "Belgium": "Brussels",
        "Austria": "Vienna",
        "Poland": "Warsaw",
    }
    #Here 10 countries are selected randomly
    countries = list(questions.keys())
    #Reorganize order of countries
    random.shuffle(countries)
    quiz_countries = countries[:10]

    #Keeps track of answers
    score = 0
    total_questions = 10
    print("Test Your Knowledge In The European Capital Quiz :)")
    print(f"You Will Be Asked {total_questions} questions.")
    print("__" * 40)

    #Loops through selected countries
    for i, country in enumerate(quiz_countries):
      correct_answer = questions[country]
      #Makes question to user
      print(f"\nQuestion {i + 1}: What Is The Capital Of {country}?")
      #Removes all types of whitespace
      user_answer = input("Your Answer:").strip().title()

      if user_answer == correct_answer:
         print("Correct!\n")
         score += 1
      else:
         print(f"Incorrect! The correct answer is {correct_answer}.\n")

    print("__" * 40)
    print(f"Your Total Score Is {score} out of {total_questions}.")  
    print("Quiz finished. Thanks You For Playing")
if __name__ == "__main__":
   european_capitals_quizlet() 