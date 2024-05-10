from django.contrib.auth.mixins import UserPassesTestMixin

class TaskOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user
    
class TaskMemberMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return self.request.user in obj.team.members.all()
    