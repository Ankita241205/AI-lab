def tower_of_hanoi(n,source, auxiliary, target):
    if n==1:
        # tower_of_hanoi(n-1, source,target, auxiliary)
        print("move disk 1 from", source, "to", target)
        return

    tower_of_hanoi(n-1, source,auxiliary, target)
    print("move disk",n,"from",source,"to",target)
    tower_of_hanoi(n-1,auxiliary,source, target)

n=3
tower_of_hanoi(n, 'A','B','C')