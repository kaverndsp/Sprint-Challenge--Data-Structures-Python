class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.queue_tail = None

    def append(self, item):
        if len(self.queue) < self.capacity:
            # if this is the first item to be added,
            # set oldest to this item if it's the first
            if len(self.queue) == 0:
                self.queue_tail = 0
            else:
                self.queue_tail += 1
            # append the item
            self.queue.append(item)

        # what if the queue is AT capacity?
        else:
            # update the oldest index

            # if the index was at the last item in
            # the array, move index to the front
            if self.queue_tail == self.capacity-1:
                self.queue_tail = 0
            # otherwise, just increment the oldest
            # index to the next item to the right
            else:
                self.queue_tail += 1

            # replace item at oldest index
            self.queue[self.queue_tail] = item

    def get(self):
        return self.queue
