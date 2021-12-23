*arr,=map(int,open("input").readlines())
print(sum(x>y for x,y in zip(arr[1:],arr)))