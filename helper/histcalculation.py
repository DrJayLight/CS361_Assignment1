import re

def hist_calc(string):
    f=string
    divider=re.compile('\\W*')
    ff=[s for s in divider.split(f) if s !='' and s.isalpha()]
    hist={}
    for each in ff:
        if each in hist:
            hist[each]+=1
        hist.setdefault(each,1)
    return hist.items()


