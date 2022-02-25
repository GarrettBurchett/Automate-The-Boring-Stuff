import string


def comma_separated_list(input_list:list) -> string:
    list_of_items = []
    if input_list == []:
        return None
    for item in input_list:
        if item == input_list[-1]:
            list_of_items.append(f"and {item}.")
        else:
            list_of_items.append(f"{item}, ")
    
    return "".join(list_of_items)

spam = ['Texans', 'Chiefs', 'Rockets', 'Astros', 'Royals', 'Cougars']
print(comma_separated_list(spam))