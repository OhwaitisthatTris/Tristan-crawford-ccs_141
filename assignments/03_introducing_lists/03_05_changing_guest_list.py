guests=["Niomi Milan", "Liam smith", "Tristan Crawford"]

for guest in guests:
    invitation = f"Dear {guest}, \n\nI would be honored if you could join me for dinner at my place this Saturday at 7 PM. Your presence would make the evening truly special, let me know if your avaible.\n\nBest regards,\n[Your Name]"
    print(invitation)
    print("\n")

guests_cant_make_it = "Liam smith"
if guests_cant_make_it in guests:
    guests.remove(guests_cant_make_it)
    new_guest = "Alex Johnson"
    guests.append(new_guest)

    print ("\nNew set of invitations:")
    for guest in guests:
        invitation = f"Dear {guest}, \n\nI would be honored if you could join me for dinner at my place this Saturday at 7 PM. Your presence would make the evening truly special, let me know if your avaible.\n\nBest regards,\n[Your Name]"
        print(invitation)
        print("\n")