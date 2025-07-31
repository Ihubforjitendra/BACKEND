from django.contrib import admin
from .models import Scheme, Session, JobRole, Trainer, Batch, Student

@admin.register(Scheme)
class SchemeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(JobRole)
class JobRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'sector', 'qp_code')
    search_fields = ('name', 'qp_code')
    list_filter = ('sector', 'scheme', 'session')  # if you add scheme/session fields to JobRole

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'trainer_id')
    search_fields = ('name', 'trainer_id')

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('batch_id', 'batch_name', 'job_role', 'get_scheme', 'get_session', 'trainer')
    search_fields = ('batch_id', 'batch_name')
    list_filter = ('job_role', 'job_role__scheme', 'job_role__session')

    def get_scheme(self, obj):
        return obj.job_role.scheme
    get_scheme.short_description = "Scheme"

    def get_session(self, obj):
        return obj.job_role.session
    get_session.short_description = "Session"

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'candidate_id', 'batch')
    search_fields = ('name', 'candidate_id')
    list_filter = ('batch', 'batch__job_role')
