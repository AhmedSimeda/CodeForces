n, t = tuple(map(int,input().split()))
Queue = input()
for _ in range(t):
    B_idx = [i for i in range(len(Queue)) if (Queue[i] == 'B') and (i != len(Queue)-1)]
    for idx in B_idx:
        if (Queue[idx] == 'B') and (Queue[idx+1] == 'G'):
            if idx < len(Queue)-2:
                Queue = Queue[:idx] + 'GB' + Queue[idx+2:]
            else:
                Queue = Queue[:idx] + 'GB'
print(Queue)