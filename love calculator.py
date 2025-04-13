def calculate_love_score(name1, name2):
    
    name = name1+name2
    name = name.lower()
    true_count = 0
    love_count = 0
    
    for i in name:
        for j in "true":
            if i == j:
                true_count += 1
    print("True count is:",true_count)
    
    for x in name:
        for y in "love":
            if x == y:
                love_count += 1
    print("Love count is:", love_count)
    
    return int(str(true_count) + str(love_count))

name_1 = input("Enter name 1:")
name_2 = input("Enter name 2:")

print(calculate_love_score(name_1, name_2))

    
