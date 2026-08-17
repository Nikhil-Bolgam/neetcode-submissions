# use delimiter approach from the hints

class Solution:
    
    def encode(self, strs: List[str]) -> str:

        encoded_string = ''
        
        for s in strs :
            encoded_string += str(len(s))+'#'+s

        return encoded_string

    
    def decode(self, s: str) -> List[str]:

        decoded_string = []
        end_of_last_string = 0
        
        for i, character in enumerate(s):

            if i < end_of_last_string:
                continue

            if character == '#':
                # fetch lenght of string 
                length_of_string = int(s[end_of_last_string:i])
                
                # extract string 
                decoded_string.append(s[i+1:i+1+length_of_string])

                # update end of lsat string 
                end_of_last_string = i+1+length_of_string

        return decoded_string


            
            








