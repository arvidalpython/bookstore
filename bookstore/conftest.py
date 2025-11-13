# ...existing code...
import os
import sys

# acrescenta a raiz do projeto ao PYTHONPATH (ajuste se necessário)
root = os.path.dirname(__file__)
if root not in sys.path:
    sys.path.insert(0, root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
# ...existing code...