from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator, FileExtensionValidator
from django.db import models

from .managers import CustomUserManager


PHONE_REGEX_VALIDATOR = RegexValidator(regex=r'/^(05\d\d{7})|\+?(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$', message="Accepting digits only! '05XXXXXXXX' '971501234567'\nMax 15 digits")
PROFILE_IMG_VALIDATOR = FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])
DOC_VALIDATOR = FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'pdf'])

class BaseUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(validators=[PHONE_REGEX_VALIDATOR], max_length=15, blank=True)
    profile_img = models.ImageField(upload_to='profile_images/', max_length=512, null=True, blank=True, default='profile_images/default_profile_img.png', validators=[PROFILE_IMG_VALIDATOR])

    # user_type = models.CharField(max_length=50, choices=USER_TYPES, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    date_deleted = models.DateTimeField(_('date deleted'), null = True, blank = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('Auth User')
        verbose_name_plural = _('Auth Users')

    def __str__(self):
        return self.get_username()
