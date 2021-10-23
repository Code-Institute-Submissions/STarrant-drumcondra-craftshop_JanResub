from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    ''' Class to create link to static file location on AWS. '''
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    ''' Class to create link to media file location on AWS. '''
    location = settings.MEDIAFILES_LOCATION
