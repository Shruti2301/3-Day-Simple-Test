# We need to return the first character that appears exactly once. If every character repeats return "_"
from collections import Counter

# Counter is a specialized dictionary for building/counting hashable objects

def first_non_repeating_character(s:str) -> str:
    counts = Counter(s)
    
    for char in s:
        if counts[char] == 1:
            return char
    
    return "_"

print(first_non_repeating_character("aaabcccdee"))

