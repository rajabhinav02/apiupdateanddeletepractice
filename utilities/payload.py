from utilities.configuration import *


def payloadadd(gquery):
    row = getquery(gquery)
    bookd = {}
    bookd['name'] = row[0]
    bookd['isbn'] = row[1]
    bookd['aisle'] = row[2]
    bookd['author'] = row[3]
    return bookd


def payloaddelete(id):
    body = {

        "ID": id

    }
    return body