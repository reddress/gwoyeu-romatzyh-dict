def u2c(raw):
    try:
        ucp = raw.upper()
        if ucp[0:2].upper() != "U+":
            ucp = "U+" + ucp
        return chr(int(ucp[2:],16))
    except:
        print("Error interpreting UCP " + raw)
        return "x"

def c2u(ch):
    return "U+" + str(hex(ord(ch[0]))[2:]).upper()

gr_lmnr=['l','m','n','r']
gr_jqx=['j','q','x']

gr_special={'zhi': ['jy', 'jyr', 'jyy', 'jyh'], \
            'chi': ['chy', 'chyr', 'chyy', 'chyh'], \
            'shi': ['shy', 'shyr', 'shyy', 'shyh'], \
            'ri': ['ry', 'ryr', 'ryy', 'ryh'], \
            'zi': ['tzy', 'tzyr', 'tzyy', 'tzyh'], \
            'ci': ['tsy', 'tsyr', 'tsyy', 'tsyh'], \
            'si': ['sy', 'syr', 'syy', 'syh'], \
            'ju': ['jiu', 'jyu', 'jeu', 'jiuh'], \
            'qu': ['chiu', 'chyu', 'cheu', 'chiuh'], \
            'xu': ['shiu', 'shyu', 'sheu', 'shiuh'], \
            'yi': ['i', 'yi', 'yii', 'yih'], \
            'ya': ['ia', 'ya', 'yea', 'yah'], \
            'yo': ['io', 'yo', 'yeo', 'yoh'], \
            'ye': ['ie', 'ye', 'yee', 'yeh'], \
            'yai': ['iai', 'yai', 'yeai', 'yay'], \
            'yao': ['iau', 'yau', 'yeau', 'yaw'], \
            'you': ['iou', 'you', 'yeou', 'yow'], \
            'yan': ['ian', 'yan', 'yean', 'yann'], \
            'yin': ['in', 'yn', 'yiin', 'yinn'], \
            'yang': ['iang', 'yang', 'yeang', 'yanq'], \
            'ying': ['ing', 'yng', 'yiing', 'yinq'], \
            'yong': ['iong', 'yong', 'yeong', 'yonq'], \
            'wu': ['u', 'wu', 'wuu', 'wuh'], \
            'wa': ['ua', 'wa', 'woa', 'wah'], \
            'wo': ['uo', 'wo', 'woo', 'woh'], \
            'wai': ['uai', 'wai', 'woai', 'way'], \
            'wei': ['uei', 'wei', 'woei', 'wey'], \
            'wan': ['uan', 'wan', 'woan', 'wann'], \
            'wen': ['uen', 'wen', 'woen', 'wenn'], \
            'wang': ['uang', 'wang', 'woang', 'wanq'], \
            'weng': ['ueng', 'weng', 'woeng', 'wenq'], \
            'yu': ['iu', 'yu', 'yeu', 'yuh'], \
            'yue': ['iue', 'yue', 'yeue', 'yueh'], \
            'yuan': ['iuan', 'yuan', 'yeuan', 'yuann'], \
            'yun': ['iun', 'yun', 'yeun', 'yunn'], \
            'r': ['el', 'erl', 'eel', 'ell'], \
            'er': ['el', 'erl', 'eel', 'ell'], \
            'nü': ['nhiu', 'niu', 'neu', 'niuh'], \
            'lü': ['lhiu', 'liu', 'leu', 'liuh'], \
            'nüe': ['nhiue', 'niue', 'neue', 'niueh'], \
            'lüe': ['lhiue', 'liue', 'leue', 'liueh']
            }

gr_initial={'b': 'b', 'p': 'p', 'm': 'm', 'f': 'f', \
            'd': 'd', 't': 't', 'n': 'n', 'l': 'l', \
            'g': 'g', 'k': 'k', 'h': 'h', \
            'j': 'j', 'q': 'ch', 'x': 'sh', \
            'r': 'r', 'z': 'tz', 'c': 'ts', 's': 's'\
            }
gr_retroflex={'zh': 'j', 'ch': 'ch', 'sh': 'sh'}

gr_final = {'a': ['a', 'ar', 'aa', 'ah'], \
            'o': ['o', 'or', 'oo', 'oh'], \
            'e': ['e', 'er', 'ee', 'eh'], \
            'ai': ['ai', 'air', 'ae', 'ay'], \
            'ei': ['ei', 'eir', 'eei', 'ey'], \
            'ao': ['au', 'aur', 'ao', 'aw'], \
            'ou': ['ou', 'our', 'oou', 'ow'], \
            'an': ['an', 'arn', 'aan', 'ann'], \
            'en': ['en', 'ern', 'een', 'enn'], \
            'ang': ['ang', 'arng', 'aang', 'anq'], \
            'eng': ['eng', 'erng', 'eeng', 'enq'], \
            'ong': ['ong', 'orng', 'oong', 'onq'], \
            'r': ['l', 'r', 'l', 'l'], \
            'i': ['i', 'yi', 'ii', 'ih'], \
            'ia': ['ia', 'ya', 'ea', 'iah'], \
            'io': ['io', 'yo', 'eo', 'ioh'], \
            'ie': ['ie', 'ye', 'iee', 'ieh'], \
            'iai': ['iai', 'yai', 'eai', 'iay'], \
            'iao': ['iau', 'yau', 'eau', 'iaw'], \
            'iu': ['iou', 'you', 'eou', 'iow'], \
            'ian': ['ian', 'yan', 'ean', 'iann'], \
            'in': ['in', 'yn', 'iin', 'inn'], \
            'iang': ['iang', 'yang', 'eang', 'ianq'], \
            'ing': ['ing', 'yng', 'iing', 'inq'], \
            'iong': ['iong', 'yong', 'eong', 'ionq'], \
            'u': ['u', 'wu', 'uu', 'uh'], \
            'ua': ['ua', 'wa', 'oa', 'uah'], \
            'uo': ['uo', 'wo', 'uoo', 'uoh'], \
            'uai': ['uai', 'wai', 'oai', 'uay'], \
            'ui': ['uei', 'wei', 'oei', 'uey'], \
            'uan': ['uan', 'wan', 'oan', 'uann'], \
            'un': ['uen', 'wen', 'oen', 'uenn'], \
            'uang': ['uang', 'wang', 'oang', 'uanq'], \
            'u:': ['iu', 'yu', 'eu', 'iuh'], \
            'u:e': ['iue', 'yue', 'eue', 'iueh'], \
            'u:an': ['iuan', 'yuan', 'euan', 'iuann'], \
            'u:n': ['iun', 'yun', 'eun', 'iunn'] \
          }

def py2gr(py):
    try:
        err = py[0]
        py = py.lower()
        out = ""
        initial = ""
        tone = int(py[-1])
        py = py[0:-1]
        
        if tone == 5:
            out += "."
            tone = 1
            
        if py in gr_special:
            out += gr_special[py][tone-1]
            return out

        elif py[0:2] in gr_retroflex:
            out += gr_retroflex[py[0:2]]
            py = py[2:]
        elif py[0] in gr_initial:
            initial = py[0]
            out += gr_initial[initial]
            py = py[1:]

        if initial in gr_jqx:
            if py[0] == 'u':
                py = 'u:' + py[1:]

        if initial in gr_lmnr:
            if tone == 1:
                out += "h"
            elif tone == 2:
                tone = 1
        out += gr_final[py][tone-1]
        return out
    except ValueError:
        return "?"+err+"#"
    except KeyError:
        return "?"+err+"?"

