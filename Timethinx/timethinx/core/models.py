from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager 
from django.db.models import CheckConstraint, Q
from django.conf import settings
from django.conf.global_settings import AUTH_USER_MODEL

class BaseModel(models.Model):
    class Meta:
        abstract = True

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('part_time', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('part_time', False)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""
    username = None
    email = models.EmailField('email address', unique=True)
    part_time = models.BooleanField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['part_time'] # removes email from REQUIRED_FIELDS

    objects = UserManager()

class Customer(BaseModel):
    customer_name = models.CharField(max_length=50, verbose_name="Müşteri Adı")

    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name = "Müşteri"
        verbose_name_plural = "Müşteriler"


class Project(BaseModel):
    project_name = models.CharField(max_length=50, verbose_name="Proje Adı")
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, verbose_name="Müşteri")

    def __str__(self):
        return f'{self.project_name} / {self.customer}'

    class Meta:
        verbose_name = "Proje"
        verbose_name_plural = "Projeler"


class Task(BaseModel):
    task_name = models.CharField(max_length=30, verbose_name="Görev Adı")
    project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL, verbose_name="Proje")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, default=1, blank=True)

    def __str__(self):
        return f'{self.task_name} / {self.project}'

    class Meta:
        verbose_name = "Görev"
        verbose_name_plural = "Görevler"


class TaskLog(BaseModel):
    task = models.ForeignKey(Task, null=True, on_delete=models.SET_NULL, verbose_name="Görev")
    created_at = models.DateField(null=True, verbose_name="Tarih")
    hours_worked = models.FloatField(validators=[MinValueValidator(0)], verbose_name="Çalışılan saat")

    def __str__(self):
        return f'{self.task}'

    class Meta:
        verbose_name = "Görev Günlüğü"
        verbose_name_plural = "Görev Günlükleri"
        constraints = (
            # for checking in the DB
            CheckConstraint(
                check=Q(hours_worked__gte=0),
                name='task_log_hours_worked_range'),
        )
