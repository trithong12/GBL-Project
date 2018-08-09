from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from myapp import models
from django.conf import settings
from django.contrib import auth
from django.core import serializers
from rest_framework import viewsets, status
from rest_framework.response import Response
from myapp.serializers import *
from myapp.models import query_products_by_args

from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        print('----------1')
        if request.user.is_authenticated:
            return HttpResponseRedirect('/index/')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')    
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            print('logged in!')
            return HttpResponseRedirect('/index/')
        else:
            return render_to_response('login.html') 
    else:
        print('----------2')
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def index(request):
    print('here:', settings.BASE_DIR)
    return render(request, 'index.html')

##@login_required
#def listProducts(request):
#    #products = models.Product.objects.all()
#    #data = serializers.serialize("json", products)
#    product_categories = models.ProductCategory.objects.all()
#    return render(request, 'listProducts.html', locals())
#
#def listProducts_asJson(request):
#    products = models.Product.objects.all() #or any kind of queryset
#    data = serializers.serialize('json', object_list)
#    print('data:', data)
#    return HttpResponse(json, content_type='application/json')

class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = EventSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = models.Album.objects.all()
    serializer_class = AlbumSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = ProductSerializer
#    def list(self, request, **kwargs):
#        try:
#            product = query_products_by_args(**request.query_params)
#            serializer = ProductSerializer(product['items'], many=True)
#            result = dict()
#            result['data'] = serializer.data
#            result['draw'] = product['draw']
#            result['recordsTotal'] = product['total']
#            result['recordsFiltered'] = product['count']
#            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)
#
#        except Exception as e:
#            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = OrderSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = models.Member.objects.all()
    serializer_class = MemberSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = MessageSerializer

