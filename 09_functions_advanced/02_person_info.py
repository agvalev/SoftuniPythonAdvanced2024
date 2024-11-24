def get_info(name, age, town, **kwargs):
    print(kwargs)
    return f"This is {name} from {town} and he is {age} years old"


data = {"name": "George", "town": "Sofia", "age": 20}

print(get_info(**data, nots=1))
