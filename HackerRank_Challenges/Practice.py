
def compareTriplets(a, b):
    score=[0,0]
    if len(a)==3 & len(b)==3:
        for i in range(3):
            if a[i]> b[i]:
                score[0]=score[0]+1
            elif a[i]<b[i]:
                score[1]=score[1]+1
            else:
                 pass
    return score



if __name__ == "__main__":
    a = list(map(int,input().strip().split()))[:3]
    b=  list(map(int,input().strip().split()))[:3]
    Result=list(compareTriplets(a,b))
    print(Result)


    