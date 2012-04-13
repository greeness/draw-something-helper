import sys
from itertools import combinations

def reg(word):
    return ''.join(sorted(word))

def load_dic():
    dic = {}
    for word in file("fulldictionary00.txt"):
        wid = reg(word.strip())
        if wid not in dic:
            dic[wid] = set()
        dic[wid].add(word.strip())
    return dic

if __name__ == '__main__':
    dic = load_dic()
    
    distinct = set()
    for choice in combinations(reg(sys.argv[1]), int(sys.argv[2])):
        wid = reg(list(choice))
        if wid not in dic: continue
        #print wid, dic[wid]
        for w in dic[wid]:
            distinct.add(w)
    print "All possible words:\n","="*60
    for i,w in enumerate(sorted(distinct)):
        print "%3d, %s" %(i, w)