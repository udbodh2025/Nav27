from authenticator.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from products.models.product_model import Product


@method_decorator(login_required, name='dispatch')
class Dashboard(View):
    def get(self, request):
        ''''
        Main dashboard view for the application.
        '''
        # user = User.objects.get(id=request.user.id)
        # notifications = user.notifications.unread()

        # for notification in notifications:
        #     print(notification.id)
        #     print(notification.verb)
        #     print(notification.target)
        #     print(notification.actor)
        #     print(notification.timestamp)
        #  Get 10 of the best-seller-selling products.
        top_sold_products = Product.objects.all().order_by('-count_sold')[:10]
        return render(request, 'core/dashboard.html', {'top_sold_products': top_sold_products})
