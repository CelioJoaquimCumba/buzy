from http import client
from operator import contains
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.db.models import F
from numpy import equal, product
from .models import Activity, Client, Product, Project, User
from datetime import datetime
# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username= request.POST["username"]
            if not username:
                return HttpResponse("Your username field is empty")
            password = request.POST["password"]
            if not password:
                return HttpResponse("Yor password field is empty")
            user = authenticate(request, username=username,password=password)

            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "buzy/login.html", {
                    "message":"Invalid credentials."
                })
        return render(request, "buzy/login.html")
    else:
        return HttpResponseRedirect(reverse("index"))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        if not username:
            return HttpResponse("The username field is empty")
        email = request.POST["email"]
        if not email:
            return HttpResponse("The email field is empty")
        password = request.POST["password"]
        if not password:
            return HttpResponse("The password field is empty")
        users = [user for user in User.objects.all()]
        usernames = [user.username for user in users]
        emails = [user.email for user in users]

        if username in usernames:
            return render(request,"buzy/register.html",{
                "invalid_username":f"The username:'{username}' is already in use, Try another username!"
            })
        if email in emails:
                        return render(request,"buzy/register.html",{
                "invalid_email":f"The email:'{email}' is already in use, try another email!"
            })
        User.objects.create_user(username, email, password)
        new_user = authenticate(request, username=username, password=password)
        if new_user is not None:
            login(request,new_user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "buzy/login.html", {
                "message":"Somethin went wrong!"
            })
        
    else:
        return render(request, "buzy/register.html")

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    projects = list(request.user.in_projects.all())
    
    return render(request, "buzy/index.html",{
        "projects":projects
    })

def create(request, id=None):
    if request.method == "POST":
        description = request.POST["description"]
        if not description:
            return render(request, "buzy/create.html",{
            "following":[f for f in request.user.following.all()],
            "message":"Invalid submission. Your field description is empty"
            })
        members_id = request.POST.getlist("members")
        members= [request.user]
        for member_id in members_id:
            member = User.objects.get(id=member_id)
            members.append(member)
        if not members:
            return render(request, "buzy/create.html",{
            "following":[f for f in request.user.following.all()],
            "message":"Invalid submission. Your field members is empty"
            })
        if id == None:

            name = request.POST["name"]
            if not name:
                return render(request, "buzy/create.html",{
                "following":list(request.user.following.all()),
                "message":"Invalid submission. Your field name is empty"
                })
            
            
            revenue = request.POST["revenue"]
            if not revenue:
                return render(request, "buzy/create.html",{
                "following":[f for f in request.user.following.all()],
                "message":"Invalid submission. Your field revenue is empty"
                })
            project = Project.objects.create(name=name, description=description, host=request.user,revenue=revenue,income=revenue)
            for member in members:
                project.members.add(member)
                
            return HttpResponseRedirect(reverse("project", kwargs={"id":project.id}))
        
        else:
            try:
                project = Project.objects.get(id=id)
            except Project.DoesNotExist:
                return HttpResponse("Project ID invalid!")
            project.description = description
            project.members.clear()
            for member in members:
                project.members.add(member)
            project.save()
            return HttpResponseRedirect(reverse("project",kwargs={"id":project.id}))
            
        
            
    else:
        if id == None:
            return render(request, "buzy/create.html",{
                "following":[f for f in request.user.following.all()]
            })
        else:
            try:
                project = Project.objects.get(id=id)
            except Project.DoesNotExist:
                return HttpResponse("Project ID is invalid")
            return render(request, "buzy/create.html",{
                "following":[f for f in request.user.following.all()],
                "project":project
            })
    

def profile(request):
    if request.method == "POST":
        id = int(request.POST["id"])
        if not id:
            return HttpResponse("The field id is empty")
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return HttpResponseRedirect(reverse('profile'))
        following = request.user.following.all()
        following_users = [f for f in following]

        
        
        if request.POST["action"] == "follow":
            if user  != request.user:
                request.user.following.add(user)
            return HttpResponseRedirect(reverse('profile'))
        else:
            if not user in following_users:
                return HttpResponseRedirect(reverse('profile'))
            request.user.following.remove(user)
        return HttpResponseRedirect(reverse('profile'))
        

    else:
        return render(request, "buzy/profile.html",{
            "user":request.user,
            "following": [f for f in request.user.following.all()],
            "users":list(User.objects.all())
        })
def project(request, id):
    try:
        project = Project.objects.get(id=id)
    except Project.DoesNotExist:
        projects = [request.user.in_projects.all()][0]
        return HttpResponse("Project does not exist!")

    if request.method == "POST":
        form = request.POST['form']
        if form == "createActivity_form":
            type = request.POST["type"]
            transactions = ["custom","deposit","withdraw","purchase","refund"]
            if type not in transactions:
                return HttpResponse("Invalid type inserted")
            name = f"{type}-{datetime.now()}"

            participants_id = request.POST.getlist("participants")
            if not participants_id:
                return HttpResponse("The participants field is empty")

            participants= []
            for participant_id in participants_id:
                participant = User.objects.get(id=participant_id)
                participants.append(participant)
            

            if type == "purchase" or type == "refund":
                product_id = int(request.POST["product"])
                product = project.products.get(pk=product_id)
                client_id = int(request.POST["client"])
                client = project.clients.get(pk=client_id)
                if not client_id:
                    return HttpResponse("The client field is empty")
                if not product:
                    return HttpResponse("The product field is empty")
                if type == "refund":
                    investement = product.buying_price
                    project.income = float(project.income) - investement
                    gain = 0
                else:
                    client.purchases.add(product)
                    investement = product.buying_price
                    project.income = float(project.income) - investement
                    gain = product.selling_price
                    color = request.POST["color"]
                    if not color:
                        return HttpResponse("The color field is empty")
                
                description = f"Transaction type:{type}\nProduct:{product}\nColor:{color}\nClient:{client}"

            if type == "deposit":
                
                investement = 0
                gain = request.POST["gain"]
                if not gain:
                    gain = 0
                description = f"Transaction 2type:{type}\nDeposited:{gain}"

            if type == "withdraw":
                gain = 0
                investement = request.POST["investement"]
                if not investement:
                    investement = 0
                description = f"Transaction type:{type}\nWithdrawed{investement}"

            if type == "custom":
                name = request.POST["name"]
                if not name:
                    return HttpResponse("The name field is empty")

                description = request.POST["description"]
                if not description:
                    return HttpResponse("The description field is empty")

                investement = request.POST["investement"]
                if not investement:
                    investement = 0
                gain = request.POST["gain"]
                if not gain:
                    gain = 0
            gain = float(gain)
            investement = float(investement)
            if investement > float(project.income):
                return HttpResponse("Your investement is grater than your income")
            activity = Activity.objects.create(name=name, description=description,investement=investement,gain=gain)
            for participant in participants:
                activity.participants.add(participant)
            project.activity.add(activity)

            project.revenue =  float(project.revenue) + gain
            print(gain)
            print(investement)
            print(project.income)
            print(gain-investement)
            project.income = float(project.income) + gain-investement
            
            project.save()
            return HttpResponseRedirect(reverse('project', kwargs={"id":id}))
        elif form == "createProduct_form":
            name = request.POST["product_name"]
            if not name:
                return HttpResponse("The name field is empty")
            buying_price = request.POST["buying_price"]
            if not buying_price:
                return HttpResponse("The buying price field is empty")
            selling_price = request.POST["selling_price"]
            if not selling_price:
                return HttpResponse("The selling price field is empty")
            product = Product.objects.create(name=name,buying_price=buying_price,selling_price=selling_price)
            project.products.add(product)
            return HttpResponseRedirect(reverse('project',kwargs={"id":id}))
        elif form == "createClient_form":
            name = request.POST["client_name"]
            if not name:
                return HttpResponse("The client name field is empty")
            contact = request.POST["client_contact"]
            if not contact:
                return HttpResponse("The client contact field is empty")
            client = Client.objects.create(name=name,contact=contact)
            project.clients.add(client)
            return HttpResponseRedirect(reverse('project',kwargs={"id":id}))
        else:
            return HttpResponse("The form is invalid")
    
    activities  = project.activity.order_by(F("timestamp").desc())

    products = list(project.products.all())
    clients = list(project.clients.all())
    return render(request, "buzy/project.html", {
        "project":project ,
        "activities": activities,
        "products": products,
        "clients":clients
    })
    