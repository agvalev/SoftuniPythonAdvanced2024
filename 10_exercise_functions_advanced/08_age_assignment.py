def age_assignment(*args, **kwargs):
    persons = {}
    for name in args:
        persons[name] = kwargs[name[0]]
    persons = sorted(persons.items())

    result = []
    for name, age in persons:
        result.append(f"{name} is {int(age)} years old.")

    return "\n".join(result)