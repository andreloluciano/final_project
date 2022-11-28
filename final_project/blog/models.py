from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
	post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	content=models.TextField()
	timestamp=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return 'comment on {} by {}'.format(self.post.title,self.user.username)

class checkmk(models.Model):
	mid = models.AutoField(primary_key=True)
	d_image=models.ImageField(upload_to="detected")

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		img = Image.open(self.d_image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.d_image.path)

	def road(self):
		return self.d_image.path