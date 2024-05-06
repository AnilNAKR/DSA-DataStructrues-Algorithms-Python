def removeDuplicates(s) -> str:
        str = []
        for i in range(len(s)):
            if str != []:
                if s[0] == str[-1]:
                    str.pop()
                else:
                    if s[i] != s[i+2]:
                        str.append(s[i])
            else:
                str.append(s[i])
        output = "".join(str)

        return output

print(removeDuplicates("aabbbcbdkan"))
        
        
        