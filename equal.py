class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        a = A
        dict = {}
        size = len(A)
        for i in range(0, size):
            for j in range(i+1, size):
                n1 = a[i]
                n2 = a[j]
                #if n1 == n2:
                    #continue
                tmp1 = n2 - n1
                tmp2 = -1*tmp1
                if tmp1 in dict and i in dict[tmp1]:
                    continue
                if tmp2 in dict:
                    if i not in dict[tmp2] and j not in dict[tmp2]:
                    #if i not in dict[tmp2]:
                        tmp3 = dict[tmp2]
                        if tmp3[0] < i and tmp3[0] < j:
                            #return dict[tmp2] + [i, j]
                            result = tmp3 + [i,j]
                            return sorted(result)
                            #return [tmp3[0]] + [i,j] + [tmp3[1]]
                    else:
                        continue
                elif tmp1 not in dict:
                    dict[tmp1] = [i, j]
                #dict[tmp1] = [i, j]
        return []


if __name__ == "__main__":
    # execute only if run as a script
    sol = Solution()
    A = [3,4,7,1,32,9,71]
    #A = [ 0, 2, 1, 1, 1, 1, 0 ]
    #A = [1, 1,1,1 ,1]
    A = [ 9, 5, 4, 9, 3, 6, 8, 7, 1, 2, 8, 7, 2, 9, 7, 1, 3, 9, 7, 8, 1, 0, 5, 5 ]
    print(A)
    a = sol.equal(A)
    print(a)
