def spiralNumbers(n):
    m = n
    a = [[0 for i in range(n)] for j in range(n)]
    k = 0 
    l = 0
    count = 1
    while (k < m and l < n) : 
		
		# Print the first row from 
		# the remaining rows 
        for i in range(l, n): 
            a[k][i] = count
            count += 1

        k += 1

		# Print the last column from 
		# the remaining columns 
        for i in range(k, m) :
            a[i][n-1] = count
            count += 1
            
        n -= 1

		# Print the last row from 
		# the remaining rows 
        if ( k < m) : 
			
            for i in range(n - 1, (l - 1), -1) : 
                a[m-1][i] = count
                count += 1 
			
            m -= 1
		
		# Print the first column from 
		# the remaining columns 
        if (l < n) : 
            for i in range(m - 1, k - 1, -1) : 
                a[i][l] = count
                count += 1
            l += 1
      
    return a

n = 10
print(spiralNumbers(n))

# 1 2 3
# 8 9 4
# 7 6 5

# 3 5
# 4 7
# 5 9
# 6 11