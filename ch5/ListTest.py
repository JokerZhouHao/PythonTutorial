from collections import deque
li = ['1', '2'];
li.extend(range(5, 10))
li.remove(5)
deque = deque(["Eric", "John", "Michael"])
deque.popleft()
print(deque)