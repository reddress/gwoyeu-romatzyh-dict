import pickle
in_hanzi_ucp_set=open('hanzi_ucp_set.pickle','rb')
hanzi_ucp_set=pickle.load(in_hanzi_ucp_set)
in_hanzi_ucp_set.close()

class Hanzi:
	kDefinition="[no English definition]"
	kMandarin="[no Mandarin pronunciation]"
	kRadical=0
	kCangjie=""

hanzi_dict={}

in_unihan_readings=open('Unihan_Readings.txt','r',encoding='utf8')

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

in_unihan_radical=open('Unihan_RadicalStrokeCounts.txt','r',encoding='utf8')
for line in in_unihan_radical:
        tokens = line.rstrip().split('\t',3)
        if tokens[0] in hanzi_dict:
                if tokens[1] == 'kRSUnicode':
                        hanzi_dict[tokens[0]].kRadical=int(tokens[2].split('.')[0].strip("'"))
in_unihan_radical.close()

# string translation from romatzyh to hantzyh
inlst = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
outlst= ["日","月","金","木","水","火","土","竹","戈","十","大","中","一","弓","人","心","手","口","尸","廿","山","女","田","難","卜","重"]

in_unihan_dictlike=open('Unihan_DictionaryLikeData.txt','r',encoding='utf8')
for line in in_unihan_dictlike:
        tokens = line.rstrip().split('\t',3)
        if tokens[0] in hanzi_dict:
                if tokens[1] == 'kCangjie':
                        outstr = "'"
                        for c in tokens[2]:
                                outstr += outlst[inlst.index(c)]
                        outstr += "'"
                        hanzi_dict[tokens[0]].kCangjie=outstr
