# Hashtable using list
class Hash_table(object):
    def __init__(self, table_size = 10):
        self.table_size = table_size
        self._make_table()

    def _make_table(self):
        table = dict()
        for sz in range(self.table_size):
            table[sz] = []
        self.table = table
        
    def append(self, value):
        key = value % self.table_size
        self.table[key].append(value)
        
    def remove(self, value):
        key = value % self.table_size
        self.table[key].remove(value)
        
    def count(self, value):
        key = value % self.table_size
        return self.table[key].count(value)