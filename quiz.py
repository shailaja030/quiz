score=0
ans=input("Who developed the language python? ")
if ans=="Guido van Rossum":
    print("Correct!")
    score=score+1
else:
    print("Incorrect!")
ans=input("What does 'OOP' stand for? ")
if ans=="Object Oriented Programming":
    print("Correct!")
    score=score+1
else:
    print("Incorrect!")
ans=input("What is the output for the code 'print(2*Hello)? ")
if ans=="Hello Hello":
    print("Correct!")
    score=score+1
else:
    print("Incorrect!")
print("Your score is",score)