class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        DELIMITER = '#'

        for s in strs:
            res = f"{res}{len(s)}{DELIMITER}{s}"

        return res

    def decode(self, s: str) -> List[str]:
        DELIMITER = '#'
        res = []
        curr_decode_string_length = ""
        count = -1
        curr_decode = ""
        for i in range(len(s)):
            if count > 0: 
                curr_decode = f"{curr_decode}{s[i]}"
                count = count - 1
                if count == 0: 
                    res.append(curr_decode)
                    curr_decode = ""

            elif s[i] == DELIMITER:
                count = int(curr_decode_string_length) 
                curr_decode_string_length = "" 
                if count == 0:          # handles zero-length strings
                    res.append("")
            
            else:
               curr_decode_string_length = f"{curr_decode_string_length}{s[i]}"
            

        return res


