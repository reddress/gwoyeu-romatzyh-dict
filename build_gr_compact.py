import hantools

gc_dict = {}

curindex = 0

for phr in HanPhraseList:
    if len(phr.hanziStr) < 6:
        gr = " ".join(map(hantools.py2gr,phr.pinyinExactStr.split()))
        if gr not in gc_dict:
            gc_dict[gr] = []
        gc_dict[gr].append(curindex)
    curindex += 1

        
