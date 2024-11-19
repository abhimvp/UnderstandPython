# hashmap datastructure - key - value pairs
# key -. hash -. gets a index - used to find a value
# lists of lists


class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def __len__(self):
        return self.size

    def __contains__(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return True
        return False

    def put(self, key, value):
        index = self._hash_function(key)
        print(index)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                break
        else:  # we only enter into else branch when we loop through if and doesn't break
            self.buckets[index].append((key, value))
            self.size += 1

    def get(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return KeyError("Key not found")

    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break
        else:
            raise KeyError("Key not found")

    def keys(self):
        return [k for bucket in self.buckets for k, _ in bucket]

    def values(self):
        return [v for bucket in self.buckets for _, v in bucket]

    def items(self):
        return [(k, v) for bucket in self.buckets for k, v in bucket]

    def _hash_function(self, key):
        key_string = str(key)
        hash_value = 0
        for char in key_string:
            hash_value = (hash_value * 31 + ord(char)) % self.capacity

        return hash_value


if __name__ == "__main__":
    hashmap = HashMap(5)
    print(hashmap.buckets)
    hashmap.put("name", "Abhishek")
    print(hashmap.buckets)
    hashmap.put("age", 30)
    print(hashmap.buckets)
    hashmap.put("city", "New York")
    print(hashmap.get("name"))
    print(hashmap.get("age"))
    print(hashmap.get("city"))
    print(hashmap.__len__())
    print(hashmap.keys())
    print(hashmap.values())
    print(hashmap.items())
    print("name" in hashmap)
    hashmap.remove("name")
    print("name" in hashmap)
    print(hashmap.__len__())
    print(hashmap.keys())
    print(hashmap.values())
    print(hashmap.items())
