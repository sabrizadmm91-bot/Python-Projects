score = 0
print('Welcome to the Python Quize!')

q1=input('What is the capital of Sri Lanka?')
if q1.lower() == 'colombo':
    print('Correct Answer!')
    score +=1
else:
    print('Wrong answer')

q2 = input("2. Which keyword is used for a function in Python? ")
if q2.lower() == "def":
    print("Correct!")
    score += 1
else:
    print("Wrong")

q3 = input("3. Which data type stores numbers? ")
if q3.lower() == "int":
    print("Correct!")
    score += 1
else:
    print("Wrong")
    
print ('Your score:' , score)