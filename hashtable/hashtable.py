class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:

    def __init__(self, length):
        self.length = length
        self.hash_table = [None]*self.length

  

    def fnv1(self, key):
        # these values come from algorithm authors
        self.offset_basis = 14695981039346656037
        self.prime = 1099511628211
        # get bytes representation of key
        bytes_representation = key.encode()
        # algorithm starts by setting hash equal to offset basis
        hash = self.offset_basis
        # loop through bytes, multiply each times the prime above and
        # then set hash equal to hash XOR byte - again, part of algorithm
        for byte in bytes_representation:
            hash *= self.prime
            hash = hash ^ byte
        # return hash
        return hash


    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

    def hash_index(self, key):
        # set capacity to length of hash table set at initialization - this will be used to create index from hash
        self.capacity = self.length
        # return index, which is hash modulo length of table
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # set value to hash_table index, which is hashed key
        self.hash_table[self.hash_index(key)] = value


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        if self.hash_table[self.hash_index(key)]:
            self.hash_table[self.hash_index(key)] = None
            return
        return "Key not found"

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        if self.hash_table[self.hash_index(key)] is not None:
            return self.hash_table[self.hash_index(key)]
        return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
