from django.db import models
# Create your models here.



class UserGroupBindUserWithRoleModel(models.Model):
    user_group = models.ForeignKey(
        "UserGroupModel",
        on_delete=models.CASCADE,
        blank=True
    )
    role = models.ForeignKey("RoleModel", on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)