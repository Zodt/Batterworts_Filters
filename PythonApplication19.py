from sympy import *
from xlwt import *
from os import system
import time

 
# region Products (on future)
from sympy import symbols, pi, cos, product
def products(n):
    p, k = symbols('p'), symbols('k', integer=True)
    if n % 2:
        a = str((p + 1) * product((p ** 2) - 2 * p * cos(((2 * k + n - 1) / (2 * n)) * pi) + 1, (k, 1, (n - 1) // 2)).evalf())
    else:
        a = str(product((p ** 2) - 2 * p * cos(((2 * k + n - 1) / (2 * n)) * pi) + 1, (k, 1, n // 2)).evalf())

    return a.replace('1.00000000000000', '1')
# endregion

def repl(n, b, fd):
    if len(b) == 6:
        a = ['Коэффициент a10', 'Коэффициент a11', 'Коэффициент a12', 'Коэффициент b10', 'Коэффициент b11',
             'Коэффициент b12']
        for i in range(6):
            n = n.replace(str(a[i]), str(b[i]))
        return n.replace('(=&@=)', str(fd))
    elif len(b) == 10:
        a = ['Коэффициент a10', 'Коэффициент a11', 'Коэффициент a12', 'Коэффициент a13', 'Коэффициент a14',
             'Коэффициент b10', 'Коэффициент b11', 'Коэффициент b12', 'Коэффициент b13', 'Коэффициент b14']
        for i in range(10):
            n = n.replace(str(a[i]), str(b[i]))
        return n.replace('(=&@=)', str(fd))
    elif len(b) == 26:
        a = ['Коэффициент a10', 'Коэффициент a11', 'Коэффициент a12', 'Коэффициент b10', 'Коэффициент b11',
             'Коэффициент b12', 'Коэффициент a20', 'Коэффициент a21', 'Коэффициент a22', 'Коэффициент a23',
             'Коэффициент a24', 'Коэффициент b20', 'Коэффициент b21', 'Коэффициент b22', 'Коэффициент b23',
             'Коэффициент b24', 'Коэффициент a30', 'Коэффициент a31', 'Коэффициент a32', 'Коэффициент a33',
             'Коэффициент a34', 'Коэффициент b30', 'Коэффициент b31', 'Коэффициент b32', 'Коэффициент b33',
             'Коэффициент b34']
        for i in range(26):
            n = n.replace(str(a[i]), str(b[i]))
        return n.replace('(=&@=)', str(fd))
    elif len(b) == 30:
        a = ['Коэффициент a10', 'Коэффициент a11', 'Коэффициент a12', 'Коэффициент a13', 'Коэффициент a14',
             'Коэффициент b10', 'Коэффициент b11', 'Коэффициент b12', 'Коэффициент b13', 'Коэффициент b14',
             'Коэффициент a20', 'Коэффициент a21', 'Коэффициент a22', 'Коэффициент a23', 'Коэффициент a24',
             'Коэффициент b20', 'Коэффициент b21', 'Коэффициент b22', 'Коэффициент b23', 'Коэффициент b24',
             'Коэффициент a30', 'Коэффициент a31', 'Коэффициент a32', 'Коэффициент a33', 'Коэффициент a34',
             'Коэффициент b30', 'Коэффициент b31', 'Коэффициент b32', 'Коэффициент b33', 'Коэффициент b34']
        for i in range(30):
            n = n.replace(str(a[i]), str(b[i]))
        return n.replace('(=&@=)', str(fd))
    else:
        return 'Error ' + n.replace('(=&@=)', str(fd))
# region Функции
def karcas(k1p):
    t = list(str(k1p))
    f = t[:t.index('/')]
    s = t[t.index('/') + 1:]
    y = s[1:s.index('*') + 5]

    k1p1 = simplify('(' + str(''.join(f)) + ')/(' + str(''.join(y)) + ')')
    k1p2 = simplify('(' + str(''.join(s)) + ')/(' + str(''.join(y)) + ')')
    k1p3 = simplify('(' + str(k1p1) + ')/(' + str(k1p2) + ')')
    return k1p1, k1p2, k1p3
def koef1(s):
    s = list(
        s.replace(' ', '').replace('+', ' + ').replace('-', ' -').replace('**', '^').replace('*', ' * ').replace('(',
                                                                                                                 ' ( ').replace(
            ')', ' ) ').split())
    t, pos, res, k, cis = [], [], [], 0, str()
    for i in range(len(s)):
        try:
            if float(s[i]) or s[i] == '0':
                t.append(s[i])
        except ValueError:
            if s[i][:2] == 'z^':
                pos.append(s[i][2:])
                try:
                    if len(pos) != 1 and int(pos[len(pos) - 2]) - int(pos[len(pos) - 1]) > 1:
                        if t[1] != 0: t.insert(1, '0')
                        t.append('0')
                except ValueError:
                    None
    if s[2] == '(' and s[1] == '*' and s[3] == 'z^2' and s[5] == ')':
        t.insert(1, '0')
        t[2] = str(float(t[0]) * float(t[2]))

    if k <= len(t):
        while float(t[k]) != 1.0:
            res.append('.define a1' + str(k) + ' ' + str(t[k]))
            r = k
            k += 1
    t[k] = int(float(t[k]))
    while t[k] != t[len(t) - 1]:
        res.append('.define b1' + str(k - r - 1) + ' ' + str(t[k]))
        k += 1
    res.append('.define b1' + str(k - r - 1) + ' ' + str(t[k]))
    for l in range(len(res)):
        cis = cis + str(res[l])
    return cis.replace('.define', '\n.define')
def koef2(s):
    s = list(
        s.replace(' ', '').replace('+', ' + ').replace('-', ' -').replace('**', '^').replace('*', ' * ').replace('(',
                                                                                                                 ' ( ').replace(
            ')', ' ) ').split())
    t, pos, res, k, cis = [], [], [], 0, str()
    for i in range(len(s)):
        try:
            if float(s[i]) or s[i] == '0':
                t.append(s[i])
        except ValueError:
            if s[i][:2] == 'z^':
                pos.append(s[i][2:])
                try:
                    if len(pos) != 1 and int(pos[len(pos) - 2]) - int(pos[len(pos) - 1]) > 1:
                        if t[1] != 0: t.insert(1, '0')
                        t.append('0')
                except ValueError:
                    None
    if s[2] == '(' and s[1] == '*' and s[3] == 'z^2' and s[5] == ')':
        t.insert(1, '0')
        t[2] = str(float(t[0]) * float(t[2]))

    if k <= len(t):
        while float(t[k]) != 1.0:
            res.append('.define a1' + str(k) + ' ' + str(t[k]))
            r = k
            k += 1
    t[k] = int(float(t[k]))
    while t[k] != t[len(t) - 1]:
        res.append('.define b1' + str(k - r - 1) + ' ' + str(t[k]))
        k += 1
    res.append('.define b1' + str(k - r - 1) + ' ' + str(t[k]))
    for l in range(len(res)):
        cis = cis + str(res[l])
    return cis.replace('.define', '\n.define')
def koef3(s):
    s = list(
        s.replace(' ', '').replace('+', ' + ').replace('-', ' -').replace('**', '^').replace('*', ' * ').replace('(',
                                                                                                                 ' ( ').replace(
            ')', ' ) ').split())
    t, pos, res, k, cis = [], [], [], 0, str()
    for i in range(len(s)):
        try:
            if float(s[i]) or s[i] == '0':
                t.append(s[i])
        except ValueError:
            if s[i][:2] == 'z^':
                pos.append(s[i][2:])
                try:
                    if len(pos) != 1 and int(pos[len(pos) - 2]) - int(pos[len(pos) - 1]) > 1:
                        if t[1] != 0: t.insert(1, '0')
                        t.append('0')
                except ValueError:
                    None
    if s[2] == '(' and s[1] == '*' and s[3] == 'z^2' and s[5] == ')':
        t.insert(1, '0')
        t[2] = str(float(t[0]) * float(t[2]))

    if k <= len(t):
        while float(t[k]) != 1.0:
            res.append('.define a1' + str(k) + ' ' + str(t[k]))
            r = k
            k += 1
    t[k] = int(float(t[k]))
    while t[k] != t[len(t) - 1]:
        res.append('.define b1' + str(k - r - 1) + ' ' + str(t[k]))
        k += 1
    res.append('.define b1' + str(k - r - 1) + ' ' + str(t[k]))
    for l in range(len(res)):
        cis = cis + str(res[l])
    return cis.replace('.define', '\n.define')
def koef4(s):
    s = list(
        s.replace(' ', '').replace('+', ' + ').replace('-', ' -').replace('**', '^').replace('*', ' * ').replace('(',
                                                                                                                 ' ( ').replace(
            ')', ' ) ').split())
    t, pos, res, k, cis = [], [], [], 0, str()
    for i in range(len(s)):
        try:
            if float(s[i]) or s[i] == '0':
                t.append(s[i])
        except ValueError:
            if s[i][:2] == 'z^':
                pos.append(s[i][2:])
                try:
                    if len(pos) != 1 and int(pos[len(pos) - 2]) - int(pos[len(pos) - 1]) > 1:
                        if t[1] != 0: t.insert(1, '0')
                        t.append('0')
                except ValueError:
                    None
    if s[2] == '(' and s[1] == '*' and s[3] == 'z^2' and s[5] == ')':
        t.insert(1, '0')
        t[2] = str(float(t[0]) * float(t[2]))

    if k <= len(t):
        while float(t[k]) != 1.0:
            res.append('.define a1' + str(k) + ' ' + str(t[k]))
            r = k
            k += 1
    t[k] = int(float(t[k]))
    while t[k] != t[len(t) - 1]:
        res.append('.define b1' + str(k - r - 1) + ' ' + str(t[k]))
        k += 1
    res.append('.define b1' + str(k - r - 1) + ' ' + str(t[k]))
    for l in range(len(res)):
        cis = cis + str(res[l])
    return cis.replace('.define', '\n.define')

# endregion
# region Перевод из 10сс в 2сс и обратно
def mk(s):
    if prob(s):
        return twototen(s)
    else:
        tentotwo(s)
        cis = str()
        for l in range(len(c)):
            cis = cis + str(c[l])
        try:
            cis = cis.replace('b', '')
        except ArithmeticError:
            return 0
        return ''.join(cis)
def prob(a):
    a = list(*a.split())
    for i in range(len(a)):
        if (a[i] == '0' or a[i] == '1'):
            flag = True
        else:
            flag = False
            break
    return flag
def tentotwo(o):
    n = 2
    t = s = float(o)
    global c
    if s < 0:
        s, c, cis = -s, ['-', bin(int(s))[2:], ","], str()
    else:
        c = [bin(int(s))[2:], ","]

    while t != 0:
        t -= int(t)
        t = t * n
        if int(t) < 0:
            c.append(int(-t))
        else:
            c.append(int(t))
        t -= int(t)
def twototen(w):
    n = 2
    if w == 0:
        return str(0)
    elif w == float(1):
        return str(1.0)
    else:
        try:
            w = w.replace('b', '').replace(',', '.')
        except AttributeError:
            return 0

        m, r = list(w), 0
        if float(w) < 0:
            w = str(-float(w))
            m.remove(m[0])
            poi = len(str(int(float(str(w)))))
            for k in range(poi):
                if poi == 1: break
                r = r + (int(m[k])) * n ** (int(len(str(int(float(str(w)))))) - 1 - k)
            for k in range(poi + 1, len(m)):
                r = r + (int(m[k])) * n ** (int(len(str(int(float(str(w)))))) - k)
            return -r
        elif float(w) > 0:
            w = str(float(w))
            poi = len(str(int(float(str(w)))))
            for k in range(poi):
                if poi == 1: break
                r = r + (int(m[k])) * n ** (int(len(str(int(float(str(w)))))) - 1 - k)
            for k in range(poi + 1, len(m)):
                r = r + (int(m[k])) * n ** (int(len(str(int(float(str(w)))))) - k)
            return r
# endregion

wb = Workbook()
ws = wb.add_sheet('Рассчеты')
file = open("Kursovaya.txt", 'w')

# region Входные значения

# fc1 = float(input('fc1 = ').replace(',','.'))
# fc2 = float(input('fc2 = ').replace(',','.'))
# fs1 = float(input('fs1 = ').replace(',','.'))
# fs2 = float(input('fs2 = ').replace(',','.'))
# d = float(input('d = ').replace(',','.'))


##Диман
# fc1 = 6.3
# fc2 = 27.5
# fs1 = 4
# fs2 = 58
# d = 33

# Рома
# fc1 = 2.5
# fc2 = 35.6
# fs1 = 1
# fs2 = 75
# d = 35

##Валя
fc1 = 10.8
fc2 = 42.5
fs1 = 5
fs2 = 90.5
d = 35

##Некит
# fc1 = 16.1
# fc2 = 43.7
# fs1 = 8
# fs2 = 87
# d = 35

##Саня
#fc1 = 5
#fc2 = 48
#fs1 = 2
#fs2 = 85
#d = 35
# endregion

# region Рассчеты
fd, dr, n = 3 * 2 * fs2, 1, 1
lc1 = 2 * pi.evalf() * Rational(fc1, fd)
lc2 = 2 * pi.evalf() * Rational(fc2, fd)
ls1 = 2 * pi.evalf() * Rational(fs1, fd)
ls2 = 2 * pi.evalf() * Rational(fs2, fd)
a = cot(Rational(lc2 - lc1, 2)).evalf()
b = Rational(sin(lc2 + lc1), (sin(lc2) + sin(lc1))).evalf()
print('Выполняются расчеты')
# endregion

# region Определение порядка
os = min(abs(Rational(a * (b - cos(ls1)), (sin(ls1))).evalf()), abs(Rational(a * (b - cos(ls2)), (sin(ls2))).evalf()))
while dr <= d:
    n += 1
    dr = 10 * log((1 + os ** (2 * n)), 10).evalf()
print('Определяется порядок')
# endregion

# region Вспомогательные строки
file.write('n ' + str(n) + '\n')
z = Symbol('z')
# endregion

# region Вывод формул и коэффициентов
print('Выполняется рассчет коэффициентов')
if n == 1:
    p = simplify(str(a) + '*((z^2)-2*' + str(b) + '*z+1)/((z^2)-1)')

    k1p = simplify('1/((' + str(p) + ')+1)')
    k1p1, k1p2, k1p3 = karcas(k1p)

    file.write('fc1 ' + str(fc1) + '\n')
    file.write('fc2 ' + str(fc2) + '\n')
    file.write('fs1 ' + str(fs1) + '\n')
    file.write('fs2 ' + str(fs2) + '\n')
    file.write('fd ' + str(fd) + '\n\n')

    file.write('lc1 ' + str(lc1) + '\n')
    file.write('lc2 ' + str(lc2) + '\n')
    file.write('ls1 ' + str(ls1) + '\n')
    file.write('ls2 ' + str(ls2) + '\n\n')

    file.write('a ' + str(a) + '\n')
    file.write('b ' + str(b) + '\n\n')

    file.write('First Kaskad ' + str(k1p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef1(str(k1p3)))
    file.write('\n\n' + str(k1p3).replace('z**4', 'z*z*z*z').replace('z**3', 'z*z*z').replace('z**2', 'z*z*') + '\n')

    cpo = str(koef1(str(k1p3))).split()
    pops = 7
    qazwsx = []
    for po in range(1, pops):
        # region Рассчетные коэффициенты
        qazwsx.append(str(cpo[3 * po - 1]))
        ws.write(kol + po, 1, "'" + str(cpo[3 * po - 1]))
        ws.write(kol + po, 3, "'" + str(mk(str(cpo[3 * po - 1]))))
        # endregion
        # region 8
        try:
            ws.write(kol + po, 7, "'" + str(mk(str(cpo[3 * po - 1]))[:8]))
        except TypeError:
            ws.write(kol + po, 7, "'" + str(0))
        try:
            ws.write(kol + po, 5, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:8])))
        except TypeError:
            ws.write(kol + po, 5, "'" + str(0))
        # endregion
        # region 12
        try:
            ws.write(kol + po, 11, "'" + str(mk(str(cpo[3 * po - 1]))[:12]))
        except TypeError:
            ws.write(kol + po, 11, "'" + str(0))
        try:
            ws.write(kol + po, 9, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:12])))
        except TypeError:
            ws.write(kol + po, 9, "'" + str(0))
        # endregion
        # region 16
        try:
            ws.write(kol + po, 15, "'" + str(mk(str(cpo[3 * po - 1]))[:16]))
        except TypeError:
            ws.write(kol + po, 15, "'" + str(0))
        try:
            ws.write(kol + po, 13, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:16])))
        except TypeError:
            ws.write(kol + po, 13, "'" + str(0))
        # endregion
        # region 20
        try:
            ws.write(kol + po, 19, "'" + str(mk(str(cpo[3 * po - 1]))[:20]))
        except TypeError:
            ws.write(kol + po, 19, "'" + str(0))
        try:
            ws.write(kol + po, 17, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:20])))
        except TypeError:
            ws.write(kol + po, 17, "'" + str(0))
        # endregion
        # region 24
        try:
            ws.write(kol + po, 23, "'" + str(mk(str(cpo[3 * po - 1]))[:24]))
        except TypeError:
            ws.write(kol + po, 23, "'" + str(0))
        try:
            ws.write(kol + po, 21, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:24])))
        except TypeError:
            ws.write(kol + po, 21, "'" + str(0))
        # endregion
        # 32
        try:
            ws.write(kol + po, 27, "'" + str(mk(str(cpo[3 * po - 1]))[:32]))
        except TypeError:
            ws.write(kol + po, 27, "'" + str(0))
        try:
            ws.write(kol + po, 25, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:32])))
        except TypeError:
            ws.write(kol + po, 25, "'" + str(0))
elif n == 2:
    p = simplify(str(a) + '*((z^2)-2*' + str(b) + '*z+1)/((z^2)-1)')

    k1p = simplify('1/((' + str(p) + ')^2+1.41421*(' + str(p) + ')+1)')
    k1p1, k1p2, k1p3 = karcas(k1p)

    file.write('fc1 ' + str(fc1) + '\n')
    file.write('fc2 ' + str(fc2) + '\n')
    file.write('fs1 ' + str(fs1) + '\n')
    file.write('fs2 ' + str(fs2) + '\n')
    file.write('fd ' + str(fd) + '\n\n')

    file.write('lc1 ' + str(lc1) + '\n')
    file.write('lc2 ' + str(lc2) + '\n')
    file.write('ls1 ' + str(ls1) + '\n')
    file.write('ls2 ' + str(ls2) + '\n\n')

    file.write('a ' + str(a) + '\n')
    file.write('b ' + str(b) + '\n\n')

    file.write('First Kaskad ' + str(k1p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef1(str(k1p3)))
    file.write('\n\n' + str(k1p3).replace('z**4', 'z*z*z*z').replace('z**3', 'z*z*z').replace('z**2', 'z*z*') + '\n')

    cpo = str(koef1(str(k1p3))).split()
    pops = 11
    for po in range(1, pops):
        # region Рассчетные коэффициенты
        ws.write(kol + po, 1, "'" + str(cpo[3 * po - 1]))
        ws.write(kol + po, 3, "'" + str(mk(str(cpo[3 * po - 1]))))
        # endregion
        # region 8
        try:
            ws.write(kol + po, 7, "'" + str(mk(str(cpo[3 * po - 1]))[:8]))
        except TypeError:
            ws.write(kol + po, 7, "'" + str(0))
        try:
            ws.write(kol + po, 5, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:8])))
        except TypeError:
            ws.write(kol + po, 5, "'" + str(0))
        # endregion
        # region 12
        try:
            ws.write(kol + po, 11, "'" + str(mk(str(cpo[3 * po - 1]))[:12]))
        except TypeError:
            ws.write(kol + po, 11, "'" + str(0))
        try:
            ws.write(kol + po, 9, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:12])))
        except TypeError:
            ws.write(kol + po, 9, "'" + str(0))
        # endregion
        # region 16
        try:
            ws.write(kol + po, 15, "'" + str(mk(str(cpo[3 * po - 1]))[:16]))
        except TypeError:
            ws.write(kol + po, 15, "'" + str(0))
        try:
            ws.write(kol + po, 13, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:16])))
        except TypeError:
            ws.write(kol + po, 13, "'" + str(0))
        # endregion
        # region 20
        try:
            ws.write(kol + po, 19, "'" + str(mk(str(cpo[3 * po - 1]))[:20]))
        except TypeError:
            ws.write(kol + po, 19, "'" + str(0))
        try:
            ws.write(kol + po, 17, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:20])))
        except TypeError:
            ws.write(kol + po, 17, "'" + str(0))
        # endregion
        # region 24
        try:
            ws.write(kol + po, 23, "'" + str(mk(str(cpo[3 * po - 1]))[:24]))
        except TypeError:
            ws.write(kol + po, 23, "'" + str(0))
        try:
            ws.write(kol + po, 21, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:24])))
        except TypeError:
            ws.write(kol + po, 21, "'" + str(0))
        # endregion
        # region 32
        try:
            ws.write(kol + po, 27, "'" + str(mk(str(cpo[3 * po - 1]))[:32]))
        except TypeError:
            ws.write(kol + po, 27, "'" + str(0))
        try:
            ws.write(kol + po, 25, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:32])))
        except TypeError:
            ws.write(kol + po, 25, "'" + str(0))
elif n == 3:
    p = simplify(str(a) + '*((z^2)-2*' + str(b) + '*z+1)/((z^2)-1)')

    k1p = simplify('1/((' + str(p) + ')+1)')
    k1p1, k1p2, k1p3 = karcas(k1p)

    k2p = simplify('1/((' + str(p) + ')^2+(' + str(p) + ')+1)')
    k2p1, k2p2, k2p3 = karcas(k2p)

    file.write('fc1 ' + str(fc1) + '\n')
    file.write('fc2 ' + str(fc2) + '\n')
    file.write('fs1 ' + str(fs1) + '\n')
    file.write('fs2 ' + str(fs2) + '\n')
    file.write('fd ' + str(fd) + '\n\n')

    file.write('lc1 ' + str(lc1) + '\n')
    file.write('lc2 ' + str(lc2) + '\n')
    file.write('ls1 ' + str(ls1) + '\n')
    file.write('ls2 ' + str(ls2) + '\n\n')

    file.write('a ' + str(a) + '\n')
    file.write('b ' + str(b) + '\n\n')

    file.write('First Kaskad ' + str(k1p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef1(str(k1p3)))

    file.write('\n\nSecond Kaskad ' + str(k2p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef2(str(k2p3)))
    file.write('\n\n' + str('(' + str(k1p3) + ')*(' + str(k2p3) + ')\n').replace('z**6', 'z*z*z*z*z*z').replace('z**5',
                                                                                                                'z*z*z*z*z').replace(
        'z**4', 'z*z*z*z').replace('z**3', 'z*z*z').replace('z**2', 'z*z'))

    for kol in [1, 8]:
        if kol == 8:
            cpo = str(koef1(str(k2p3))).split()
            pops = 11
        elif kol == 1:
            cpo = str(koef1(str(k1p3))).split()
            pops = 7
        for po in range(1, pops):
            # region Рассчетные коэффициенты
            ws.write(kol + po, 1, "'" + str(cpo[3 * po - 1]))
            ws.write(kol + po, 3, "'" + str(mk(str(cpo[3 * po - 1]))))
            # endregion
            # region 8
            try:
                ws.write(kol + po, 7, "'" + str(mk(str(cpo[3 * po - 1]))[:8]))
            except TypeError:
                ws.write(kol + po, 7, "'" + str(0))
            try:
                ws.write(kol + po, 5, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:8])))
            except TypeError:
                ws.write(kol + po, 5, "'" + str(0))
            # endregion
            # region 12
            try:
                ws.write(kol + po, 11, "'" + str(mk(str(cpo[3 * po - 1]))[:12]))
            except TypeError:
                ws.write(kol + po, 11, "'" + str(0))
            try:
                ws.write(kol + po, 9, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:12])))
            except TypeError:
                ws.write(kol + po, 9, "'" + str(0))
            # endregion
            # region 16
            try:
                ws.write(kol + po, 15, "'" + str(mk(str(cpo[3 * po - 1]))[:16]))
            except TypeError:
                ws.write(kol + po, 15, "'" + str(0))
            try:
                ws.write(kol + po, 13, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:16])))
            except TypeError:
                ws.write(kol + po, 13, "'" + str(0))
            # endregion
            # region 20
            try:
                ws.write(kol + po, 19, "'" + str(mk(str(cpo[3 * po - 1]))[:20]))
            except TypeError:
                ws.write(kol + po, 19, "'" + str(0))
            try:
                ws.write(kol + po, 17, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:20])))
            except TypeError:
                ws.write(kol + po, 17, "'" + str(0))
            # endregion
            # region 24
            try:
                ws.write(kol + po, 23, "'" + str(mk(str(cpo[3 * po - 1]))[:24]))
            except TypeError:
                ws.write(kol + po, 23, "'" + str(0))
            try:
                ws.write(kol + po, 21, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:24])))
            except TypeError:
                ws.write(kol + po, 21, "'" + str(0))
            # endregion
            # region 32
            try:
                ws.write(kol + po, 27, "'" + str(mk(str(cpo[3 * po - 1]))[:32]))
            except TypeError:
                ws.write(kol + po, 27, "'" + str(0))
            try:
                ws.write(kol + po, 25, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:32])))
            except TypeError:
                ws.write(kol + po, 25, "'" + str(0))
elif n == 4:

    p = simplify(str(a) + '*((z^2)-2*' + str(b) + '*z+1)/((z^2)-1)')

    k1p = simplify('1/((' + str(p) + ')^2+0.76537*(' + str(p) + ')+1)')
    k1p1, k1p2, k1p3 = karcas(k1p)

    k2p = simplify('1/((' + str(p) + ')^2+1.84776*(' + str(p) + ')+1)')
    k2p1, k2p2, k2p3 = karcas(k2p)

    file.write('fc1 ' + str(fc1) + '\n')
    file.write('fc2 ' + str(fc2) + '\n')
    file.write('fs1 ' + str(fs1) + '\n')
    file.write('fs2 ' + str(fs2) + '\n')
    file.write('fd ' + str(fd) + '\n\n')

    file.write('lc1 ' + str(lc1) + '\n')
    file.write('lc2 ' + str(lc2) + '\n')
    file.write('ls1 ' + str(ls1) + '\n')
    file.write('ls2 ' + str(ls2) + '\n\n')

    file.write('a ' + str(a) + '\n')
    file.write('b ' + str(b) + '\n\n')

    file.write('First Kaskad ' + str(k1p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef1(str(k1p3)))

    for kol in [1, 12]:
        if kol == 12:
            cpo = str(koef1(str(k2p3))).split()
            pops = 11
        elif kol == 1:
            cpo = str(koef1(str(k1p3))).split()
            pops = 11
        for po in range(1, pops):
            # region Рассчетные коэффициенты
            ws.write(kol + po, 1, "'" + str(cpo[3 * po - 1]))
            ws.write(kol + po, 3, "'" + str(mk(str(cpo[3 * po - 1]))))
            # endregion
            # region 8
            try:
                ws.write(kol + po, 7, "'" + str(mk(str(cpo[3 * po - 1]))[:8]))
            except TypeError:
                ws.write(kol + po, 7, "'" + str(0))
            try:
                ws.write(kol + po, 5, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:8])))
            except TypeError:
                ws.write(kol + po, 5, "'" + str(0))
            # endregion
            # region 12
            try:
                ws.write(kol + po, 11, "'" + str(mk(str(cpo[3 * po - 1]))[:12]))
            except TypeError:
                ws.write(kol + po, 11, "'" + str(0))
            try:
                ws.write(kol + po, 9, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:12])))
            except TypeError:
                ws.write(kol + po, 9, "'" + str(0))
            # endregion
            # region 16
            try:
                ws.write(kol + po, 15, "'" + str(mk(str(cpo[3 * po - 1]))[:16]))
            except TypeError:
                ws.write(kol + po, 15, "'" + str(0))
            try:
                ws.write(kol + po, 13, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:16])))
            except TypeError:
                ws.write(kol + po, 13, "'" + str(0))
            # endregion
            # region 20
            try:
                ws.write(kol + po, 19, "'" + str(mk(str(cpo[3 * po - 1]))[:20]))
            except TypeError:
                ws.write(kol + po, 19, "'" + str(0))
            try:
                ws.write(kol + po, 17, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:20])))
            except TypeError:
                ws.write(kol + po, 17, "'" + str(0))
            # endregion
            # region 24
            try:
                ws.write(kol + po, 23, "'" + str(mk(str(cpo[3 * po - 1]))[:24]))
            except TypeError:
                ws.write(kol + po, 23, "'" + str(0))
            try:
                ws.write(kol + po, 21, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:24])))
            except TypeError:
                ws.write(kol + po, 21, "'" + str(0))
            # endregion
            # region 32
            try:
                ws.write(kol + po, 27, "'" + str(mk(str(cpo[3 * po - 1]))[:32]))
            except TypeError:
                ws.write(kol + po, 27, "'" + str(0))
            try:
                ws.write(kol + po, 25, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:32])))
            except TypeError:
                ws.write(kol + po, 25, "'" + str(0))
                # endregion

    file.write('\n\nSecond Kaskad ' + str(k2p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef2(str(k2p3)))
    file.write('\n\n' + ('(' + str(k1p3) + ')*(' + str(k2p3) + ')\n').replace('z**6', 'z*z*z*z*z*z').replace('z**5',
                                                                                                             'z*z*z*z*z').replace(
        'z**4', 'z*z*z*z').replace('z**3', 'z*z*z').replace('z**2', 'z*z'))
elif n == 5:
    # region
    p = simplify(str(a) + '*((z^2)-2*' + str(b) + '*z+1)/((z^2)-1)')

    k1p = simplify('1/((' + str(p) + ')+1)')
    k1p1, k1p2, k1p3 = karcas(k1p)

    k2p = simplify('1/((' + str(p) + ')^2+0.618*(' + str(p) + ')+1)')
    k2p1, k2p2, k2p3 = karcas(k2p)

    k3p = simplify('1/((' + str(p) + ')^2+1.618*(' + str(p) + ')+1)')
    k3p1, k3p2, k3p3 = karcas(k3p)

    file.write('fc1 ' + str(fc1) + '\n')
    file.write('fc2 ' + str(fc2) + '\n')
    file.write('fs1 ' + str(fs1) + '\n')
    file.write('fs2 ' + str(fs2) + '\n')
    file.write('fd ' + str(fd) + '\n\n')

    file.write('lc1 ' + str(lc1) + '\n')
    file.write('lc2 ' + str(lc2) + '\n')
    file.write('ls1 ' + str(ls1) + '\n')
    file.write('ls2 ' + str(ls2) + '\n\n')

    file.write('a ' + str(a) + '\n')
    file.write('b ' + str(b) + '\n\n')

    f = open('Testoviy.cir', 'r')
    # endregion
    # region Создание микрокаповских файлов
    print('Создание микрокаповских файлов')
    ideal_ = open('Ideal.cir', 'w')
    bit8_ = open('bit8.cir', 'w')
    bit12_ = open('bit12.cir', 'w')
    bit16_ = open('bit16.cir', 'w')
    bit20_ = open('bit20.cir', 'w')
    bit24_ = open('bit24.cir', 'w')
    bit32_ = open('bit32.cir', 'w')

    n5 = str(f.read())

    qazwsx = []
    bit8, bit16, bit12, bit20, bit24, bit32 = [], [], [], [], [], []

    # endregion

    for kol in [1, 8, 19]:
        if kol == 8:
            cpo = str(koef1(str(k2p3))).split()
            pops = 11
        elif kol == 19:
            cpo = str(koef1(str(k3p3))).split()
            pops = 11
        elif kol == 1:
            cpo = str(koef1(str(k1p3))).split()
            pops = 7
        for po in range(1, pops):
            # region Рассчетные коэффициенты
            ws.write(kol + po, 1, "'" + str(cpo[3 * po - 1]))
            ws.write(kol + po, 3, "'" + str(mk(str(cpo[3 * po - 1]))))
            qazwsx.append(str(cpo[3 * po - 1]))

            # endregion
            # region 8
            try:
                ws.write(kol + po, 7, "'" + str(mk(str(cpo[3 * po - 1]))[:8]))
                bit8.append(str(twototen(mk(str(cpo[3 * po - 1]))[:8])))
            except TypeError:
                ws.write(kol + po, 7, "'" + str(0))
                bit8.append(str(0))
            try:
                ws.write(kol + po, 5, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:8])))
            except TypeError:
                ws.write(kol + po, 5, "'" + str(0))
            # endregion
            # region 12
            try:
                ws.write(kol + po, 11, "'" + str(mk(str(cpo[3 * po - 1]))[:12]))
                bit12.append(str(twototen(mk(str(cpo[3 * po - 1]))[:12])))
            except TypeError:
                ws.write(kol + po, 11, "'" + str(0))
                bit12.append(str(0))
            try:
                ws.write(kol + po, 9, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:12])))
            except TypeError:
                ws.write(kol + po, 9, "'" + str(0))
            # endregion
            # region 16
            try:
                ws.write(kol + po, 15, "'" + str(mk(str(cpo[3 * po - 1]))[:16]))
                bit16.append(str(twototen(mk(str(cpo[3 * po - 1]))[:16])))
            except TypeError:
                ws.write(kol + po, 15, "'" + str(0))
                bit16.append(str(0))
            try:
                ws.write(kol + po, 13, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:16])))
            except TypeError:
                ws.write(kol + po, 13, "'" + str(0))
            # endregion
            # region 20
            try:
                ws.write(kol + po, 19, "'" + str(mk(str(cpo[3 * po - 1]))[:20]))
                bit20.append(str(twototen(mk(str(cpo[3 * po - 1]))[:20])))
            except TypeError:
                ws.write(kol + po, 19, "'" + str(0))
                bit20.append(str(0))
            try:
                ws.write(kol + po, 17, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:20])))
            except TypeError:
                ws.write(kol + po, 17, "'" + str(0))
            # endregion
            # region 24
            try:
                ws.write(kol + po, 23, "'" + str(mk(str(cpo[3 * po - 1]))[:24]))
                bit24.append(str(twototen(mk(str(cpo[3 * po - 1]))[:24])))
            except TypeError:
                ws.write(kol + po, 23, "'" + str(0))
                bit24.append(str(0))
            try:
                ws.write(kol + po, 21, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:24])))
            except TypeError:
                ws.write(kol + po, 21, "'" + str(0))
            # endregion
            # region 32
            try:
                ws.write(kol + po, 27, "'" + str(mk(str(cpo[3 * po - 1]))[:32]))
                bit32.append(str(twototen(mk(str(cpo[3 * po - 1]))[:32])))
            except TypeError:
                ws.write(kol + po, 27, "'" + str(0))
                bit32.append(str(0))
            try:
                ws.write(kol + po, 25, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:32])))
            except TypeError:
                ws.write(kol + po, 25, "'" + str(0))

                # region Экспорт в Микрокаповские файлы разной разрядности
    ideal_.write(str(repl(n5, qazwsx, fd)))
    bit8_.write(str(repl(n5, bit8, fd)))
    bit12_.write(str(repl(n5, bit12, fd)))
    bit16_.write(str(repl(n5, bit16, fd)))
    bit20_.write(str(repl(n5, bit20, fd)))
    bit24_.write(str(repl(n5, bit24, fd)))
    bit32_.write(str(repl(n5, bit32, fd)))
    # endregion
    file.write('First Kaskad ' + str(k1p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef1(str(k1p3)))

    file.write('\n\nSecond Kaskad ' + str(k2p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef2(str(k2p3)))

    file.write('\n\nThird Kaskad ' + str(k3p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef3(str(k3p3)))
    file.write('\n\n' + ('(' + str(k1p3) + ')*(' + str(k2p3) + ')*(' + str(k3p3) + ')\n').replace('z**6',
                                                                                                  'z*z*z*z*z*z').replace(
        'z**5', 'z*z*z*z*z').replace('z**4', 'z*z*z*z').replace('z**3', 'z*z*z').replace('z**2', 'z*z'))
elif n == 6:

    p = simplify(str(a) + '*((z^2)-2*' + str(b) + '*z+1)/((z^2)-1)')

    k1p = simplify('1/((' + str(p) + ')^2+0.51764*(' + str(p) + ')+1)')
    k1p1, k1p2, k1p3 = karcas(k1p)
    k2p = simplify('1/((' + str(p) + ')^2+1.41421*(' + str(p) + ')+1)')
    k2p1, k2p2, k2p3 = karcas(k2p)
    k3p = simplify('1/((' + str(p) + ')^2+1.93185*(' + str(p) + ')+1)')
    k3p1, k3p2, k3p3 = karcas(k3p)

    file.write('fc1 ' + str(fc1) + '\n')
    file.write('fc2 ' + str(fc2) + '\n')
    file.write('fs1 ' + str(fs1) + '\n')
    file.write('fs2 ' + str(fs2) + '\n')
    file.write('fd ' + str(fd) + '\n\n')

    file.write('lc1 ' + str(lc1) + '\n')
    file.write('lc2 ' + str(lc2) + '\n')
    file.write('ls1 ' + str(ls1) + '\n')
    file.write('ls2 ' + str(ls2) + '\n\n')

    file.write('a ' + str(a) + '\n')
    file.write('b ' + str(b) + '\n\n')

    file.write('First Kaskad ' + str(k1p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef1(str(k1p3)))

    f = open('Testoviy.cir', 'r')

    # region Создание микрокаповских файлов
    print('Создание микрокаповских файлов')
    ideal_ = open('Ideal.cir', 'w')
    bit8_ = open('bit8.cir', 'w')
    bit12_ = open('bit12.cir', 'w')
    bit16_ = open('bit16.cir', 'w')
    bit20_ = open('bit20.cir', 'w')
    bit24_ = open('bit24.cir', 'w')
    bit32_ = open('bit32.cir', 'w')

    n5 = str(f.read())

    qazwsx = []
    bit8, bit16, bit12, bit20, bit24, bit32 = [], [], [], [], [], []

    # endregion

    for kol in [1, 12, 23]:
        if kol == 1:
            cpo = str(koef1(str(k1p3))).split()
            pops = 11
        elif kol == 23:
            cpo = str(koef1(str(k3p3))).split()
            pops = 11
        elif kol == 12:
            cpo = str(koef2(str(k2p3))).split()
            pops = 11
        for po in range(1, pops):
            # region Рассчетные коэффициенты
            ws.write(kol + po, 1, "'" + str(cpo[3 * po - 1]))
            ws.write(kol + po, 3, "'" + str(mk(str(cpo[3 * po - 1]))))
            qazwsx.append(str(cpo[3 * po - 1]))
            # endregion
            # region 8
            try:
                ws.write(kol + po, 7, "'" + str(mk(str(cpo[3 * po - 1]))[:8]))
                bit8.append(str(twototen(mk(str(cpo[3 * po - 1]))[:8])))
            except TypeError:
                ws.write(kol + po, 7, "'" + str(0))
                bit8.append(str(0))
            try:
                ws.write(kol + po, 5, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:8])))
            except TypeError:
                ws.write(kol + po, 5, "'" + str(0))
            # endregion
            # region 12
            try:
                ws.write(kol + po, 11, "'" + str(mk(str(cpo[3 * po - 1]))[:12]))
                bit12.append(str(twototen(mk(str(cpo[3 * po - 1]))[:12])))
            except TypeError:
                ws.write(kol + po, 11, "'" + str(0))
                bit12.append(str(0))
            try:
                ws.write(kol + po, 9, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:12])))
            except TypeError:
                ws.write(kol + po, 9, "'" + str(0))
            # endregion
            # region 16
            try:
                ws.write(kol + po, 15, "'" + str(mk(str(cpo[3 * po - 1]))[:16]))
                bit16.append(str(twototen(mk(str(cpo[3 * po - 1]))[:16])))
            except TypeError:
                ws.write(kol + po, 15, "'" + str(0))
                bit16.append(str(0))
            try:
                ws.write(kol + po, 13, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:16])))
            except TypeError:
                ws.write(kol + po, 13, "'" + str(0))
            # endregion
            # region 20
            try:
                ws.write(kol + po, 19, "'" + str(mk(str(cpo[3 * po - 1]))[:20]))
                bit20.append(str(twototen(mk(str(cpo[3 * po - 1]))[:20])))
            except TypeError:
                ws.write(kol + po, 19, "'" + str(0))
                bit20.append(str(0))
            try:
                ws.write(kol + po, 17, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:20])))
            except TypeError:
                ws.write(kol + po, 17, "'" + str(0))
            # endregion
            # region 24
            try:
                ws.write(kol + po, 23, "'" + str(mk(str(cpo[3 * po - 1]))[:24]))
                bit24.append(str(twototen(mk(str(cpo[3 * po - 1]))[:24])))
            except TypeError:
                ws.write(kol + po, 23, "'" + str(0))
                bit24.append(str(0))
            try:
                ws.write(kol + po, 21, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:24])))
            except TypeError:
                ws.write(kol + po, 21, "'" + str(0))
            # endregion
            # region 32
            try:
                ws.write(kol + po, 27, "'" + str(mk(str(cpo[3 * po - 1]))[:32]))
                bit32.append(str(twototen(mk(str(cpo[3 * po - 1]))[:32])))
            except TypeError:
                ws.write(kol + po, 27, "'" + str(0))
                bit32.append(str(0))
            try:
                ws.write(kol + po, 25, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:32])))
            except TypeError:
                ws.write(kol + po, 25, "'" + str(0))
                # endregion

                # region Экспорт в Микрокаповские файлы разной разрядности
    ideal_.write(str(repl(n5, qazwsx, fd)))

    # file.write("\n\n\n"+str(bit8)+"\n\n\n")


    bit8_.write(str(repl(n5, bit8, fd)))
    bit12_.write(str(repl(n5, bit12, fd)))
    bit16_.write(str(repl(n5, bit16, fd)))
    bit20_.write(str(repl(n5, bit20, fd)))
    bit24_.write(str(repl(n5, bit24, fd)))
    bit32_.write(str(repl(n5, bit32, fd)))

    file.write('\n\nSecond Kaskad ' + str(k2p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef2(str(k2p3)))

    file.write('\n\nThird Kaskad ' + str(k3p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef3(str(k3p3)))
    file.write('\n\n' + str('(' + str(k1p3) + ')*(' + str(k2p3) + ')*(' + str(k3p3) + ')\n').replace('z**6',
                                                                                                     'z*z*z*z*z*z').replace(
        'z**5', 'z*z*z*z*z').replace('z**4', 'z*z*z*z').replace('z**3', 'z*z*z').replace('z**2', 'z*z'))
elif n == 7:

    p = simplify(str(a) + '*((z^2)-2*' + str(b) + '*z+1)/((z^2)-1)')

    k1p = simplify('1/((' + str(p) + ')+1)')
    k1p1, k1p2, k1p3 = karcas(k1p)

    k2p = simplify('1/((' + str(p) + ')^2+0.44504*(' + str(p) + ')+1)')
    k2p1, k2p2, k2p3 = karcas(k2p)

    k3p = simplify('1/((' + str(p) + ')^2+1.24698*(' + str(p) + ')+1)')
    k3p1, k3p2, k3p3 = karcas(k3p)

    k4p = simplify('1/((' + str(p) + ')^2+1.80194*(' + str(p) + ')+1)')
    k4p1, k4p2, k4p3 = karcas(k4p)

    file.write('fc1 ' + str(fc1) + '\n')
    file.write('fc2 ' + str(fc2) + '\n')
    file.write('fs1 ' + str(fs1) + '\n')
    file.write('fs2 ' + str(fs2) + '\n')
    file.write('fd ' + str(fd) + '\n\n')

    file.write('lc1 ' + str(lc1) + '\n')
    file.write('lc2 ' + str(lc2) + '\n')
    file.write('ls1 ' + str(ls1) + '\n')
    file.write('ls2 ' + str(ls2) + '\n\n')

    file.write('a ' + str(a) + '\n')
    file.write('b ' + str(b) + '\n\n')

    file.write('First Kaskad ' + str(k1p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef1(str(k1p3)))

    for kol in [1, 8, 19, 30]:
        if kol == 8:
            cpo = str(koef1(str(k2p3))).split()
            pops = 11
        elif kol == 19:
            cpo = str(koef1(str(k3p3))).split()
            pops = 11
        elif kol == 1:
            cpo = str(koef1(str(k1p3))).split()
            pops = 7
        else:
            cpo = str(koef1(str(k4p3))).split()
            pops = 11
        for po in range(1, pops):
            # region Рассчетные коэффициенты
            ws.write(kol + po, 1, "'" + str(cpo[3 * po - 1]))
            ws.write(kol + po, 3, "'" + str(mk(str(cpo[3 * po - 1]))))
            # endregion
            # region 8
            try:
                ws.write(kol + po, 7, "'" + str(mk(str(cpo[3 * po - 1]))[:8]))
            except TypeError:
                ws.write(kol + po, 7, "'" + str(0))
            try:
                ws.write(kol + po, 5, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:8])))
            except TypeError:
                ws.write(kol + po, 5, "'" + str(0))
            # endregion
            # region 12
            try:
                ws.write(kol + po, 11, "'" + str(mk(str(cpo[3 * po - 1]))[:12]))
            except TypeError:
                ws.write(kol + po, 11, "'" + str(0))
            try:
                ws.write(kol + po, 9, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:12])))
            except TypeError:
                ws.write(kol + po, 9, "'" + str(0))
            # endregion
            # region 16
            try:
                ws.write(kol + po, 15, "'" + str(mk(str(cpo[3 * po - 1]))[:16]))
            except TypeError:
                ws.write(kol + po, 15, "'" + str(0))
            try:
                ws.write(kol + po, 13, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:16])))
            except TypeError:
                ws.write(kol + po, 13, "'" + str(0))
            # endregion
            # region 20
            try:
                ws.write(kol + po, 19, "'" + str(mk(str(cpo[3 * po - 1]))[:20]))
            except TypeError:
                ws.write(kol + po, 19, "'" + str(0))
            try:
                ws.write(kol + po, 17, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:20])))
            except TypeError:
                ws.write(kol + po, 17, "'" + str(0))
            # endregion
            # region 24
            try:
                ws.write(kol + po, 23, "'" + str(mk(str(cpo[3 * po - 1]))[:24]))
            except TypeError:
                ws.write(kol + po, 23, "'" + str(0))
            try:
                ws.write(kol + po, 21, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:24])))
            except TypeError:
                ws.write(kol + po, 21, "'" + str(0))
            # endregion
            # region 32
            try:
                ws.write(kol + po, 27, "'" + str(mk(str(cpo[3 * po - 1]))[:32]))
            except TypeError:
                ws.write(kol + po, 27, "'" + str(0))
            try:
                ws.write(kol + po, 25, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:32])))
            except TypeError:
                ws.write(kol + po, 25, "'" + str(0))
                # endregion

    file.write('\n\nSecond Kaskad ' + str(k2p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef2(str(k2p3)))

    file.write('\n\nThird Kaskad ' + str(k3p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef3(str(k3p3)))

    file.write('\n\nFourth Kaskad ' + str(k4p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef4(str(k4p3)))

    file.write(
        '\n\n' + str('(' + str(k1p3) + ')*(' + str(k2p3) + ')*(' + str(k3p3) + ')*(' + str(k4p3) + ')\n').replace(
            'z**6', 'z*z*z*z*z*z').replace('z**5', 'z*z*z*z*z').replace('z**4', 'z*z*z*z').replace('z**3',
                                                                                                   'z*z*z').replace(
            'z**2', 'z*z'))
elif n == 8:

    p = simplify(str(a) + '*((z^2)-2*' + str(b) + '*z+1)/((z^2)-1)')

    k1p = simplify('1/((' + str(p) + ')^2+0.39018*(' + str(p) + ')+1)')
    k1p1, k1p2, k1p3 = karcas(k1p)

    k2p = simplify('1/((' + str(p) + ')^2+1.11114*(' + str(p) + ')+1)')
    k2p1, k2p2, k2p3 = karcas(k2p)

    k3p = simplify('1/((' + str(p) + ')^2+1.66294*(' + str(p) + ')+1)')
    k3p1, k3p2, k3p3 = karcas(k3p)

    k4p = simplify('1/((' + str(p) + ')^2+1.96157*(' + str(p) + ')+1)')
    k4p1, k4p2, k4p3 = karcas(k4p)

    file.write('fc1 ' + str(fc1) + '\n')
    file.write('fc2 ' + str(fc2) + '\n')
    file.write('fs1 ' + str(fs1) + '\n')
    file.write('fs2 ' + str(fs2) + '\n')
    file.write('fd ' + str(fd) + '\n\n')

    file.write('lc1 ' + str(lc1) + '\n')
    file.write('lc2 ' + str(lc2) + '\n')
    file.write('ls1 ' + str(ls1) + '\n')
    file.write('ls2 ' + str(ls2) + '\n\n')

    file.write('a ' + str(a) + '\n')
    file.write('b ' + str(b) + '\n\n')

    file.write('First Kaskad ' + str(k1p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef1(str(k1p3)))

    file.write('\n\nSecond Kaskad ' + str(k2p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef2(str(k2p3)))

    file.write('\n\nThird Kaskad ' + str(k3p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef3(str(k3p3)))

    file.write('\n\nFourth Kaskad ' + str(k4p3) + '\n')
    file.write('\nKoef\n')
    file.write(koef4(str(k4p3)))

    for kol in [1, 12, 23, 34]:
        for po in range(1, 11):
            # region Рассчетные коэффициенты
            ws.write(kol + po, 1, "'" + str(cpo[3 * po - 1]))
            ws.write(kol + po, 3, "'" + str(mk(str(cpo[3 * po - 1]))))
            # endregion
            # region 8
            try:
                ws.write(kol + po, 7, "'" + str(mk(str(cpo[3 * po - 1]))[:8]))
            except TypeError:
                ws.write(kol + po, 7, "'" + str(0))
            try:
                ws.write(kol + po, 5, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:8])))
            except TypeError:
                ws.write(kol + po, 5, "'" + str(0))
            # endregion
            # region 12
            try:
                ws.write(kol + po, 11, "'" + str(mk(str(cpo[3 * po - 1]))[:12]))
            except TypeError:
                ws.write(kol + po, 11, "'" + str(0))
            try:
                ws.write(kol + po, 9, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:12])))
            except TypeError:
                ws.write(kol + po, 9, "'" + str(0))
            # endregion
            # region 16
            try:
                ws.write(kol + po, 15, "'" + str(mk(str(cpo[3 * po - 1]))[:16]))
            except TypeError:
                ws.write(kol + po, 15, "'" + str(0))
            try:
                ws.write(kol + po, 13, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:16])))
            except TypeError:
                ws.write(kol + po, 13, "'" + str(0))
            # endregion
            # region 20
            try:
                ws.write(kol + po, 19, "'" + str(mk(str(cpo[3 * po - 1]))[:20]))
            except TypeError:
                ws.write(kol + po, 19, "'" + str(0))
            try:
                ws.write(kol + po, 17, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:20])))
            except TypeError:
                ws.write(kol + po, 17, "'" + str(0))
            # endregion
            # region 24
            try:
                ws.write(kol + po, 23, "'" + str(mk(str(cpo[3 * po - 1]))[:24]))
            except TypeError:
                ws.write(kol + po, 23, "'" + str(0))
            try:
                ws.write(kol + po, 21, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:24])))
            except TypeError:
                ws.write(kol + po, 21, "'" + str(0))
            # endregion
            # region 32
            try:
                ws.write(kol + po, 27, "'" + str(mk(str(cpo[3 * po - 1]))[:32]))
            except TypeError:
                ws.write(kol + po, 27, "'" + str(0))
            try:
                ws.write(kol + po, 25, "'" + str(twototen(mk(str(cpo[3 * po - 1]))[:32])))
            except TypeError:
                ws.write(kol + po, 25, "'" + str(0))
                # endregion

    file.write(
        '\n\n' + str('(' + str(k1p3) + ')*(' + str(k2p3) + ')*(' + str(k3p3) + ')*(' + str(k4p3) + ')\n').replace(
            'z**6', 'z*z*z*z*z*z').replace('z**5', 'z*z*z*z*z').replace('z**4', 'z*z*z*z').replace('z**3',
                                                                                                   'z*z*z').replace(
            'z**2', 'z*z'))
# endregion

# region Экспорт в Excel
print('Выполняется экспорт данных в Excel-таблицу')
if n == 1:

    for cala in range(1, 41):
        if cala % 2 != 0:
            ws.col(cala).width = 100
        elif cala == 3:
            ws.col(3).width = 20000
        elif cala == 1:
            ws.col(1).width = 7000
        elif cala % 2 == 0:
            ws.col(cala).width = 10000

    ws.write(0, 1, 'Рассчетные коэффициенты')
    ws.write(1, 1, '10 СС')
    ws.write(1, 3, '2 СС')

    ws.write(0, 5, '8 Разрядов')
    ws.write(1, 5, '10СС')
    ws.write(1, 7, '2СС')

    ws.write(0, 9, '12 Разрядов')
    ws.write(1, 9, '10СС')
    ws.write(1, 11, '2СС')

    ws.write(0, 13, '16 Разрядов')
    ws.write(1, 13, '10СС')
    ws.write(1, 15, '2СС')

    ws.write(0, 17, '20 Разрядов')
    ws.write(1, 17, '10СС')
    ws.write(1, 19, '2СС')

    ws.write(0, 21, '24 Разрядов')
    ws.write(1, 21, '10СС')
    ws.write(1, 23, '2СС')

    ws.write(0, 25, '32 Разрядов')
    ws.write(1, 25, '10СС')
    ws.write(1, 27, '2СС')

    ws.write(1, 0, '1-й Каскад')
    ws.write(2, 0, 'a0')
    ws.write(3, 0, 'a1')
    ws.write(4, 0, 'a2')
    ws.write(5, 0, 'b0')
    ws.write(6, 0, 'b1')
    ws.write(7, 0, 'b2')
elif n == 2:

    for cala in range(1, 41):
        if cala % 2 != 0:
            ws.col(cala).width = 100
        elif cala == 3:
            ws.col(3).width = 20000
        elif cala == 1:
            ws.col(1).width = 7000
        elif cala % 2 == 0:
            ws.col(cala).width = 10000

    ws.write(0, 1, 'Рассчетные коэффициенты')
    ws.write(1, 1, '10 СС')
    ws.write(1, 3, '2 СС')

    ws.write(0, 5, '8 Разрядов')
    ws.write(1, 5, '10СС')
    ws.write(1, 7, '2СС')

    ws.write(0, 9, '12 Разрядов')
    ws.write(1, 9, '10СС')
    ws.write(1, 11, '2СС')

    ws.write(0, 13, '16 Разрядов')
    ws.write(1, 13, '10СС')
    ws.write(1, 15, '2СС')

    ws.write(0, 17, '20 Разрядов')
    ws.write(1, 17, '10СС')
    ws.write(1, 19, '2СС')

    ws.write(0, 21, '24 Разрядов')
    ws.write(1, 21, '10СС')
    ws.write(1, 23, '2СС')

    ws.write(0, 25, '32 Разрядов')
    ws.write(1, 25, '10СС')
    ws.write(1, 27, '2СС')

    ws.write(1, 0, '1-й Каскад')
    ws.write(2, 0, 'a0')
    ws.write(3, 0, 'a1')
    ws.write(4, 0, 'a2')
    ws.write(5, 0, 'a3')
    ws.write(6, 0, 'a4')
    ws.write(7, 0, 'b0')
    ws.write(8, 0, 'b1')
    ws.write(9, 0, 'b2')
    ws.write(10, 0, 'b3')
    ws.write(11, 0, 'b4')
elif n == 3:

    for cala in range(1, 41):
        if cala % 2 != 0:
            ws.col(cala).width = 100
        elif cala == 3:
            ws.col(3).width = 20000
        elif cala == 1:
            ws.col(1).width = 7000
        elif cala % 2 == 0:
            ws.col(cala).width = 10000

    ws.write(0, 1, 'Рассчетные коэффициенты')
    ws.write(1, 1, '10 СС')
    ws.write(1, 3, '2 СС')

    ws.write(0, 5, '8 Разрядов')
    ws.write(1, 5, '10СС')
    ws.write(1, 7, '2СС')

    ws.write(0, 9, '12 Разрядов')
    ws.write(1, 9, '10СС')
    ws.write(1, 11, '2СС')

    ws.write(0, 13, '16 Разрядов')
    ws.write(1, 13, '10СС')
    ws.write(1, 15, '2СС')

    ws.write(0, 17, '20 Разрядов')
    ws.write(1, 17, '10СС')
    ws.write(1, 19, '2СС')

    ws.write(0, 21, '24 Разрядов')
    ws.write(1, 21, '10СС')
    ws.write(1, 23, '2СС')

    ws.write(0, 25, '32 Разрядов')
    ws.write(1, 25, '10СС')
    ws.write(1, 27, '2СС')

    ws.write(1, 0, '1-й Каскад')
    ws.write(2, 0, 'a0')
    ws.write(3, 0, 'a1')
    ws.write(4, 0, 'a2')
    ws.write(5, 0, 'b0')
    ws.write(6, 0, 'b1')
    ws.write(7, 0, 'b2')

    ws.write(8, 0, '2-й Каскад')
    ws.write(9, 0, 'a0')
    ws.write(10, 0, 'a1')
    ws.write(11, 0, 'a2')
    ws.write(12, 0, 'a3')
    ws.write(13, 0, 'a4')
    ws.write(14, 0, 'b0')
    ws.write(15, 0, 'b1')
    ws.write(16, 0, 'b2')
    ws.write(17, 0, 'b3')
    ws.write(18, 0, 'b4')
elif n == 4:

    for cala in range(1, 41):
        if cala % 2 != 0:
            ws.col(cala).width = 100
        elif cala == 3:
            ws.col(3).width = 20000
        elif cala == 1:
            ws.col(1).width = 7000
        elif cala % 2 == 0:
            ws.col(cala).width = 10000

    ws.write(0, 1, 'Рассчетные коэффициенты')
    ws.write(1, 1, '10 СС')
    ws.write(1, 3, '2 СС')

    ws.write(0, 5, '8 Разрядов')
    ws.write(1, 5, '10СС')
    ws.write(1, 7, '2СС')

    ws.write(0, 9, '12 Разрядов')
    ws.write(1, 9, '10СС')
    ws.write(1, 11, '2СС')

    ws.write(0, 13, '16 Разрядов')
    ws.write(1, 13, '10СС')
    ws.write(1, 15, '2СС')

    ws.write(0, 17, '20 Разрядов')
    ws.write(1, 17, '10СС')
    ws.write(1, 19, '2СС')

    ws.write(0, 21, '24 Разрядов')
    ws.write(1, 21, '10СС')
    ws.write(1, 23, '2СС')

    ws.write(0, 25, '32 Разрядов')
    ws.write(1, 25, '10СС')
    ws.write(1, 27, '2СС')

    ws.write(1, 0, '1-й Каскад')
    ws.write(2, 0, 'a0')
    ws.write(3, 0, 'a1')
    ws.write(4, 0, 'a2')
    ws.write(5, 0, 'a3')
    ws.write(6, 0, 'a4')
    ws.write(7, 0, 'b0')
    ws.write(8, 0, 'b1')
    ws.write(9, 0, 'b2')
    ws.write(10, 0, 'b3')
    ws.write(11, 0, 'b4')

    ws.write(12, 0, '2-й Каскад')
    ws.write(13, 0, 'a0')
    ws.write(14, 0, 'a1')
    ws.write(15, 0, 'a2')
    ws.write(16, 0, 'a3')
    ws.write(17, 0, 'a4')
    ws.write(18, 0, 'b0')
    ws.write(19, 0, 'b1')
    ws.write(20, 0, 'b2')
    ws.write(21, 0, 'b3')
    ws.write(22, 0, 'b4')
elif n == 5:

    for cala in range(1, 41):
        if cala % 2 != 0:
            ws.col(cala).width = 100
        elif cala == 3:
            ws.col(3).width = 20000
        elif cala == 1:
            ws.col(1).width = 7000
        elif cala % 2 == 0:
            ws.col(cala).width = 10000

    ws.write(0, 1, 'Рассчетные коэффициенты')
    ws.write(1, 1, '10 СС')
    ws.write(1, 3, '2 СС')
    ws.write(1, 0, '1-й Каскад')
    ws.write(2, 0, 'a0')
    ws.write(3, 0, 'a1')
    ws.write(4, 0, 'a2')
    ws.write(5, 0, 'b0')
    ws.write(6, 0, 'b1')
    ws.write(7, 0, 'b2')

    ws.write(0, 5, '8 Разрядов')
    ws.write(1, 5, '10СС')
    ws.write(1, 7, '2СС')

    ws.write(0, 9, '12 Разрядов')
    ws.write(1, 9, '10СС')
    ws.write(1, 11, '2СС')

    ws.write(0, 13, '16 Разрядов')
    ws.write(1, 13, '10СС')
    ws.write(1, 15, '2СС')

    ws.write(0, 17, '20 Разрядов')
    ws.write(1, 17, '10СС')
    ws.write(1, 19, '2СС')

    ws.write(0, 21, '24 Разрядов')
    ws.write(1, 21, '10СС')
    ws.write(1, 23, '2СС')

    ws.write(0, 25, '32 Разрядов')
    ws.write(1, 25, '10СС')
    ws.write(1, 27, '2СС')

    ws.write(8, 0, '2-й Каскад')
    ws.write(9, 0, 'a0')
    ws.write(10, 0, 'a1')
    ws.write(11, 0, 'a2')
    ws.write(12, 0, 'a3')
    ws.write(13, 0, 'a4')
    ws.write(14, 0, 'b0')
    ws.write(15, 0, 'b1')
    ws.write(16, 0, 'b2')
    ws.write(17, 0, 'b3')
    ws.write(18, 0, 'b4')

    ws.write(19, 0, '3-й Каскад')
    ws.write(20, 0, 'a0')
    ws.write(21, 0, 'a1')
    ws.write(22, 0, 'a2')
    ws.write(23, 0, 'a3')
    ws.write(24, 0, 'a4')
    ws.write(25, 0, 'b0')
    ws.write(26, 0, 'b1')
    ws.write(27, 0, 'b2')
    ws.write(28, 0, 'b3')
    ws.write(29, 0, 'b4')
elif n == 6:

    for cala in range(1, 41):
        if cala % 2 != 0:
            ws.col(cala).width = 100
        elif cala == 3:
            ws.col(cala).width = 20000
        elif cala == 1:
            ws.col(cala).width = 7000
        elif cala % 2 == 0:
            ws.col(cala).width = 10000

    ws.write(0, 1, 'Рассчетные коэффициенты')
    ws.write(1, 1, '10 СС')
    ws.write(1, 3, '2 СС')

    ws.write(0, 5, '8 Разрядов')
    ws.write(1, 5, '10СС')
    ws.write(1, 7, '2СС')

    ws.write(0, 9, '12 Разрядов')
    ws.write(1, 9, '10СС')
    ws.write(1, 11, '2СС')

    ws.write(0, 13, '16 Разрядов')
    ws.write(1, 13, '10СС')
    ws.write(1, 15, '2СС')

    ws.write(0, 17, '20 Разрядов')
    ws.write(1, 17, '10СС')
    ws.write(1, 19, '2СС')

    ws.write(0, 21, '24 Разрядов')
    ws.write(1, 21, '10СС')
    ws.write(1, 23, '2СС')

    ws.write(0, 25, '32 Разрядов')
    ws.write(1, 25, '10СС')
    ws.write(1, 27, '2СС')

    ws.write(1, 0, '1-й Каскад')
    ws.write(2, 0, 'a0')
    ws.write(3, 0, 'a1')
    ws.write(4, 0, 'a2')
    ws.write(5, 0, 'a3')
    ws.write(6, 0, 'a4')
    ws.write(7, 0, 'b0')
    ws.write(8, 0, 'b1')
    ws.write(9, 0, 'b2')
    ws.write(10, 0, 'b3')
    ws.write(11, 0, 'b4')

    ws.write(12, 0, '2-й Каскад')
    ws.write(13, 0, 'a0')
    ws.write(14, 0, 'a1')
    ws.write(15, 0, 'a2')
    ws.write(16, 0, 'a3')
    ws.write(17, 0, 'a4')
    ws.write(18, 0, 'b0')
    ws.write(19, 0, 'b1')
    ws.write(20, 0, 'b2')
    ws.write(21, 0, 'b3')
    ws.write(22, 0, 'b4')

    ws.write(23, 0, '3-й Каскад')
    ws.write(24, 0, 'a0')
    ws.write(25, 0, 'a1')
    ws.write(26, 0, 'a2')
    ws.write(27, 0, 'a3')
    ws.write(28, 0, 'a4')
    ws.write(29, 0, 'b0')
    ws.write(30, 0, 'b1')
    ws.write(31, 0, 'b2')
    ws.write(32, 0, 'b3')
    ws.write(33, 0, 'b4')
elif n == 7:

    for cala in range(1, 41):
        if cala % 2 != 0:
            ws.col(cala).width = 100
        elif cala == 3:
            ws.col(cala).width = 20000
        elif cala == 1:
            ws.col(cala).width = 7000
        elif cala % 2 == 0:
            ws.col(cala).width = 10000

    ws.write(0, 1, 'Рассчетные коэффициенты')
    ws.write(1, 1, '10 СС')
    ws.write(1, 3, '2 СС')

    ws.write(0, 5, '8 Разрядов')
    ws.write(1, 5, '10СС')
    ws.write(1, 7, '2СС')

    ws.write(0, 9, '12 Разрядов')
    ws.write(1, 9, '10СС')
    ws.write(1, 11, '2СС')

    ws.write(0, 13, '16 Разрядов')
    ws.write(1, 13, '10СС')
    ws.write(1, 15, '2СС')

    ws.write(0, 17, '20 Разрядов')
    ws.write(1, 17, '10СС')
    ws.write(1, 19, '2СС')

    ws.write(0, 21, '24 Разрядов')
    ws.write(1, 21, '10СС')
    ws.write(1, 23, '2СС')

    ws.write(0, 25, '32 Разрядов')
    ws.write(1, 25, '10СС')
    ws.write(1, 27, '2СС')

    ws.write(1, 0, '1-й Каскад')
    ws.write(2, 0, 'a0')
    ws.write(3, 0, 'a1')
    ws.write(4, 0, 'a2')
    ws.write(5, 0, 'b0')
    ws.write(6, 0, 'b1')
    ws.write(7, 0, 'b2')

    ws.write(8, 0, '2-й Каскад')
    ws.write(9, 0, 'a0')
    ws.write(10, 0, 'a1')
    ws.write(11, 0, 'a2')
    ws.write(12, 0, 'a3')
    ws.write(13, 0, 'a4')
    ws.write(14, 0, 'b0')
    ws.write(15, 0, 'b1')
    ws.write(16, 0, 'b2')
    ws.write(17, 0, 'b3')
    ws.write(18, 0, 'b4')

    ws.write(19, 0, '3-й Каскад')
    ws.write(20, 0, 'a0')
    ws.write(21, 0, 'a1')
    ws.write(22, 0, 'a2')
    ws.write(23, 0, 'a3')
    ws.write(24, 0, 'a4')
    ws.write(25, 0, 'b0')
    ws.write(26, 0, 'b1')
    ws.write(27, 0, 'b2')
    ws.write(28, 0, 'b3')
    ws.write(29, 0, 'b4')

    ws.write(30, 0, '4-й Каскад')
    ws.write(31, 0, 'a0')
    ws.write(32, 0, 'a1')
    ws.write(33, 0, 'a2')
    ws.write(34, 0, 'a3')
    ws.write(35, 0, 'a4')
    ws.write(36, 0, 'b0')
    ws.write(37, 0, 'b1')
    ws.write(38, 0, 'b2')
    ws.write(39, 0, 'b3')
    ws.write(40, 0, 'b4')
elif n == 8:

    for cala in range(1, 41):
        if cala % 2 != 0:
            ws.col(cala).width = 100
        elif cala == 3:
            ws.col(3).width = 20000
        elif cala == 1:
            ws.col(1).width = 7000
        elif cala % 2 == 0:
            ws.col(cala).width = 10000

    ws.write(0, 1, 'Рассчетные коэффициенты')
    ws.write(1, 1, '10 СС')
    ws.write(1, 3, '2 СС')

    ws.write(0, 5, '8 Разрядов')
    ws.write(1, 5, '10СС')
    ws.write(1, 7, '2СС')

    ws.write(0, 9, '12 Разрядов')
    ws.write(1, 9, '10СС')
    ws.write(1, 11, '2СС')

    ws.write(0, 13, '16 Разрядов')
    ws.write(1, 13, '10СС')
    ws.write(1, 15, '2СС')

    ws.write(0, 17, '20 Разрядов')
    ws.write(1, 17, '10СС')
    ws.write(1, 19, '2СС')

    ws.write(0, 21, '24 Разрядов')
    ws.write(1, 21, '10СС')
    ws.write(1, 23, '2СС')

    ws.write(0, 25, '32 Разрядов')
    ws.write(1, 25, '10СС')
    ws.write(1, 27, '2СС')

    ws.write(1, 0, '1-й Каскад')
    ws.write(2, 0, 'a0')
    ws.write(3, 0, 'a1')
    ws.write(4, 0, 'a2')
    ws.write(5, 0, 'a3')
    ws.write(6, 0, 'a4')
    ws.write(7, 0, 'b0')
    ws.write(8, 0, 'b1')
    ws.write(9, 0, 'b2')
    ws.write(10, 0, 'b3')
    ws.write(11, 0, 'b4')

    ws.write(12, 0, '2-й Каскад')
    ws.write(13, 0, 'a0')
    ws.write(14, 0, 'a1')
    ws.write(15, 0, 'a2')
    ws.write(16, 0, 'a3')
    ws.write(17, 0, 'a4')
    ws.write(18, 0, 'b0')
    ws.write(19, 0, 'b1')
    ws.write(20, 0, 'b2')
    ws.write(21, 0, 'b3')
    ws.write(22, 0, 'b4')

    ws.write(23, 0, '3-й Каскад')
    ws.write(24, 0, 'a0')
    ws.write(25, 0, 'a1')
    ws.write(26, 0, 'a2')
    ws.write(27, 0, 'a3')
    ws.write(28, 0, 'a4')
    ws.write(29, 0, 'b0')
    ws.write(30, 0, 'b1')
    ws.write(31, 0, 'b2')
    ws.write(32, 0, 'b3')
    ws.write(33, 0, 'b4')

    ws.write(34, 0, '4-й Каскад')
    ws.write(35, 0, 'a0')
    ws.write(36, 0, 'a1')
    ws.write(37, 0, 'a2')
    ws.write(38, 0, 'a3')
    ws.write(39, 0, 'a4')
    ws.write(40, 0, 'b0')
    ws.write(41, 0, 'b1')
    ws.write(42, 0, 'b2')
    ws.write(43, 0, 'b3')
    ws.write(44, 0, 'b4')
# endregion

file.close()
wb.save('TablKurs.xls')
print('Ok')

