from django.core.cache import cache
from .models import Product
from config.settings import CACHE_ENABLED

class ProductService:

    @staticmethod
    def get_products_by_category(category_id):
        if not CACHE_ENABLED:
            return Product.objects.filter(category_id=category_id)

        key = f'products_by_category_{category_id}'
        products = cache.get(key)

        if products is not None:
            return products

        products = Product.objects.filter(category_id=category_id)
        cache.set(key, products, timeout=60 * 15)

        return products
