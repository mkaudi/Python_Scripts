vowels = ('a','e','i','o','u')
vowel_cnt_list = []

vowel_count =0

s = input().lower()

while s != "end":
    for i in range(len(s)):
        check = s[i]
        for l in range(len(vowels)):
            if check == vowels[l]:   
                vowel_count += 1
    vowel_cnt_list.append(vowel_count)
    vowel_count =0
    s = input().lower()

for i in range(len(vowel_cnt_list)):
    print(vowel_cnt_list[i])
