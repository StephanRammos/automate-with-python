#randomQuizGenerator.py
import random
capitals = {'Alabama': 'Montgomery', 'Alaska': "Juneau", 'Arizona':'Phoenix', 'Arkansas':'Little Rock', 'California':'Sacramento',
'Colorado':'Denver','Connecticut':'Hartford', 'Delaware':'Dover', 'Florida':'Tallahassee',
'Georgia':'Atlanta', 'Hawaii':'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana':'Baton Rouge', 'Maine':'Augusta', 'Maryland': 'Annapolis',
'Massachusetts': 'Boston', 'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi':'Jackson',
'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismark', 
'Ohio': 'Colombus','Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
'Rhode Island': 'Providence', 'South Carolina':'Columbia', 'South Dakota':'Pierre', 'Tennessee': 'Nashville',
'Texas': 'Austin', 'Utah':'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond',
'Washington':'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#Generate 35 quiz files:
for quizNum in range(35):
	#Create the quiz and answer key files
	quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
	answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')

	#Write out the header for the quiz.
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' ' * 20)+ f'State Capitals Quiz (Form{quizNum + 1})')
	quizFile.write('\n\n')

	#Shuffle the order of the states.
	states = list(capitals.keys())
	random.shuffle(states)

#Loop through all the 50 stats, making a question for each.
	for questionNum in range(50):
		#index the states list by the ith iteration of for loop and then we index the capitals dictionary by the name of the state.
		correctAnswer = capitals[states[questionNum]]
		#make a list of capitals
		wrongAnswers = list(capitals.values())
		#lists are mutable , so can use del stmt, overwrites old list
		# finds the index (position) of the correct answer in the wrongAnswers list.
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers,3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)

		#Write the question and answer options to the quiz file.
		quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
		for i in range(4):
			quizFile.write(f"	{'ABCD'[i]}. { answerOptions[i]}\n") 
		quizFile.write('\n')

		#Write the answer key to a file.
		answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}") 

#Close files after all 50 questions		
quizFile.close() 
answerKeyFile.close()






