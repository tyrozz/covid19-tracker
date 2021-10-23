from django.contrib.admin.views.decorators import (
    staff_member_required as _staff_member_required,
)


def staff_member_required(f):
    return _staff_member_required(f, login_url="account:login")