from django.db import models

# Create your models here.
from django.db import models

class Scheme(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class Session(models.Model):
    name = models.CharField(max_length=20, unique=True)  # e.g. 2023-2024

    def __str__(self):
        return self.name

class JobRole(models.Model):
    name = models.CharField(max_length=150)
    sector = models.CharField(max_length=50, choices=[('IT-ITES', 'IT-ITES'), ('Green Jobs', 'Green Jobs')])
    qp_code = models.CharField(max_length=50, unique=True)
    scheme = models.ForeignKey(Scheme, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.scheme} - {self.session})"


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    trainer_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name} ({self.trainer_id})"



class Batch(models.Model):
    # Existing fields...
    job_role = models.ForeignKey(JobRole, on_delete=models.CASCADE)
    batch_id = models.CharField(max_length=20, unique=True)
    batch_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    theory_end_date = models.DateField()
    ojt_start_date = models.DateField()
    ojt_end_date = models.DateField()
    theory_hours = models.IntegerField(default=7)
    ojt_hours = models.IntegerField(default=8)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    no_of_students = models.IntegerField()

    # ✅ Assessment fields
    attendance_sheet = models.FileField(upload_to='attendance/', null=True, blank=True)
    ojt_file = models.FileField(upload_to='ojt_files/', null=True, blank=True)
    candidates_assessed = models.IntegerField(null=True, blank=True)
    assessment_agency = models.CharField(max_length=100, null=True, blank=True)
    assessor_name = models.CharField(max_length=100, null=True, blank=True)
    assessor_aadhar = models.CharField(max_length=12, null=True, blank=True)
    is_assessment_done = models.BooleanField(default=False)
    assessment_document = models.FileField(upload_to='assessment_docs/', null=True, blank=True)

    # ✅ Reassessment fields
    reassessment_date = models.DateField(null=True, blank=True)
    reassigned_students = models.IntegerField(null=True, blank=True)
    reassessment_agency = models.CharField(max_length=100, null=True, blank=True)
    reassessor_name = models.CharField(max_length=100, null=True, blank=True)
    reassessor_id = models.CharField(max_length=20, null=True, blank=True)
    reassessor_aadhar = models.CharField(max_length=12, null=True, blank=True)
    reassessment_type = models.CharField(max_length=30, choices=[('Regular', 'Regular'), ('Re-assessment', 'Re-assessment')], null=True, blank=True)
    reassessment_document = models.FileField(upload_to='reassessment_docs/', null=True, blank=True)
    candidates_passed = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.batch_name} ({self.job_role.scheme} - {self.job_role.session})"




class Student(models.Model):
    name = models.CharField(max_length=100)
    candidate_id = models.CharField(max_length=50, unique=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    certificate_file = models.FileField(upload_to='certificates/', null=True, blank=True)
    marksheet_file = models.FileField(upload_to='marksheets/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.candidate_id})"
