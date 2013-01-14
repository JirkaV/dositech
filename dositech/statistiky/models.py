from django.db import models

class Pojistovna(models.Model):
    cislo = models.CharField(max_length=5)

    class Meta:
        app_label = 'statistiky'

    def __unicode__(self):
        return self.cislo

class Pacient(models.Model):
    rc = models.CharField(max_length=20)
    pohlavi = models.CharField(max_length=1)

    class Meta:
        app_label = 'statistiky'

    def __unicode__(self):
        return self.rc

class Kod(models.Model):
    cislo = models.CharField(max_length=20)

    class Meta:
        app_label = 'statistiky'

    def __unicode__(self):
        return self.cislo

class Diagnoza(models.Model):
    nazev = models.CharField(max_length=8)

    class Meta:
        app_label = 'statistiky'

    def __unicode__(self):
        return self.nazev

class Lecba(models.Model):
    ucet = models.CharField(max_length=15)
    pacient = models.ForeignKey(Pacient)
    diagnoza = models.ForeignKey(Diagnoza, related_name='lecba')
    pojistovna = models.ForeignKey(Pojistovna)

    class Meta:
        app_label = 'statistiky'

class Vykon(models.Model):
    lecba = models.ForeignKey(Lecba, related_name='vykon')
    datum = models.DateField()
    kod = models.ForeignKey(Kod)
    pocet = models.PositiveIntegerField(default=1)

    class Meta:
        app_label = 'statistiky'
