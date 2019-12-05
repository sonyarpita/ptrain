from collections import deque 
u_deque=deque('Hello 123')
for elem in u_deque:
	print(elem.upper()) 
u_deque.append('x')
u_deque.appendleft('y')
print(u_deque)
u_deque.pop()
u_deque.popleft()
print(list(u_deque))
print(u_deque[0])
print(u_deque[-1])
print(list(reversed(u_deque)))
u_deque.extend('456')
print(u_deque)
u_deque.rotate(3) #right rotation
print(u_deque)
u_deque.rotate(-1) # left rotation
print(u_deque)
print(deque(reversed(u_deque)))
print(u_deque.pop())
u_deque.extendleft('xyz')
print(u_deque)
u_deque.clear()
print(u_deque)

