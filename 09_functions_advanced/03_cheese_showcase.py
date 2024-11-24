def sorting_cheeses(**kwargs):
    result = ""
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvp:(-len(kvp[1]), kvp[0]))

    for chees_name, quantity_list in sorted_cheeses:
        result += f"{chees_name}\n"
        sorted_quantity_list = sorted(quantity_list, reverse=True)
        result += "\n".join(str(el) for el in sorted_quantity_list) + "\n"
    return result
