# stable_marriage.py

# This function returns true if 
# woman 'w' prefers man 'm1' over man 'm'
def wPrefersM1OverM(prefer, w, m, m1, N):
     
    # Check if w prefers m over her 
    # current engagement m1
    for i in range(N):
         
        # If m1 comes before m in list of w, 
        # then w prefers her current engagement,
        # don't do anything
        if (prefer[w][i] == m1):
            return True
 
        # If m comes before m1 in w's list, 
        # then free her current engagement 
        # and engage her with m
        if (prefer[w][i] == m):
            return False

def stable_marriage(N, Women_Pref, Men_Pref):
    Men_Free = [i for i in range(len(Men_Pref))]
    
    Matches = {k:-1 for k in range(len(Men_Pref))}
    key_list = list(Matches.keys())

    # the algorithm

    while len(Men_Free) > 0:
        for man in Men_Free:
            for woman in Men_Pref[man]:
                if woman not in list(Matches.values()):
                    Matches[man] = woman
                    Men_Free.remove(man)
                    break
                elif woman in list(Matches.values()):
                    current_suitor = list(Matches.keys())[list(Matches.values()).index(woman)]
                    w_list = Women_Pref[woman-1]
                    if w_list.index(man+1) < w_list.index(current_suitor+1):
                        Matches[man] = woman
                        Men_Free.remove(man)
                        Matches[current_suitor] = -1
                        Men_Free.append(current_suitor)
                        break

    d = {k:v for k,v in sorted(Matches.items(), key = lambda x: x[1])}
    l=[]
    for man in d.keys():
        l.append((man+1, d[man]))
    return l

    # # Stores partner of women. This is our output 
    # # array that stores passing information. 
    # # The value of wPartner[i] indicates the partner 
    # # assigned to woman N+i. Note that the woman numbers 
    # # between N and 2*N-1. The value -1 indicates 
    # # that (N+i)'th woman is free
    # wPartner = [-1 for i in range(N)]
 
    # # An array to store availability of men. 
    # # If mFree[i] is false, then man 'i' is free,
    # # otherwise engaged.
    # mFree = [False for i in range(N)]
 
    # freeCount = N
 
    # # While there are free men
    # while (freeCount > 0):
         
    #     # Pick the first free man (we could pick any)
    #     m = 0
    #     while (m < N):
    #         if (mFree[m] == False):
    #             break
    #         m += 1
 
    #     # One by one go to all women according to 
    #     # m's preferences. Here m is the picked free man
    #     i = 0
    #     while i < N and mFree[m] == False:
    #         w = boy_preferences[m][i]
 
    #         # The woman of preference is free, 
    #         # w and m become partners (Note that 
    #         # the partnership maybe changed later). 
    #         # So we can say they are engaged not married
    #         if (wPartner[w - 1] == -1):
    #             wPartner[w - 1] = m
    #             mFree[m] = True
    #             freeCount -= 1
 
    #         else: 
                 
    #             # If w is not free
    #             # Find current engagement of w
    #             m1 = wPartner[w - 1]
 
    #             # If w prefers m over her current engagement m1,
    #             # then break the engagement between w and m1 and
    #             # engage m with w.
    #             if (wPrefersM1OverM(girl_preferences, w, m, m1, N) == False):
    #                 wPartner[w - 1] = m
    #                 mFree[m] = True
    #                 mFree[m1] = False
    #         i += 1
 
    #         # End of Else
    #     # End of the for loop that goes 
    #     # to all women in m's list
    # # End of main while loop
 
    # # Print solution
    # l = []
    # for i in range(N):
    #     l.append((wPartner[i]+1, i+1))
    # print(l)
    # return l
