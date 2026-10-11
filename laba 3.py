# grrMondays
milky = {"Cow milk":35, "Cheese":77, "Yogurt":40}
bread = {"Buns":25, "Bread":32.5, "Baguette":35.5}
meat = {"Beef":125.35, "Chicken":75, "Turkey":105.45}
quantity = {'Cow milk': 2, 'Cheese':3, 'Yogurt':5, 'Buns':10, 'Bread':15, 'Baguette':12, 'Beef':4, 'Chicken':10, 'Turkey':3}
products = {}
products.update(milky)
products.update(bread)
products.update(meat)

bag = []
bag_price = 0
wallet = 200

x = lambda t : t + ", ласкаво просимо у наш магазин! "
def main():
    print(x(input("Введіть ваш логін аккаунта: ")))

    while True:
        print("Будь ласка, виберіть опцію: "
          " 1 - Увійти"
          " 2 - Переглянути продукти"
          " 3 - Онлай покупка"
          " 4 - Переглянути кошик"
          " 5 - Видалити товар"
          " 6 - Закінчити операцію")
        user_input = int(input("Введіть опцію: "))
        if user_input == 1:
            if input("Введіть логін: ") == "admin" and input("Введіть пароль: ") == "1234":
                print("Ласкаво просимо!")
                print(quantity)
            else: print("невірний логін або пароль")
        elif user_input == 3:
            counter = 0
            print("Виберіть секцію:"
                  " 1 - milky"
                  " 2 - bread"
                  " 3 - meat")
            user_choice = int(input("> "))
            if user_choice == 1:
                print(milky)
                print("Виберіть продукт в кошик: ")
                user_choice_product = int(input("> "))
                for a in milky:
                    counter = counter + 1
                    if counter == user_choice_product:
                        if a in quantity and quantity.get(a) > 0:
                            bag.append(a)
                            bag_price = bag_price + milky.get(a)
                            quantity[a] = quantity.get(a) - 1
                            print("Додано товар", a, "в кошик")
                        else:
                            print("Не вистачає товару")
                    elif user_choice_product > 4:
                        break
            elif user_choice == 2:
                print(bread)
                print("Виберіть продукт в кошик: ")
                user_choice_product = int(input("> "))
                for a in bread:
                    counter = counter + 1
                    if counter == user_choice_product:
                        bag.append(a)
                        bag_price = bag_price + bread.get(a)
                    elif user_choice_product > 4:
                        break
            elif user_choice == 3:
                print(meat)
                print("Виберіть продукт в кошик: ")
                user_choice_product = int(input("> "))
                for a in meat:
                    counter = counter + 1
                    if counter == user_choice_product:
                        bag.append(a)
                        bag_price = bag_price + meat.get(a)
                    elif user_choice_product > 4:
                        break
        elif user_input == 4:
            print(bag)
            print(bag_price)
        elif user_input == 2:
            print(products)
        elif user_input == 5:
            print("Впишіть в пермінал подукт який ви хочите видалити з кошика",
                  bag)
            while True:
                remove_product = input("> ")
                if remove_product in bag:
                    bag.remove(remove_product)
                    bag_price = bag_price - products.get(remove_product)
                elif remove_product == "exit":
                    break
                else:
                    print("Введено невірний товар")
        elif user_input == 6:
            print("...")
            wallet = wallet - bag_price
            if wallet > 0:
                print("Покупка завершена! Гарного дня")
                break
            elif wallet < 0:
                print("Недостатньо коштів")
                wallet = wallet + bag_price
            else:
                print("Гарного дня")
        else: print("Введено невірну цифру/символ")

if __name__ == '__main__':
    main()
