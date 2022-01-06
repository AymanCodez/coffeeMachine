# class PiggyBank:
#     def __init__(self, dollars, cents):
#         self.dollars = dollars
#         self.cents = cents
#
#     def add_money(self, deposit_dollars, deposit_cents):
#         self.dollars += deposit_dollars
#
#         if 0 < self.cents + deposit_cents < 100:
#             self.cents += deposit_cents
#         elif self.cents + deposit_cents >= 100:
#             self.dollars += (self.cents + deposit_cents) // 100
#             self.cents = (self.cents + deposit_cents) % 100
#
#     def show(self):
#         print(self.dollars)
#         print(self.cents)
#
#
# savings = PiggyBank(1, 1)
# savings.add_money(500, 500)
# savings.show()


# import math
#
#
# class Hexagon:
#     def __init__(self, side_length):
#         self.side_length = side_length
#
#     # create get_area here
#     def get_area(self):
#         a = (3 * math.sqrt(3) / 2) * pow(self.side_length, 2)
#         return f'{a:.3f}'
#
#
# first_hexagon = Hexagon(5.4)
# print(first_hexagon.get_area())


# class RightTriangle:
#     def __init__(self, hyp, leg_1, leg_2):
#         self.c = hyp
#         self.a = leg_1
#         self.b = leg_2
#         self.s = self.a * self.b / 2
#
#
# # triangle from the input
# input_c, input_a, input_b = [int(x) for x in input().split()]
#
# first = RightTriangle(input_c, input_a, input_b)
# c_squared = first.c ** 2
# a_squared = first.a ** 2
# b_squared = first.b ** 2
#
# if c_squared == a_squared + b_squared:
#     print(first.s)
# else:
#     print('Not right')


# def enough_supplies(water, milk, beans, cups):
#     a = water // 200
#     b = milk // 50
#     c = beans // 15
#     d = cups // 1
#     answer = min(a, b, c, d)
#
#     return answer > 0
#
# a = water // 200
# b = milk // 50
# c = beans // 15
# answer = min(a, b, c)
#
# if answer > cups:
#     print(f'Yes, I can make that amount of coffee (and even {answer - cups} more than that)')
# elif answer == cups:
#     print('Yes, I can make that amount of coffee ')
# else:
#     print(f'No, I can make only {answer} cups of coffee')
#
#
# amountt, interestt, timee, = input().split()
#
#
# def calculate(amount, interest_rate, time):
#     # your code here
#     interest = amount * interest_rate * time / 100
#     total_amount = amount + interest
#     return interest, total_amount
#
#
# def print_result(interest, total_amount):
#     print(f'The interest is: {interest}')
#     print(f'The total amount is: {total_amount}')
#
#
# def fahrenheit_to_celsius(temps_f):
#     temps_c = (temps_f - 32) * 5 / 9
#     return round(temps_c, 2)
#
#
# def celsius_to_fahrenheit(temps_c):
#     temps_f = temps_c * 9 / 5 + 32
#     return round(temps_f, 2)
#
#
# def main():
#     """Entry point of the program."""
#     temperature, unit = input().split()  # read the input
#     temperature = int(temperature)
#
#     if unit == 'F':
#         print(fahrenheit_to_celsius(temperature), 'C')
#     elif unit == 'C':
#         print(celsius_to_fahrenheit(temperature), 'F')
#
#
# main()


# k = 'snakeCase'
# print(k)
#
# for char in k:
#     if char == char.capitalize():
#         k = k.replace(char, f'_{char.lower()}')
#
# print(k)

# for i in range(10):
#     line = ""
#     for j in range(10):
#         if i == j:
#             break
#         line += "{} ".format(j)
#     print(line)

# number = int(input())
# factors = []
#
# for i in range(1, number + 1):
#     if number % i == 0 and number % number == 0:
#         factors.append(i)
#
# if len(factors) > 2 or number < 2:
#     print('This number is not prime')
# elif len(factors) == 2 and (1 in factors and number in factors):
#     print('This number is prime')

# cafes = {}
#
# while True:
#     string = input()
#     if string == 'MEOW':
#         break
#     else:
#         values = string.split()
#         name = values[0]
#         number = int(values[1])
#         cafes[name] = number
#
# v = max(list(cafes.values()))
# for key in cafes.keys():
#     if cafes[key] == v:
#         print(key)

# income = int(input())
#
# if 0 <= income <= 15527:
#     print(f'the tax {income} is {0}%. That is {round(income * 0 / 100)} dollars!')
# elif 15528 <= income <= 42707:
#     print(f'the tax {income} is {15}%. That is {round(income * 15 / 100)} dollars!')
# elif 42708 <= income <= 132406:
#     print(f'the tax {income} is {25}%. That is {round(income * 25 / 100)} dollars!')
# else:
#     print(f'the tax {income} is {28}%. That is {round(income * 28 / 100)} dollars!')
