from django import forms
from django.core import validators
from django.contrib.admin.widgets import AdminTimeWidget,AdminDateWidget
import re

class_join_option = [['','A class: Monday and Thurday 1800-1930'],['','B class : Tuesday and Friday 1800-1930'],['3','I am OK with either of them']]

def is_empty(value):
    if value:
        raise forms.ValidationError("is not empty")

def clean_mobile(value):
    pattern = re.compile("^([9,8,7]{1})([0-9]{1})([0-9]{8})$")
    if not pattern.match(str(value)):
        raise forms.ValidationError("Invalid Mobile Number")


class apply_form(forms.Form):
    class_join_option = forms.CharField(label="Class join option",widget=forms.Select(choices=[('A class: Monday and Thursday 18:00-19:30','A class: Monday and Thurday 18:00-19:30'),('B class : Tuesday and Friday 18:00-19:30','B class : Tuesday and Friday 18:00-19:30'),('I am OK with either of them','I am OK with either of them')]))
    Do_you_know_the_policy_of_getting_certificate_in_this_course_Please_copy_and_paste_the_policy_here = forms.CharField(widget=forms.Textarea,required=False)
    cancel_policy = forms.TypedChoiceField(label="The candidature of those who will be absent in the first class without prior notice shall stand cancelled. Do you agree with this policy ?",coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')),widget=forms.RadioSelect)
    sel_japan_internship = forms.TypedChoiceField(label="Have you already been selected for an internship/exchange programme in Japan in 2017 or 2018 ?",coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')),widget=forms.RadioSelect)
    the_name_of_the_organisation_for_which_you_are_selected_for_internship_or_exchange_student = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')),widget=forms.RadioSelect)
    department = forms.CharField(label="What is your Department",widget=forms.Select(choices=[('BSBE','BSBE'),('CL','CL'),('CH','CH'),('CSE','CSE'),('Des','Des'),('EEE','EEE'),('HSS','HSS'),('MA','MA'),('ME','ME'),('Phy','Phy'),('Centre for Energy','Centre for Energy'),('Centre for Environment','Centre for Environment'),('Centre for Linguistic Sc and Tech','Centre for Linguistic Sc and Tech'),('Centre for NanoTech','Centre for Linguistic Sc and NanoTech'),('Centre for Rural Tech','Centre for Rural Tech'),('Others','Others')]))
    designation = forms.CharField(label="Programme enrolled : ",widget=forms.Select(choices=[('PhD','PhD'),('Masters','Masters'),('3/4 year BTech/BDes','3/4 year BTech/BDes')]))
    present_year_of_study = forms.CharField(label="Your current year of Programme:",widget=forms.Select(choices=[('1st Year','1st Year'),('2nd Year','2nd Year'),('3rd Year','3rd Year'),('4th Year','4th Year'),('5th Year','5th Year'),('Other','Other')]))
    taken_japanese_course = forms.CharField(label="Have you ever taken Japanese Course",widget=forms.Select(choices=[('Yes,last semester February to April 2017','Yes,last semester February to April 2017'),('Yes,summer course','Yes,summer course'),('Yes, I took a a course in Japan','Yes, I took a a course in Japan'),('No','No'),('Other','Other')]))
    visited_japan = forms.CharField(label="Have you ever visited Japan",widget=forms.Select(choices=[('yes','yes'),('no','no')]))
    name = forms.CharField()
    roll_number = forms.IntegerField()
    mobile_number = forms.IntegerField(validators=[clean_mobile])
    email = forms.EmailField()
    queries = forms.CharField(widget=forms.Textarea,required=False)
    honeypot = forms.CharField(required=False,widget=forms.HiddenInput,label="Leave It Empty",validators=[is_empty])

    def clean_honeypot(self):
        honeypot = self.cleaned_data['honeypot']
        if len(honeypot):
            raise forms.ValidationError("It should be empty")
        return honeypot

class apply_form_france(forms.Form):
    Do_you_know_the_policy_of_getting_certificate_in_this_course_Please_copy_and_paste_the_policy_here = forms.CharField(widget=forms.Textarea,required=False)
    cancel_policy = forms.TypedChoiceField(label="The candidature of those who will be absent in the first class without prior notice shall stand cancelled. Do you agree with this policy ?",coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')),widget=forms.RadioSelect)
    sel_france_internship = forms.TypedChoiceField(label="Have you already been selected for an internship/exchange programme in France in 2017 or 2018 ?",coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')),widget=forms.RadioSelect)
    the_name_of_the_organisation_for_which_you_are_selected_for_internship_or_exchange_student = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')),widget=forms.RadioSelect)
    department = forms.CharField(label="What is your Department",widget=forms.Select(choices=[('BSBE','BSBE'),('CL','CL'),('CH','CH'),('CSE','CSE'),('Des','Des'),('EEE','EEE'),('HSS','HSS'),('MA','MA'),('ME','ME'),('Phy','Phy'),('Centre for Energy','Centre for Energy'),('Centre for Environment','Centre for Environment'),('Centre for Linguistic Sc and Tech','Centre for Linguistic Sc and Tech'),('Centre for NanoTech','Centre for Linguistic Sc and NanoTech'),('Centre for Rural Tech','Centre for Rural Tech'),('Others','Others')]))
    designation = forms.CharField(label="Programme enrolled : ",widget=forms.Select(choices=[('PhD','PhD'),('Masters','Masters'),('3/4 year BTech/BDes','3/4 year BTech/BDes')]))
    present_year_of_study = forms.CharField(label="Your current year of Programme:",widget=forms.Select(choices=[('1st Year','1st Year'),('2nd Year','2nd Year'),('3rd Year','3rd Year'),('4th Year','4th Year'),('5th Year','5th Year'),('Other','Other')]))
    taken_french_course = forms.CharField(label="Have you ever taken French Course",widget=forms.Select(choices=[('Yes,last semester February to April 2017','Yes,last semester February to April 2017'),('Yes,summer course','Yes,summer course'),('Yes, I took a a course in France','Yes, I took a a course in France'),('No','No'),('Other','Other')]))
    name = forms.CharField()
    roll_number = forms.IntegerField()
    mobile_number = forms.IntegerField(validators=[clean_mobile])
    email = forms.EmailField()
    queries = forms.CharField(widget=forms.Textarea,required=False)
    honeypot = forms.CharField(required=False,widget=forms.HiddenInput,label="Leave It Empty",validators=[is_empty])

    def clean_honeypot(self):
        honeypot = self.cleaned_data['honeypot']
        if len(honeypot):
            raise forms.ValidationError("It should be empty")
        return honeypot


class select_form(forms.Form):
    roll_number = forms.IntegerField(label="Roll Number : ")
    lang_choice = forms.CharField(label="Language Course : ",widget=forms.Select(choices=[("Japanese","Japanese"),("French","French")]))
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput, label="Leave It Empty", validators=[is_empty])

    def clean_honeypot(self):
        honeypot = self.cleaned_data['honeypot']
        if len(honeypot):
            raise forms.ValidationError("It should be empty")
        return honeypot


