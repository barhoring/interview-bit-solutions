class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        a = A
        dict = {}
        size = len(A)
        for i in range(0, size-3):
            n1 = a[i]
            for j in range(i+1, size-2):
                n2 = a[j]
                sum1 = n1 + n2
                if sum1 in dict:
                    result = dict[sum1] + [i, j]
                    return sorted(result)
                else:
                    dict[sum1] = [i, j]
                for k in range(j+1, size-1):
                    n3 = a[k]
                    for m in range(k+1, size):
                        n4 = a[m]
                        sum2 = n3 + n4
                        if sum2 in dict:
                            if k not in dict[sum2]:
                                result = dict[sum2] + [k, m]
                                return sorted(result)
                        #else:
                            #dict[sum2] = [k, m]
        return []


if __name__ == "__main__":
    # execute only if run as a script
    sol = Solution()
    #A = [3,4,7,1,32,9,71]
    #A = [ 0, 2, 1, 1, 1, 1, 0 ]
    #A = [1, 1,1,1 ,1]
    #A = [ 9, 5, 4, 9, 3, 6, 8, 7, 1, 2, 8, 7, 2, 9, 7, 1, 3, 9, 7, 8, 1, 0, 5, 5 ]
    A = [ 0, 0, 1, 0, 2, 1 ]
    print(A)
    a = sol.equal(A)
    print(a)
