from django.contrib import admin
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from referral.views import ReferralListView, SignUpView, UserProfileView
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API_referral",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('referrals/', ReferralListView.as_view(), name='referrals'),
    re_path(
        r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    )

]
