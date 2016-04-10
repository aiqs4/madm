from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class RestApiApphook(CMSApp):
    name = _("RestApi")
    urls = ["madm_restapi.urls"]

apphook_pool.register(RestApiApphook)
