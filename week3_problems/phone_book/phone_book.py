# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries_naive_solution(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

def process_queries_fast(queries):
    contacts = {}
    results = []
    for query in queries:
        if query.type == 'add':
            contacts[query.number] = query
        elif query.type == 'del':
            if query.number in contacts:
                del(contacts[query.number])
            else:
                next
        elif query.type == 'find':
            if query.number in contacts:
                results.append(contacts[query.number].name)
            else:
                results.append('not found')

    return results

# input = [['add', '911', 'police'],
#     ['add', '76213', 'Mom'],
#     ['add', '17239', 'Bob'],
#     ['find', '76213'],
#     ['find', '910'],
#     ['find', '911'],
#     ['del', '910'],
#     ['del', '911'],
#     ['find', '911'],
#     ['find', '76213'],
#     ['add', '76213', 'daddy'],
#     ['find', '76213']]
# queries = [Query(i) for i in input]
# print(process_queries_fast(queries))
# Mom
# not found
# police
# not found
# Mom
# daddy

if __name__ == '__main__':
    write_responses(process_queries_fast(read_queries()))
