"""
def strcounter(s):
    for sym in set (s) :
        count = 0
        for subsym in s :
            if sym == subsym:
                count+=1
        print (sym,count)

strcounter("abbcdaa")
"""



def strcounter(s):      #O
    syms_counter={}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym,0) + 1
    for sym,count in syms_counter.items():
        print(sym,count)

strcounter('adcnra')





