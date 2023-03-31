from django.conf import settings

#secure
settings.SESSION_COOKIE_SECURE = True
settings.CSRF_COOKIE_SECURE = True
settings.SECURE_BROWSER_XSS_FILTER = True
settings.SECURE_CONTENT_TYPE_NOSNIFF = True
settings.SECURE_SSL_REDIRECT = True
settings.X_FRAME_OPTIONS = 'DENY'


