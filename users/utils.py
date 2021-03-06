from pyhunter import PyHunter
from rest_framework import serializers
from requests import exceptions
from django.conf import settings


def email_verify(email):
    """
    Check is email valid and is it deliverable
    :param email: email to check
    :return: True if email valid
    :raise ValidationError if email invalid or undeliverable
    """
    hunter = PyHunter(settings.HUNTER_API_KEY)
    try:
        response = hunter.email_verifier(email)
        if response['result'] == 'undeliverable':
            raise serializers.ValidationError
    except exceptions.HTTPError:
        raise serializers.ValidationError

    return True
