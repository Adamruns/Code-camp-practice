
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(2, "Kelly")
friends.remove("Jim")
friends[1] = "Mike"
friends.pop()

friends2 = friends.copy()

print(friends.count("Mike"))
print(friends2)
