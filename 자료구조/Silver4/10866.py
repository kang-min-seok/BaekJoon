from collections import deque

N = int(input())
M = [str(input()) for _ in range(N)]

queue = deque()

for command in M:
    if "push_front" in command:
        command = command.replace('push_front ', '')
        queue.appendleft(command)

    elif "push_back" in command:
        command = command.replace('push_back ', '')
        queue.append(command)

    elif "pop_front" in command:
        if(len(queue) > 0):
            print(queue[0])
            queue.popleft()
        else:
            print('-1')

    elif "pop_back" in command:
        if(len(queue) > 0):
            print(queue[-1])
            queue.pop()
        else:
            print('-1')

    elif "size" in command:
        print(len(queue))

    elif "empty" in command:
        if(len(queue) > 0):
            print('0')
        else:
            print('1')
    
    elif "front" in command:
        if(len(queue) > 0):
            print(queue[0])
        else:
            print('-1')

    elif "back" in command:
        if(len(queue) > 0):
            print(queue[-1])
        else:
            print('-1')