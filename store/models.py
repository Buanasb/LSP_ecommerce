# untuk mendefinisikan model dan attribut yang nanti akan dimigarate ke database
from django.db import models


class Description(models.Model):
    name = models.CharField(max_length=200, null=True)
    topc_1 = models.CharField(max_length=50, null=True)
    desc_1 = models.CharField(max_length=3000, null=True)
    image_1 = models.CharField(max_length=3000, null=True)
    topc_2 = models.CharField(max_length=50, null=True)
    desc_2 = models.CharField(max_length=3000, null=True)
    image_2 = models.CharField(max_length=3000, null=True)
    topc_3 = models.CharField(max_length=50, null=True)
    desc_3 = models.CharField(max_length=3000, null=True)
    image_3 = models.CharField(max_length=3000, null=True)
    topc_4 = models.CharField(max_length=50, null=True)
    desc_4 = models.CharField(max_length=3000, null=True)
    image_4 = models.CharField(max_length=3000, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=200, null=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=False)
    description = models.ForeignKey(
        Description, on_delete=models.CASCADE, verbose_name=('Deskripsi produk'), blank=True, null=True)

    def __str__(self):
        return self.name

    # ngebuat url produk masing2
    def get_absolute_url(self):
        return reverse('description', kwargs={'pk': self.pk})

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
