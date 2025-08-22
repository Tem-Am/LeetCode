class Solution:
    def addBinary(self, a: str, b: str):
        # binary add
        i, j = len(a) - 1, len(b)-1
        carry = 0
        ans = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            

            # current bit 
            # depening on number we will add to asn by % of 2
            ans.append(str(total%2))

            # update carry
            # if total is 2 or 3. carry will be 1
            carry = total // 2
        return "".join(reversed(ans))