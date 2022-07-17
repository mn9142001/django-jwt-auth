import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

from channels.routing import ProtocolTypeRouter, URLRouter
from .middlewares import TokenAuthMiddleware
application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    'websocket' : TokenAuthMiddleware(URLRouter([]))
})
