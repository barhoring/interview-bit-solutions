class Solution:
    def addBinary(self, A,B):
        # f("100") =  [1,0,0]
        f = lambda arr: [int(c) for c in arr]
        a = f(A)
        b = f(B)
        # made a the bigger number
        diff = abs(len(A) - len(B))
        if len(B) > len(A):
            a,b = b,a
        # padd with 0 to make a,b same length
        b = diff*[0] + b
        result = []
        aux = 0;
        size = len(a)
        for i in range(size-1,-1,-1):
            t1, t2 = a[i], b[i]
            print(t1,t2)
            t3 = t1 ^ t2  ^ aux
            if(t1 + t2 + aux > 1):
                aux = 1
            else:
                aux = 0
            result.append(t3)
            print(result)
        print(aux)
        if aux:
            print("he")
            result.append(aux)
        result = result[::-1]
        return ''.join([str(x) for x in result])

if __name__ == "__main__":
    # execute only if run as a script
    z = Solution()
    A, B = "1010110111001101101000", "1000011011000000111100110"
    print(A[0], A[1])
    result = z.addBinary(B, A)
    print(result)