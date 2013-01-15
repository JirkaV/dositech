import datetime
from django.db.models import Count
from models import *

X = datetime.date(year=2012, month=1, day=1)

vykony = Vykon.objects.filter(datum__gte=X)
# muzi = vykony.filter(lecba__pacient__pohlavi='M')
# zeny = vykony.filter(lecba__pacient__pohlavi='Z')


# print 'Vykony: %s' % vykony.count()
# print 'Vykony muzi: %s' % muzi.count()
# print 'Vykony zeny: %s' % zeny.count()
# print
#
# for kod in Kod.objects.all().order_by('cislo'):
#     print '%s: %s' % (kod, vykony.filter(kod=kod).count())
#
# for kod in Kod.objects.all().order_by('cislo'):
#     cnt = muzi.filter(kod=kod).count()
#     if cnt:
#         print 'M: %s: %s' % (kod, muzi.filter(kod=kod).count())

# for kod in Kod.objects.all().order_by('cislo'):
#     cnt = vykony.filter(kod=kod).count()
#     if cnt:
#         print '%s: %s' % (kod, cnt)

lecby = Lecba.objects.filter(vykon__datum__gte=X).distinct()
# lecby_m = Lecba.objects.filter(vykon__datum__gte=X, pacient__pohlavi='M').distinct()
# lecby_z = Lecba.objects.filter(vykon__datum__gte=X, pacient__pohlavi='Z').distinct()
#
# print lecby.count(), lecby_m.count(), lecby_z.count()

# diags = {}
# for line in open('diag_muzi.txt'):
#    dg, pocet = line.strip().split(';')
#    diags[dg] = {'w': pocet, 'd': 0}
#
# for diagnoza in Diagnoza.objects.all().order_by('nazev'):
#     cnt = lecby_m.filter(diagnoza=diagnoza).count()
#     dg = diagnoza.nazev
#     if cnt:
#         try:
#             diags[dg]['d'] = cnt
#         except KeyError:
#             diags[dg] = {'w': 0, 'd': cnt}
#
# for k, v in diags.items():
#     print '%s;%s;%s' % (k, v['w'], v['d'])
#

pacienti_w = set()
for line in open('rc.txt'):
    rc = line.strip()
    x = int(rc)
    if len(rc) < 10:
        if x % 11 == 0:
            rc = '0%s' % rc
        else:
            c = int(rc[2:4])
            if not (c <= 12 or 50 <= c <= 62):
                print '[!] %s' % rc
    pacienti_w.add(rc)
print 'W: %s' % len(pacienti_w)

pacienti_d = set(vykony.values_list('lecba__pacient__rc', flat=True).distinct())
for p in sorted(pacienti_d):
    print p
print 'D: %s' % len(pacienti_d)

pacienti = pacienti_w | pacienti_d
print 'Celkem: %s' % len(pacienti)

# for p in pacienti:
#     print p
