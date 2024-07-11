from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from store.views.index import Index
from store.views.about import About
from store.views.account import Account
from store.views.blank import Blank
from store.views.block_printed_bag import BlockPrintedBag
from store.views.blog import Blog
from store.views.blog_detail import BlogDetail
from store.views.cart import Cart
from store.views.checkout import Checkout
from store.views.compare import Compare
from store.views.contact import Contact
from store.views.forgot_password import ForgotPassword
from store.views.forum import Forum
from store.views.forum_detail import ForumDetail
from store.views.my_account import MyAccount
from store.views.my_account_order import MyAccountOrder
from store.views.policy import Policy
from store.views.product_detail import ProductDetail
from store.views.signup import Sign_Up
from store.views.home import Home
from store.views.login import Login
from store.views.logout import Logout
from store.views.collectionview import CollectionDetailView
from store.views.categoryview import CategoryDetailView
from store.views.collection import Collection
from store.views.category import Category



urlpatterns = [
    path('', Index.as_view(),name='homepage'),
    path('collection/<int:pk>', CollectionDetailView.as_view(), name='collection-detail'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category-detail'),
    path('collection/<int:collection_id>',Collection.as_view(),name='collection'),
    path('category/<int:category_id>',Category.as_view(),name='category'),
    path('about/',About.as_view(),name='about'),
    path('signup/',Sign_Up.as_view(),name='signup'),
    path('home/',Home.as_view(),name='home'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('account/', Account.as_view(),name='account'),
    path('blank/', Blank.as_view(),name='blank'),
    path('block-printed-bag/', BlockPrintedBag.as_view(),name='block-printed-bag'),
    path('blog/', Blog.as_view(),name='blog'),
    path('blog-detail/', BlogDetail.as_view(),name='blog-detail'),
    path('cart/', Cart.as_view(),name='cart'),
    path('checkout/', Checkout.as_view(),name='checkout'),
    path('compare/', Compare.as_view(),name='compare'),
    path('contact/', Contact.as_view(),name='contact'),
    path('forgot-password/', ForgotPassword.as_view(),name='forgot-password'),
    path('forum/', Forum.as_view(),name='forum'),
    path('forum-detail/', ForumDetail.as_view(),name='forum-detail'),
    path('my-account/', MyAccount.as_view(),name='my-account'),
    path('my-account-order/', MyAccountOrder.as_view(),name='my-account-order'),
    path('policy/', Policy.as_view(),name='policy'),
    path('product-detail/', ProductDetail.as_view(),name='product-detail'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)