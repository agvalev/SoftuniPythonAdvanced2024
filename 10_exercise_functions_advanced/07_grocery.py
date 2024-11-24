def grocery_store(**kwargs):
    recept = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = []
    for product, quantity in recept:
        result.append("".join(f"{product}: {quantity}"))
    return ("\n".join(result)) # split gi vkarva v list a join gi izkarva



print(grocery_store(

bread=5,

pasta=12,

eggs=12,

))

