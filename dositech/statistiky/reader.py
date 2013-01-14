import os
from dbfpy.dbf import Dbf

from models import *

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
main_db_file = os.path.join(data_dir, 'stack.dbf')

main_db = Dbf(main_db_file)

databases = []

for rec in main_db:
    fmask = '%s.%s' % (rec['PRESS'][1:], rec['DBF_EXT'])
    databases.append(fmask)

for db_mask in databases:
    print '* %s' % db_mask

    ucty = 'E%s' % db_mask
    fname = os.path.join(data_dir, ucty)
    db = Dbf(fname)

    for rec in db:
        if rec.deleted:
            print '[d] skipping deleted record, %s' % rec['HCID']
            continue
        rc = rec['HROD'].strip()
        if rc[2] in ['0', '1']:
            pohlavi = 'M'
        elif rc[2] in ['5', '6']:
            pohlavi = 'Z'
        else:
            print '[!] Spatne RC: %s' % rc
            continue
        pojistovna, _ = Pojistovna.objects.get_or_create(cislo=rec['HCPO'].strip())
        diagnoza, _ = Diagnoza.objects.get_or_create(nazev=rec['HZDG'].strip())
        pacient, _ = Pacient.objects.get_or_create(rc=rc, pohlavi=pohlavi)
        ucet = rec['HCID']
        lecba, _ = Lecba.objects.get_or_create(ucet=ucet,
                                               pacient=pacient,
                                               diagnoza=diagnoza,
                                               pojistovna=pojistovna)


    vykony = '&%s' % db_mask
    fname = os.path.join(data_dir, vykony)
    try:
        db = Dbf(fname)
    except IOError:
        continue
    for rec in db:
        if rec.deleted:
            print '[d] skipping deleted record, %s' % rec['UCET']
            continue

        datum = rec['VDAT']
        ucet = rec['UCET']
        pocet = rec['VPOC']
        kod, _ = Kod.objects.get_or_create(cislo=rec['VKOD'])
        try:
            lecba = Lecba.objects.get(ucet=ucet)
        except Lecba.MultipleObjectsReturned:
            print '[!] Duplicate: ucet=%s' % ucet
#            lecby = Lecba.objects.filter(ucet=ucet)
#             for lecba in lecby:
#                 print ucet, datum
            continue

        vykon, _ = Vykon.objects.get_or_create(kod=kod,
                                               datum=datum,
                                               pocet=pocet,
                                               lecba=lecba)
