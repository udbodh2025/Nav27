
from customers.models import Customer
from django.shortcuts import redirect, render
from django.views import View


class CreateCustomer(View):
    ''' Create a new customer '''

    def get(self, request, *args, **kwargs):
        ''' Respond to GET request '''
        return render(request,  'customers/add_customer.html')

    def post(self, request, *args, **kwargs):
        ''' Respond to POST request '''
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        mobile_no = request.POST.get('mobile_no')
        customer_address = request.POST.get('customer_address')
        balance = request.POST.get('balance')
        customer = Customer(
            user=request.user,
            customer_name=customer_name,
            customer_email=customer_email,
            mobile_no=mobile_no,
            customer_address=customer_address,
            balance=balance
        )
        customer.save()
        '''Provide a redirect on GET request.'''
        return redirect('customer_list')
