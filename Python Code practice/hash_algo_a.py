class AlgoHashTable:

    def __init__(self,size):
        self.size=size
        self.hashtable= self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]


    def set_val(self, key, value):
       val = hash(value)%self.size
       bucket = self.hashtable[val]
       found = False
       for index,record in enumerate(bucket):
           record_key,record_value = record
           if record_key ==key:
               found=True
               break
       if found:
           bucket[index]=(key,value)
       else:
           bucket.append((key,value))
       bucket.append((key,value))

    def get_val(self, key):
        pass

    def __str__(self):
       return "".join(str(item) for item in self.hashtable)


hash_table = AlgoHashTable(256)
print(hash_table)
hash_table.set_val("mahsrur","something something")
hash_table.set_val("mahs"," something")
print(hash_table)