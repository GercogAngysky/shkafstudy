from django.db import models

class Person(models.Model):
    name = models.CharField("имя", max_length=128)
    family_name = models.CharField("фамилия", max_length=128)
    father_name = models.CharField("отчество", max_length=128)
    date_of_birth = models.DateField("день рождения", default = "yyyy-mm-dd")
    passport_number = models.CharField("номер паспорта", max_length=20, unique = True)
    phone_number_1 = models.CharField("номер телефона 1", max_length=20)
    phone_number_2 = models.CharField("номер телефона 2", max_length=20, null=True, blank = True)
    email = models.EmailField("email", null=True, blank = True)
    note  = models.CharField("примечание", max_length=128, null=True, blank = True)
    adress = models.ForeignKey("Adress",  on_delete = models.SET_NULL, null=True, blank = False)

    def __str__(self):
        return f"{self.name} {self.father_name} {self.family_name}"

    class Meta:
        unique_together = [('name', 'family_name', 'father_name', 'date_of_birth'),]
        ordering = ['family_name', 'name', 'father_name']


class Adress(models.Model):
    city = models.CharField("город", max_length=128, default = 'Ноябрьск')
    street = models.CharField("улица", max_length=128)
    house = models.CharField("№ дома", max_length=128)
    apartment = models.CharField("№ квартиры", max_length=128)
    porch = models.CharField("№ подъезда", max_length=128, null=True, blank = True)
    floor = models.CharField("№ этажа", max_length=128, null=True, blank = True)
    intercom = models.CharField("№ домофона", max_length=128)
    note  = models.CharField("примечание", max_length=128, null=True, blank = True)

    def __str__(self):
        return f"{self.street} {self.house} {self.apartment}"

    class Meta:
        unique_together = [('street', 'house', 'apartment'),]
        ordering = ['street', 'house', 'apartment']


class Organization(models.Model):
    name = models.CharField("название организации", max_length=128, unique = True)
    inn = models.CharField("ИНН", max_length=128)
    okwed = models.CharField("ОКВЭД", max_length=128)
    bank = models.CharField("банк", max_length=128)
    bik = models.CharField("БИК", max_length=128)
    account = models.CharField("расчетный_счет", max_length=128)
    phone_number_1 = models.CharField("номер телефона", max_length=128)
    phone_number_2 = models.CharField("номер телефона", max_length=128)
    email = models.EmailField("email", null=True, blank = True)
    adress = models.CharField("адрес", max_length=128, null=True, blank = True)
    wedsite = models.CharField("wedsite", max_length=128, null=True, blank = True)
    note = models.CharField("примечание", max_length=128, null=True, blank = True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['name']

