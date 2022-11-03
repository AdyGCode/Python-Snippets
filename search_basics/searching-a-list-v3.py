word_list = [
    "cat", "dog", "bird", "oyster", "rat", "mouse", "crow",
    "magpie", "raven", "aardvark", "zebra", "yak", "pig",
]
word_list.sort()
print(word_list)

# ['aardvark', 'bird', 'cat', 'crow', 'dog', 'magpie',...]
# Binary search:
# Begin_pos = 0                             End_pos =  13
#                        Middle = (13+0)//2 = 6
#                        "magpie"
# is "dog" < "magpie"? Yes
# Begin_pos = 0         End_pos = Middle (6)
#            Middle = (6 + 0) // 2 = 3
# is "dog" < "crow"? No
# is "dog > "crow"? Yes
#            Begin_pos = 3        End_pos = 6
#                Middle = (6 + 3) // 2 = 4
# is "dog" < "dog"? No
# is "dog" > "dog"? No
# is "dog" == "dog"? Yes - FOUND!


# NO built-in methods for the search

find_me = "zebra"
# Binary Search - useful for SORTED data

found_it = False
position = -1
steps = 0

begin_position = 0
end_position = len(word_list)
while True:
    steps += 1
    middle = (begin_position + end_position) // 2
    current_word = word_list[middle]
    if current_word == find_me:
        position = middle
        found_it = True
        break

    if current_word > find_me:
        end_position = middle
    if current_word < find_me:
        begin_position = middle

if found_it:
    print(f"Word {find_me} was found at position {position}"
          f" in {steps} steps")
else:
    print(f"Word {find_me} was not found in {steps} steps")
