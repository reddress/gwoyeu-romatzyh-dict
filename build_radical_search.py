import pickle
import re

in_hanzi_ucp_set=open('hanzi_ucp_set.pickle','rb')
hanzi_ucp_set=pickle.load(in_hanzi_ucp_set)
in_hanzi_ucp_set.close()

in_hanzi_ucp_set=open('hanzi_ucp_set.pickle','rb')
hanzi_ucp_set=pickle.load(in_hanzi_ucp_set)
in_hanzi_ucp_set.close()

in_unihan_rad=open('Unihan_RadicalStrokeCounts.txt','r',encoding='utf8')

search_rad={}

def add_radcode(rc,ucp):
        if rc not in search_rad:
                search_rad[rc] = set()
        search_rad[rc].add(ucp)

for line in in_unihan_rad:
        tokens = line.rstrip().split('\t',3)
        if tokens[0] in hanzi_ucp_set:
                if tokens[1] == 'kRSKangXi' or tokens[1] == 'kRSUnicode':
                        tokens_rc = tokens[2].split()
                        for rc in tokens_rc:
                                rcclean = re.sub("\'","",rc)
                                add_radcode(rcclean, tokens[0])

in_unihan_rad.close()

out_search_rad=open('search_rad.pickle','wb')
pickle.dump(search_rad,out_search_rad)
out_search_rad.close()
