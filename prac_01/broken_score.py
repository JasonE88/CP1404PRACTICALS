MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50

score = float(input("Enter score: "))
if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
    print("Invalid Score")
elif score >= EXCELLENT_SCORE:
    print("Excellent")
elif score >= PASSABLE_SCORE:
    print("Passable")
else:
    print("Bad")