import pickle
import re

in_hanzi_ucp_set=open('hanzi_ucp_set.pickle','rb')
hanzi_ucp_set=pickle.load(in_hanzi_ucp_set)
in_hanzi_ucp_set.close()

in_unihan_dict=open('Unihan_DictionaryLikeData.txt','r',encoding='utf8')

search_cj={}

def add_cjcode(cj,ucp):
        if cj not in search_cj:
                search_cj[cj] = set()
        search_cj[cj].add(ucp)

for line in in_unihan_dict:
        tokens = line.rstrip().split('\t',3)
        if tokens[0] in hanzi_ucp_set:
                if tokens[1] == 'kCangjie':
                        cj = tokens[2].lower()
                        add_cjcode(cj, tokens[0])

in_unihan_dict.close()

out_search_cj=open('search_cj.pickle','wb')
pickle.dump(search_cj,out_search_cj)
out_search_cj.close()
