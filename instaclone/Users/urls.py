from django.urls import path
from Users.views import(
    registration_view,
    ObtainAuthTokenView,
    user_info_view,
	update_user_view,
	does_user_exist_view,
	ChangePasswordView,
)
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'Users'

urlpatterns = [
    path('check_if_user_exists/', does_user_exist_view, name="check_if_user_exists"),
	path('change_password/', ChangePasswordView.as_view(), name="change_password"),
	path('info', user_info_view, name="info"),
	path('info/update', update_user_view, name="update"),
    path('register', registration_view, name="register"),
    path('login', ObtainAuthTokenView.as_view(), name="login"),
]
