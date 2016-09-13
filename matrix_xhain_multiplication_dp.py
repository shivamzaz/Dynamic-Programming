import sys
class Store(object):
	def __init__(self,i,j,k):
		self.i=i
		self.j=j
		self.k=k
def multiplication(p,n):
	op=[]
	m=[[0 for i in range(n)] for i in range(n)]
	# (2) is  for it end with 2
	for l in range(2,n): 
		for i in range(0,n-l):
			j=i+l
			m[i][j]=sys.maxint
			for k in range(i+1,j):
				g=m[i][k]+m[k][j]+p[k]*p[i]*p[j]
				if(g<m[i][j]):
					op.append(Store(i,j,k))
					m[i][j]=g
	return m[0][n-1],l,m
a=[1,2,3,4]
n=4
re,lit,m=multiplication(a,n)
print m
