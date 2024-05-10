from django.contrib.auth.mixins import UserPassesTestMixin

class TeamOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.owner
    


class TeamMemberMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return self.request.user in obj.members.all()
    