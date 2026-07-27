from collections import defaultdict

def groupAnagrams(words):
    anagrams = defaultdict(list) # Empty dictionary

    for word in words: 
        # Sort characters to create a unique key
=        key = "".join(sorted(word)) # Needed to make ["a","e","t"] -> ["aet"]

        value = anagrams.get(key)
        if (value is None): 
            value = []
        value.append(word)
        anagrams[key] = value

    values = anagrams.values()
    return list(values)

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(words))