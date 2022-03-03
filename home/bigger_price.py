from pprint import pprint


def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    # creating new sorted dictionary
    sort_dict = {}
    # sorting of dictionary by price using lamda-function
    sort_dict = sorted(data, key=lambda x: x['price'], reverse = True)
    sort_dict_limited = sort_dict[:limit]


    return sort_dict_limited


pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))