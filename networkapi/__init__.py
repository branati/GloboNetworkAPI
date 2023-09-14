# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .celery_app import app as celery_app

# from networkapi.equipamento.models import *
# from networkapi.api_vrf.models import *

__all__ = ('celery_app', 'VERSION')

MAJOR_VERSION = '3'
MINOR_VERSION = '4'
PATCH_VERSION = '2'
VERSION = '.'.join((MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION,))
