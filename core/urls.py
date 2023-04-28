from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/post/', include("post.api.urls")),
    path('api/comment/', include("comment.api.urls")),
    path('api/favourite/', include("favourite.api.urls")),
    path("api/user/", include("account.api.urls"), name='account'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name="token_ontain_pair"),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
