import random;

n = random.randint(0, 100)
attempts = 0
print('Please guess the number (between 0 and 100): ')
userInput = int(input())

while n != userInput:
    if n > userInput:
        print('It\'s more')
        attempts += 1
        userInput = int(input())
    elif n < userInput:
        print('It\'s less')
        attempts += 1
        userInput = int(input())

print('Congrats! You find the number in ' + str(attempts) + ' attempt(s).')