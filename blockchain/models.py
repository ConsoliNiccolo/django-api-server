from django.db import models

class Token(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField(blank=True)
    image = models.URLField(max_length=500, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    external_url = models.URLField(max_length=500, null=True, blank=True, default='')
    attributes = models.JSONField(default=dict, null=True, blank=True)

    def __str__(self):
        return f'{self.id} {self.name} - Token'

    @property
    def get_len_attributes(self):
        return f'{len(self.attributes)}'
