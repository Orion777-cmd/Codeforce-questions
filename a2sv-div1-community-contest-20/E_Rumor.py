from collections import defaultdict
import sys, threading

def main():
    people, friends = map(int, input().split())
    golds = list(map(int, input().split()))
    friends_list = []

    for _ in range(friends):
        friends_list.append(list(map(int, input().split())))

    def dfs(n):
        visited.add(n)
        min_ = golds[n]
        for friend in graph[n]:
            if friend not in visited:
                min_ = min(min_, dfs(friend))
        return min_

    graph = defaultdict(list)
    for friend in friends_list:
        a, b = friend
        a, b = a - 1, b - 1
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    total = 0
    for i in range(people):
        if i not in visited:
            total += dfs(i)

    print(total)


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()