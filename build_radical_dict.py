import pickle

def ucp2chr(ucp):
    return chr(int(ucp[2:],16))

def chr2ucp(ch):
    return "U+" + str(hex(ord(ch[0]))[2:]).upper()

class Radical:
	display=""
	pinyin="" # get from Unihan_Readings
	strokes=0 # get from Unihan_Dictionary
	definition="" # unihan_readings

in_unihan_radical=open('Unihan_RadicalStrokeCounts.txt','r')

radical_dict={}

for line in in_unihan_radical:
    tokens=line.rstrip().split('\t',3)
    if tokens[1] == 'kRSKangXi':
            rad_codes = tokens[2].split()
            rad_num = rad_codes[0].split('.')[0]
            if rad_codes[0].split('.')[1] == '0':
                    if rad_num not in radical_dict:
                            radical_dict[rad_num] = Radical()
                            radical_dict[rad_num].display = tokens[0]
                    else:
                            print("Radical number: " + rad_num + " Old: " + ucp2chr(radical_dict[rad_num].display) + " new: " + ucp2chr(tokens[0]))
                            prompt=input("Replace? ")
                            if prompt == 'y':
                                    radical_dict[rad_num].display = tokens[0]
                                    
                    
            
in_unihan_radical.close()

