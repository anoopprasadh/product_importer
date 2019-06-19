from django.shortcuts import render
import csv ,io
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Product
import pandas as pd
import numpy as np


# Create your views here.
def index(request):
	# print_it = {'insert_me':"Hey I'm from first_app/views.py "}
	return render(request,'products/base_page.html')

def generate_choices():
		lt_choices = ['Active','Inactive']
		return np.random.choice(lt_choices)


# @permission_required('admin.can_add_log_entry')
def contact_upload(request):
	template = "products/upload_page.html"
	text_message = {
	'order': "Upload the file in name ,sku ,description format"
	}

	if request.method == 'GET':
		return render(request,template,text_message)


	csv_file = request.FILES['file']

	if not csv_file.name.endswith('.csv'):
		messages.error(request,"This is not CSV file")

	io_string = io.StringIO(csv_file.read().decode('UTF-8'))
	next(io_string)
	for column in csv.reader(io_string, delimiter=','):
		_, created = Product.objects.get_or_create(
				name = column[0],
				sku = column[1],
				description = column[2],
				status = generate_choices()
			)

	for row in Product.objects.all():
		if Product.objects.filter(name=row.name).count() > 1 :
			row.delete()

	# input_file = csv.DictReader(open(csv_file))
	# for rows in input_file:
	# 	_, created = Product.objects.get_or_create(
	# 			name = column[0],
	# 			sku = column[1],
	# 			description = column[2]
	# 		)

	context = {}
	# return render(request,'products/product_views.html',context)

	return HttpResponseRedirect('/products/')



def display_products(request):
	webpages_list = Product.objects.all()
	display_dict  = {'products_list': webpages_list}
	return render(request,'products/product_views.html',context=display_dict)


