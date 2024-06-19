import sqlite3

from django.shortcuts import render, redirect
from .models import contact , login , detail , biodata , choices , savelist , feedback ,city , state
from django.contrib import messages


MESSAGE_TAGS = {
    messages.SUCCESS: 'success',
    messages.WARNING: 'danger'
}

# Create your views here.

def about(request):
    return render(request,'about.html')

#########################----- BIODATA -----#########################

def showbidata(request):
    return render(request,'biodata.html')

def showbidata2(request):
    return render(request,'biodata2.html')

def showbidata3(request):
    return render(request,'biodata3.html')

def insertbiodata(request):
    uid = request.session['log_id']
    if request.method == 'POST':
        fname = request.POST.get("fname")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        caste = request.POST.get("caste")
        income = request.POST.get("income")
        skintone = request.POST.get("skintone")
        siblings = request.POST.get("siblings")
        education = request.POST.get("education")
        meternal = request.POST.get("meternal")
        expectation = request.POST.get("expectation")
        # native = request.POST.get("native")
        mobile = request.POST.get("mobile")
        profilepicture = request.FILES["dp"]

        uid = request.session['log_id']
        addbio = biodata(lid=login(id=uid),pname=fname,picture=profilepicture,height=height,weight=weight,caste=caste,income=income,skintone=skintone,siblings=siblings,education=education,expectation=expectation,meternal=meternal,mobile=mobile)
        addbio.save()
        messages.success(request, 'biodata added successfully!!')
        return render(request,'index.html')


    return render(request, 'biodata.html')


#########################----- UPDATE BIODATA -----#########################

def updatebiodata(request,id):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        caste = request.POST.get("caste")
        income = request.POST.get("income")
        skintone = request.POST.get("skintone")
        siblings = request.POST.get("siblings")
        education = request.POST.get("education")
        meternal = request.POST.get("meternal")
        expectation = request.POST.get("expectation")
        cityid = request.POST.get("city")
        stateid = request.POST.get("state")
        mobile = request.POST.get("mobile")
        profilepicture = request.FILES["dp"]


        uid = request.session['log_id']
        fetchdetails = biodata.objects.get(lid=uid)
        fetchdata = detail.objects.get(lid=uid)
        fetchdetails.pname = fname
        fetchdetails.height = height
        fetchdetails.weight = weight
        fetchdetails.caste = caste
        fetchdetails.income = income
        fetchdetails.skintone = skintone
        fetchdetails.siblings = siblings
        fetchdetails.education = education
        fetchdetails.expectation = expectation
        fetchdetails.meternal =  meternal
        fetchdetails.mobile = mobile
        fetchdetails.picture = profilepicture

        fetchdata.cityid = city(id=cityid)
        fetchdata.stateid = state(id=stateid)


        fetchdetails.save()
        fetchdata.save()
        messages.success(request, 'Biodata Updating Successfully!!')
        return render(request,'index.html')

    return render(request, 'biodata.html')

#########################----- CONTACT US -----#########################


def contactus(request):
    return render(request,'contact.html')

def insertcontactus(request):
    if request.method == 'POST':
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        subject = request.POST.get("Subject")
        msg = request.POST.get("Message")

        query = contact(name=name, email=email, subject=subject, message=msg)
        query.save()
        messages.add_message(request, messages.SUCCESS, "Thank you for Contacting Us!! We'll reach out to you soon.")

    return render(request,'contact.html')


def index(request):
    return render(request,'index.html')

#########################----- FORGOT PASSWORD -----#########################


def forgot(request):
    return render(request,'forgot_password.html')

def forgotpass(request):
    if request.method == 'POST':
        username = request.POST['Email']
        try:
            user = login.objects.get(email=username)
            request.session['log_user'] = user.email
            request.session['log_id'] = user.id
            request.session.save()

        except login.DoesNotExist:
            user = None

        if user is not None:
            return render(request, 'change_password.html')

        else:
            messages.info(request, 'Username does not exit plz try again...')
    return render(request, 'forgot_password.html')

def changepass(request):
    if request.method == 'POST':
        password = request.POST.get("new_password")
        conpassword = request.POST.get("confirm_password")

        uid = request.session['log_id']

        capcount = 0
        digitcount = 0
        spcialcount = 0
        if len(password) >= 8 and len(password) <= 12:
            for i in password:
                if ord(i) >= 65 and ord(i) <= 90:
                    capcount = capcount + 1
                elif ord(i) >= 48 and ord(i) <= 57:
                    digitcount = digitcount + 1
                elif ord(i) == 35 or ord(i) == 36 or ord(i) == 64:
                    spcialcount = spcialcount + 1

            if capcount >= 1 and digitcount >= 1 and spcialcount >= 1:
                if password == conpassword:
                    fetchdetails = login.objects.get(id=uid)
                    fetchdetails.password = password

                    fetchdetails.save()
                    messages.success(request, 'Change Password Successfully!!')
                    try:
                        del request.session['log_user']
                        del request.session['log_id']
                    except:
                        pass
                    return render(request, 'login.html')
                else:
                    messages.info(request, 'Your password and confirmation password do not match!!!')

            else:
                messages.info(request,"Password must contain in One Digit, One Capital Character, One Special Character!!!")
    return render(request,'change_password.html')

#########################----- VIEW OTHE BIODATA -----#########################


def viewperson(request,id):
    uid = request.session['log_id']
    fetchpdata = savelist.objects.get(id=id)
    bioid = fetchpdata.bioid
    fetchperdata = biodata.objects.get(pname=bioid)
    fetchdata = detail.objects.get(lid=uid)
    print(fetchdata)

    return render(request,'viewperson.html',{'data':fetchperdata,'data2':fetchdata})

#########################----- PROFILE -----#########################
from datetime import date

# calculate age by Date of Birth...
def calculate_age(date_of_birth):
    today = date.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    return age

def profile(request):
    uid = request.session['log_id']
    print(uid)
    # try:
    fatchreg = login.objects.get(id=uid)
    # print(fatchreg)
    fetchdetails = detail.objects.get(lid=uid)
    # print(fetchdetails)
    fetchbdetails = biodata.objects.get(lid=uid)

    person = detail.objects.get(lid=uid)
    age = calculate_age(person.dob) # use calculate_age function to calculate age
    # print(age) # print age
    context = {
        'dat':fatchreg,
        'detail':fetchdetails,
        'data':fetchbdetails,
        'age':age
    }
        # return render(request,'profile.html', context)
    # except biodata.DoesNotExist:
    #     return render(request,'biodata.html')

    return render(request,"profile.html", context)


def editbiodata(request,id):
    uid = request.session['log_id']
    fetchdetails = biodata.objects.get(lid=uid)
    fetchcity = city.objects.all()
    fetchstate = state.objects.all()

    context = {
        'data':fetchdetails,
        'city':fetchcity,
        'state':fetchstate,
        'id':uid
    }
    return render(request,"editbiodata.html",context)

#########################----- SAVE LIST -----#########################


def savelistpage(request):
    uid = request.session['log_id']
    print(uid)
    fetchdata = savelist.objects.all()
    print(fetchdata)
    return render(request,'savelist.html',{'data':fetchdata})

def saveid(request , id):
    uid = request.session['log_id']
    savebio = savelist(lid=login(id=uid),bioid=biodata(id=id))
    savebio.save()
    personname = biodata.objects.get(id=id)
    messages.info(request,"You have shown interest in  " + personname.pname)
    return redirect('/matches')

#########################----- REGISTER -----#########################


def register(request):
    fetchcity = city.objects.all()
    fetchstate = state.objects.all()
    return render(request,'register.html',{'city':fetchcity,'state':fetchstate})

def viewdata(request):
    try:
        if request.method == 'POST':
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            password = request.POST.get("password")
            file = request.FILES['dp']

            capcount = 0
            digitcount = 0
            spcialcount = 0
            if len(password) >= 8 and len(password) <= 12:
                for i in password:
                    if ord(i) >= 65 and ord(i) <= 90:
                        capcount = capcount + 1
                    elif ord(i) >= 48 and ord(i) <= 57:
                        digitcount = digitcount + 1
                    elif ord(i) == 35 or ord(i) == 36 or ord(i) == 64:
                        spcialcount = spcialcount + 1

                if capcount >= 1 and digitcount >= 1 and spcialcount >= 1:
                    logindata = login(email=email, phone=phone, password=password, dp=file, role=2, status=1)
                    logindata.save()

                    fetchid = login.objects.get(email=email)
                    fetchid = login.objects.get(phone=phone)
                    uid = fetchid.id

                    address = request.POST.get("address")
                    name = request.POST.get("name")
                    radio = request.POST.get("radio")
                    dob = request.POST.get("dob")
                    cityid = request.POST.get("city")
                    stateid = request.POST.get("state")

                    import datetime
                    dob = datetime.datetime.strptime(dob, '%m/%d/%Y').strftime('%Y-%m-%d')

                    detaildata = detail(lid=login(id=uid), name=name, dob=dob, address=address, gender=radio, cityid=city(id=cityid), stateid=state(id=stateid))
                    detaildata.save()
                    messages.success(request, 'Successfully Registered, You can Login Now')
                    return render(request,'login.html')

                else:
                    messages.info(request,"Password must contain in One Digit, One Capital Character, One Special Character!!!")
                    fetchcity = city.objects.all()
                    fetchstate = state.objects.all()
                    # return render(request, 'register.html', {'city': fetchcity, 'state': fetchstate})

            else:
                messages.error(request, 'Password must be have 8 to 12 characters!!')
                fetchcity = city.objects.all()
                fetchstate = state.objects.all()
                # return render(request, 'register.html', {'city': fetchcity, 'state': fetchstate})

        else:
            messages.error(request, 'error occured')
            fetchcity = city.objects.all()
            fetchstate = state.objects.all()
            # return render(request, 'register.html', {'city': fetchcity, 'state': fetchstate})

    except login.MultipleObjectsReturned:
        fetchcity = city.objects.all()
        fetchstate = state.objects.all()
        messages.info(request, 'Email and Phone not Already exist!!')
        # return render(request, 'register.html', {'city': fetchcity, 'state': fetchstate})

    return render(request,'register.html',{'city': fetchcity, 'state': fetchstate})

#########################----- LOGIN -----#########################

def loginpage(request):
    return render(request,'login.html')

def checklogin(request):
    if request.method == 'POST':
        username = request.POST['Email']
        password = request.POST['Password']
        try:
            user = login.objects.get(email=username, password=password)
            request.session['log_user'] = user.email
            request.session['log_id'] = user.id
            request.session.save()
            messages.info(request, 'Successfully Logged in!!')

        except login.DoesNotExist:
            user = None

        if user is not None:
            return render(request, 'index.html')

        else:
            messages.info(request, 'account does not exit plz sign in again')
    return render(request,'login.html')


#########################----- LOGOUT -----#########################

def logout(request):
   try:
      del request.session['log_user']
      del request.session['log_id']
   except:
      pass
   return render(request,'login.html')


#########################----- MATCHES -----#########################

def matches(request):
    fetchbiodatas = biodata.objects.all()
    fetchdetails = detail.objects.all()
    fetchall = zip(fetchbiodatas,fetchdetails)
    return render(request, 'matches.html',{'biodata':fetchbiodatas,'detail':fetchdetails , 'all':fetchall})


#########################----- FEEDBACK -----#########################

def addfeedback(request):
    uid = request.session['log_id']
    rating = request.POST.get("rate")
    comment = request.POST.get("comment")
    savedata = feedback(lid=login(id=uid), ratings=rating, comment=comment)
    savedata.save()
    messages.info(request, "Thank you for submitting feedback")
    return render(request, 'index.html')


#########################----- GET MAIL SYSTEM -----#########################

def getmail(request , id):
    uid = request.session['log_id']
    personname = biodata.objects.get(id=id)
    mobilenumber = personname.mobile

    fetchdetails = login.objects.get(id=uid)
    uemail = fetchdetails.email

    body = 'Hello , Thank you for showing intrest in Kalyanam.\n ' \
           'Hope we are able to help you find a best match. here is mobile number ' \
           ' ' + str(mobilenumber)
    ############ code for sending mail ########################

    from django.core.mail import send_mail

    send_mail(
        'Request Mobile Number - Kalyanam',
        body,
        'mit@gmail.com',
        [uemail],
        fail_silently=False,
    )

    # import smtplib
    #
    # gmail_user = 'mit@gmail.com'
    # gmail_password = ''
    #
    # sent_from = gmail_user
    # to = [uemail]
    # subject = 'Request Mobile Number - Kalyanam'
    # body = 'Hello , Thank you for showing intrest in Vivaah.\n ' \
    #        'Hope we are able to help you find a best match. here is mobile number ' \
    #        ' ' + str(mobilenumber)
    #
    # email_text = """\
    #             From: %s
    #             To: %s
    #             Subject: %s
    #
    #             %s
    #             """ % (sent_from, ", ".join(to), subject, body)
    #
    # try:
    #     smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #     smtp_server.ehlo()
    #     smtp_server.login(gmail_user, gmail_password)
    #     smtp_server.sendmail(sent_from, to,email_text)
    #     smtp_server.close()
    #     print("Email sent successfully!")
    # except Exception as ex:
    #     print("Something went wrong….", ex)
    msg = "Mobile Number has been shared to your mail."
    messages.info(request,msg)
    return redirect(matches)

