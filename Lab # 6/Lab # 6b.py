
def TowerOfHanoi(disks, from_rod, to_rod, aux_rod):
    if disks == 0:
        return 'no disk found'
    else:
        TowerOfHanoi(disks - 1, from_rod, aux_rod, to_rod)
        print("Move disk", {disks}, "from rod", {from_rod}, "to", {to_rod})
        TowerOfHanoi(disks - 1, aux_rod, to_rod, from_rod)


if __name__ == "__main__":
    disk = 3
    TowerOfHanoi(disk, 'A', 'C', 'B')
