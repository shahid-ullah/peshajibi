from django.http import JsonResponse
from rest_framework.views import exception_handler


def error_404(request, exception):
    message = 'Requested url is not found'
    data = {
        'message': message,
        'status': 'failed',
    }
    response = JsonResponse(data=data)
    response.status_code = 404

    return response


def error_500(request):
    message = 'An Error occured on server'
    data = {
        'message': message,
        'status': 'failed',
    }
    response = JsonResponse(data=data)
    response.status_code = 500

    return response


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    handlers = {
        'ValidationError': _handle_generic_error,
        'Http404': _handle_generic_error,
        'PermissionDenied': _handle_generic_error,
        'NotAuthenticated': _handle_authentication_error,
        'AuthenticationFailed': _handle_authentication_error,
    }

    exception_class = exc.__class__.__name__
    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status'] = 'failed'

    return response


def _handle_generic_error(exec, context, response):
    if response is not None:
        response.data['status'] = 'failed'

    return response


def _handle_authentication_error(exec, context, response):
    if response is not None:
        response.data['status'] = 'failed'

    return response
