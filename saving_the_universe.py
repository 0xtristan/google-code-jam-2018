def calc_damage(p):
    damage = 0
    multiplier = 1
    for x in p:
        if x == 'C':
            multiplier*=2
        else:
            damage += multiplier
    return damage


T = int(input())

for t in range(1,T+1):
    test = input().split()
    d = int(test[0]) # shield amount
    p = list(test[1]) # string representing the attack sequence

    # Physically impossible if number of S outweighs d no matter how its rearranged
    if test[1].count('S') > d:
        print('Case #' + str(t) + ': IMPOSSIBLE')
        continue

    inv_num = 0
    while calc_damage(p) > d:
        # We want to make an inversion between the last 'CS' pair
        prev = p[-1]
        canInvert = False
        for i in reversed(range(len(p))):
            if p[i] == 'C' and prev == 'S':
                # Invert
                p[i], p[i+1] = p[i+1], p[i]
                inv_num+=1
                canInvert = True
                break
            prev = p[i]
    print('Case #'+str(t)+': '+str(inv_num))