import random
my_ticket = (3, 5, 9)

attempts = 0

while True:
    winning_ticket = tuple(random.sample(range(1, 11), 3))
    attempts += 1

    if winning_ticket == my_ticket:
        break

print(f"Your ticket {my_ticket} won after {attempts} attempts!")
