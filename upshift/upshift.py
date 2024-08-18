s = input()
output = ""
i =0

for i in range(len(s)):
    char = ord(s[i]) +1
    output += chr(char)

print(output)
