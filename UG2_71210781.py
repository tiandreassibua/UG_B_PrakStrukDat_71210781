def deret_ajaib(n):
    data = [1,2,3,4,5]
    for i in range(1, n+1):
        if i > len(data)+1:
            data.append((i-2)+(i//2))
    return data
print(deret_ajaib(10))