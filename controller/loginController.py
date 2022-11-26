from django.shortcuts import render
from helper.encryption import __encryptorMD5
from helper.loginDetails import __getUser


def getLogin(request):
    csrf_token = 'bfbff'
    result = ["",""]

    if request.method == "POST":
        customerEmail = request.POST["email"]
        customerPassword = __encryptorMD5(request.POST["password"])
        
        result = __getUser(customerEmail , customerPassword)
        print(result,"111111111111")

    return render(request , "login.html",{
        "login_status":result
    })