def list_roman_emperors(*args, **kwargs):
    successful_emperors = []
    unsuccessful_emperors = []

    for emperor_name, is_successful in args:
        if is_successful:
            successful_emperors.append(emperor_name)
        else:
            unsuccessful_emperors.append(emperor_name)

    sorted_successful = sorted(successful_emperors, key=lambda name: (-kwargs.get(name, 0), name))

    sorted_unsuccessful = sorted(unsuccessful_emperors, key=lambda name: (kwargs.get(name, 0), name))

    result = []

    result.append(f"Total number of emperors: {len(successful_emperors) + len(unsuccessful_emperors)}")

    if sorted_successful:
        result.append("Successful emperors:")
        for emperor_name in sorted_successful:
            result.append(f"****{emperor_name}: {kwargs.get(emperor_name)}")

    if sorted_unsuccessful:
        result.append("Unsuccessful emperors:")
        for emperor_name in sorted_unsuccessful:
            result.append(f"****{emperor_name}: {kwargs.get(emperor_name)}")

    return "\n".join(result)
