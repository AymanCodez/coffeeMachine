water_reserve = 400
milk_reserve = 540
beans_reserve = 120
cups_reserve = 9
money_reserve = 550


def print_state(water, milk, beans, cups, money):
    print(f'The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'{money} of money')


def espresso_maker(water, beans, cups):
    return water >= 250 and beans >= 16 >= cups >= 1


def latte_maker(water, milk, beans, cups):
    return water >= 350 and milk >= 75 and beans >= 20 and cups >= 1


def cappuccino_maker(water, milk, beans, cups):
    return water >= 200 and milk >= 100 and beans >= 12 and cups >= 1


def buy_coffee(water, milk, beans, cups, money):
    order = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')

    if order == 'back':
        return water, milk, beans, cups, money
    else:
        order = int(order)

        if order == 1:
            if espresso_maker(water, beans, cups):
                print('I have enough resources, making you a coffee!')
                water -= 250
                beans -= 16
                cups -= 1
                money += 4
            else:
                print(f'sorry not enough water!')

        elif order == 2:
            if latte_maker(water, milk, beans, cups):
                print('I have enough resources, making you a coffee!')
                water -= 350
                milk -= 75
                beans -= 20
                cups -= 1
                money += 7
            else:
                print(f'sorry not enough water!')

        elif order == 3:
            if cappuccino_maker(water, milk, beans, cups):
                print('I have enough resources, making you a coffee!')
                water -= 200
                milk -= 100
                beans -= 12
                cups -= 1
                money += 6
            else:
                print(f'sorry not enough water!')

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


def main(water, milk, beans, cups, money):
    while True:
        action = input('Write action (buy, fill, take): ')

        if action == 'remaining':
            print_state(water, milk, beans, cups, money)
        elif action == 'buy':
            water, milk, beans, cups, money = buy_coffee(water, milk, beans, cups, money)
        elif action == 'fill':
            water, milk, beans, cups = fill_supply(water, milk, beans, cups)
        elif action == 'take':
            money = take_money(money)
        elif action == 'exit':
            break

        print()


main(water_reserve, milk_reserve, beans_reserve, cups_reserve, money_reserve)
# self.water, self.milk, self.beans, self.cups, self.money = self.water, self.milk, self.beans, self.cups, self.money
