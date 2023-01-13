#create a dictionary where u.s. states are keys and their capitals are values
#randomly quiz user by displaying state name and asking for its capital name
#keep a count of number or correct and incorrect responses
import random
dictionary = {'Alabama':'Montgomery', 'Alaska':'Juneau', 'Arizona':'Phoenix', 'Arkansas':'Little Rock', 'California':'Sacramento', 'Colorado':'Denver', 'Connecticut':'Hartford', 'Delaware':'Dover', 'Florida':'Tallahassee', 'Georgia':'Atlanta', 'Hawaii':'Honolulu', 'Idaho':'Boise', 'Illinois':'Springfield', 'Indiana':'Indianapolis', 'Iowa':'Des Moines', 'Kansas':'Topeka', 'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge', 'Maine':'Augusta', 'Maryland':'Annapolis', 'Massachusetts':'Boston', 'Michigan':'Lansig', 'Minnesota':'Saint Paul', 'Mississippi':'Jackson', 'Missouri':'Jefferson City', 'Montana':'Helena', 'Nebraska':'Lincoln', 'Nevada':'Carson City', 'New Hampshire':'Concord', 'New Jersey':'Trenton', 'New Mexico':'Santa Fe', 'New York':'Albany', 'North Carolina':'Raleigh', 'North Dakota':'Bismarck', 'Ohio':'Columbus', 'Oklahoma':'Oklahoma City', 'Oregon':'Salem', 'Pennsylvannia':'Harrisburg', 'Rhode Island':'Providence', 'South Carolina':'Columbia', 'South Dakota':'Pierre','Tennessee':'Nashville', 'Texas':'Austin', 'Utah':'Salt Lake City', 'Vermont':'Montpelier', 'Virginia':'Richmond', 'Washington':'Olympia', 'West Virginia':'Charleston', 'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}
print('Be sure to spell each word properly.')
state_names = list(dictionary)
correct = 0
incorrect = 0
keep_going = 'y'
while(keep_going == 'y'):
  num = random.randint(1, 50)
  state = state_names[num]
  print('Enter the capital of ' + state)
  capital = input('Capital: ')
  if(capital == dictionary[state]):
    correct += 1
    keep_going = input("Enter 'y' to continue and any other key to stop: ")
  else:
    incorrect += 1
    keep_going = input("Enter 'y' to continue and any other key to stop: ")

print('Correct answers: ', correct)
print('Incorrect answers: ', incorrect)
