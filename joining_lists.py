# joining lists
ages_one = [25, 30, 49, 60, 75]
ages_two = [19, 65, 21, 44, 38]
ages_three=[12,13,14,25]

joined_ages=ages_one + ages_two + ages_three #combine to lists into one
print(ages_one)
print("joined ages:", joined_ages)

ages_one.extend(ages_two)
print("ages_one extended:", ages_one)
print(ages_two)