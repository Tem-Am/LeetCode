class Solution:
    def countAndSay(self, n: int):
        # Recursive function where i call it until n 
        # if input is 1 = "1" default 
        # for each number, output consist of number of times and number

        def value(output : str, val : int):
            # If val is equal to n
            if val == n:
                return output
            # Size is duplicates of certain number in s    
            size = 0

            # Temp for first var in string
            temp = int(output[0])

            # Save for nextRLE
            RLE = []
            for s in output:
                
                # Convert into number
                number = int(s)
                if temp == number:
                    size += 1
                else:
                    RLE.append(str(size))
                    RLE.append(str(temp))
                    size = 1
                    temp = number
            RLE.append(str(size))
            RLE.append(str(temp))
            newRLE= "".join(RLE)
            a = value(newRLE, val+1)
            return a
        return value("1",1)
