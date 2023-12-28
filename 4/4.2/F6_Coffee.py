in_stock = {"coffee": 4, "milk": 4, "cream": 0}
components = {
    'Эспрессо': {'coffee': 1, 'milk': 0, 'cream': 0},
    'Капучино': {'coffee': 1, 'milk': 3, 'cream': 0},
    'Макиато': {'coffee': 2, 'milk': 1, 'cream': 0},
    'Кофе по-венски': {'coffee': 1, 'milk': 0, 'cream': 2},
    'Латте Макиато': {'coffee': 1, 'milk': 2, 'cream': 1},
    'Кон Панна': {'coffee': 1, 'milk': 0, 'cream': 1}
}


def order(*coffees):

    no_ing = 'К сожалению, не можем предложить Вам напиток'

    for coffee in coffees:
        changes = components[coffee]

        for component, count in changes.items():
            if in_stock[component] < count:
                break

        else:
            for component, count in changes.items():
                in_stock[component] -= count

            return coffee

    else:
        return no_ing


print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
