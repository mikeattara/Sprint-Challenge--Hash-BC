#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    for index, weight in enumerate(weights):
        hash_table_insert(ht, weight, index)

    for index, weight in enumerate(weights):
        key = limit - weight
        entry = hash_table_retrieve(ht, key)
        if entry is not None:
            if index > entry:
                return index, entry
            else:
                return entry, index

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0]) + " " + str(answer[1]))
    else:
        print("None")


print_answer(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
print_answer(get_indices_of_item_weights(
    [12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7))
