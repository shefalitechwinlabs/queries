from django.core.exceptions import ValidationError

# Email validator accepts only gmail username
def validate_google_mail(value):
    if "@gmail.com" in value:
        return value
    else:
        raise ValidationError("Email field accepts gmail username only")
