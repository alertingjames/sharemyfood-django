from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from sharemyfood import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sharemyfood/', include('sharemyfood.urls')),
    # url(r'^$', views.index, name='index'),
    url(r'^register',views.register,  name='register'),
    url(r'^getAllProducts',views.getAllProducts,  name='getAllProducts'),
    url(r'^uploadProduct',views.uploadProduct,  name='uploadProduct'),
    url(r'^login',views.login,  name='login'),
    url(r'^likeProduct',views.likeProduct,  name='likeProduct'),
    url(r'^unlikeProduct',views.unlikeProduct,  name='unlikeProduct'),
    url(r'^deleteProduct',views.deleteProduct,  name='deleteProduct'),
    url(r'^updateProduct',views.updateProduct,  name='updateProduct'),
    url(r'^placeOrder',views.placeOrder,  name='placeOrder'),
    url(r'^delAccount',views.delAccount,  name='delAccount'),
    url(r'^updateAccount',views.updateAccount,  name='updateAccount'),
    url(r'^getProduct',views.getProduct,  name='getProduct'),
    url(r'^getMember',views.getMember,  name='getMember'),
    url(r'^getNotifications',views.getNotifications,  name='getNotifications'),

    url(r'^sendFeedback',views.sendFeedback,  name='sendFeedback'),
    url(r'^sendAmbassador',views.sendAmbassador,  name='sendAmbassador'),

    url(r'^fcm_insert',views.fcm_insert,  name='fcm_insert'),
    url(r'^submitFCM',views.submitFCM,  name='submitFCM'),
    url(r'^transact',views.transact,  name='transact'),
    url(r'^getConsumedProductInfo',views.getConsumedProductInfo,  name='getConsumedProductInfo'),

    url(r'^setMyLocation',views.updateMyLocation,  name='updateMyLocation'),

    url(r'^checkFeedback',views.checkFeedback,  name='checkFeedback'),
    url(r'^checkAmbassador',views.checkAmbassador,  name='checkAmbassador'),

    url(r'^mkContact',views.mkContact,  name='mkContact'),
    url(r'^getContacts',views.getContacts,  name='getContacts'),





    ####################################################################################################### ADMIN #################################################################################################################################

    url(r'^$', views.loginpage, name='loginpage'),
    url(r'^signin',views.signin,  name='signin'),
    url(r'^home',views.home,  name='home'),
    url(r'^products',views.products,  name='products'),
    url(r'^allproducts',views.allproducts,  name='allproducts'),
    url(r'^member',views.member,  name='member'),
    url(r'^filtermember',views.filtermember,  name='filtermember'),
    url(r'^cities',views.cities,  name='cities'),
    url(r'^adminsetting',views.adminsetting,  name='adminsetting'),
    url(r'^editaccount',views.editaccount,  name='editaccount'),
    url(r'^removeuser',views.removeuser,  name='removeuser'),
    url(r'^logout',views.logout,  name='logout'),
    url(r'^filtermapmember',views.filtermapmember,  name='filtermapmember'),
    url(r'^feedback',views.feedback,  name='feedback'),
    url(r'^ambassador',views.ambassador,  name='ambassador'),
    url(r'^delvolunteer',views.delvolunteer,  name='delvolunteer'),
    url(r'^delfeedback',views.delfeedback,  name='delfeedback'),
    url(r'^adminmessage',views.adminmessage,  name='adminmessage'),

    url(r'^to_page',views.to_page,  name='to_page'),
    url(r'^to_previous',views.to_previous,  name='to_previous'),
    url(r'^to_next',views.to_next,  name='to_next'),
    url(r'^export_xlsx',views.export_xlsx,  name='export_xlsx'),

    url(r'^analysis',views.analysis,  name='analysis'),

    url(r'^emm',views.emm,  name='emm'),
    url(r'^dmm',views.dmm,  name='dmm'),

]



urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns=format_suffix_patterns(urlpatterns)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
























































