import pickle
in_hanzi_ucp_set=open('hanzi_ucp_set.pickle','rb')
hanzi_ucp_set=pickle.load(in_hanzi_ucp_set)
in_hanzi_ucp_set.close()

class Hanzi:
	kDefinition="[no English definition]"
	kMandarin="[no Mandarin pronunciation]"
	kRadical=0

hanzi_dict={}

in_unihan_readings=open('Unihan_Readings.txt','r',encoding='utf8')
in_unihan_radical=open('Unihan_RadicalStrokeCounts.txt','r',encoding='utf8')

for line in in_unihan_readings:
	tokens = line.rstrip().split('\t',3)
	if tokens[0] in hanzi_ucp_set:
		if tokens[0] not in hanzi_dict:
			hanzi_dict[tokens[0]]=Hanzi()
		if tokens[1] == 'kMandarin':
			hanzi_dict[tokens[0]].kMandarin=tokens[2]
		elif tokens[1] == 'kDefinition':
			hanzi_dict[tokens[0]].kDefinition=tokens[2]
in_unihan_readings.close()

for line in in_unihan_radical:
        tokens = line.rstrip().split('\t',3)
        if tokens[0] in hanzi_dict:
                if tokens[1] == 'kRSUnicode':
                        hanzi_dict[tokens[0]].kRadical=int(tokens[2].split('.')[0].strip("'"))

