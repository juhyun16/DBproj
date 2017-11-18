import re
from django.forms import ValidationError

PHONE_REGEX=re.compile(r'(\d+)[-](\d+)[-](\d+)$')

def phone_validator(phone):
    if not PHONE_REGEX.match(phone):
        raise ValidationError("{}는 적절한 전화번호 형식이 아닙니다.".format(phone))

