import pickle

def ucp2chr(ucp):
    return chr(int(ucp[2:],16))

def chr2ucp(ch):
    return "U+" + str(hex(ord(ch[0]))[2:]).upper()


in_unihan_data=open('Unihan_DictionaryLikeData.txt','r',encoding='utf8')

grade_dict={}

for line in in_unihan_data:
    tokens=line.rstrip().split('\t',3)
    if tokens[1] == 'kGradeLevel':
        grade_dict[tokens[0]] = int(tokens[2]);
            
in_unihan_data.close()

out_gradedict = open('grade_dict.pickle','wb')
pickle.dump(grade_dict, out_gradedict)
out_gradedict.close()
