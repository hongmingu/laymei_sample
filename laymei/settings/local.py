from laymei.settings.base import *
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'email-smtp.us-west-2.amazonaws.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = '보내는 사람이름 <내 이메일 아이디@gmail.com>'
