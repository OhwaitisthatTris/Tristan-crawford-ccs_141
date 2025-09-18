guests= ["Niomi Milan", "Tristan Crawford", "Alex Johnson"]

for guest in guests:
    invitation = f"Dear {guest}, \n\nI would be honored if you could join me for dinner at my place this Saturday at 7 PM. Your presence would make the evening truly special, let me know if your avaible.\n\nBest regards,\n[Your Name]"
    print(invitation)
    print("\n")

    guests_cant_make_it = "Liam smith"
    print(f"[{guests_cant_make_it}] can't make it to the dinner")

    if guests_cant_make_it in guests:
        guests.remove(guests_cant_make_it)
        new_guest = "Alex Johnson"
        guests.append(new_guest)

print ("\nNew set of invitations:")
for guest in guests:
    invitation = f"Dear {guest}, \n\nI would be honored if you could join me for dinner at my place this Saturday at 7 PM. Your presence would make the evening truly special, let me know if your avaible.\n\nBest regards,\n[Your Name]"
    print(invitation)
    print("\n")

print("Great news! I've found a bigger dinner table, so I can invite more guests.") 

guests.insert(0, "Niomi Milan")
guests.insert(2, "Liam smith")
guests.append("Emma Brown")

print("\nUpdated set of invitations:")
for guest in guests:
    invitation = f"Dear {guest}, \n\nI would be honored if you could join me for dinner at my place this Saturday at 7 PM. Your presence would make the evening truly special, let me know if your avaible.\n\nBest regards,\n[Your Name]"
    print(invitation)
    print("\n")

    print("Sorry, due to unforeseen circumstances, I can only invite two guests for dinner.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Dear {removed_guest}, I regret to inform you that due to unforeseen circumstances, I can only invite two guests for dinner. I apologize for any inconvenience this may cause and hope we can catch up another time.")

    print("\nYou are still invited:")
for guest in guests:
    invitation = f"Dear {guest}, you are still invited to dinner at my place this Saturday at 7 PM. Looking forward to your presence!"
    print(invitation)
    print("\n")

    del guests[:]
print("\nFinal guest list:")
print(guests)  