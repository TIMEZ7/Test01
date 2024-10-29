



class solution:
    def merge(self,A,m,B,n):
        A[m:m+n]=B
        return A.sort()

