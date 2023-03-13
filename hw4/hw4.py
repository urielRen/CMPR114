
# Uriel Renteria
# 3/7/23

# project 1
#test_tup = (15, 20, 123, 47, 26, 81)
#index = 0
#total = 0

#while index < len(test_tup):
#    total += test_tup[index]
#    index += 1

#print(f"Total: {total}")

# project 2
#test_tup = (15, 20, 123, 47, 26, 81)
#largest = -1
#index = 0

#while index < len(test_tup):
#    if largest < test_tup[index]:
#        largest = test_tup[index]
#    index += 1

#print(test_tup)
#print(f"The largest number in the tuple is: {largest}")

# project 3
#test_tup = ([17, 28], [93,11], [20,17])

#print(test_tup)
#print(f"\n{test_tup[0]}: {sum(test_tup[0])}")
#print(f"{test_tup[1]}: {sum(test_tup[1])}")
#print(f"{test_tup[2]}: {sum(test_tup[2])}\n")
#total = sum(test_tup[0] + test_tup[1] + test_tup[2])

#print(f"Sum: {total}")

# project 4
input_tup = ([2, 20], [44, 1], [3, 13])
print("Displaying unsorted tuple:")
print(input_tup)

sort_tup = sorted(input_tup, key = lambda x: x[0] + x[1])

print("\nDisplaying sorted tuple by list total: ")
print(sort_tup)