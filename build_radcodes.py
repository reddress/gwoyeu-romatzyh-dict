outlst = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
inlst = ["日","月","金","木","水","火","土","竹","戈","十","大","中","一","弓","人","心","手","口","尸","廿","山","女","田","難","卜","重"]

fin = open("cj_rads.txt",'r',encoding='utf8')

ctr = 0
for line in fin:
    tokens = line.split()
    print("'", end="")
    
    for c in tokens[1]:
        #print (c)
        print(outlst[inlst.index(c)].lower(),end="")
    print("', #" + str(ctr) + " \\")
    ctr += 1

    
