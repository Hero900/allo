
def rm(chemin,nom):
    import os
    chemin_3 = chemin
    dos = os.path.join(chemin_3,nom)
    if os.path.exists(dos):
       os.removedirs(dos)
       print('Fini')

def mk(chemin,name):
    import os
    chemin_2 = chemin
    do = os.path.join(chemin_2,name)
    if not os.path.exists(do):
       os.makedirs(do)
       print('Fini')

def dir_c():
    li = ['mk(chemin,nom)','rm(chemin,nom)','p(print)']
    print(li)

def p(tex = 't'):
    liste = ['caca','con','Con','CON','CACA','Caca']
    li = ['',' ','  ','   ','    ','     ','      ']
    if tex in liste:
        num = len(tex)
        tet = '*' * num
        print(tet) 
    elif tex in li:
        print('Allo')    
    else:
        print(tex)

