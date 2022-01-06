class CoffeeMachine:
    def __init__(self):
        # self.state = None

        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def __str__(self):
        return (f'The coffee machine has:\n' f'{self.water} of water\n' f'{self.milk} of milk\n' f'{self.beans} '
                f'of coffee beans\n' f'{self.cups} of disposable cups\n' f'{self.money} of money')

    def fill_supply(self):
        water_added = int(input('Write how many ml of water you want to add: '))
        self.water += water_added

        milk_added = int(input('Write how many ml of milk you want to add: '))
        self.milk += milk_added

        beans_added = int(input('Write how many grams of coffee beans you want to add: '))
        self.beans += beans_added

        cups_added = int(input('Write how many disposable coffee cups you want to add: '))
        self.cups += cups_added

    def take_money(self):
        print(f'i gave you {self.money}')
        self.money -= self.money
        return self.money

    def espresso_maker(self):
        return self.water >= 250 and self.beans >= 16 >= self.cups >= 1

    def latte_maker(self):
        return self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1

    def cappuccino_maker(self):
        return self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1

    def buy_coffee(self):
        order = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')

        if order == 'back':
            pass
        else:
            order = int(order)

            if order == 1:
                if self.espresso_maker():
                    print('I have enough resources, making you a coffee!')
                    self.water -= 250
                    self.beans -= 16
                    self.cups -= 1
                    self.money += 4
                else:
                    print('sorry not enough water!')

            elif order == 2:
                if self.latte_maker():
                    print('I have enough resources, making you a coffee!')
                    self.water -= 350
                    self.milk -= 75
                    self.beans -= 20
                    self.cups -= 1
                    self.money += 7
                else:
                    print('sorry not enough water!')

            elif order == 3:
                if self.cappuccino_maker():
                    print('I have enough resources, making you a coffee!')
                    self.water -= 200
                    self.milk -= 100
                    self.beans -= 12
                    self.cups -= 1
                    self.money += 6
                else:
                    print(f'sorry not enough water!')

    def manage_action(self):
        while True:
            answer = input('Write action (buy, fill, take, remaining, exit): ')

            if answer == 'remaining':
                print(self.__str__())
            elif answer == 'buy':
                self.buy_coffee()
            elif answer == 'fill':
                self.fill_supply()
            elif answer == 'take':
                self.take_money()
            elif answer == 'exit':
                break

            print()


espresso = CoffeeMachine()
espresso.manage_action()
