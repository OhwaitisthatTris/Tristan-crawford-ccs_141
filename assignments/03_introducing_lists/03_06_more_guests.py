guests= ["Niomi Milan", "Liam smith", "Tristan Crawford"]

for guest in guests:
    invitation = f"Dear {guest}, you are cordially invited to dinner at my place this Saturday at 7 PM. Looking forward to your presence!"
    print(invitation)
    print("\n")

    guests_cant_make_it = "Liam smith"
print(f"Unfortunately, {guests_cant_make_it} can't make it to the dinner.")

if guests_cant_make_it in guests:
    guests.remove(guests_cant_make_it)
    new_guest = "Alex Johnson"
    guests.append(new_guest)

    print ("\nNew set of invitations:")
    for guest in guests:
        invitation = f"Dear {guest}, you are cordially invited to dinner at my place this Saturday at 7 PM. Looking forward to your presence!"
        print(invitation)
        print("\n")

        print ("Good news! We found a bigger dinner table, so we can invite more guests.")
               
               #guests.insert(0, "Niomi Milan")  # Add at the beginning
                #guests.insert 2, = "Tristan Crawford")  # Add in the middle
                              #guests.append = "Alex Johnson)  # Add at the end
                                  
    print("\nUpdated set of invitations:")
    for guest in guests:
        invitation = f"Dear {guest}, you are cordially invited to dinner at my place this Saturday at 7 PM. Looking forward to your presence!"
        print(invitation)
        print("\n")