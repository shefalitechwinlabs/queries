from django.core.exceptions import ValidationError

def validate_google_mail(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError("This field accepts mail id of google only")
