from django.contrib.auth.models import User, Group
from django.utils.translation import get_language

from apps.mainpage.models import MainPage
from apps.parameter.models import Menu, SiteSettings
from apps.profile.models import Profile


def site(request):
    site_settings = SiteSettings.objects.last()
    main_page = MainPage.objects.last()
    urlObject = request.get_host()
    url = request.build_absolute_uri()
    return {'site_settings': site_settings, 'main_page': main_page, 'showURL': urlObject, 'URL': url, }


def menu(request):
    user_group = []
    if request.user.is_authenticated:
        user_group = Group.objects.filter(user=request.user)
    header_menu = Menu.objects.filter(menu_type_id=1, groupList__in=user_group).order_by('alignment')
    footer_menu = Menu.objects.filter(menu_type_id=2).order_by('alignment')
    lang = get_language()
    return {'header_menu': header_menu, 'footer_menu': footer_menu, 'lang': lang}


def first_creat(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).last()
        if not profile:
            profile = Profile.objects.create(user=request.user, )
            User.objects.filter(id=request.user.id).update(first_name=request.user.username)

        return {'profile': profile}
    return {}


# def group(request):
#     if request.user.is_authenticated:
#         call_status_deletion_authority = Group.objects.filter(user=request.user, id=6).first()
#         call_status_adding_authority = Group.objects.filter(user=request.user, id=7).first()
#         call_status_update_authority = Group.objects.filter(user=request.user, id=8).first()
#
#         community_update_authority = Group.objects.filter(user=request.user, id=9).first()
#         community_add_authority = Group.objects.filter(user=request.user, id=10).first()
#         community_deletion_authority = Group.objects.filter(user=request.user, id=11).first()
#
#         right_click_authority = Group.objects.filter(user=request.user, id=12).first()
#
#         call_adding_authority = Group.objects.filter(user=request.user, id=13).first()
#         call_update_authority = Group.objects.filter(user=request.user, id=14).first()
#         call_deletion_authority = Group.objects.filter(user=request.user, id=15).first()
#         return {
#             'call_status_deletion_authority': call_status_deletion_authority,
#             'call_status_adding_authority': call_status_adding_authority,
#             'call_status_update_authority': call_status_update_authority,
#             'community_update_authority': community_update_authority,
#             'community_add_authority': community_add_authority,
#             'community_deletion_authority': community_deletion_authority,
#             'right_click_authority': right_click_authority,
#             'call_adding_authority': call_adding_authority,
#             'call_update_authority': call_update_authority,
#             'call_deletion_authority': call_deletion_authority,
#         }
#     return {}
