from __future__ import unicode_literals

from django.db import models

class response(models.Model):
    request_id = models.CharField(max_length=16,blank=False)
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(blank=False)
    mobile_number = models.IntegerField(blank=False)
    email = models.EmailField(blank=False)
    queries = models.TextField(max_length=700)
    creation_time = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    payment_amount = models.IntegerField()
    payment_commission_charges = models.IntegerField()
    form_category = models.CharField(max_length=10)
    class_join_option_sel = models.CharField(max_length=100)
    policy_getting_certificate = models.CharField(max_length=100)
    cancel_policy = models.CharField(max_length=100)
    sel_japan_internship = models.CharField(max_length=100)
    name_of_org_sel_internship = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    present_year_of_study = models.CharField(max_length=100)
    taken_japanese_course = models.CharField(max_length=100)
    visited_japan = models.CharField(max_length=100)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return str('%s %s' %(self.roll_number,self.request_id))


class response_french(models.Model):
    request_id = models.CharField(max_length=16, blank=False)
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(blank=False)
    mobile_number = models.IntegerField(blank=False)
    email = models.EmailField(blank=False)
    queries = models.TextField(max_length=700)
    creation_time = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    payment_amount = models.IntegerField()
    payment_commission_charges = models.IntegerField()
    form_category = models.CharField(max_length=10)
    policy_getting_certificate = models.CharField(max_length=100)
    cancel_policy = models.CharField(max_length=100)
    sel_france_internship = models.CharField(max_length=100)
    name_of_org_sel_internship = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    present_year_of_study = models.CharField(max_length=100)
    taken_french_course = models.CharField(max_length=100)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return str('%s %s' % (self.roll_number, self.request_id))

class access_model(models.Model):
    access_id = models.CharField(max_length=43)
    roll_number = models.IntegerField(blank=False)
    is_filled = models.BooleanField(default=False)
    filled_option = models.CharField(max_length=25)
    is_blocked = models.BooleanField(default=False)


    def __str__(self):
        return self.access_id