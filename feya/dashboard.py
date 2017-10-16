from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard


class CustomIndexDashboard(Dashboard):
    columns = 2

    def init_with_context(self, context):
        self.available_children.append(modules.AppList)
        self.children.append(modules.AppList(
            _('Applications'),
            column=0,
            order=0
        ))
        self.available_children.append(modules.RecentActions)
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            10,
            column=1,
            order=0
        ))

        # TODO: Instalar google Analytics
