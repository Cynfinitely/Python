import sys

print("Welcome the Quiz!")

answer = input('Do you want to solve this quiz? Please write yes or no.')

# This code is for answer 'no' . It will cause to end quiz.
if answer.lower() != 'yes' :
    print('\nOkay , thats sad! Bye!')
    sys.exit()

print('\nThats great! Lets start with the first question!')
#score holder for calculate final point.
score = 0

answer = input("What does CPU stand for? ")

#We need answer in lower case , thats why I used .lower()
if answer.lower() == 'central processing unit':
    print('Correct!')
    #correct answers will add 1 point to final result.
    score += 1
else:
    print('Wrong!')

answer = input("What does RAM stand for? ")

if answer.lower() == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Wrong!')

answer = input("What does GPU stand for? ")

if answer.lower() == 'graphical processing unit':
    print('Correct!')
    score += 1
else:
    print('Wrong!')

answer = input("What does Bios stand for? ")

if answer.lower() == 'basic income output system':
    print('Correct!')
    score += 1
else:
    print('Wrong!')

answer = input("What does OS stand for? ")

if answer.lower() == 'operating system':
    print('Correct!')
    score += 1
else:
    print('Wrong!')

print('\nThank you for solving quiz!')
print('You got  ' + str(score) + ' questions correct and your percentage is ' + str((score/5)*100) + '%')
