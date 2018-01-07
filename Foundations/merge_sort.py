def main():
	Arr = [5,2,4,7,1,3,2,6]
	merge_sort(Arr,0,len(Arr)-1)
	print (Arr)
def merge_sort(A,p,r):
	if p < r:
		q = (p + r)//2
		merge_sort(A,p,q)
		merge_sort(A,q+1,r)

		merge(A,p,q,r)
		
def merge(A,p,q,r):
	L = []
	i=0
	for x in range(p,q+1):
		L.insert(i,A[x])
		i+=1
		
	R = []
	i=0
	for x in range(q+1,r+1):
		R.insert(i,A[x])
		i+=1
		
	#print (L,R,A,p,r)
	i = 0 
	j = 0
	k = p	
	while  i < len(L) and j < len(R):
		if L[i] <= R[j]:
			#print (i,j,k,L[i],R[j])
			A[k] = L[i]
			i+=1
		else:
			A[k] = R[j]
			j+=1
		k+=1
	while i < len(L):
		A[k] = L[i]
		i+=1
	while j < len(R):
		A[k] = R[j]
		j+=1				
	return A		

main()
