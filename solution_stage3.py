water_needed = 200
milk_needed = 50
beans_needed = 15
one_cup = 265

water = int(input('Write how many ml of water the coffee machine has: '))
milk = int(input('Write how many ml of milk the coffee machine has: '))
beans = int(input('Write how many grams of coffee beans the coffee machine has: '))
cups = int(input('Write how many cups of coffee you will need: '))

a = water // water_needed
b = milk // milk_needed
c = beans // beans_needed
answer = min(a, b, c)

if answer > cups:
    print(f'Yes, I can make that amount of coffee (and even {answer - cups} more than that)')
elif answer == cups:
    print('Yes, I can make that amount of coffee ')
else:
    print(f'No, I can make only {answer} cups of coffee')