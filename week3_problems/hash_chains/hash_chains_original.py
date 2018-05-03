# python3
import ipdb
class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]

class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count, queries):
        self.bucket_count = bucket_count
        self.queries = queries
        # store all strings in one list
        self.elems = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def process_query(self, query):
        if query.type == "check":
            # ipdb.set_trace()
            # use reverse order, because we append strings to the end
            index_to_check = query.ind
            self.write_chain(cur for cur in reversed(self.elems) if self._hash_func(cur) == index_to_check)
        else:
            ipdb.set_trace()
            try:
                ind = self.elems.index(query.s)
                print(f'index: {ind}')
            except ValueError:
                # ValueError when query string doesn't exist
                # in self.elems
                print('ValueError')
                ind = -1
            if query.type == 'find':
                print(f'query.type == find. was_found(ind != -1): {ind != -1}, ind: {ind}')
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                print(f'query.type == add')
                if ind == -1:
                    print(f'ind == -1: {ind == -1}. appending to self.elems')
                    self.elems.append(query.s)
                    print(f'self.elems: {self.elems}')
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_queries(self):
        for query in queries:
            blah = Query(query)
            self.process_query(blah)
            print(f'\nquery: {query}, query.type: {blah.type}')

queries = [['add','world'],['add','HellO'],['check','4'],['find','World'],['find','world'],['del','world'],['check','4'],['del','HellO'],['add','luck'],['add','GooD'],['check','2'],['del','good']]
query_proc = QueryProcessor(5, queries)
query_proc.process_queries()

# HellO world
# no
# yes
# HellO
# GooD luck
