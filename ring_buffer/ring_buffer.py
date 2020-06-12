class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.queue_tail = None

    def append(self, item):
        if len(self.queue) < self.capacity:

            if len(self.queue) == 0:
                self.queue_tail = 0
            else:
                self.queue_tail += 1

            self.queue.append(item)

        else:
            if self.queue_tail == self.capacity-1:
                self.queue_tail = 0
            else:
                self.queue_tail += 1

            self.queue[self.queue_tail] = item

    def get(self):
        return self.queue
