import pygr
import re
import hantools
import pickle

MAXLEN = 1
MAXGRADE = 6
OUTFILE="gr_grade6chars.txt"

class HanPhrase:
    hanziStr=""
    pinyinExactStr=""
    definition=""

in_HanPhraseList=open('HanPhraseList_compact.pickle','rb')
HanPhraseList=pickle.load(in_HanPhraseList)
in_HanPhraseList.close()

in_gradedict=open('grade_dict.pickle','rb')
grade_dict=pickle.load(in_gradedict)
in_gradedict.close()


def replaceTone(py):
    return re.sub('[0-9]','1',py)

def buildGlossary():
    glossary = []
    curindex = 0
    for phr in HanPhraseList:
        gradelvl = checkphr(phr)
        if gradelvl > 0:
            toneinfo = "".join(map(lambda x: x[-1], phr.pinyinExactStr.split()))
            pysyl = map(replaceTone, phr.pinyinExactStr.split())
            grsyl = " ".join(map(pygr.py2gr, pysyl))
            tmpGlossaryEntry = glossaryEntry()
            tmpGlossaryEntry.sortkey = str(gradelvl) + grsyl + " " + toneinfo
            tmpGlossaryEntry.phrindex = curindex
            glossary.append(tmpGlossaryEntry)
        curindex += 1
    return glossary

def checkphr(phr):
    global MAXLEN
    global MAXGRADE
#    printPhrase(phr)
    phrlen = len(phr.hanziStr)
    
    if phrlen > MAXLEN:
        return 0
        #return False
#gradesum = 0.01
    gradelst=[]
#    gradedist = "["
#    if ord(phr.pinyinList[0][0]) > 64 and ord(phr.pinyinList[0][0]) < 91:
#        return False
    for c in phr.hanziStr:
        if hantools.c2u(c) not in grade_dict:
            #return False
            return 0
        else:
            gradelst.append(grade_dict[hantools.c2u(c)])
#gradesum += grade_dict[hantools.c2u(c)]
#            gradedist += str(grade_dict[c])
#    gradedist += "]"
#    gradeavg = (gradesum / phrlen)
#    print("length: " + str(phrlen) + " gradeavg: " + str(gradeavg))
    if phrlen == 1:
        #if gradeavg < 1.9 or gradeavg > 3.1:
        #if gradeavg > MAXGRADE:
        if max(gradelst) > MAXGRADE:
            #return False
            return 0
    elif phrlen <= 3:
        #if gradeavg < 2.1 or gradeavg > 2.6:
        #if gradeavg > 2.1:
        if max(gradelst) > MAXGRADE:
            #return False
            return 0
##    print(gradedist, end=" ")
#    if phrlen == 1:
#        print(gradeavg, end=" ")
#        printPhrase(phr)
    return max(gradelst)

class glossaryEntry:
    sortkey = ""
    phrindex = 0
    gradekey = 0


gloss = buildGlossary()
gloss.sort(key = lambda x: x.sortkey)

out_gloss = open(OUTFILE,"w",encoding="utf8")

for entry in gloss:
    p = HanPhraseList[entry.phrindex]
    print(p.hanziStr + \
          " [" + " ".join(map(pygr.py2gr,p.pinyinExactStr.split())) + "] "+ p.definition, \
          file = out_gloss)
    
    #+ \
    #      " " + " ".join(p.hanziList) + " {" + p.pinyinExactStr.upper() + "}" + \
    #      "")
    
out_gloss.close()





