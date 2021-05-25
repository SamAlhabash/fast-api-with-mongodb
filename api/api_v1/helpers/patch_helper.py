def remove_all_none_from_dict(dictionary: dict):
    result = None
    for key,value in dictionary.items():
        if type(value) is dict:
            remove_all_none_from_dict(value)
        result.update(key, value)
    
    return result
