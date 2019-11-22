from django.contrib import admin
from .models import Post

admin.site.register(Post)

#As you can see, we import (include) the Post model defined in the previous chapter.
#  To make our model visible on the admin page, 
# we need to register the model with admin.site.register(Post).