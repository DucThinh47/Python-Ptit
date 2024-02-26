# def longest_common_prefix(strings):
#     if not strings:
#         return ""
#
#     # Find the set of characters in the first string
#     common_chars = set(strings[0])
#
#     # Iterate through the remaining strings
#     for s in strings[1:]:
#         # Update common_chars to contain only characters present in both sets
#         common_chars.intersection_update(s)
#
#         # If common_chars becomes empty, there's no common prefix
#         if not common_chars:
#             return ""
#
#     # Concatenate the characters in common_chars to form the prefix
#     return ''.join(sorted(common_chars))


def solve(a):
    sett = set(a[0])

    #sett = {'r', 'q', 'p'}

    # print(tmp)

    for i in a[1::]:
        # tim phan tu chung
        #x = {"apple", "banana"}
        #y = {"apple", "orange"}
        #x.intersection_update(y) = "apple"
        sett.intersection_update(i)
    #join set to string using "" as separator
    return "".join(sorted(sett))



# Test the function
a = ["pqra", "pqrae", "pqrio"]
print(solve(a))
# output = longest_common_prefix(a)
# print(output)  # Output: "pq"
