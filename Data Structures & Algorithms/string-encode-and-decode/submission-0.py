class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        
        for s in strs:
            encoded_string += (str(len(s)) + '#' + s)
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        cursor = 0

        while cursor < len(s):

            # find the end of the length number
            delimiter = cursor
            while s[delimiter] != "#":
                delimiter += 1

            length = int(s[cursor:delimiter])

            # start of the word
            word_start = delimiter + 1
            word_end = word_start + length

            result.append(s[word_start:word_end])

            cursor = word_end

        return result