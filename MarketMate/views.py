from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    markets = [
        {
            'name': 'Billa',
            'image': 'marketmate/images/billa_img.jpg',  # Updated path to match static directory structure
            'url': '/billa'
        },
        {
            'name': 'Lidl',
            'image': 'marketmate/images/lidl.png',
            'url': '/lidl'
        },
        {
            'name': 'Fantastico',
            'image': 'marketmate/images/fantastico_img.png',
            'url': '/fantastico'
        },
        {
            'name': 'T-Market',
            'image': 'marketmate/images/t_market.png',
            'url': '/t-market'
        },
        {
            'name': 'Dar',
            'image': 'marketmate/images/dar_img.png',
            'url': '/dar'
        }
    ]

    offers = [
        {'title': 'Special Offer 1', 'image': '/api/placeholder/300/240'},
        {'title': 'Special Offer 2', 'image': '/api/placeholder/300/240'},
        {'title': 'Special Offer 3', 'image': '/api/placeholder/300/240'},
        {'title': 'Special Offer 4', 'image': '/api/placeholder/300/240'},
    ]

    recipes = [
        {
            'name': 'Пълнен печен картоф',
            'image': '/api/placeholder/400/300',
            'ingredients': 'картофи, кашкавал, сметана, бекон',
            'difficulty': 'Награждаван'
        },
        {
            'name': 'Хрупкава бяла риба със сос тартар',
            'image': '/api/placeholder/400/300',
            'ingredients': 'бяла риба, панировка, сос тартар',
            'difficulty': 'Награждаван'
        }
    ]

    context = {
        'markets': markets,
        'offers': offers,
        'recipes': recipes
    }
    return render(request, 'marketmate/home.html', context)


def search(request):
    query = request.GET.get('q', '')
    # Implement search logic here
    results = []  # Replace with actual search results
    return JsonResponse({'results': results})


def market_detail(request, market_name):
    # Implement market detail view
    return render(request, 'marketmate/market_detail.html', {'market_name': market_name})


def category_view(request, category):
    # Implement category view
    return render(request, 'marketmate/category.html', {'category': category})


def recipes(request):
    # Implement recipes view
    return render(request, 'marketmate/recipes.html')