#think about the base case
dp[0]=1# at least one way TO PAY PRICE 0
for i in l:
	for j in range(l,1000,1):
			# Question was what is the total way to pay the specifc money via given coin(s)
			# either we are not using the specific coi(n) dp[j]
			# or we using the currrrent coin dp[j-i]
			dp[j]=dp[j]+dp[j-i]