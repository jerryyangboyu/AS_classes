from FileHandler import FileHandler

def add_new_scores():
    comp = lambda x, upper, lower: x < lower or x > upper
    score_date: str = input("Input the date for the scores")
    with FileHandler("ScoreDetails.txt", 'a') as file:
        while (member_ship_number := input("Input the Membership number")) != "":
            while comp(score := int(input("Input the score")), 99, 50):
                print("Input a valid score from 50 to 99")
            file.write("{0}{1}{2}".format(member_ship_number, score_date, score))


if __name__ == '__main__':
    add_new_scores()
