from django.db import models

class BaiViet(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image  = models.ImageField(null=True, blank=True, upload_to='media/img')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title
    