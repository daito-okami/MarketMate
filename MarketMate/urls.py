from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, search, market_detail, category_view, recipes  # Import from local views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('<str:market_name>/', market_detail, name='market_detail'),
    path('category/<str:category>/', category_view, name='category'),
    path('recipes/', recipes, name='recipes'),
    path('api/', include('MarketMate.LLM.urls')),  # LLM URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)