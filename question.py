//1
n,m=map(int,input().split())
mat=[]
res=[]
for i in range(n):
    arr=list(map(int,input().split()))
    mat.append(arr)
for i in range(m):
    mn=999999999
    for j in range(n):
        x=mat[j][i]
        mn=min(x,mn)
    res.append(mn)
print(*res)
//2
tc=int(input())
for i in range(tc):
   bri,gro=map(int,input().split())
   if bri>=18 and gro>=21:
       print("Marry")
   else:
       print("Can't Marry")

//3
def solve(st):
    di={}
    for i in range(len(st)):
            di[st[i]]=1
            if(st[i]=="B" and di.get("b")==None):
                print("NO")
                return
            elif(st[i]=="S" and di.get("s")==None):
                print("NO")
                return
            if(st[i]=="G" and di.get("g")==None):
                print("NO")
                return
    print("YES")
def inpu():
    t=int(input())
    for i in range(t):
        st=input()
        solve(st)
inpu()
//4
n,m=map(int,input().split())
mat=[]
for i in range(n):
    arr=list(map(int,input().split()))
    mat.append(arr)
for i in range(m):
    for j in range(n):
        print(mat[j][i],end=" ")
    print()
//5
tc=int(input())
for i in range(tc):
    mat=[]
    n,m=map(int,input().split())
    for j in range(n):
        arr=list(map(int,input().split()))
        mat.append(arr)
    
    if m!=n:
        print(-1)

    else:
        di = {};
        for i in range(n):
            for j in range(m):
                if i==j or i+j==n-1:
                        di[mat[i][j]]=1
        product=1
        for k,v in di.items():
            product*=k
        print(product)