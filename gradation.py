# -*- coding: utf-8 -*-

PXS = (10, 30, 60)        # percent of d_10, d_30, d_60

class _pos:
    def __init__(self, index, pn):
        self.id = index
        self.pn = pn
        
def position(L, p):
    """
    L: list, p:百分含量
    找到百分含量p在list里的位置返回（i）
    """
    for elem in L:
        if elem <= p:
            return _pos(L.index(elem),p)
    
def interp1(dl, du, pl, pu, pn):
    return dl+(du-dl)*(pn-pl)/(pu-pl)
    
def taylorAN(sieve, n):
     """
     Taylor A.N equation: P=100*(d_i/d_max)^n
     """
     num = len(sieve)
     assert sieve[0] == max(sieve)
     dm = sieve[0]
     return [100*(sieve[i]/dm)**n for i in range(num)]
             
def gradprint(List):
    print('[', end = '')
    for i in List:
        print('%.4f' % i, end=' ')
    print(']')
             
def print_grad_prop(sieve, gradlist):
    gradprint(gradlist)       # need format ptint
    positions = [position(gradlist, px) for px in PXS]
    args = [(sieve[i.id], sieve[i.id-1], gradlist[i.id], gradlist[i.id-1], i.pn) for i in positions]
    for arg in args:
        print('d%d' % arg[-1], ': %.4f' % interp1(*arg))
    
#def fenxing(): 

if __name__ == '__main__':
    from gradationdata import sieve, P5_50, P5_65, P5_80, AC25_upper, AC25_lower, AC25_mid
    datas = [P5_50, P5_65, P5_80, AC25_upper, AC25_lower, AC25_mid]
    ANdatas = [taylorAN(sieve, n) for n in (0.4, 0.5, 0.6)]
    print('*'*6, 'Taylor A.N gradation :', '*'*6)
    for data in ANdatas:
        print_grad_prop(sieve, data)
    print('*'*6, 'AC-25 gradation :', '*'*6)    
    for data in datas:        
        print_grad_prop(sieve, data)