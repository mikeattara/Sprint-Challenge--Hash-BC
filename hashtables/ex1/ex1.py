#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,)


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
