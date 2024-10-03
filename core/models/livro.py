from django.db import models

from core.models import Categoria


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='livros')

    def __str__(self):
        return f"({self.id}) {self.titulo}"
