def create_tuple():
    return (1,2,3,[4,5,5],'as','3')

def create_tuple2():
    tpl = (1,2,3,4,5,6,)
    print( tpl[-2::1] )

def exe3():
    tpl = (1,2,3,4,5,6,)
    [a,b,c,d,e,f] = tpl
    print(a,b,c,d,e,f)

def exe4():
    tpl = (1,2,3,4,5,6,)
    lst = list(tpl)
    lst.append(7)
    return tuple(lst)

def exe5(ind):
    tpl = (1,2,3,4,5,6,)
    lst = list(tpl)
    lst.insert(ind, 7)
    return tuple(lst)

def exe6():
    lst = [1,2,3,4,5,6,]
    return tuple(lst)

def exe7():
    tpl = (1,2,3,4,5,6,)
    return len(tpl)

def exe8():
    tpl = ("Orange",[10,20,30],(5,15,25))
    return tpl[1][1]

def exe9():
    tpl = (10,20,30,40)
    [a,b,c,d] = tpl
    return a,b,c,d

# exe 10
# (1,1,2)

