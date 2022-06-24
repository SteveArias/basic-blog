from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique blog post comments

class User(models.Model):
	"""Model representing a user."""
	username = models.CharField(max_length=100)
	
	location = models.CharField(max_length=100)

	date_of_birth = models.DateField(null=True, blank=True)

	bio = models.CharField(max_length=500)

	class Meta:
		ordering = ['username']

	def get_absolute_url(self):
		"""Returns the url to access a particular user."""
		return reverse('user-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.username}'

class BlogPost(models.Model):
    """Model representing a blog post."""
    title = models.CharField(max_length=100)

    author = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    date = models.DateField(null=True, blank=True)

    text = models.CharField(max_length=1000)

    class Meta:
        ordering = ['-date']
    
    def get_absolute_url(self):
        """Returns the url to access a particular blog post."""
        return reverse('blog-post-detail', args=[str(self.id)]) 

class Comment(models.Model):
    """Model representing a comment on a blog post."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this blog post comment')

    blog_post = models.ForeignKey('BlogPost', on_delete=models.SET_NULL, null=True)

    author = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    date = models.DateField(null=True, blank=True)

    text = models.CharField(max_length=200)

    class Meta:
        ordering = ['date']