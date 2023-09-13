class HashTable:
    def __init__(self):
        self.capacity = self.get_prime(10)  # Initialize capacity with a prime number
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
            # Handle collisions by appending to a list at the same index
            self.table[index].append((key, data))

    def remove(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i, (k, _) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return
        else:
            print("No value present at Key")

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, data in self.table[index]:
                if k == key:
                    return data
        return None

# Example usage:
hash_table = HashTable()

hash_table.insert(123, "apple")
hash_table.insert(432, "mango")
hash_table.insert(213, "banana")
hash_table.insert(654, "guava")

print("HashTable:")
print(hash_table.table)

hash_table.remove(123)
print("\nHashTable after removing key 123:")
print(hash_table.table)

print("\nSearch for key 432:", hash_table.search(432))
print("Search for key 123 (after removal):", hash_table.search(123))
