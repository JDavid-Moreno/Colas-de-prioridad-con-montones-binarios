class MaxHeap:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def father(self, i):
        return (i - 1) // 2

    def left_son(self, i):
        return  (2 * i) + 1

    def right_son(self, i):
        return (2 * i) + 2

    def sift_up(self, i):
        while i > 0 and self.data[i] > self.data[self.father(i)]:
            father = self.father(i)
            self.data[i], self.data[father] = self.data[father], self.data[i]
            i = father

    def insert(self, value):
        self.data.append(value)
        self.sift_up(len(self.data) - 1)

    def sitf_down(self, i):
        n = len(self.data)
        while True:
            left = self.left_son(i)
            right = self.right_son(i)
            high = i

            if left < n and self.data[left] > self.data[high]:
                high = left
            if right < n and self.data[right] > self.data[high]:
                high = right

            if high == i:
                break

            self.data[i], self.data[high] = self.data[high], self.data[i]
            i = high

    def extract_maximum(self):
        if self.is_empty():
            print("heap vacío")
        root = self.data[0]

        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self.sitf_down(0)
        return root

class Tuple:
    def __init__(self):
        self.heap = MaxHeap()
        self.counter = 0

    def append(self, name, priority):
        insert = (priority, -self.counter, name)
        self.heap.insert(insert)
        self.counter += 1

    def next(self):
        priority, _, name = self.heap.extract_maximum()
        return name, priority

    def is_empty(self):
        return self.heap.is_empty()

    def __len__(self):
        return len(self.heap)


def main():
    tail = Tuple()
    tail.append("Ana", 2)
    tail.append("Juan", 5)
    tail.append("Sara", 5)
    tail.append("Pablo", 4)
    tail.append("David", 1)
    tail.append("Sofia", 7)
    tail.append("Carla", 4)

    while not tail.is_empty():
        name, priority = tail.next()
        print(name, priority)

main()

