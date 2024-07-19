# joining lists
ages_one = [25, 30, 49, 60, 75]
ages_two = [19, 65, 21, 44, 38]

joined_ages = ages_one + ages_two
print(ages_one)
print("joined ages:", joined_ages)

ages_one.extend(ages_two)
print("ages_one extended:", ages_one)
print(ages_two)

# slicing lists
scores = [100, 99, 25, 44, 85, 77, 64]

print("from start to index 2:", scores[:3])
print("from index 3 to end:", scores[3:]) 
print("from index 1 to 4:", scores[1:4])
print("from start to 4 with step of 2:", scores[:5:2])
print("from start to end with step of 2:", scores[::2])
print("reversing the list:", scores[::-1])