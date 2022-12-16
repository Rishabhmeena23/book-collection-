from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import redirect
from .models.model import Product
from .models.category import Categorie
from .models.customer import Customer
from django.views import View


def index(request):
    products = None
    categories = Categorie.get_all_category()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories

    print("ypu are : ", request.session.get('email'))
    print("ypu are : ", request.session.get('first_name'))
    return render(request, 'home.html', data)


class Category(View):
    def post(self, request):
        product = request.POST.get('product')
        print(product)
        return redirect('categories')


    def get(self, request):
        products = None
        categories = Categorie.get_all_category()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        return render(request, 'categories.html', data)


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        password = request.POST.get('password')
        mobile_number = request.POST.get('mobilenumber')
        email = request.POST.get('email')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'mobile_number': mobile_number,
            'email': email
        }

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            password=password,
                            mobile_number=mobile_number,
                            email=email)

        error_message = None

        if len(first_name) < 4:
            error_message = "First Name must 4 character long or more !! "

        elif len(last_name) < 4:
            error_message = "Last Name must 4 character long or more !! "

        elif len(mobile_number) < 10:
            error_message = "Mobile No. must be valid !! "

        elif customer.isExists():
            error_message = "This Email Address is already registered !! "

        if not (error_message):
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('homepage')

        else:
            data = {
                'error': error_message,
                'values': value
            }

            return render(request, 'signup.html', data)


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email
                request.session['first_name'] = customer.first_name
                return redirect('homepage')
            else:
                error_message = "Email or Password invalid !! "
        else:
            error_message = "Email or Password invalid !! "
        return render(request, 'login.html', {'error': error_message})


