

def petr_and_a_combination_lock(rotations, n):
    def rotate(total, i):
        if i == n:
            return 1 if total % 360 == 0 else 0
        return max(rotate(total + rotations[i], i+1), rotate(total - rotations[i], i+1))

    return "YES" if rotate(0, 0) else "NO"







n = int(input())
rotations = []
for _ in range(n):
    rotations.append(int(input()))
print(petr_and_a_combination_lock(rotations, n))