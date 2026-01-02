def create_the_teams(n, x, arr):
    arr.sort(reverse=True)
    team_total = 0
    team_count = 0
    for i in range(n):
        team_total += 1
        if team_total * arr[i] >= x:
            team_count += 1
            team_total = 0
    return team_count


t = int(input())
for _ in range(t):
    n, x = [int(num) for num in input().split()]
    arr =  [int(num) for num in input().split()]
    print(create_the_teams(n, x, arr))