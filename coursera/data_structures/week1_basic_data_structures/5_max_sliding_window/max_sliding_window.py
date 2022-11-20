# python3


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


def max_sliding_window(sequence, m):
    q_wi_max = QueueWithMax()
    for i in sequence[:m]:
        q_wi_max.add(i)

    maximums = [q_wi_max.smax]
    for i in range(m, len(sequence)):
        q_wi_max.pop()
        q_wi_max.add(i)

        maximums.append(q_wi_max.smax)

    return maximums


class QueueWithMax():
    def __init__(self):
        self.smax = None
        self.queue = []

    def add(self, elem):
        if elem > self.smax:
            new_elem = 2 * elem - self.smax
            self.smax = elem
            self.queue.append(new_elem)


    def pop(self):
        pass


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))
