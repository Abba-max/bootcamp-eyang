from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from .views import IndexView, AddCertificationView, AddRelatedView, CertificationDetailView, login, registration, logout

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("add/", AddCertificationView.as_view(), name="add_certification"),
    path("add-related/<str:model_name>/", AddRelatedView.as_view(), name="add_related"),
    path("certification/<int:pk>/", CertificationDetailView.as_view(), name="certification_detail"),
    path('login/',views.login, name= 'login'),
    path('registration/',views.registration, name= 'registration'),
    path('logout',views.logout, name= 'logout'),
    # path('accounts/', include('allauth.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
