import pickle
import fnmatch
import hantools
import datetime

# show cangjie in printphrase
SHOWCJ = False

# use with j, jj, jt commands
LASTJ = ""

# global, last entered, chosen cangjie character
last_cj = "U+3007"

# FEATURE IDEAS
#
# see deprecated ideas in load_all.py
#
# sorting list of Hanzi:
# mysorted=sorted(mylst,key=lambda x: x.kRadical)

class MemoItem:
    phrIndex = 0
    dateAdded = ""
    comment = ""

class HanPhrase:
    hanziStr=""
    pinyinExactStr=""
    definition=""

class Radical:
	display=""
	pinyin=""
	strokes=0
	definition=""
	number=0

class Hanzi:
	kDefinition="[no English definition]"
	kMandarin="[no Mandarin pronunciation]"
	kRadical=0
	kCangjie=""
	kFrequency=6

# cangjie code -> hanzi
in_search_cj = open('search_cj.pickle','rb')
search_cj = pickle.load(in_search_cj)
in_search_cj.close()

def show_cj_match(cj):
    global last_cj
    try:
        ctr = 1
        choice = 1
        cjcharlst=sorted(search_cj[cj])
        for ucp in cjcharlst:
            print(str(ctr) + ". ", end="")
            hanziview(ucp)
            ctr += 1
        #if len(cjcharlst) > 1:
        #    user_in = input("Choose a number from above (leave blank for 1.): ")
        #    if user_in.strip() == "":
        #        pass
        #    else:
        #        choice = int(user_in)
        last_cj = cjcharlst[choice-1]
    except:
        print("Could not find Cangjie code: " + cj + " or error interpreting choice")

in_radical_list = open('radical_list.pickle','rb')
radical_list = pickle.load(in_radical_list)
in_radical_list.close()

def radview(n):
    rad = radical_list[n]
    print(str(rad.number) + " /" + str(rad.strokes) + "/ " + \
          rad.display + " [" + hantools.py2gr(rad.pinyin) + "] " + rad.definition + " {" + rad.pinyin + "}")

def radcompact(n):
    try:
        rad = radical_list[n]
        print("[" + str(rad.number) + " " + rad.display + "] ", end="")
    except:
        print("Radical outside range 1-214")
    
def raddef(d):
    for i in range(1,215):
        if fnmatch.fnmatch(radical_list[i].definition, "*"+d+"*"):
            radview(i)

def radstr(s):
    try:
        ct = 0
        print("  ", end = "")
        for i in range(1,215):
            if s == radical_list[i].strokes:
                radcompact(i)
                ct += 1
                if ct % 10 == 0:
                    print("")
                    print("  ", end = "")
    except:
        print("error printing radical list")

in_hanzi_dict=open('hanzi_dict.pickle','rb')
hanzi_dict=pickle.load(in_hanzi_dict)
in_hanzi_dict.close()

in_search_rad=open('search_rad.pickle','rb')
search_rad=pickle.load(in_search_rad)
in_search_rad.close()

# View cangjie codes for all chars in a string
def showcj(s):
    try:
        for c in s:
            print(" " + c + " (" + hanzi_dict[hantools.c2u(c)].kCangjie + ")    ", end="")
        print()
        print()
    except:
        print("Error: " + c + " not found in Hanzi dict")
        print()

def hanziview(ucp):
        try:
            h = hanzi_dict[ucp]
            pe = h.kMandarin
            rad = h.kRadical
            gr = ", ".join(map(hantools.py2gr,pe.split()))
            cj = h.kCangjie
            print("(" + str(rad) + " " + radical_list[rad].display + ") " + chr(int(ucp[2:],16)) + " [" + gr + "] " + h.kDefinition + " (" + ucp + ")" + " {" + pe + "} " + cj)
        except KeyError:
            print("[no further information]")

def show_rc_match(rc):
    try:
        for ucp in search_rad[rc]:
            hanziview(ucp)
    except:
        print("Could not match radical with remaining strokes: " + rc)

in_HanPhraseList=open('HanPhraseList_compact.pickle','rb')

HanPhraseList=pickle.load(in_HanPhraseList)
in_HanPhraseList.close()

#load gr2py
in_gr2py=open('gr2py.pickle','rb')
gr2py=pickle.load(in_gr2py)
in_gr2py.close()

#load gc_compact (exact Gwoyeu Romatzyh dict)
in_gcdict=open('gc_dict.pickle','rb')
gc_dict=pickle.load(in_gcdict)
in_gcdict.close()

print("Run dictloop() function for a simple command-line interface.")
charlim = 20
showidiom = False

memodict = {}
curmemo = "no memo"

#define cangjie typing rows
cj_homepos=['A','S','D','F','J','K','L']
cj_homerow=cj_homepos.extend(['G','H'])

def cj_in(cj, lst):
    res = True
    for c in cj:
        if c not in lst:
            return False
    return res

#load memo file
def loadMemo():
    global curmemo
    promptload = input("Load memo pickle: unsaved changes will be lost: are you sure? (y/n) ")
    if promptload == "y":
        global memodict
        print("Loading memo pickle...")
        in_memofile= open('memodict.pickle', 'rb')
        memodict = pickle.load(in_memofile)
        in_memofile.close()
        curmemo = "scratch"

def saveMemo():
    global memodict
    print("Saving memo pickle...")
    out_memo = open('memodict.pickle', 'wb')
    pickle.dump(memodict, out_memo)
    out_memo.close()

def timestamp():
    dtoday = datetime.datetime.today()
    dyr = str(dtoday.year)[2:4]
    dmo = str(dtoday.month)
    ddy = str(dtoday.day)

    if dtoday.month < 10:
        dmo = "0" + dmo
    if dtoday.day < 10:
        ddy = "0" + ddy
    return dyr + "-" + dmo + "-" + ddy

def charGRStr(i):
    p = HanPhraseList[i]
    hp = p.hanziStr
    pe = p.pinyinExactStr
    gr = " ".join(map(hantools.py2gr,pe.split()))
    return(hp + " [" + gr + "]")

def choosePhr(i,h,g,e):
    p = HanPhraseList[i]
    hp = p.hanziStr
    pe = p.pinyinExactStr
    gr = " ".join(map(hantools.py2gr,pe.split()))
    en = p.definition
    res = ""
    if h:
        res += hp + " "
    if g:
        res += "[" + gr + "] "
    if e:
        res += en
    return res

def printPhrase(p):
    global charlim
    global showidiom
    global SHOWCJ
    
    defn = p.definition
    if showidiom == False:
        if fnmatch.fnmatch(defn,"*(idiom)*"):
            return
    hp = p.hanziStr
    pe = p.pinyinExactStr
    gr = " ".join(map(hantools.py2gr,pe.split()))
    ucps = " ".join(map(hantools.c2u,list(hp)))
    if len(hp) <= charlim:
        print(hp + " [" + gr + "] " + defn + " " + ucps + " {" + pe + "}")
        #print(hp + " [" + gr + "] " + defn)
        # set SHOWCJ to False to remove cangjie codes
        if SHOWCJ:
            showcj(hp)

def pinyinFuzzy(mystr):
    pinyinExact("? ".join(mystr.split()) + "?")

lastresults=[]

def pinyinExact(mystr):
    global lastresults
    lastresults = []
    resultsindex = 0
    curindex = 0
    for phrase in HanPhraseList:
        if fnmatch.fnmatch(phrase.pinyinExactStr, mystr):
            print("{"+str(resultsindex)+"} ", end="")
            printPhrase(phrase)
            lastresults.append(curindex)
            resultsindex += 1
        curindex += 1

# direct search
def tzyh(mystr):
#    global lastresults
#    lastresults = []
#    resultsindex = 0
#    curindex = 0
    for phrase in HanPhraseList:
        if fnmatch.fnmatch(phrase.hanziStr, mystr):
#            print("{"+str(resultsindex)+"} ", end="")
            printPhrase(phrase)
#            lastresults.append(curindex)
#            resultsindex += 1
#        curindex += 1


lowerlst = [' ','',"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
cjlst= [' ','',"日","月","金","木","水","火","土","竹","戈","十","大","中","一","弓","人","心","手","口","尸","廿","山","女","田","難","卜","z"]

def abc2cjcode(abc):
    out = "'"
    for c in abc:
        try:
                out += cjlst[lowerlst.index(c)]
        except:
                pass
    return out + "'"

def cj2tzyh(cj):
    out = ""
    print(abc2cjcode(cj) + " " , end="")
    try:
        choice = 1
        cjcharlst=sorted(search_cj[cj])
        if len(cjcharlst) > 1:
            print(">>> Choose for code " + abc2cjcode(cj))
            for i in range(0,len(cjcharlst)):
                    print(str(i+1) + ". ", end="")
                    hanziview(cjcharlst[i])
            user_in = input("Choose a number from above (leave blank for 1.): ")
            if user_in.strip() == "":
                pass
            else:
                choice = int(user_in)
        out = cjcharlst[choice-1]
    except:
        print("Could not find Cangjie code: " + cj + " or error interpreting choice")
        out = "U+3007" # ling 0
    return hantools.u2c(out)

def abcphr2tzyh(s):
        out = ""
        for w in s.split():
                if w == "*":
                        out += "*"
                else:
                        out += cj2tzyh(w)
        return out


def showAllLastResults():
    global lastresults
    for i in lastresults:
        printPhrase(HanPhraseList[i])

def showPhrIndexFromLastResults(i):
    global lastresults
    try:
        return lastresults[i]
    except:
        print("Index out of range")

def phraseDef(mydef):
    for phrase in HanPhraseList:
        if fnmatch.fnmatch(phrase.definition, mydef):
            printPhrase(phrase)

def wordSearch(w):
    phraseDef("*/"+w+"/*")

def hanziSearch(ucp):
    for phrase in HanPhraseList:
        if hantools.u2c(ucp) in phrase.hanziStr:
            printPhrase(phrase)

def hanziBeginsWith(ucp):
    hchar = hantools.u2c(ucp)
    if hchar == 'x':
        print("Please enter a valid hex UCP. e.g. 123a")
    else:
        for phrase in HanPhraseList:
            if hantools.u2c(ucp) == phrase.hanziStr[0]:
                printPhrase(phrase)

#def joinUCPPinyin(ucp,myp):
#    for phrase in HanPhraseList:
#        if ucp in phrase.hanziList and myp in phrase.pinyinList:
#            printPhrase(phrase)

def stripGR(gr):
    try:
        if gr == '*':
            return '*'
        else:
            return gr2py[gr][0:-1]
    except KeyError:
        print("WARNING: GR not found: " + gr)
        return "v"
    
def grfuzzy(gr):
    pinyinFuzzy(" ".join(map(stripGR, gr.split())))

def gr2pytone(gr):
    try:
        if gr == '*':
            return '*'
        else:
            return gr2py[gr]
    except KeyError:
        print("WARNING: GR not found: " + gr)
        return "v"

def grexact(gr):
    pinyinExact(" ".join(map(gr2pytone, gr.split())))

def grcompact(gr):
    global lastresults
    lastresults = []
    resultsindex = 0
    curindex = 0

    if gr in gc_dict:
        for i in gc_dict[gr]:
            print("{"+str(resultsindex)+"} ", end="")
            printPhrase(HanPhraseList[i])
            lastresults.append(i)
            resultsindex += 1

def dictloop():
    user_input="z"
    cmd="z"
    cur_rad = 1
    global charlim
    charlim = 3
    global showidiom
    showidiom = False
    global curmemo
    global memodict
    global lastresults
    global SHOWCJ
    global last_cj
    global LASTJ

    print("Enter 'mb' to load memo files if this is the first time running dictloop.")

    if len(memodict.keys()) > 0:
        print("Memo contains " + str(len(memodict.keys())) + " word lists.")
    else:
        print("Loading memo pickle...")
        in_memofile= open('memodict.pickle', 'rb')
        memodict = pickle.load(in_memofile)
        in_memofile.close()
        curmemo = "scratch"

    print("Press h for help. Enter command token followed by arguments.")

    while cmd != "q":
        radcompact(cur_rad)
        print("[", end="")
        if SHOWCJ:
            print("CJ ", end="")
        print(hantools.u2c(last_cj[2:6]) + "] ", end="")
        if showidiom == True:
            print("(idOn ", end="")
        else:
            print("(iOff ", end="")
        print("c<=" + str(charlim) + ") " + curmemo, end = "")
        user_input=input(" >>> ")
        if len(user_input) == 0:
            cmd = 'h'
            args = ''
        else:
            try:
                cmd = user_input.split()[0]
            except:
                print("error parsing command. enter h for help")
                cmd = "0"
            args = " ".join(user_input.split()[1:])
        #print("received command : " + cmd + " with args " + args)

        if cmd == 'pf':
            pinyinFuzzy(args)
        elif cmd == 'pe':
            pinyinExact(args)
        elif cmd == 'w':
            wordSearch(args)
        elif cmd == 'phr':
            phraseDef("*" + args + "*")
        elif cmd == 'gf':
            if len(args.split()) > charlim:
                print("Warning: character limit less than arguments. Resetting character limit.")
                charlim = len(args.split())
            grfuzzy(args)
        elif cmd == 'ge':
            if len(args.split()) > charlim:
                print("Warning: character limit less than arguments. Resetting character limit.")
                charlim = len(args.split())
            grexact(args)
        elif cmd == 'hs':
            if len(args) < 3:
                hanziSearch(last_cj[2:6])
            else:
                hanziSearch(args)
        elif cmd == 'hb':
            if len(args) < 3:
                hanziBeginsWith(last_cj[2:6])
            else:
                hanziBeginsWith(args)
        elif cmd == 'rs':
            if len(args) < 1:
                print ("enter a number")
            else:
                try:
                    radstr(int(args))
                    print("")
                except:
                    print("please enter a number")
        elif cmd == 'i':
            if showidiom == False:
                showidiom = True
                charlim = 8
            else:
                showidiom = False
                charlim = 3
        elif cmd == 'll':
            charlim = 3
        elif cmd == 'l':
            try:
                charlim = int(args)
            except:
                charlim = 20
                print("Enter the character limit as [1-20]. Reverting to 20.")
        elif cmd == 'c':
                try:
                    cur_rad = int(args)
                except:
                    print("Radical not valid.")
        elif cmd == 'rd':
                raddef(args)
        elif cmd == 'rv':
                radview(cur_rad)
        elif cmd == 's':
                show_rc_match(str(cur_rad) + "." + args)
        elif cmd == 'resall':
            showAllLastResults()
        elif cmd == 'resi':
            showPhrIndexFromLastResults(int(args))

        # memo commands
        elif cmd == 'mb':
            loadMemo()
        elif cmd == 'ml':
            if len(args) < 1:
                print("Please enter a word list name. 'mf' for all word lists")
            else:
                curmemo = args
                if args not in memodict:
                    memodict[curmemo] = []
                print("Visiting memo word list " + curmemo + ": (" + str(len(memodict[curmemo])) + ")")
        elif cmd == 'ms':
            saveMemo()
        elif cmd == 'mf':
            lstnames = sorted(memodict.keys())
            for f in lstnames:
                print(f + " (" + str(len(memodict[f])) + ")")
        elif cmd == 'ma':
            if len(args) < 1:
                print("Enter the index from the last 'ge' results.")
            else:
                try:
                    addindex = showPhrIndexFromLastResults(int(args))
                    charGR = charGRStr(addindex)
                    promptcomments = input("[" + charGR + "] Add any additional comments (x to cancel): ")
                    if promptcomments == 'x':
                        print ("Add action canceled.")
                    else:
                        tmpMemoItem = MemoItem()
                        tmpMemoItem.phrIndex = addindex
                        tmpMemoItem.dateAdded = timestamp()
                        tmpMemoItem.comment = promptcomments
                        memodict[curmemo].append(tmpMemoItem)
                        #charGR = charGRStr(addindex)
                        print("adding HanPhraseList index " + str(addindex) + " " + charGR)
                        print("Don't forget 'ms' to save the memo pickle when done.")
                except:
                    print("error adding phrase to word list")
        elif cmd == 'md':
            print('to be implemented')
        elif cmd == 'mr':
            print('to be implemented')
        elif cmd == 'mi':
            lastresults=[]
            lastresults.append(1)
            mi_i = 1
            for mi in memodict[curmemo]:
                lastresults.append(mi.phrIndex)
                print(str(mi_i) + ". {"+str(mi.phrIndex)+"} " + charGRStr(mi.phrIndex) + " " + mi.comment + " " + HanPhraseList[mi.phrIndex].definition + " [" + mi.dateAdded + "]")
                if SHOWCJ:
                    showcj(HanPhraseList[mi.phrIndex].hanziStr)
                
                mi_i += 1
        elif cmd == 'mc':
            for mi in memodict[curmemo]:
                print(choosePhr(mi.phrIndex,True,False,False))
        elif cmd == 'mg':
            for mi in memodict[curmemo]:
                print(choosePhr(mi.phrIndex,False,True,False))
        elif cmd == 'me':
            for mi in memodict[curmemo]:
                print(choosePhr(mi.phrIndex,False,False,True))
        elif cmd == 'desc':
            if len(args) < 1:
                print("Enter a HanPhraseList index number.")
            else:
                try:
                    phr = HanPhraseList[showPhrIndexFromLastResults(int(args))]
                    printPhrase(phr)
                    for c in phr.hanziStr:
                        hanziview(hantools.c2u(c))
                except:
                    print("error describing phrase. use index from 'v' search results.")
        elif cmd == 'v':
            if len(args.split()) > charlim:
                print("Warning: character limit less than arguments. Resetting character limit.")
                charlim = len(args.split())
            grcompact(args)
        elif cmd == 'ccj':
            showcj(args)
        elif cmd == 'n':
            cur_rad += 1
        elif cmd == 'scj':
            if SHOWCJ:
                print("Turning off phrase cangjie display.")
                SHOWCJ = False
            else:
                print("Activating phrase cangjie display.")
                SHOWCJ = True
        elif cmd == 'z' or cmd == 'cj':
            show_cj_match(args)
        elif cmd == 'cs':  # combines hs with saved "last_cj"
            hanziSearch(last_cj[2:6].lower())
        elif cmd == 'cb':
            hanziBeginsWith(last_cj[2:6].lower())
        elif cmd == 'tz':
            tzyh(args)
        elif cmd == 'jk':
            mytzyh = abcphr2tzyh(args)
            print(mytzyh)
            LASTJ=mytzyh
            print("Set LASTJ to " + LASTJ)
        elif cmd == 'jj':
            print("Direct search on LASTJ " + LASTJ)
            print()
            tzyh(mytzyh)
        elif cmd == 'j':
            if len(args) < 1:
                print("Enter chars as cangjie separated by spaces. Wildcard * allowed")
            else:
                mytzyh = abcphr2tzyh(args)
                print()
                if '〇' in mytzyh:
                    print("Fix 〇 from " + mytzyh)
                else:
                    print("Direct search on " + mytzyh)
                    print()
                    tzyh(mytzyh)
        elif cmd == 'h':
            print("""Help:
Display Commands
================
l n: limit display to phrases with n or fewer characters
ll: set character limit to 5
i: toggle idiom display

Character Commands
==================
c n: change radical to n
rs n: show radicals with n strokes
rd d: show radicals with definition d
rv: view current radical's details
s: remaining strokes beyond radical (uses current chosen radical)
cj s: show Cangjie codes for Hanzi string s

Phrase Commands
===============
pf: pinyinFuzzy
pe: pinyinExact
w: wordSearch
phr: phraseDef
gf: grfuzzy
ge: grexact
hs: hanziSearch (enter Unicode Code Point 4-digit hex lowercase, e.g. 9f8d)
hb: hanziBeginsWith

Memo File Commands
==================
mb:   memo begin: load pickle from file.  defaults to "scratch" word list
mf:   show all existing word list names
ml f: visit word list f
ms:   save all memo word lists into pickle
ma n: add phrase from last result set with index n into current word list
md n: delete all phrases matching HanPhraseList index n, if exists

Memo Review Commands
====================
mr: randomize word order (cannot undo)
mi: show all HanPhraseIndex, characters, and Gwoyeu Romatzyh
mc: show all characters from current word list
mg: show all Gwoyeu Romatzyh from current word list
me: show all English definitions from current word list

Quick command
=============
v gr: show phrases matching exact gr

q: exit""")
        elif cmd == 'q':
            promptsave = input("Save memo pickle? (y/n) ")
            if promptsave == 'y':
                saveMemo()
                print("Memo pickle saved.")
            print('Goodbye.')
        else:
            print("'" + cmd + "' command unknown. Enter h for help.")
