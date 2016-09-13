def a(a1,low,high):
	if(low<=high):
		mid=(low+(high-low)/2)
		#print mid,mid+1
		if(a1[mid]>a1[mid+1]):
			return mid
		else:
			return a(a1,low,mid) or  a(a1,mid+1,high)
	else:
		return -1
#once we find the pivot, that's it, then each of part will follow binaru search
def a_(a1,low,high,x):
	piv=a(a1,low,high)
	if(a1[piv]==x):
		return piv
	elif(a1[piv]<x):
		return b_s(a1,low,piv-1,x)
	else:
		return b_s(a1,piv+1,high,x)
def b_s(a1,low,high,x):
	if(low<=high):
		mid=low+(high-low)/2
		#print mid
		if(a1[mid]==x):
			return mid
		elif(a1[mid]>x):
			print "gg"
			return b_s(a1,low,mid-1,x)
		else:
			return b_s(a1,mid+1,high,x)
print a_([4,5,6,1,2,3],0,5,3)
