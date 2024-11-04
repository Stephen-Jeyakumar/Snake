word = input("what value would you like to spell? ")

try:
  word = int(word) - 1
except ValueError:
  print('You must input a number! System shutdown...... Self Destruct in 3.... 2..... 1..........')
  quit()



if word >5: 
  print ('You must type a number that is 7 or less. Try again.')


list = ["test", "food", "buffer Error", "penpineappleapplepen", "PPAP", "LOL I GTG CYA LATER PEOPLEZ", "27-9+34+9-61=0"]

for i in list[word]:
  print (i)