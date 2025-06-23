# Given A Sorted Array and target find the index place of that target if found else return not found
def bs(A,x):
  lo=0
  hi=len(A)-1
  while(lo<=hi):
    mid=(lo+hi)//2
    if(A[mid]==x):
      return mid;
    elif A[mid] <x:
      lo=mid+1
    else:
      hi=mid-1
  return "Not Found"


A=[1,2,3,4,5,6,8,9,10]
target=25
res=bs(A,target)
print(res)
