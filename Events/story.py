inv=[]
invc=[]
notes=[]

def inventory():
    for i in range(len(inv)):
        if invc[i]>0:
            print(f"{invc[i]} {inv[i]}")

def shownotes():
    for i in notes():
        print(i)

def removeitem(name, count):
    name=name.capitalize()
    count=int(count)
    if name in inv:
        i=inv.index(name)
        if invc[i]>count:
            invc[i]-=count
            return True
    return False

def additem(name, count):
    name=name.capitalize()
    count=int(count)
    if name in inv:
        i=inv.index(name)
        invc[i]+=count
        return True
    else:
        inv.append(name)
        invc.append(count)
        return True

def checkitem(name, count):
    name=name.capitalize()
    count=int(count)
    if name in inv:
        i=inv.index(name)
        if invc[i]>=count:
            return True
    return False

def start():
    additem("Coins", 20)
