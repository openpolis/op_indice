from django.db import models
from markdown import markdown

class TextBlockEnIt(models.Model):
    slug = models.CharField(blank=True, max_length=100)
    txt_en = models.TextField(blank=True)
    html_en = models.TextField(editable=False, blank=True)
    txt_it = models.TextField(blank=True)
    html_it = models.TextField(editable=False, blank=True)
    def save(self, *args, **kwargs):
      """override save method and transform markdown into html"""
      if self.txt_en:
        self.html_en = markdown(self.txt_en)
      if self.txt_it:
        self.html_it = markdown(self.txt_it)
      super(TextBlockEnIt, self).save(*args, **kwargs)

    class Meta:
      verbose_name_plural = "Text blocks EN/IT"
