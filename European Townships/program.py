with open("input.txt",'r') as file:
    lst=file.read().splitlines()
    testcase=int(lst[0])
    index=1
    while(index<len(lst)):
        house=int(lst[index])
        index+=1
        rooms=[]
        for i in range(0,house):
            rooms.append([int(no) for no in lst[index].split(',')])
            index+=1
        hrs,accentQty,regularQty=0,0,0
        for room in rooms:
            hrs+=(2*2.5+4*3.25)*room[3]+room[2]*(4*2.5/3+8*3.25/3)+room[1]*(2.5+3.25*2)
            accentQty+=1.5*(2*room[3]+room[2]*4/3+room[1])
            regularQty+=2.25*(4*room[3]+room[2]*8/3+room[1]*2)
        hrs,accentQty,regularQty=round(hrs,2),round(accentQty,2),round(regularQty,2)
        with open("output.txt",'a') as files:
            files.write(str(hrs)+' '+str(accentQty)+' '+str(regularQty)+'\n')
