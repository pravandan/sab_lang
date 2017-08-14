from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from . import forms
from form_app.models import response,access_model,response_french
from time import gmtime, strftime
from string import ascii_uppercase,digits
import string
import random

from form_app.payments_create_request import create_request

def create_request_id():
    return 'IITG'+'L' + ''.join(random.choice(string.digits) for _ in range(11))

def create_access_id():
    return ''.join(random.choice(string.digits + string.ascii_uppercase + string.ascii_lowercase) for _ in range(43))

request_id = ''
access_id = ''

def sel_index(request):
    form = forms.select_form()
    if request.method == 'POST':
        form = forms.select_form(request.POST)

        if form.is_valid():
            try:
                q_access_model = access_model.objects.get(roll_number=form.cleaned_data['roll_number'])
            except:
                q_access_model = None
            if q_access_model:
                if not q_access_model.is_filled:
                    if q_access_model.filled_option == 'Japanese':
                        return redirect('/form/fill/' + q_access_model.access_id)
                    else:
                        return redirect('/form/fill/france/' + q_access_model.access_id)
                else:
                    return HttpResponse('You have already applied')
            else:

                new_model = access_model()
                access_id = create_access_id()
                new_model.access_id = access_id
                new_model.roll_number = form.cleaned_data['roll_number']
                new_model.filled_option = form.cleaned_data['lang_choice']
                new_model.save()
                if new_model.filled_option == 'Japanese':
                    return redirect('/form/fill/'+access_id)
                else:
                    return redirect('/form/fill/france/' + access_id)

    return render(request,'form_app/form_choice.html',{'form':form})


def index(request,access_id):
    access_response = get_object_or_404(access_model,access_id=access_id)
    if access_response.filled_option == 'Japanese':
        form = forms.apply_form()
    else:
        form = forms.apply_form_france()
    showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    if access_response:
        if access_response.is_filled:
            return HttpResponse('You have already filled the form')


        if access_response.filled_option == 'Japanese':
            form = forms.apply_form()

            if request.method == 'POST':

                form = forms.apply_form(request.POST)

                if form.is_valid():
                    request_id = create_request_id()
                    new_response = response()
                    new_response.request_id = request_id
                    new_response.name = form.cleaned_data['name']
                    new_response.roll_number = form.cleaned_data['roll_number']
                    new_response.mobile_number = form.cleaned_data['mobile_number']
                    new_response.email = form.cleaned_data['email']
                    new_response.queries = form.cleaned_data['queries']
                    new_response.creation_time = showtime
                    new_response.payment_id = 'UNDER MAINTENANCE'
                    new_response.payment_amount = '0'
                    new_response.payment_commission_charges = '0'
                    new_response.form_category = 'TEST'
                    new_response.class_join_option_sel = form.cleaned_data['class_join_option']
                    new_response.cancel_policy = form.cleaned_data['cancel_policy']
                    new_response.sel_japan_internship = form.cleaned_data['sel_japan_internship']
                    new_response.name_of_org_sel_internship = form.cleaned_data['the_name_of_the_organisation_for_which_you_are_selected_for_internship_or_exchange_student']
                    new_response.department = form.cleaned_data['department']
                    new_response.designation = form.cleaned_data['designation']
                    new_response.present_year_of_study = form.cleaned_data['present_year_of_study']
                    new_response.taken_japanese_course = form.cleaned_data['taken_japanese_course']
                    new_response.visited_japan = form.cleaned_data['visited_japan']
                    new_response.policy_getting_certificate = form.cleaned_data['Do_you_know_the_policy_of_getting_certificate_in_this_course_Please_copy_and_paste_the_policy_here']
                    #print (new_response)
                    new_response.save()
                    q_access_model = access_model.objects.get(access_id=access_id)
                    q_access_model.is_filled = True
                    q_access_model.save()
                    return redirect('/form/'+request_id[5:])

        return render(request, 'form_app/index.html', {'form': form,'access_id':access_id})

    return HttpResponse('Invalid')

def french_form(request,access_id):
    access_response = get_object_or_404(access_model, access_id=access_id)
    showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    if access_response:
        print('works_access')
        if access_response.is_filled:
            return HttpResponse('You have already filled the form')
        else:
            print('works_else')
            form = forms.apply_form_france()

            if request.method == 'POST':
                form = forms.apply_form_france(request.POST)
                if form.is_valid():

                    request_id = create_request_id()
                    new_response = response_french()
                    new_response.request_id = request_id
                    new_response.name = form.cleaned_data['name']
                    new_response.roll_number = form.cleaned_data['roll_number']
                    new_response.mobile_number = form.cleaned_data['mobile_number']
                    new_response.email = form.cleaned_data['email']
                    new_response.creation_time = showtime
                    new_response.queries = form.cleaned_data['queries']
                    new_response.policy_getting_certificate = form.cleaned_data['Do_you_know_the_policy_of_getting_certificate_in_this_course_Please_copy_and_paste_the_policy_here']
                    new_response.cancel_policy = form.cleaned_data['cancel_policy']
                    new_response.sel_france_internship = form.cleaned_data['sel_france_internship']
                    new_response.name_of_org_sel_internship = form.cleaned_data['the_name_of_the_organisation_for_which_you_are_selected_for_internship_or_exchange_student']
                    new_response.department = form.cleaned_data['department']
                    new_response.designation = form.cleaned_data['designation']
                    new_response.present_year_of_study = form.cleaned_data['present_year_of_study']
                    new_response.taken_french_course = form.cleaned_data['taken_french_course']
                    new_response.payment_id = 'UNDER MAINTENANCE'
                    new_response.payment_amount = '0'
                    new_response.payment_commission_charges = '0'
                    new_response.form_category = 'TEST'
                    new_response.save()
                    q_access_model = access_model.objects.get(access_id=access_id)
                    q_access_model.is_filled = True
                    q_access_model.save()
                    return redirect('/form/' + request_id[5:])

        return render(request, 'form_app/france_index.html', {'form': form, 'access_id': access_id})

    return HttpResponse('Invalid')

def success(request,request_id):
    response_obj = None
    try:
        response_obj = response.objects.get(request_id='IITGL'+request_id)
    except response.DoesNotExist:
        response_obj = None
    try:
        response_obj = response_french.objects.get(request_id='IITGL'+request_id)
        
    except response_french.DoesNotExist:
        response_obj = None
    if response_obj:
        return render(request,'form_app/success.html',{'request_id':request_id})
    else:
        return HttpResponse('Invalid')
