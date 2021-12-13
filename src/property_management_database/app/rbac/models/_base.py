from django.db import models


class NameMixin:
    def __str__(self):
        if hasattr(str, 'removesuffix'):
            return f"<{self.__class__.__name__.removesuffix('Model')}{self.pk} {self.name}>"
        return f"<{self.__class__.__name__}{self.pk} {self.name}>"