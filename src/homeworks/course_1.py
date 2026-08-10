products = [
    {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
    {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
    {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
    {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25},
    {
        "name": "Cookie",
        "category": "sweets",
        "price": 200,
        "quantity": 12,
        "brand": "ABC",
    },
    {
        "name": "Donut",
        "category": "sweets",
        "price": 300,
        "quantity": 7,
        "brand": "XYZ",
    },
    {
        "name": "Cake",
        "category": "sweets",
        "price": 400,
        "quantity": 3,
        "brand": "DEF",
        "discount": 10,
    },
    {"name": "Orange", "category": "fruit", "price": 150, "quantity": 18},
    {
        "name": "Lettuce",
        "category": "veggie",
        "price": 80,
        "quantity": 30,
        "organic": True,
    },
    {
        "name": "Chocolate",
        "category": "sweets",
        "price": 250,
        "quantity": 10,
        "brand": "GHI",
        "flavor": "Dark",
    },
]

morse = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}

words_to_decode = [
    "java",
    "python",
    "ruby",
    "php",
    "fortran",
    "javascript",
    "kotlin",
    "swift",
    "basic",
    "pascal",
]

products = [
    {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
    {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
    {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
    {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25},
    {
        "name": "Cookie",
        "category": "sweets",
        "price": 200,
        "quantity": 12,
        "brand": "ABC",
    },
    {
        "name": "Donut",
        "category": "sweets",
        "price": 300,
        "quantity": 7,
        "brand": "XYZ",
    },
    {
        "name": "Cake",
        "category": "sweets",
        "price": 400,
        "quantity": 3,
        "brand": "DEF",
        "discount": 10,
    },
    {"name": "Orange", "category": "fruit", "price": 150, "quantity": 18},
    {
        "name": "Lettuce",
        "category": "veggie",
        "price": 80,
        "quantity": 30,
        "organic": True,
    },
    {
        "name": "Chocolate",
        "category": "sweets",
        "price": 250,
        "quantity": 10,
        "brand": "GHI",
        "flavor": "Dark",
    },
]

# Задача 1

morse_code = input()


def count_morse_characters():
    point_counter = morse_code.count(".")
    dash_counter = morse_code.count("-")
    total_counter = point_counter + dash_counter

    return total_counter


print(count_morse_characters())


# Задача 2


def morse_encode(morse_code, word):
    simbols = []

    for simbol in word:

        if simbol.lower() == " ":
            simbols.append(" ")
        elif simbol.lower() in morse:
            simbols.append(morse[simbol.lower()])
    return " ".join(simbols)


print(morse_encode(morse, word="javascript"))


# Задача 3


def morse_decode(morse_code, word):
    word_encode = word.split()
    simbols = []

    for simbol in word_encode:
        for k, v in morse.items():
            if simbol == v:
                simbols.append(k)

    return "".join(simbols)


i = input()

print(morse_decode(morse, i))


# Задача 4


def calculate_total_cost(products):
    total_price = 0

    try:
        for i in products:
            total_price += i["price"] * i["quantity"]
    except KeyError:
        i["quantity"] = 0
        i["price"] = 0

    return total_price


print(calculate_total_cost(products))


# Задача 5


def filter_products_by_price(products, max_price):
    filtered_products = []
    if products == [{}]:
        filtered_products.append({})

    for product in products:
        product_price = product.get("price")
        if product_price is not None and product_price <= max_price:
            filtered_products.append(product)

    return filtered_products


max_price = 200
print(filter_products_by_price([{}], max_price))


# Задача 6


def find_product_by_name(products, name):
    for product in products:
        if name == product.get("name"):
            return product
    else:
        return "Продукт с таким именем не найден в списке"


print(find_product_by_name(products, "Banana"))


# Задача 7


def update_product_info(products, name, new_data):
    for product in products:
        if name == product.get("name"):
            product.update(new_data)
            return products
    else:
        return "Продукт с таким именем не найден в списке"


product_to_update = "Broccoli"
new_info = {"quantity": 10, "organic": False}
update_result = update_product_info(products, product_to_update, new_info)
print(update_result)


# Задача 8


def sort_products_by_quantity(products, ascending=False):
    # for product in products:
    sorted_products = sorted(
        products, key=lambda product: product.get("quantity", 0), reverse=ascending
    )
    return sorted_products


print(sort_products_by_quantity(products))


# Задача 9


def average_price_per_category(products):
    new_dict = {}
    category_list = []

    if products == [{}]:
        return {}
    for product in products:
        if product.get("category") not in category_list:
            category_list.append(product["category"])
    for category in category_list:
        sum_price = 0
        count = 0
        for product in products:
            if product.get("category") == category:
                sum_price += product["price"]
                count += 1
                new_dict[category] = round(sum_price / count, 1)
    return new_dict


print(average_price_per_category(products))


# Задача 10


def group_products_by_category(products):
    new_dict = {}
    category_list = []

    if products == [{}]:
        return {}
    for product in products:
        if product.get("category") not in category_list:
            category_list.append(product["category"])
    for category in category_list:
        products_list = []
        for product in products:
            if product.get("category") == category:
                products_list.append(product)
                new_dict[category] = products_list
    return new_dict


print(group_products_by_category(products))
