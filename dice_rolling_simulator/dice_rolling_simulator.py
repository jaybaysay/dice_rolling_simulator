import random

min_int = 1
max_int = 6
user_yes = 'Y'
user_no = 'N'
user_acceptable_answers = [user_yes,user_no]
ask_to_roll_again = 'Do you want to roll again? Y/N'
error_ask_to_roll_again = 'Try Again. Acceptable Answers are Y/N'

def roll_dice():
  
  dice_roll = random.randint(min_int,max_int)
  print("You rolled {}!" .format(dice_roll))


def main():
    roll_dice()

    while True:
        print(ask_to_roll_again)

        current_input_status = input()

        while current_input_status.upper() not in user_acceptable_answers:
            print(error_ask_to_roll_again)
            current_input_status = input()

        if current_input_status.upper() == user_no:
            return
        else: roll_dice()
  
if __name__ == '__main__':
    main()