import datetime
from django.db.models import Count
from models import *

X = datetime.date(year=2012, month=1, day=1)

vykony = Vykon.objects.filter(datum__gte=X)
muzi = vykony.filter(lecba__pacient__pohlavi='M')
zeny = vykony.filter(lecba__pacient__pohlavi='Z')

print 'Vykony: %s' % vykony.count()
print 'Vykony muzi: %s' % muzi.count()
print 'Vykony zeny: %s' % zeny.count()
print

# for kod in Kod.objects.all().order_by('cislo'):
#     print '%s: %s' % (kod, vykony.filter(kod=kod).count())
#
# for kod in Kod.objects.all().order_by('cislo'):
#     cnt = muzi.filter(kod=kod).count()
#     if cnt:
#         print 'M: %s: %s' % (kod, muzi.filter(kod=kod).count())

for kod in Kod.objects.all().order_by('cislo'):
    cnt = zeny.filter(kod=kod).count()
    if cnt:
        print 'Z: %s: %s' % (kod, cnt)

# lecby = Lecba.objects.filter(vykon__datum__gte=X).distinct()
# lecby_m = Lecba.objects.filter(vykon__datum__gte=X, pacient__pohlavi='M').distinct()
# lecby_z = Lecba.objects.filter(vykon__datum__gte=X, pacient__pohlavi='Z').distinct()
#
# print lecby.count(), lecby_m.count(), lecby_z.count()

# diags = {}
# for line in open('diagnozy.csv'):
#    dg, pocet = line.strip().split(';')
#    diags[dg] = {'w': pocet, 'd': 0}
#
# for diagnoza in Diagnoza.objects.all().order_by('nazev'):
#     cnt = lecby_z.filter(diagnoza=diagnoza).count()
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
