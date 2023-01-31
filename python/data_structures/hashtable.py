class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [[] for _ in range(self.size)]

    def set(self, key, value):
        index = self.hash(key)
        found = False
        for i, kv in enumerate(self._buckets[index]):
            if kv[0] == key:
                self._buckets[index][i] = (key, value)
                found = True
                break
        if not found:
            self._buckets[index].append((key, value))

    def get(self, key):
        index = self.hash(key)
        for kv in self._buckets[index]:
            if kv[0] == key:
                return kv[1]
        return None

    def has(self, key):
        index = self.hash(key)
        for kv in self._buckets[index]:
            if kv[0] == key:
                return True
        return False

    def keys(self):
        keys = []
        for bucket in self._buckets:
            for kv in bucket:
                keys.append(kv[0])
        return keys

    def hash(self, key):
        return hash(key) % self.size

    def display(self):
        return self._buckets


hashtable = Hashtable(1024)
hashtable.set("ahmad", 30)
hashtable.set("silent", True)
hashtable.set("listen", "to me")

actual = []

# NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
for item in hashtable._buckets:
    if item:
        actual.append(item)

print(actual)
