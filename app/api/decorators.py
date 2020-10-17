from functools import wraps
from flask import g
from ..models import Permission
from .errors import forbidden

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def inner(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient permissions')
            return f(*args, **kwargs)
        return inner
    return decorator

def admin_required(f):
    return permission_required(Permission.ADMIN)(f)
