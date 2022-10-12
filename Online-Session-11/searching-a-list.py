word_list = [
    "cat", "dog", "bird", "oyster", "rat", "mouse", "crow",
    "magpie", "raven", "aardvark", "zebra", "yak", "pig",
]

word_list.sort()

# NO built-in methods for the search

find_me = "horse"
# Brute Force Search - useful for unsorted data
found_it = False
position = -1
steps = 0
for word in word_list:
    steps += 1
    if word == find_me:
        found_it = True
        position = steps - 1
        break

if found_it:
    print(f"Word {find_me} was found at position {position}"
          f" in {steps} steps")
else:
    print(f"Word {find_me} was not found in {steps} steps")
