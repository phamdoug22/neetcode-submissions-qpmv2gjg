class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        
        for s in strs:
            encoded_string += (str(len(s)) + '#' + s)
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        pointer = 0

        while pointer < len(s):
            delimiter = pointer

            while s[delimiter] != '#':
                delimiter += 1
            
            length = int(s[pointer:delimiter])

            start_word = delimiter + 1
            word_end = start_word + length

            result.append(s[start_word:word_end])

            pointer = word_end
        return result