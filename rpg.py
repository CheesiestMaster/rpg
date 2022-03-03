import conf
e=-1
while True:
    n=conf.story+"/Events/"+str(e)
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
            for i in range(len(l)):
                if l[i]=="[":
                    a=1
                elif l[i]==",":
                    a=2
                    i+=1
                elif l[i]=="]":
                    a=3
                elif a==1:
                    c=c+l[i]
                elif a==2:
                    n=n+l[i]
            if u==c:
                e=n.lstrip()
                
#    break
