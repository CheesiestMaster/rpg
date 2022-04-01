import random
inv={"No Armor":1,"Fists":1}
equ={"Armor":"No Armor","Wep":"Fists"}
equips={"No Armor":["A",0],"Leather":["A",5],"Fists":["W",1],"Sword":["W",5]}
notes=[]
hp=10
dc=0
dmg=1
cmbmeta=dict()

def inventory():
    for k in inv.keys():
        if inv[k]!=0:
            print(f"{inv[k]} {k}")

def shownotes():
    for i in notes:
        print(i)

def equip():
    inventory()
    i=input("What Item do you want to equip")
    if i in inv.keys():
        if i not in equ.values():
            for k in equips:
                if k==i:
                    if equips[k][0]=="A":
                        equ["Armor"]=i
                        dc=equips[k][1]
                    else:
                        equ["Wep"]=i
                        dmg=equips[k][1]         
        else:
            print("That is already equipped")
    else:
        print("You don't have one of that to equip")

def removeitem(name, count):
    name=name.capitalize()
    count=int(count)
    if name in inv.keys():
        if inv[name]>=count:
            inv[name]-=count
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
    additem("Gold", 20)

def startcombat(ename, ehp, eac, edmg, rew, n):
    ehp=int(ehp)
    eac=int(eac)
    edmg=int(edmg)
    global cmbmeta
    cmbmeta={"name":ename, 'hp':ehp, 'ac':eac, 'dmg':edmg, 'rew':rew, 'aiblk':False, 'next': n}
    try:
        f=open("./Events/combat.rpg", "w")
    except OSError:
        f=open("./Events/combat.rpg", "x")
    f.write("##### Begin Story #####\n")
    f.newlines
    f.write(f"You are being attacked by a {ename}\n")
    f.write(f"You have {hp} Health\n")
    f.write(f"1: Attack with {equ['Wep']}\n")
    f.write("2: Block\n")
    f.write("3: Use a Potion\n")
    f.write("##### End Story #####\n##### Begin Args #####\n")
    f.write("[1, combat, combatturn('atk')]\n")
    f.write("[2, combat, combatturn('blk')]\n")
    f.write("[3, combat, combatturn('pot')]\n")
    f.write("##### End Args #####")
    f.close()

def combatturn(act):
    pblk=False
    global cmbmeta,hp
    if act=='atk':
        if cmbmeta['aiblk']:
            cmbmeta['ehp']-=max(0,dmg-cmbmeta['eac'])
        else:
            cmbmeta['ehp']-=dmg
    if cmbmeta['ehp'] <= 0:
        e=n
        return True
    elif act=='blk':
        print("You Blocked")
        pblk=True
    elif act=='pot':
        if checkitem("Potion",1):
            removeitem("Potion", 1)
            hp+=10
        
    ai=random.choice(['atk','blk'])
    if ai=='atk':
        if pblk:
            hp-=max(0,cmbmeta['edmg']-dc)
            print(f"The {cmbmeta['ename']} attacked you but you blocked it, you took {max(0,cmbmeta['edmg']-dc)} damage.")
        else:
            hp-=cmbmeta['edmg']
            print(f"The {cmbmeta['ename']} attacked you but you blocked it, you took {cmbmeta['edmg']} damage.")
        if hp<=0:
            raise ValueError("HP Must be Greater Than 0, You Lose")
    elif ai=='blk':
        cmbmeta['aiblk']=True
    
def e011():
    if checkitem("Gold", 10):
        removeitem("Gold", 10)
        additem("Sword", 1)
    else:
        print("Insufficient Funds")
def e012():
    if checkitem("Gold", 10):
        removeitem("Gold", 10)
        additem("Leather", 1)
    else:
        print("Insufficient Funds")
def e013():
    if checkitem("Gold", 10):
        removeitem("Gold", 10)
        additem("Potion", 1)
    else:
        print("Insufficient Funds")
def e021():
    if "Defeat 10 bandits" not in notes:
        notes.append("Defeat 10 bandits")
        print("New Quest Added: Defeat 10 bandits")
