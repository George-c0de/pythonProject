from django.contrib import admin
from .models import Films
from .models import User
from .models import Favorite
from .models import Views

admin.site.register(Films)
admin.site.register(User)
admin.site.register(Favorite)
admin.site.register(Views)

