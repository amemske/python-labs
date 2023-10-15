#variables
def get_choices():
    player_choice = input("Enter a choice - rock, paper, scissors -")
    computer_choice = 'paper'
    choices = {"player": player_choice, "computer": computer_choice}
    return choices
    


all_choices = get_choices();
print(all_choices)

#dict = { "name" : "beau", "color": all_choices}

#def greeting():
 #   return "Hi"
    
#print(greeting())