from django.shortcuts import render

from products.models import ProductCategory,Product

# Create your views here.
def index(request):
    context = {
        'title' : 'Store',
        'username' : 'Samir',
    }
    return render(request, 'products/index.html',context)

def products(request):
    context = {
        'title': 'Store-Каталог',
         'products': Product.objects.all(),
         'categories': ProductCategory.objects.all(),
         
         
        # [
        #     {'image': '/static/vendor/img/products/Adidas-hoodie.png',
        #      'name' : 'Худи черного цвета с монограммами adidas Originals',
        #      'price': 6990,
        #      'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
        #     },
        #      {'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
        #      'name' : 'Синяя куртка The North Face',
        #      'price': 23725,
        #      'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
        #     },
        #      {'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
        #      'name' : 'Коричневый спортивный oversized-топ ASOS DESIGN',
        #      'price': 3990,
        #      'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'
        #     }
        # ]
    }
    return render(request, 'products/products.html',context)