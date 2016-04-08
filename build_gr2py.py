# build gr2py dictionary
import pygr

py_init=['','b','p','m','f','d','t','n','l','g','k','h', \
         #'j','q','x',
         #'zh','ch','sh',
         'r','z','c','s','y','w']
py_final=['a','o','e','ai','ei','ao','ou','an','en','ang','eng','er', \
          'i','ia','io','ie','iai','iao','iu','ian','in','iang','ing', \
          'u','ua','uo','uai','ui','uan','un','uang','ong', \
          'u:','u:e','u:an','u:n','iong','ue']
py_tones=['1','2','3','4','5']

py_jqx=['j','q','x']
py_jqx_final=['i','ia','io','ie','iai','iao','iu','ian','in','iang','ing', \
              'u','ue','uan','un','iong']

py_zhchsh=['zh','ch','sh']
py_zhchsh_final=['i','a','e','ai','ei','ao','ou','an','en','ang','eng', \
                 'u','ua','uo','uai','ui','uan','un','uang','ong']

syllist=[i+f for i in py_init for f in py_final]
syltonelist=[s+t for s in syllist for t in py_tones]

sl2=[i+f for i in py_jqx for f in py_jqx_final]
slt2=[s+t for s in sl2 for t in py_tones]

sl3=[i+f for i in py_zhchsh for f in py_zhchsh_final]
slt3=[s+t for s in sl3 for t in py_tones]

gr2py={}

for syl in syltonelist:
    gr2py[pygr.py2gr(syl)]=syl

for syl in slt2:
    gr2py[pygr.py2gr(syl)]=syl

for syl in slt3:
    gr2py[pygr.py2gr(syl)]=syl

