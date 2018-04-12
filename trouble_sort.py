def trouble_sort(L):
    done = False
    while not done:
        done = True
        for i in range(len(L)-2):
            if L[i] > L[i + 2]:
                done = False
                L[i], L[i+2] = L[i+2], L[i]


T = int(input())

for t in range(1,T+1):
    N = int(input())
    V = [int(x) for x in input().split()]
    L = V.copy()

    trouble_sort(L)
    V.sort()
    #print(V,L)

    if L == V:
        print('Case #'+str(t)+': OK')
    else:
        for i in range(N-1):
            if L[i+1] < L[i]:
                print('Case #' + str(t) + ': '+str(i))
                break
