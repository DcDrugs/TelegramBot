from django.db import models


class Profiler(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name="User ID"
    )

    name = models.TextField(
        verbose_name="User name"
    )

    def __str__(self) -> str:
        return f'#{self.external_id} {self.name}'

    class Meta:
        verbose_name = "Profile"


class Message(models.Model):
    profiler = models.ForeignKey(
        to='ugc.Profiler',
        verbose_name='Profile',
        on_delete=models.PROTECT,
    )
    text = models.TextField(
        verbose_name='Text',
    )
    created_at = models.DateTimeField(
        verbose_name='Time create',
        auto_now_add=True,
    )

    def __str__(self) -> str:
        return f'Message {self.pk} from {self.profiler}'

    class Meta:
        verbose_name = "Message"
