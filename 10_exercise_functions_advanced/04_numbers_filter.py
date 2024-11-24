def even_odd_filter(**kwargs):
    for key, numbers in kwargs.items():
        if key == "even":
            kwargs[key] = [x for x in numbers if x % 2 == 0]
        else:
            kwargs[key] = [x for x in numbers if x % 2 == 1]

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1]))) #davat ni na posiciqta "x" cql tuple i nie vzimame
    # elementa na indeks 1 koito vsushtnost sa chislata