import conf,osdetect,os

o=osdetect.whereami()

def clear():
    if o=="idle":
        0+0
    elif o=="lin":
        os.system('clear')
    elif o=="win":
        os.system('cls')
pe=-1
e=-1
try:
    f=open(f"{conf.story}/Events/story.py")
except OSError:
    pass
else:
    f.close()
    from Events.story import *

try:
    f=open(f"{conf.story}/Events/-1.rpg")
except BaseException:
    raise
else:
    f.close()

while True:
    n=f"{conf.story}/Events/{e}.rpg"
    try:
        f=open(n)
    except OSError:
        print(f"Event {e} Does Not Exist")
        e=pe
        n=f"{conf.story}/Events/{e}.rpg"
        f=open(n)
    l=""
    while l!='##### Begin Story #####\n':
        l=f.readline()
    s=""
    while l!='##### End Story #####\n':
        l=f.readline()
        if l!='##### End Story #####\n':
            i=l.lstrip("'")
            i=i.rstrip("n'")
            i=i.rstrip("//")
            s=s+i
    print(s)
    u=input()
    while l!='##### Begin Args #####\n':
        l=f.readline()
    while l!='##### End Args #####':
        l=f.readline()
        if l!='##### End Args #####':
            i=0
            a=0
            c=""
            n=""
            tmp=""
            for i in l:
                if i=="[":
                    a=1
                elif i=="]":
                    a=2
                elif a==1:
                    tmp+=i
                elif a==2:
                    tmp=tmp.split(", ",2)
                    break
            if type(tmp)==type([]):
                c=tmp[0]
                n=tmp[1]
            if u==c:
                pe=e
                clear()
                if n=="end":
                    break
                if len(tmp)>2:
                    ev=tmp[2]
                    eval(ev)
                e=n.lstrip()
            elif u=="i":
                inventory()
                u=""
            elif u=="n":
                shownotes()
                u=""
#    break
