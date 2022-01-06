water = 400
milk = 540
beans = 120
cups = 9
money = 550


def print_state(water, milk, beans, cups, money):
    print(f'The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'{money} of money')


def buy_coffee(water, milk, beans, cups, money):
    order = int(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: '))
    if order == 1:
        if water >= 250 and beans >= 16 and cups >= 1:
            water -= 250
            beans -= 16
            cups -= 1
            money += 4

    elif order == 2:
        if water >= 350 and milk >= 75 and beans >= 20 and cups >= 1:
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
            money += 7

    elif order == 3:
        if water >= 200 and milk >= 100 and beans >= 12 and cups >= 1:
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
            money += 6

    return water, milk, beans, cups, money


def fill_supply(water, milk, beans, cups):
    water_added = int(input('Write how many ml of water you want to add: '))
    water += water_added

    milk_added = int(input('Write how many ml of milk you want to add: '))
    milk += milk_added

    beans_added = int(input('Write how many grams of coffee beans you want to add: '))
    beans += beans_added

    cups_added = int(input('Write how many disposable coffee cups you want to add: '))
    cups += cups_added

    return water, milk, beans, cups


def take_money(money):
    print(f'i gave you {money}')
    money -= money
    return money


print_state(water, milk, beans, cups, money)
print()

action = input('Write action (buy, fill, take): ')
if action == 'buy':
    water, milk, beans, cups, money = buy_coffee(water, milk, beans, cups, money)
elif action == 'fill':
    water, milk, beans, cups = fill_supply(water, milk, beans, cups)
elif action == 'take':
    money = take_money(money)

print()
print_state(water, milk, beans, cups, money)
