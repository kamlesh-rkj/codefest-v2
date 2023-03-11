import math

T = int(input())

for i in range(1, T+1):
    N = int(input())
    H_total = A_total = R_total = 0
    
    for j in range(1, N+1):
        l=[int(input()) for i in range(1,4)]
        H,S,R = l
        W_total = 6*H + 4*S + 3*R
        A = (1/3)*W_total*1.5
        R = (2/3)*W_total*2.25
        H = (1/3)*W_total*2.5 + (2/3)*W_total*3.25
        H_total += H
        A_total += A
        R_total += R
        
    print("Case #%d: %.2f, %.2f, %.2f" % (i, H_total, A_total, R_total))
