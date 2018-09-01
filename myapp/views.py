from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from rest_framework.decorators import action
from myapp import models
from django.conf import settings
from django.contrib import auth
from django.core import serializers
from rest_framework import viewsets, status, generics, permissions, serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.serializers import *
from datetime import datetime
#from myapp.models import query_products_by_args

from django.contrib import admin
admin.autodiscover()

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

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

#@api_view(['GET', 'POST'])
#def post_list(request):
#    """
#    List all code snippets, or create a new snippet.
#    """
#    if request.method == 'GET':
#        posts = models.Post.objects.all()
#        serializer = PostSerializer(posts, many=True)
#        return Response(serializer.data)
#
#    elif request.method == 'POST':
#        post = PostSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#@api_view(['GET', 'PUT', 'DELETE'])
#def post_detail(request, pk):
#    """
#    Retrieve, update or delete a code snippet.
#    """
#    try:
#        post = models.Post.objects.get(pk=pk)
#    except Post.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
#
#    if request.method == 'GET':
#        serializer = PostSerializer(post)
#        return Response(serializer.data)
#
#    elif request.method == 'PUT':
#        serializer = PostSerializer(post, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    elif request.method == 'DELETE':
#        post.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer

class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = models.Event.objects.all()
    serializer_class = EventSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = models.Album.objects.all()
    serializer_class = AlbumSerializer

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
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
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = models.Order.objects.all()
    serializer_class = OrderSerializer

class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = models.Member.objects.all()
    serializer_class = MemberSerializer
    
    def create(self, request):
        # 如果只接到身份證字號-->回傳會員資料
        if len(request.data) == 1 and list(request.data.keys())[0] == 'member_pid':
            member = models.Member.objects.get(member_pid=request.data['member_pid'])
            serializer = MemberSerializer(member)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # 否則為新增會員
        else:
            # 如果會員email不為空則先檢查會員是否已存在，若已存在則回傳錯誤訊息，否則新增會員
            if request.data['member_email'] != None and request.data['member_email'] != '': 
                try:
                    member = models.Member.objects.get(member_email=request.data['member_email'])
                    return Response({'message':'Member has already existed!'}, status=status.HTTP_400_BAD_REQUEST)
                except:
                    serializer = MemberSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(status=status.HTTP_200_OK)
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # 如果會員email為空則回傳錯誤訊息
            else:
                return Response({'message':'Email cannot be empty!'}, status=status.HTTP_400_BAD_REQUEST)

class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = models.Message.objects.all()
    serializer_class = MessageSerializer
    
class LoginViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = models.LoginForm.objects.all()
    serializer_class = LoginSerializer
    
    def create(self, request):
        user = request.data
        try:
            member = models.Member.objects.get(
                    member_email=user['email'],
                    member_password=user['password']
                    )
            print(member)
            serializer = MemberSerializer(member)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
#    
#    def create(self, validated_data):
#        try:
#            print('email:', validated_data['email'])
#            print('password:', validated_data['password'])
#            member = models.Member.objects.get(
#                    member_email=validated_data['email'],
#                    member_password=validated_data['password']
#                    )
#            print(member)
#            return member
#        except e:
#            return e   
    
class PostDetailView(DetailView):
    model = models.Post
    template_name = "post/post_detail.html"
    pk_url_kwarg = "post_id"
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True
    
def post_detail_view(request, primary_key):
    try:
        post = Post.objects.get(pk=primary_key)
        print(post.post_title)
    except Post.DoesNotExist:
        raise Http404('文章不存在')
    return render(request, 'post/post_detail.html', context={'post': post})