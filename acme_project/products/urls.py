from django.conf.urls import url
from products import views


urlpatterns = [
	url(r'^$',views.index,name='base_page'),
	url(r'^upload_page',views.contact_upload,name='upload_page'),
	url(r'^products/upload_page',views.display_products,name='display_products'),
]
