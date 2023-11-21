#CTI-110
#P4HW1-Score List
#Londono William 
#2023-11-21

#Get the number of scores to enter
num_scores = int(input("How many scores do you want to enter? "))

#Create a list to store the scores
scores = []

#Loop to collect the scores
for i in range(num_scores):
    #Get the score from the user
    score = float(input("Enter score #{}: ".format(i + 1)))

    #Validate the score
    while score < 0 or score > 100:
        print("INVALID Score entered!!!")
        print("Score should be between 0 and 100")
        score = float(input("Enter score #{} again: ".format(i + 1)))

    #Add the valid score to the list
    scores.append(score)

#Calculate the average score, dropping the lowest score
lowest_score = min(scores)
scores.remove(lowest_score)
average_score = sum(scores) / len(scores)

#Display the average score and a letter grade
print("Average score:", average_score)

if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print("Letter grade:", letter_grade)
