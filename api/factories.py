import factory
from api.models import User, Product

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.Sequence(lambda n: f'user{n}@example.com')
    first_name = 'Test'
    last_name = 'User'
    country = 'Brasil'
    state = 'São Paulo'
    city = 'São Paulo'
    postal_code = '01310-100'
    address = 'Rua Test, 123'

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Sequence(lambda n: f'Product {n}')
    description = 'Test product description'
    price = 99.99
    inventory = 10