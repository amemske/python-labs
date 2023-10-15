def averageGrade(term1, term2, term3):
    average = (term1 + term2 + term3) / 3
    if average < 70:
        if term1 < 60 or term2 < 60 or term2 < 60:
            print(f"You need to improve in at least one term. Your average was {average}")
        else:
            print(f"Your grade {average} is low")
    else:
        print(f"Keep up the good work, your grade is {average}!")


averageGrade(50, 60, 70)
#You need to improve in at least one term. Your average was 60.0

#In this example, we have a nested conditional. First, it checks if the average is less than 70.
#If it is, it further checks if any of the individual term grades (term1, term2, or term3) is below 60.
# Depending on the result of this inner check, it prints different messages. This structure allows for
# more detailed feedback based on both the overall average and individual term grades.