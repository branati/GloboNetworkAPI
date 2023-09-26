# -*- coding: utf-8 -*-
from rest_framework.views import APIView

from networkapi.extra_logging import local


class CustomAPIView(APIView):

    def finalize_response(self, request, *args, **kwargs):
        response = super(CustomAPIView, self)\
            .finalize_response(request, *args, **kwargs)

        # TODO
        # Tratado quando os objetos não existirem em local

        response['X-Request-Context'] = local.request_context if hasattr(local, 'request_context') else ''
        # response['X-Request-Context'] = getattr(local.request_context, 'request_context', '')
        response['X-Request-Id'] = local.request_id if hasattr(local, 'request_id') else '',
        # response['X-Request-Id'] = local.request_id

        return response
