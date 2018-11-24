class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        def isPrime(n):
            if n <= 1:
                return False
            if n == 2:
                return True

            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

        def numofBits(n):
            count = 0
            while n > 0:
                if n % 2:
                    count += 1
                n = n >> 1
            return count


        rs = 0
        for i in range(L, R+1):
            n = numofBits(i)
            if isPrime(n):
                rs += 1
        return rs"""

        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(x).count("1") in primes for x in range(L, R+1))

        
