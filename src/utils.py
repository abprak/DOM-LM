

# label2id = {
#     'name': 0,
#     'phone': 1,
#     'type': 2,
#     'website': 3,
#     'director': 4,
#     'genre': 5,
#     'mpaa_rating': 6,
#     'title': 7
# }

# id2label = {
#     0: 'name',
#     1: 'phone',
#     2: 'type',
#     3: 'website',
#     4: 'director',
#     5: 'genre',
#     6: 'mpaa_rating',
#     7: 'title'
# }

id2label = {
    0: 'address',
    1: 'author',
    2: 'company',
    3: 'cuisine',
    4: 'date_posted',
    5: 'director',
    6: 'engine',
    7: 'fuel_economy',
    8: 'genre',
    9: 'height',
    10: 'isbn_13',
    11: 'location',
    12: 'manufacturer',
    13: 'model',
    14: 'mpaa_rating',
    15: 'name',
    16: 'phone',
    17: 'price',
    18: 'publication_date',
    19: 'publisher',
    20: 'team',
    21: 'title',
    22: 'type',
    23: 'website',
    24: 'weight'
}

label2id = {v: k for k, v in id2label.items()}


def padding(data, max_len, pad_value=1) -> list:
    """
    :param data: list of list
    :param max_len: int
    :param pad_value: int
    :return: list of list
    """
    pad_data = []
    for d in data:
        if len(d) < max_len:
            pad_data.append(d + [pad_value] * (max_len - len(d)))
        else:
            pad_data.append(d[:max_len])
    return pad_data


def truncate(data, max_len) -> list:
    """
    :param data: list of list
    :param max_len: int
    :return: list of list
    """
    trunc_data = []
    for d in data:
        if len(d) > max_len:
            trunc_data.append(d[:max_len])
        else:
            trunc_data.append(d)
    return trunc_data
