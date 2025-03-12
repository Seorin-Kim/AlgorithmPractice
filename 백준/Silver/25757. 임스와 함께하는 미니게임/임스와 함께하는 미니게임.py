import sys

input = list(sys.stdin.readline().rstrip().split())
n, game = int(input[0]), input[1]

players_per_game = {'Y': 1, 'F': 2, 'O': 3}
players = set()
for _ in range(n):
    players.add(sys.stdin.readline().rstrip())

print(len(players) // players_per_game[game])
