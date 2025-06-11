def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} → {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} → {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)
n = int(input("Enter number of disks: "))
tower_of_hanoi(n, 'A', 'B', 'C')
