DEBUG = True


##--------------------------------------------------------------
# Anagram Problem
##--------------------------------------------------------------
def ans_v1(str1, str2):
    result = 0
    s1_map = {}
    s2_map = {}
    # hashmap for str1
    for s1 in str1:
        s1_map[s1] = s1_map[s1]+1 if s1 in s1_map else 1
    # hashmap for str2
    for s2 in str2:
        s2_map[s2] = s2_map[s2]+1 if s2 in s2_map else 1
    # counting the char
    print("s1", s1_map)
    print("s2", s2_map)
    for s, count in s1_map.items():
        if s in s2_map and s2_map[s] != s1_map[s]:
            result += abs(s2_map[s] - s1_map[s])   
            print(f"for[{s}]::if::result: ", result)      

        if not(s in s2_map):
        	print(f"if::2:: s:{s} :: count: {s1_map[s]}")
        	result += s1_map[s]

    for s, count in s2_map.items():
        if not(s in s1_map):
        	print(f"if::2:: s2_s:{s} :: s2_count: {s2_map[s]}")
        	result += s2_map[s]

    if len(s2_map) != len(s1_map):
        print("if::result: ", result)      
        result += abs(len(s2_map) - len(s1_map))

    return result


count  = 0
tc = [('except', 'accept'), ('buy', 'bye')]
for t1, t2, in tc:
	result = ans_v1(t1, t2)
	print(f"TC[{tc[count]}] : {result}")
	count += 1


##---------------------------------------------------------------
# Longest substring with k distinct problem
##---------------------------------------------------------------
# def getLengthofLongestSubstring(ch, k):
#     n = len(ch)
#     i, j = 0, 0
#     result = 0
#     char_map = {}
#     while(j < n):
#         if len(char_map) <= k:
#             char_map[ch[j]] = char_map[ch[j]] + 1 \
#                 if ch[j] in char_map else 1
#             result = max(result, sum(char_map.values()))
#             j += 1
#         else:
#             while(len(char_map) > k):
#                 if char_map[ch[i]] > 0:
#                     char_map[ch[i]] -= 1
#                 else:
#                     char_map.pop(ch[i])
#                 i += 1
#     return result



# tc = [('abcbc', 2), ('abcc', 1), ('abcba', 6), ('acbdab', 3)]

# for tc1, tc2 in tc:	
# 	x = getLengthofLongestSubstring(tc1, tc2)
# 	print(f"for tc1: {tc1}, result: {tc2}")


