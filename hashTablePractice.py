class HashTable:
  def __init__(self):
    self.capacity = self.get_prime(10)
    self.table = [None] * self.capacity
  
  def get_prime(self, n):
    if n % 2 == 0:
      n += 1
    
    while not self.check_prime(n):
      n += 2
      
    return n
  
  def check_prime(self, n):
    if n <= 1:
      return False
    if n <= 3:
      return True
    if n % 2 == 0 or n % 3 == 0:
      return False
    i = 5
    while i * i <= n:
      if n % i == 0 or n % (i + 2) == 0:
        return False
      i += 6
    return True
  
  def hash_function(self, key):
    return key % self.capacity
  
  def insert(self, key, data):
    index = self.hash_function(key)
    if self.table[index] is None:
      self.table[index] = [(key, data)]
    else:
      self.table[index].append((key, data))
  
  def remove(self, key):
    index = self.hash_function(key)
    if self.table[index] is not None:
      for i, (k, _) in enumerate(self.table[index]):
        if k == key:
          del self.table[index][i]
          return
    else:
      print("No value at key ", key)
  
  def search(self, key):
    index = self.hash_function(key)
    if self.table[index] is not None:
      for k, data in self.table[index]:
        if k == key:
          return data
        else:
          return "Wrong key"
    else:
      return "No data at this key"
  
hash_table = HashTable()

hash_table.insert(123, 'apple')
hash_table.insert(234, 'mango')
hash_table.insert(567, 'banana')

print("HashTable: ")
print(hash_table.table)

rm_key = int(input("Enter key to remove data "))

hash_table.remove(rm_key)
print("\nAfter removing " + str(rm_key) + " the hash table is: ")
print(hash_table.table)

search_key = int(input("\nEnter key to display data: 1. 123\n 2. 234\n 3. 567 \n"))

print("\nSearch for key "+ str(search_key) + " is: ", hash_table.search(search_key))
