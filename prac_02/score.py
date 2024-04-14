import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50


def determine_result(score):
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid Score"
    elif score >= EXCELLENT_SCORE:
        return "Excellent"
    elif score >= PASSABLE_SCORE:
        return "Passable"
    else:
        return "Bad"


def main():
    user_score = float(input("Enter score: "))

    print(determine_result(user_score))

    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)

    print("Random score:", random_score)
    print(determine_result(random_score))


main()
