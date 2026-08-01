from django.db import models
from django.db.models import CheckConstraint, Q


class UserProfile(models.Model):
    full_name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("O", "Other"))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
        ordering = ["-age"]
        db_table = "customer_user_profile"

    def __str__(self) -> str:
        return f"{self.full_name} - {self.age}"


# Abstract Model (Template)
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Main Model inheriting from TimeStampedModel
class Employee(TimeStampedModel):
    department = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=10)
    age = models.IntegerField()

    class Meta(TimeStampedModel.Meta):  # Parent Meta inherit ki hai
        # Sahi Spelling: 'indexes'
        indexes = [
            models.Index(fields=["department"]),
        ]

        # Sahi Syntax: Simple list of tuples/lists
        unique_together = [["department", "employee_id"]]

        # Django 5/6 Standard: 'condition' keyword parameter
        constraints = [
            CheckConstraint(
                condition=Q(age__gte=18),
                name="employee_age_must_be_18_or_above",  # Spaces removed for clean SQL constraint name
            )
        ]

    def __str__(self) -> str:
        return f"{self.department} - {self.employee_id}"


# One to One Relation


class UserSettings(models.Model):   
    user = models.OneToOneField(
        UserProfile, 
        on_delete=models.CASCADE, 
        related_name="settings"
    )
    dark_mode = models.BooleanField(default=False)
    receive_notifications = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"Settings for {self.user.full_name} {self.user.is_active}"
