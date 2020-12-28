class DisjointSet:
    def __init__(self, data):
        self.parent = self
        self.data = data

    def root(self):
        if self.parent == self:
            return self

        return self.parent.root()

    def union(self, set2):
        our_root = self.root()
        set2_root = set2.root()

        our_root.parent = set2_root


class DisjointSets:
    def __init__(self, init_list):
        self.sets_list = list(map(lambda x: DisjointSet(x), init_list))

    def root(self, data):
        for item in self.sets_list:
            if item.data == data:
                return item.root()

    def union(self, data1, data2):
        item1, item2 = None, None

        for item in self.sets_list:
            if item.data == data1:
                item1 = item

            if item.data == data2:
                item2 = item

        return item1.union(item2)

    def size(self):
        count = 0

        for item in self.sets_list:
            if item.parent == item:
                count += 1

        return count
