from django.db import models


class Posts(models.Model):
    title = models.CharField(verbose_name='Titulo de la publicacion', max_length=150)
    content = models.TextField(verbose_name='Agrega el contenido de la publicacion')
    status = models.SmallIntegerField(verbose_name='Indica el estado de la publicacion')
    publishedDate = models.DateTimeField(verbose_name='Especificar fecha de publicacion')


    def __str__(self):
        return self.title
        

    class Meta:
        verbose_name = 'publicacion'
        verbose_name_plural = 'publicaciones'

