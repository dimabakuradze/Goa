# Shortest Word


def num(number):
    word = number.split()
    shortest_length = len(word[0])
    for word in word[1:]:
        length = len(word)
        if length < shortest_length:
            shortest_length = length
    
    return shortest_length
print(num("bitcoin take over the world maybe who knows perhaps")) 
