import pickle

class Hanzi:
	kDefinition="[no English definition]"
	kMandarin="[no Mandarin pronunciation]"
	kFrequency=0
	radical=0
	total_strokes=0
	
in_rev_hanzi_ucp=open('revised_hanzi_ucp.pickle','rb')
revised_hanzi_ucp=pickle.load(in_rev_hanzi_ucp)
in_rev_hanzi_ucp.close()

in_hanzi_dict=open('hanzi_dict.pickle','rb')
hanzi_dict=pickle.load(in_hanzi_dict)
in_hanzi_dict.close()

in_unihan_radical=open('Unihan_RadicalStrokeCounts.txt','r',encoding="utf8")

for line in in_unihan_radical:
    
