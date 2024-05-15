# Friend or Foe?

def filter_friends(names):
    friends = []
    for name in names:
        if len(name) == 4:
            friends.append(name)

    return friends
names = ["Ryan", "Kieran", "Mark"]
print(filter_friends(names)) 
