# python3
# import ipdb
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

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.queries = self.read_queries()
        self.query_chain = self.bucket_count * [[]]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def read_queries(self):
        queries = []
        n = int(input())
        for i in range(n):
            queries.append(Query(input().split()))

        return queries

    def process_queries(self):
        for query in self.queries:
            # print(f'\nquery.type: {query.type}')

            if query.type != 'check':
                hashed_key = self._hash_func(query.s)
                # print(f'hashed_key: {hashed_key}, query.s: {query.s}')

            if query.type == 'add':
                self.query_chain[hashed_key] = self.query_chain[hashed_key] + [query.s]
                # print(f'add! self.query_chain: {self.query_chain}')

            if query.type == 'del':
                try:
                    # self.query_chain[hashed_key].remove(query.s)
                    items = self.query_chain[hashed_key]
                    self.query_chain[hashed_key] = list(filter(lambda a: a != query.s, items))

                    # print(f'delete! self.query_chain: {self.query_chain}')
                except ValueError:
                    next

            if query.type == 'find':
                was_found = query.s in self.query_chain[hashed_key]
                print('yes' if was_found else 'no')

            if query.type == 'check':
                print(' '.join(reversed(self.query_chain[query.ind])))


# blah = [['add','world'],['add','HellO'],['check','4'],['find','World'],['find','world'],['del','world'],['check','4'],['del','HellO'],['add','luck'],['add','GooD'],['check','2'],['del','good']]
# query_proc = QueryProcessor(5, blah)
# query_proc.process_queries()

# HellO world
# no
# yes
# HellO
# GooD luck

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
