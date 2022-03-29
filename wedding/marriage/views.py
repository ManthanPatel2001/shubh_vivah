from difflib import Match
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Customer,Intrest, Reject, Matched
from datetime import date
import json
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe          
# Create your views here.


# def header Current User Name
def name_cur_user(request):
    if 'login_check' in request.session:
        cur_user = Customer.objects.get(email = request.session['login_check'])
        return [cur_user.image,cur_user.f_name]
    else:
        return cur_user['','']
# login Page
def login(request):
    if request.method == 'GET':
        loginForm = request.GET
        # check for email and Password are filds are empty or not
        if loginForm.get('email') and loginForm.get('password'):
            # check email and password exists in database
            if Customer.objects.filter(email = loginForm.get('email'), password = loginForm.get('password')).exists():
                # set the session 
                request.session['login_check'] = loginForm.get('email')
                return redirect('home')
            else:
                return render(request, 'register/login.html',{'errorMsg':'PLEASE ENTER VALID EMAIL OR PASSWORD'})
    elif request.method == 'POST':
        registerForm = request.POST
        today = date.today()
        # make an array of date
        printDate = registerForm.get('birthDate').split('-')
        age = today.year - int(printDate[0]) - ((today.month, today.day) < (int(printDate[1]), int(printDate[2])))
        customer = Customer()
        # check email and mobile number are exists or not in database 
        if Customer.objects.filter(email = registerForm.get('email')).exists():
            return render(request,'register/error_login.html',{"errorMsg":"This Email ID is already Exists Try to LogIn"});
        elif Customer.objects.filter(mobile = registerForm.get('mobile')).exists():
            return render(request,'register/error_login.html',{"errorMsg":"This Mobile No is already Exists Try to LogIn"});
        else:
            # Insert data in the database
            customer.f_name = registerForm.get('fname')
            customer.l_name = registerForm.get('lname')
            customer.email = registerForm.get('email')
            customer.password = registerForm.get('pass')
            customer.city = registerForm.get('city')
            customer.state = registerForm.get('state')
            customer.mobile = registerForm.get('mobile')
            customer.gender = registerForm.get('gender')
            customer.birth_date = date(year = int(printDate[0]),month = int(printDate[1]),day = int(printDate[2]))
            customer.age = age
            customer.qualification = registerForm.get('qualification')
            customer.occupation = registerForm.get('profession')
            customer.mother_tounge = registerForm.get('mothertoung')
            customer.cast = registerForm.get('cast')
            customer.Religene = registerForm.get('religene')
            customer.sunshine = ''
            customer.image = ''
            customer.about = '' 
            customer.save()
            # set the session
            request.session['login_check'] = registerForm.get('email')
            return redirect('home')
    return render(request, 'register/login.html')


# register page view
def register(request):
    return render(request, 'register/register.html')


# home page View
def home(request):
    member_count = Customer.objects.all();
    match_count = len(Matched.objects.all());
    city_Count = set(list(Customer.objects.all().values_list('city',flat=True)))
    counts_dynamic = {'cities':len(city_Count),'member':len(member_count),'match':match_count}
    if 'login_check' in request.session:
        cur_user = name_cur_user(request)
        return render(request,'main/home.html',{'user_login_check':True,'counts':counts_dynamic,'fname':cur_user[1],'img':cur_user[0]})
    else:
        return render(request,'main/home.html',{'user_login_check':False,'counts':counts_dynamic})


# search page view
def search(request):
    # check session is set or not 
    if 'login_check' in request.session:
        cur_user = name_cur_user(request)
        if request.method == 'GET':
            search = request.GET
            # select query from the database
            if search.get('age-start') and search.get('age-end'):
                searchResult = Customer.objects.filter(gender  = search.get('gender'), age__gte = int(search.get('age-start')), age__lte = int(search.get('age-end')), mother_tounge = search.get('mothertounge')).exclude(email = request.session['login_check'])
                print(list(search.get('mothertounge')))
                # Get id from the email session of user 
                user_id = Customer.objects.values_list('id',flat=True).get(email = request.session['login_check'])
                # if database row exists
                if searchResult.exists():
                    searchDictionary = []
                    for searchList in searchResult:
                        if (Reject.objects.filter(person = user_id , notinterested = searchList.id).exists() != False or Intrest.objects.filter(person = user_id , interested = searchList.id).exists() != False):
                            pass
                        else:
                            if Matched.objects.filter(person = user_id, matched_person = searchList.id).exists() or Matched.objects.filter(person = searchList.id, matched_person = user_id).exists():
                                pass
                            else:
                                name = searchList.f_name +' '+ searchList.l_name
                                searchDictionary.append({'id':searchList.id,
                                'name':name,
                                'age':searchList.age,
                                'religene':searchList.Religene,
                                'profession':searchList.occupation,
                                'city':searchList.city,
                                'state':searchList.state,
                                'img':searchList.image})
                    if len(searchDictionary) == 0:
                        return render(request,'main/search.html',{'emptyMsg':'Your Match Not Found'})
                    search_data_filter = {'gender_search':search.get('gender'),'age_start_search':search.get('age-start'),'age_end_search':search.get('age-end'),'mother_toungue_search':search.get('mothertounge')}
                    
                    return render(request,'main/search.html',{'searchDictionary':searchDictionary,'search_data_filter':mark_safe(json.dumps(search_data_filter)),'fname':cur_user[1],'img':cur_user[0]})
                else:
                    return render(request,'main/search.html',{'emptyMsg':'Your Match Not Found','fname':cur_user[1],'img':cur_user[0]})
            else:
                return redirect('home')
        else:
            
            return redirect('home')
    else:
        return redirect('../login')

def intress(request):
    # session check login or not
    if 'login_check' in request.session:
        # form check
        cur_user = name_cur_user(request)
        if request.method == 'POST':
            search_id = request.POST.get('interst')
            userID = Customer.objects.values_list('id', flat=True).get(email = request.session['login_check'])
            if Intrest.objects.filter(person = userID, interested = int(search_id)).exists():
                return redirect('../search')
            else:
                if Intrest.objects.filter(person = int(search_id), interested = userID).exists():
                    Intrest.objects.filter(person = int(search_id), interested = userID).delete();
                    matched_data = Matched()
                    matched_data.person = Customer.objects.get(email = request.session['login_check'])
                    matched_data.matched_person = Customer.objects.get(id = int(search_id))
                    matched_data.save()
                    return redirect('../Matched')
                else:
                    intrest = Intrest()
                    intrest.person = Customer.objects.get(email = request.session['login_check'])
                    intrest.interested = Customer.objects.get(id = int(search_id))
                    intrest.save()
                    return redirect('../intress')
        else:
            userID = request.session['login_check']
            interested_user = Intrest.objects.filter(person = Customer.objects.get(email = userID))
            if interested_user.exists():
                interested_dict = []
                for i_user in interested_user:
                    if Intrest.objects.filter(person = i_user.interested.id, interested = i_user.person.id).exists():
                        pass
                    else:
                        data = Customer.objects.values_list('f_name','l_name','image','age','Religene','occupation','city','state').get(id = i_user.interested.id)
                        interested_dict.append({
                            'id':i_user.interested.id,
                            'fname': data[0],
                            'lname': data[1],
                            'img' : data[2],
                            'age':data[3],
                            'religene':data[4],
                            'profession':data[5],
                            'city':data[6],
                            'state':data[7],
                        })
                if interested_dict:
                    return render(request,'main/interested.html',{'interest':interested_dict,'fname':cur_user[1],'img':cur_user[0]})
                else:
                    return render(request,'main/interested.html',{'emptyMsg':'Your Intrest Box is Empty ','fname':cur_user[1],'img':cur_user[0]})
            else:
                return render(request,'main/interested.html',{'emptyMsg':'Your Intrest Box is Empty','fname':cur_user[1],'img':cur_user[0]})
    else:
        return redirect('../login')

# not Intrested
def notintrest(request):
    # session check login or not
    if 'login_check' in request.session:
        # form check 
        if request.method == 'POST':
            search_id = request.POST.get('notintrest')
            userID = Customer.objects.values_list('id', flat=True).get(email = request.session['login_check'])
            if Reject.objects.filter(person = userID, notinterested = int(search_id)).exists():
                return redirect('../intress')
            else:
                if Intrest.objects.filter(person = int(search_id), interested = userID).exists():
                    Intrest.objects.filter(person = int(search_id), interested = userID).delete()
                if Intrest.objects.filter(person = userID, interested = int(search_id)).exists():
                    Intrest.objects.filter(person = userID, interested = int(search_id)).delete()
                reject = Reject()
                reject.person = Customer.objects.get(email = request.session['login_check'])
                reject.notinterested = Customer.objects.get(id = int(search_id))
                reject.save()
                return redirect('../Match-request')
        else:
            return redirect('home')
    else:
        return redirect('../login')


# search Profile Page
def searchDetail(request):
    # session check login or not 
    if 'login_check' in request.session:
        cur_user = name_cur_user(request)
        # get method check for form
        if request.method == 'GET':
            search = request.GET 
            searchResult = Customer.objects.filter(id = int(search.get('view')))
            if searchResult.exists():
                searchDetail = {}
                for searchList in searchResult:
                    name = searchList.f_name +' '+ searchList.l_name
                    searchDetail = {'id':searchList.id,
                    'name':name,
                    'city':searchList.city,
                    'state':searchList.state,
                    'gender':searchList.gender,
                    'birthdate':searchList.birth_date,
                    'qualification':searchList.qualification,
                    'mother_tounge':searchList.mother_tounge,
                    'cast':searchList.cast,
                    'Religene':searchList.Religene,
                    'sunshine':searchList.sunshine,
                    'about':searchList.about,
                    'age':searchList.age,
                    'heightInFeet':searchList.height_feet,
                    'heightInInch':searchList.height_inch,
                    'profession':searchList.occupation,
                    'income':searchList.income,
                    'phone':searchList.mobile,
                    'income':searchList.income,
                    'img':searchList.image}
                button_show = search.get('relation');
                print(button_show)
                return render(request,'main/search-detail.html',{'button_show':button_show,'searchDetail':searchDetail,'fname':cur_user[1],'img':cur_user[0]})
            else:
                return render(request,'main/search-detail.html',{'emptyMsg':'Your Match Not Found','fname':cur_user[1],'img':cur_user[0]})
    else:
        return redirect('../login')
    return redirect('home')



# about page 
def about(request):
    if 'login_check' in request.session:
        cur_user = name_cur_user(request)
        return render(request,'main/about.html',{'user_login_check':True,'fname':cur_user[1],'img':cur_user[0]})
    else:
        return render(request,'main/about.html',{'user_login_check':False})

# user profile page
def profile(request):
    # session check 
    if 'login_check' in request.session:
        # select query for get data of user
        profileDetail = Customer.objects.filter(email = request.session['login_check'])
        if profileDetail.exists():
            for profileList in profileDetail:
                if profileList.height_feet is None:
                    profile_height = ""
                else:
                    profile_height = profileList.height_feet
                if profileList.height_inch is None:
                    profile_hinch = ""
                else:
                    profile_hinch = profileList.height_inch
                if profileList.income is None:
                    profile_income = ""
                else:
                    profile_income = profileList.income
                Profile = {'id':profileList.id,
                'fname':profileList.f_name,
                'lname':profileList.l_name,
                'city':profileList.city,
                'state':profileList.state,
                'gender':profileList.gender,
                'birthdate':profileList.birth_date,
                'qualification':profileList.qualification,
                'mother_tounge':profileList.mother_tounge,
                'cast':profileList.cast,
                'Religene':profileList.Religene,
                'sunshine':profileList.sunshine,
                'about':profileList.about,
                'age':profileList.age,
                'heightInFeet':profile_height,
                'heightInInch':profile_hinch,
                'profession':profileList.occupation,
                'income':profile_income,
                'mobile':profileList.mobile,
                'password':profileList.password,
                'img':profileList.image}
            return render(request,'main/profile.html',Profile)
        else:
            return redirect('../login')


# update profile of user
def updateProfile(request):
    # check form is submit or not
    if request.method == 'POST':
        formData = request.POST
        today = date.today()
        customer = Customer()
        printDate = formData.get('birthdate').split('-')
        age = today.year - int(printDate[0]) - ((today.month, today.day) < (int(printDate[1]), int(printDate[2])))
        if Customer.objects.filter(email = request.session['login_check']):
            records = Customer.objects.filter(email = request.session['login_check'])
            if Customer.objects.filter(mobile = formData.get('mobile')).exclude(email = request.session['login_check']).exists():
                return redirect('../profile')
            else:
                for updaterecord in records:
                    updaterecord.f_name = formData.get('fname')
                    updaterecord.l_name = formData.get('lname')
                    updaterecord.city = formData.get('city')
                    updaterecord.state = formData.get('state')
                    updaterecord.mobile = formData.get('mobile')
                    updaterecord.gender = formData.get('gender')
                    updaterecord.birth_date = date(year = int(printDate[0]),month = int(printDate[1]),day = int(printDate[2]))
                    updaterecord.age = age
                    updaterecord.qualification = formData.get('qualification')
                    updaterecord.occupation = formData.get('profession')
                    updaterecord.mother_tounge = formData.get('mothertoung')
                    updaterecord.cast = formData.get('cast')
                    updaterecord.Religene = formData.get('religene')
                    updaterecord.sunshine = formData.get('sunshine')
                    if formData.get('heightInFeet') != 'None' and formData.get('heightInFeet') != '':
                        updaterecord.height_feet  = formData.get('heightInFeet')
                    if formData.get('heightInInch') != 'None' and formData.get('heightInInch') != '':
                        updaterecord.height_inch  = formData.get('heightInInch')
                    if formData.get('income') != 'None' and formData.get('income') != '':
                        updaterecord.income = formData.get('income')
                    if  'image' in request.FILES:
                        updaterecord.image = request.FILES['image']
                    updaterecord.about = formData.get('about')
                    updaterecord.save()
                return redirect('../profile')
        else:
            return redirect('../login')
    return redirect('home')
#matched
def matched(request):
    if 'login_check' in request.session:
        cur_user = name_cur_user(request)
        userID = request.session['login_check']
        matched_user = Matched.objects.filter(person = Customer.objects.get(email = userID)) | Matched.objects.filter(matched_person = Customer.objects.get(email = userID))
        if matched_user.exists():
            interested_dict = []
            for i_user in matched_user:
                if i_user.person == Customer.objects.get(email = userID):
                    data = Customer.objects.values_list('f_name','l_name','image').get(id = i_user.matched_person.id)
                    interested_dict.append({
                        'id':i_user.matched_person.id,
                        'fname': data[0],
                        'lname': data[1],
                        'img' : data[2]
                    })
                else:
                    data = Customer.objects.values_list('f_name','l_name','image').get(id = i_user.person.id)
                    interested_dict.append({
                        'id':i_user.person.id,
                        'fname': data[0],
                        'lname': data[1],
                        'img' : data[2]
                    })
            if interested_dict:
                return render(request,'main/match.html',{'interest':interested_dict,'fname':cur_user[1],'img':cur_user[0]})
            else:
                return render(request,'main/match.html',{'msg':"No Matches Found",'fname':cur_user[1],'img':cur_user[0]})
        else:
            return render(request,'main/match.html',{'msg':"No Matches Found",'fname':cur_user[1],'img':cur_user[0]})
    return redirect('../login')
# Pending Matches
def request(request):
    # check session is set or not 
    if 'login_check' in request.session:
        cur_user = name_cur_user(request)
        userID = request.session['login_check']
        interested_user = Intrest.objects.filter(interested = Customer.objects.get(email = userID))
        if interested_user.exists():
            interested_dict = []
            for i_user in interested_user:
                if Intrest.objects.filter(person = i_user.interested.id, interested = i_user.person.id).exists() or Reject.objects.filter(person = Customer.objects.get(email = userID), notinterested = i_user.person.id).exists():
                    pass
                else:
                    data = Customer.objects.values_list('f_name','l_name','image').get(id = i_user.person.id)
                    interested_dict.append({
                        'id':i_user.person.id,
                        'fname': data[0],
                        'lname': data[1],
                        'img' : data[2]
                    })
            if interested_dict:
                return render(request,'main/request.html',{'interest':interested_dict,'fname':cur_user[1],'img':cur_user[0]})
            else:
                return render(request,'main/request.html',{'msg':"No Match Request Found",'fname':cur_user[1],'img':cur_user[0]})

        else:
            return render(request,'main/request.html',{'msg':"No Match Request Found",'fname':cur_user[1],'img':cur_user[0]})
    return redirect('../login')

# filter data in search 

def filter_data(request):
    ages_filter = request.GET.getlist('ages[]')
    prof_filter = request.GET.getlist('prof[]')
    cities_filter = request.GET.getlist('city[]')


    gender = request.GET.get('gender')
    age_start = request.GET.get('age_start')
    age_end = request.GET.get('age_end')
    mother_tounge = request.GET.get('mother_tounge')
    print('GENDER    AGE    MOTHER TOUNGUE',gender,age_start,age_end,mother_tounge)
    searchResult = Customer.objects.filter(gender = gender,  age__gte = age_start, age__lte = age_end, mother_tounge = mother_tounge).exclude(email = request.session['login_check'])
    if len(ages_filter) > 0:
        ages_filter = list(map(int,ages_filter))
        print(ages_filter)
        searchResult = searchResult.filter(age__in = ages_filter).distinct()

    if len(prof_filter) > 0:
        searchResult = searchResult.filter(occupation__in = prof_filter).distinct()

    if len(cities_filter) > 0:
        searchResult = searchResult.filter(city__in = cities_filter).distinct()
        

    if searchResult.exists():
        user_id = Customer.objects.values_list('id',flat=True).get(email = request.session['login_check'])
        searchDictionary = []
        for searchList in searchResult:
            if Reject.objects.filter(person = user_id , notinterested = searchList.id).exists() != True:
                name = searchList.f_name +' '+ searchList.l_name
                searchDictionary.append({'id':searchList.id,
                'name':name,
                'age':searchList.age,
                'religene':searchList.Religene,
                'profession':searchList.occupation,
                'city':searchList.city,
                'state':searchList.state,
                'img':searchList.image})
            else:
                return JsonResponse({'emptyMsg':'Your Match Not Found'})
        print(searchDictionary)
        t=render_to_string('main/ajax/filter-list.html',{'searchDictionary':searchDictionary})
        return JsonResponse({'searchDictionary':t})
    else:
        return JsonResponse({'emptyMsg':'Your Match Not Found'})

    # return JsonResponse({'gender': json.dumps(searchResult)})

# logout
def logout(request):
    if 'login_check' in request.session:
        del request.session['login_check']
        return redirect('../login')
    return redirect('../login')