def sortDesc(a):
    return a[1]
def sortAsc(a):
    return a[0]
with open("input.txt",'r') as file:
    lst=file.read().splitlines()
    testcase=int(lst[0])
    noLst=[]
    for i in range(1,testcase+1):
        noLst.append([int(n.strip()) for n in lst[i].strip().split('  ') if n!=''])
    noLst.sort(key=sortDesc,reverse=True)
    noLst.sort(key=sortAsc,)
    with open("output.txt",'a') as files:
        for el in noLst:
            files.write(str(el[0])+","+str(el[1])+","+str(el[2])+"\n")
