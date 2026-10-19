# Day 43: Group Anagrams using Hash Map
# -------------------------------------
from collections import defaultdict

def group_anagrams(strs):
    anagram_map = defaultdict(list)
    for s in strs:
        sorted_key = ''.join(sorted(s))
        anagram_map[sorted_key].append(s)
    return list(anagram_map.values())

if __name__ == '__main__':
    words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    print(f'Grouped: {group_anagrams(words)}')
