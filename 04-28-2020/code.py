# Write your unique_values function here:
def unique_values(my_dictionary):
    unique_list = []
    unique_count = 0
    for value in my_dictionary.values():
        if value not in unique_list:
            unique_list.append(value)
            unique_count += 1
    return unique_count


# Uncomment these function calls to test your  function:
print(unique_values({0: 3, 1: 1, 4: 1, 5: 3}))
# should print 2
print(unique_values({0: 3, 1: 3, 4: 3, 5: 3}))
# should print 1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Write your frequency_dictionary function here:


def frequency_dictionary(words):
    frequency_list = []
    for word in words:
        frequency = words.count(word)
        frequency_list.append(frequency)
    return {key: value for key, value in zip(words, frequency_list)}


# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0, 0, 0, 0, 0]))
# should print {0:5}
