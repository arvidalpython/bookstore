from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Campos customizados (opcionais)
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    # CORREÇÃO: Adicione related_name únicos para resolver conflitos
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='api_user_set',  # LINHA CRÍTICA - related_name único
        related_query_name='api_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='api_user_permissions_set',  # LINHA CRÍTICA - related_name único
        related_query_name='api_user',
    )

    class Meta:
        app_label = 'api'

    def __str__(self):
        return self.username
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.title