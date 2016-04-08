import pickle
in_hanzi_ucp_set=open('hanzi_ucp_set.pickle','rb')
hanzi_ucp_set=pickle.load(in_hanzi_ucp_set)
in_hanzi_ucp_set.close()

class Hanzi:
	kDefinition="[no English definition]"
	kMandarin="[no Mandarin pronunciation]"
	kFrequency=0

hanzi_dict={}
search_pinyin_exact={}
search_pinyin_fuzzy={}

in_unihan_readings=open('Unihan_Readings.txt','r',encoding='utf8')

for line in in_unihan_readings:
	tokens = line.rstrip().split('\t',3)
	if tokens[0] in hanzi_ucp_set:
		if tokens[0] not in hanzi_dict:
			hanzi_dict[tokens[0]]=Hanzi()
		if tokens[1] == 'kMandarin':
			hanzi_dict[tokens[0]].kMandarin=tokens[2]
			for kM_token in tokens[2].split():
				if kM_token not in search_pinyin_exact:
					search_pinyin_exact[kM_token]=set()
				search_pinyin_exact[kM_token].add(tokens[0])

				kM_stripped=kM_token[0:-1]
				if kM_stripped not in search_pinyin_fuzzy:
					search_pinyin_fuzzy[kM_stripped]=set()
				search_pinyin_fuzzy[kM_stripped].add(tokens[0])			
		elif tokens[1] == 'kDefinition':
			hanzi_dict[tokens[0]].kDefinition=tokens[2]
in_unihan_readings.close()
