from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# import education.models
from account.forms import CreateUserForm, UpdateUserForm
from account.decorators import unauthenticated_user
from account.models import User
from account.api.serializers import UserSerializer


@csrf_exempt
def userApi(request, id=0):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("success", safe=False)
        return JsonResponse("error", safe=False)
    elif request.method == "PUT":
        user_data = JSONParser().parse(request)
        user = User.objects.get(id=user_data['id'])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("success", safe=False)
        return JsonResponse("error", safe=False)
    elif request.method == "DELETE":
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse("success", safe=False)


# @login_required(login_url='login')
# def profile_page(request):
#     user = request.user
#     if user.is_teacher:
#         courses = education.models.Course.objects.filter(user=user)
#         return render(request, 'accounts/teacher_profile.html',
#                       context={'user': user, 'courses': courses})
#     groups = education.models.Group.objects.filter(user=user)
#     return render(request, 'accounts/student_profile.html',
#                   context={'user': user, 'groups': groups})


@login_required(login_url='login')
def edit_profile(request):
    user = request.user
    form = UpdateUserForm(instance=user)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'accounts/edit_user.html', {'form': form})


# @unauthenticated_user
def register_page(request, is_teacher):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(email=request.POST.get('email'))
            messages.success(request, "Account was created for " + str(user))
            return redirect('login')
    return render(request, 'account/registration.html', {"is_teacher": is_teacher, "form": form})


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        messages.info(request, "Username OR password is incorrect")
    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('login')
