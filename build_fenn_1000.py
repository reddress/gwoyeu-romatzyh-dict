import pickle
import hantools

class Hanzi:
	kDefinition="[no English definition]"
	kMandarin="[no Mandarin pronunciation]"
	kRadical=0
	kCangjie=""
	kFrequency=6

in_hanzi_dict=open('hanzi_dict.pickle','rb')
hanzi_dict=pickle.load(in_hanzi_dict)
in_hanzi_dict.close()

in_hanzi_ucp_set=open('hanzi_ucp_set.pickle','rb')
hanzi_ucp_set=pickle.load(in_hanzi_ucp_set)
in_hanzi_ucp_set.close()

in_dictlike=open("Unihan_DictionaryLikeData.txt","r",encoding="utf-8")


counter = 0

fout = open("fenn1000.txt", "w", encoding="utf-8")

#for ucp in hanzi_lst:
for line in in_dictlike:
        tokens=line.split()
        #if hanzi_dict[ucp].kFrequency < 6:
        if tokens[1]=="kFenn":
                #print(tokens[2] + " " + tokens[0])
                if (tokens[0] in hanzi_ucp_set) and (("A" in tokens[2]) or ("B" in tokens[2])):
                        try:
                                ucp=tokens[0]
                                char_tzyh = hantools.u2c(ucp)
                                char_cj = hanzi_dict[ucp].kCangjie.strip("'")
                                #print(char_cj)
                                char_pystr = hanzi_dict[ucp].kMandarin
                                if char_pystr == "[no Mandarin pronunciation]":
                                        char_pystr = 'x'
                                char_pylst = char_pystr.split()
                                char_grlst = list(map(hantools.py2gr,char_pylst))
                                char_def = hanzi_dict[ucp].kDefinition
                                counter += 1

                                print(char_tzyh + " " + str(char_grlst) + " " + char_def + " (" + char_cj + ")", file=fout)
                                #for syl in char_grlst:
                                #        syl=syl.strip('.')
                                #        if syl not in gr2cj_dict:
                                #                gr2cj_dict[syl]=[]
                                #gr2cj_dict[syl].append(char_tzyh + " (" + char_cj + ")")
                        except:
                                #print(ucp + " " + hantools.u2c(ucp) +  " not found.")
                                pass
