*arr,=map(int,open("input").readlines())
*cv_arr,=map(sum,zip(arr,arr[1:],arr[2:]))
print(sum(x>y for x,y in zip(cv_arr[1:],cv_arr)))