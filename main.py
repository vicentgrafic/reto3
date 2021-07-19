import random

def create_menu():

    dishes_master_food = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9"]
    dishes_master_price = [10, 20, 30, 40, 50, 60, 70, 80, 1000]

    #declara una estructura de tipo DICTIONARY
    dishes_daily_dictionary = {}

    #crea la carta diaria con 4-7 platos
    for i in range(random.randint(4, 7)):
        dishes_daily_dictionary[dishes_master_food[i]] = dishes_master_price[random.randint(0, 8)]

    return dishes_daily_dictionary

#selector por texto
def ask_menu_text(menu):

    while True:

        selection = input("Type a dish name in the list, type nothing to exit:")

        if len(selection) == 0:
            break

        else:
            customer_selection.append(selection)

def set_billet_distribution(amount_distribution, total_amount, billet, changed):

    if total_amount >= billet:
        total_amount = total_amount - billet
        amount_distribution = amount_distribution + str(billet) + ", "
        changed = True

    return amount_distribution, total_amount, changed

# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    new_menu = create_menu()

    print("Choose dish number, without number exits:")
    dish_quantity=0
    for key, value in new_menu.items():

        print(dish_quantity, key, " > ", value, "€")
        dish_quantity=dish_quantity+1

    #declara una estructura de tipo LISTA
    customer_selection = []

    #ask menu by text
    ask_menu_text(new_menu)

    total_amount = 0
    inexsitent_dish = ""
    for index, value in enumerate(customer_selection):
        if not value in new_menu:
            inexsitent_dish = inexsitent_dish + str(value) + ", "
        else:
            total_amount = total_amount + new_menu.get(value)

    if inexsitent_dish.count(',') == 1:
        print("El plato " + inexsitent_dish[:-2] + " no existe en el menú")

    elif inexsitent_dish.count(',') > 1:
        print("Los platos " + inexsitent_dish[:-2] + " no existen en el menú")

    total_amount_end = total_amount
    billet_5 = 5
    billet_10 = 10
    billet_20 = 20
    billet_50 = 50
    billet_100 = 100
    billet_200 = 200
    billet_500 = 500
    amount_distribution = ""

    while total_amount > 0:

        changed = False
        amount_distribution, total_amount, changed = set_billet_distribution(amount_distribution, total_amount, billet_500, changed)
        if changed == True:
                continue
        amount_distribution, total_amount, changed = set_billet_distribution(amount_distribution, total_amount, billet_200, changed)
        if changed == True:
                continue
        amount_distribution, total_amount, changed = set_billet_distribution(amount_distribution, total_amount, billet_100, changed)
        if changed == True:
                continue
        amount_distribution, total_amount, changed = set_billet_distribution(amount_distribution, total_amount, billet_50, changed)
        if changed == True:
                continue
        amount_distribution, total_amount, changed = set_billet_distribution(amount_distribution, total_amount, billet_20, changed)
        if changed == True:
                continue
        amount_distribution, total_amount, changed = set_billet_distribution(amount_distribution, total_amount, billet_10, changed)
        if changed == True:
                continue
        amount_distribution, total_amount, changed = set_billet_distribution(amount_distribution, total_amount, billet_5, changed)

    print("Yoy have to pay " + str(total_amount_end) + "€ with these billets: " + amount_distribution[:-2])