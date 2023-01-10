from django.contrib import admin

from apps.training.models import *

admin.site.register(InterviewStatus)
admin.site.register(Interview)


class InterviewInLine(admin.TabularInline):
    model = Interview
    extra = 1


class CommunityAdmin(admin.ModelAdmin):
    inlines = [
        InterviewInLine,
    ]
    list_display = (
        "full_name",
        "phone_one",
        "phone_two",
        "phone_three",
        "block",
        "apartment",
        "period",
        "period_code",
        "tc",
        "circuit_start",
        "circuit_finish",
    )
    search_fields = (
        "full_name",
        'period_code',
    )

    class Meta:
        model = Community


admin.site.register(Community, CommunityAdmin)
