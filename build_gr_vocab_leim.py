#see original build_hklevel glossary

import pygr
import hantools
import pickle

class HanPhrase:
    hanziStr=""
    pinyinExactStr=""
    definition=""


in_grade_dict = open('grade_dict.pickle','rb')
grade_dict = pickle.load(in_grade_dict)
in_grade_dict.close()

in_HanPhraseList=open('HanPhraseList_compact.pickle','rb')
HanPhraseList=pickle.load(in_HanPhraseList)
in_HanPhraseList.close()


#grv_dict['jyyshyh'] = ['xx', 'yy']

#    hp = p.hanziStr
#    pe = p.pinyinExactStr
#    gr = "".join(map(hantools.py2gr,pe.split()))

gr_vocab_dict = dict()

def checkphr(phr):
    phrlen = len(phr.hanziStr)
    
    if phrlen > 5 or phrlen < 2:
        return False
    for c in phr.hanziStr:
        if hantools.c2u(c) not in grade_dict:
            return False
    return True

for phr in HanPhraseList:
        if checkphr(phr):
            hp = phr.hanziStr
            pe = phr.pinyinExactStr
            gr = "".join(map(hantools.py2gr,pe.split()))
            if gr not in gr_vocab_dict:
                gr_vocab_dict[gr] = []
            gr_vocab_dict[gr].append(hp)

out_grv_txt=open("gr_vocab_list.txt","w",encoding="utf8")

for k in gr_vocab_dict.keys():
	print('("'+k+'" [' , end="",file=out_grv_txt)
	for hp in gr_vocab_dict[k]:
		print('"'+hp+'"',end="",file=out_grv_txt)
	print('])',file=out_grv_txt)

out_grv_txt.close()
