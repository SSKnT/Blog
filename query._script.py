import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic_test.settings')
django.setup()

from My_List.models import Post
from django.contrib.auth.models import User
from users.models import Profile


post = Post.objects.first()
print(post.Author.id)
