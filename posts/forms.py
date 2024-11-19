from django.forms import ModelForms
from posts.models import Post

class postForm(ModelForms):
    class meta:
        model = Post
        fields = ['category' , 'title' , 'intro' , 'body' , ]





        
    16:50