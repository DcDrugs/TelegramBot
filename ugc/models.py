from django.db import models
import uuid


class Profiler(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name="User ID",
        unique=True,
    )

    name = models.TextField(
        verbose_name="User name"
    )

    def __str__(self) -> str:
        return f'#{self.external_id} {self.name}'

    class Meta:
        verbose_name = "Profile"


class Item(models.Model):
    profiler = models.ForeignKey(
        to='ugc.Profiler',
        verbose_name='Profile',
        on_delete=models.PROTECT,
    )

    id = models.UUIDField(
        primary_key=True,
    )

    name = models.TextField(
        verbose_name="Item",
    )

    cost = models.IntegerField(
        verbose_name='Text',
    )

    created_at = models.DateTimeField(
        verbose_name='Time create',
        auto_now_add=True,
    )

    def __str__(self) -> str:
        return 'Item name:' + str(self.name) + '\n' + 'cost:' + str(self.cost) + '\n' + 'from:' + str(self.profiler) + '\n' + 'date:' + str(self.created_at)

    class Meta:
        verbose_name = "Item"
