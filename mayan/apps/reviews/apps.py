### Application Configurations File ###
from django.apps import apps
from django.utils.translation import ugettext_lazy as _

from mayan.apps.acls.classes import ModelPermission
from mayan.apps.acls.permissions import permission_acl_edit, permission_acl_view
from mayan.apps.common.apps import MayanAppConfig
from mayan.apps.common.classes import ModelCopy, ModelQueryFields
from mayan.apps.common.menus import (
    menu_facet, menu_list_facet, menu_main, menu_multi_item, menu_object,
    menu_secondary
)
from .links import (
    link_review_list, link_review_create
)
from .menus import menu_reviews

class ReviewsApp(MayanAppConfig):
    # config information for the app
    app_namespace = 'reviews'
    app_url = 'reviews'
    has_rest_api = False
    has_tests = False
    name = 'mayan.apps.reviews'
    verbose_name = _('Reviews')

    def ready(self):
        super().ready()
        # attach links to the menu component
        menu_reviews.bind_links(
            links=(
                link_review_list, link_review_create
            )
        )
        # add item to the menu
        menu_main.bind_links(links=(menu_reviews,), position=96)
