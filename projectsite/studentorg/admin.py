from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

admin.site.register(College)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("college_name", "created_at", "updated_at" )                
    search_fields = ("college_name")
    list_filter = ("college_at")

admin.site.register(Program)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("program_name", "college",)
    search_fields = ("college_name", "prog_name",)
    list_filter = ("college")

admin.site.register(Organization)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "college", "description")
    search_fields = ("org_name", "description",)
    list_filter = ("college")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", 
                    "firstname", "middlename", "program")
    search_fields = ("lastname", "firstname",)
    
@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "get_member_program", "organization",
                    "date_joined",)
    search_fields = ("student__lastname", "student__firstname",)

    def get_member_program(self, obj):
        try:
            member = Student.objects.get(id=obj.student_id)
            return member.program
        except Student.DoesNotExist:
            return None