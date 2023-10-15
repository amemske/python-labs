# suppose you want to determine if an item get features on a home page based on the number of user likes

def determine_featured(total_likes, average_likes):
    if total_likes > average_likes:
        if total_likes <= 10:
            return "Feature for a day"
        elif 10 < total_likes < 50:
            return "Feature for 3 days"
        else:
            return "Feature for a week"
    else:
        return "Item cannot be featured"


print(determine_featured(100, 120))

#deep nesting in conditionals, where the decision-making process involves multiple levels of indentation to determine the outcome


# Equivalent Single Conditional Example:

def determine_featured2(total_likes, average_likes):
    if average_likes < total_likes <= 10:
        return "Feature for a day"
    elif total_likes > average_likes and 10 < total_likes < 50:
        return "Feature for 3 days"
    elif total_likes > average_likes:
        return "Feature for a week"
    else:
        return "Item cannot be featured"


print(determine_featured2(100, 120))

# I used a single conditional with multiple elif clauses to check the conditions in a simpler way.
