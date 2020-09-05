"""The included code stub will read an integer, n , from STDIN.
Without using any string methods, try to print the following:
123..n"""
if __name__ == '__main__':
    n = int(input())
for x in range(1,n+1):#n+1 yazmagimizin sebebi n-de daxil etmekdir
   print(x,end="")



"""n=int(input("Eded daxil edin:"))
for x in range(1,n+1):
    print(x,end="")"""
#Default olaraq print funksiyasin sonu /n-lƏ bitir.
## Python’un print () funksiyası ‘end’ adlı bir parametrlə gəlir.
#Default olaraq  bu parametrin dəyəri ‘\ n’, yəni yeni sətir simvoludur