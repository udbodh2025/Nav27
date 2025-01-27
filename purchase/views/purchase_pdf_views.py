from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from purchase.models import Purchase
from utils.helper.decorators.filter import _currentUser
from utils.render_to_pdf import generate_pdf


class ViewPurchasePDF(LoginRequiredMixin, View):
	'''
	Automaticly open PDF file.
	'''
	@method_decorator(_currentUser())
	def get(self, request, *args, **kwargs):
		purchase = Purchase.objects.all().order_by('-id')
		pdf = generate_pdf('purchase/pdf/purchase_pdf.html', {'purchase': purchase})
		return HttpResponse(pdf, content_type='application/pdf')
