from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout
from polls.models import UserFollowing,QuestionTable,Groupcode,UserFollowers
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        following = UserFollowing.objects.filter(user__exact = request.user).count()
        followers = UserFollowers.objects.filter(user__exact = request.user).count()

        params = {
            'followers':followers,
            'following':following
        }
        return render(request,'index.html',params)
    else:
        return render(request,'index.html')

def passreset(request):
    return render(request,'passreset.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['susername']
        firstname = request.POST['sfirstname']
        lastname =request.POST['slastname']
        email =request.POST['semail']
        password =request.POST['spassword']
        password2 = request.POST['spassword2']

        # add parameters checking prog   
        if len(username) > 10:
            messages.error(request,"Username must be under 10 characters")
            return redirect('home')
        

        if password != password2:
            messages.error(request,"passwords do not match")
            return redirect('home')
        
        if username.isalnum():
            messages.error(request,"do no include numbers in username")
        # make user 
        myuser = User.objects.create_user(username ,email ,password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, 'Profile is created.')
        return redirect('home')
    else:
        return HttpResponse("Error 404")
        
def handlelogin(request):
    if request.method == 'POST':
        password = request.POST['lpassword']
        email = request.POST['lemail']
        username = User.objects.get(email=email.lower()).username

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request,"succesfully logged in.")
            return redirect('home')
        
        else:
            messages.error(request, "Invalid Credentials , please try again")
            return redirect('home')
    
def handlelogout(request):
    logout(request)
    messages.success(request, "Logout Succesfully.")
    return redirect('home')

def search(request):
    if request.user.is_authenticated:
            following = UserFollowing.objects.filter(following__exact = request.user).all()
            query = request.GET['search']
            users = User.objects.filter(username__icontains = query).exclude(username__exact = request.user)
            results = {
                "following":following,
                "query":query,
                "result":users
            }
            return render(request,'search.html',results)
        
    
def following(request):
    pass
    

def followers(request):
    pass
def profile(request):
    pass


def follow(request):
    if request.method== 'POST':
        followid = request.POST["usernameoffollower"]
        myid = request.user
        query = request.POST["query"]
        # finfollow = User.objects.get(username = followid)
        # addfollowing = UserFollowing(user = myid, following = finfollow)
        # addfollowing.save()
        # addfollowers = UserFollowers(user = finfollow, followers = myid)
        # addfollowers.save()
        if request.user.is_authenticated:
            following = UserFollowing.objects.filter(following__exact = request.user).count()
            params = {'following':following}
            print("000000000000000000000000",following)
        return redirect('/search?search='+query,params)


def askquestion(request):
    pass