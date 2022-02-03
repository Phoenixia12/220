"""
Ashley Eidenberger
lab3.py
Problem: Create a program that allows the user to calculate the average amount of cars traveling down separate roads
and calculate the overall average across all roads surveyed.
Certificate of Authenticity: I certify that this assignment is entirely my own work
"""


def traffic():
    road = int(input("How many roads were surveyed?: "))
    car_sum = 0
    for i in range(1, road + 1):
        print("How many days was Road", i, "surveyed?", ": ", end="")
        tot_day = int(input(""))
        car_tot = 0
        for j in range(1, tot_day + 1):
            print("\t", "How many cars traveled on day", j, ": ", end="")
            car_day = int(input(""))
            car_tot = car_tot + car_day
        road_avg = car_tot / tot_day
        car_sum = car_sum + car_tot
        print("Road", i, "average vehicles per day:", road_avg)
    print("The total number of vehicles traveled on all roads: ", car_sum)
    total_average = car_sum / road
    round(total_average, 2)
    print("Average number of vehicles per road: ", total_average)


traffic()
