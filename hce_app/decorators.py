from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def allowed_to(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login', auths:list = None):
    '''
    Decorator for views that checks that the logged in user is in auths,
    redirects to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.authorize in auths,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

