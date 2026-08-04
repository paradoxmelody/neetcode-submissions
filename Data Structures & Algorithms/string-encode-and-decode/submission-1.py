from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        #eoncode a list of strings to a single string
        for s in strs:
            encoded += str(len(s))
            encoded += '#'
            encoded += s
        return encoded
    def decode(self, s: str) -> List[str]:
        #decodes a single str back to list of str
        decoded = []
        i = 0
        n = len(s)

        while i < n:
            length = 0
            #find the pos of the mext '#'
            
            while s[i] != '#':
                length = length * 10 + (ord(s[i]) - ord('0'))
                i += 1
            #skip '#'
            i += 1

            #extract the string using length
            temp = s[i:i + length]
            decoded.append(temp)

            i += length

        return decoded
