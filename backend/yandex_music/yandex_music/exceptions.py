from rest_framework.views import exception_handler
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

def core_exception_handler(exc, context):
    response = exception_handler(exc, context)
    handlers = {
        'ValidationError': _handle_generic_error
    }
    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    return response


def _handle_generic_error(exc, context, response):
    if response is not None and hasattr(response, 'data'):
        logger.error(f"ValidationError: {response.data}")
        response.data = {
            'errors': response.data
        }
    else:
        logger.error("Unknown error occurred.")
        response = Response({
            'errors': 'Unknown error occurred.'
        }, status=500)

    return response