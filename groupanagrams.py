from collections import defaultdict

def groupAnagrams(strs):
    # Dictionary to store groups of anagrams
    anagrams = defaultdict(list)

    for s in strs:
        # Sort characters to create a unique key
        key = "".join(sorted(s))

        # Add original string to its group
        anagrams[key].append(s)

    # Return all groups
    return list(anagrams.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(strs))