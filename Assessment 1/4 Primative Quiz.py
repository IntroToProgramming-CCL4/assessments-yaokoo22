countries_quiz = {
  #Dictionary of each country and their capital.
  "France" : "Paris",
  "Germany" : "Berlin",
  "Netherlands" : "Amsterdam",
  "Italy" : "Rome",
  "Spain" : "Madrid",
  "Portugal" : "Lisbon",
  "United Kingdom" : "London",
  "Poland" : "Warsaw",
  "Finland" : "Helsinki",
  "Sweden" : "Stockholm"
}
#It loops in each country and capitals in the dictionary.
for country, capital in countries_quiz.items():
  #Ask the users about the capital of the country given.
  quiz_answer = input(f"What is the capital of {country}? ")
  if quiz_answer == capital:
    #If answer is correct it will print out correct.
    print("Correct Answer !")
  else:
    #If its not it will print wrong and give the true answer.
    print("Wrong! the correct answer is" ,capital,".")