"""
Name: Ashley Eidenberger
hw1.py

Problem: The following programs are fairly simple, the user
inputs a set of values, and using algebra, gives the user a
result

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)




def calc_volume():
    length_volume = eval(input("Enter the length: "))
    width_volume = eval(input("Enter the width: "))
    height_volume = eval(input("Enter the height: "))
    volume = length_volume * width_volume * height_volume
    print("Volume =", volume)


def shooting_percentage():
    total_shot = eval(input("Enter the player's total shots: "))
    shots_made = eval(input("Enter how many shots the player made: "))
    percentage = (shots_made / total_shot) * 100
    print("Shooting Percentage:", percentage,"%")



def coffee():
    pounds = eval(input("How many pounds of coffee would you like"))
    total = (10.50 * pounds) + (0.86 * pounds) + 1.50
    print("Your total is: $", total)



def kilometers_to_miles():
    kilo = eval(input("How many kilometers did you travel?: "))
    mile = kilo / 1.61
    print("That's", mile, "miles!")


if __name__ == '__main__':
    pass
