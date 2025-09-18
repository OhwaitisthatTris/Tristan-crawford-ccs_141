games= ["baseball", "football", "basketball", "hockey", "tennis"]

print("Original list:", games)

games.append("baseball")
print("After append:", games)

games.insert(2, "football")
print("After insert:", games)

del games[0]
print("After del:", games)

popped_game = games.pop()
print("popped:", popped_game)
print("After pop:", games)

games.remove("basketball")
print("After remove:", games)

games.sort()
print("sorted:", games)