#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    index = 0
    source = 'NONE'
    while True:
        destination = hash_table_retrieve(hashtable, source)
        if destination is not "NONE":
            route[index] = destination
            source, index = destination, index + 1
        else:
            break

    return route
