from django import forms
from .models import Batch, Trainer, JobRole, Student, Scheme, Session


class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'theory_end_date': forms.DateInput(attrs={'type': 'date'}),
            'ojt_start_date': forms.DateInput(attrs={'type': 'date'}),
            'ojt_end_date': forms.DateInput(attrs={'type': 'date'}),
            'reassessment_date': forms.DateInput(attrs={'type': 'date'}),
        }


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"

class JobRoleForm(forms.ModelForm):
    class Meta:
        model = JobRole
        fields = "__all__"

# This version is for direct upload using student_id (optional use)
class SimpleCertificateUploadForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['certificate_file', 'marksheet_file']

# This is for admin to upload certificates using filters
class CertificateUploadForm(forms.Form):
    session = forms.ModelChoiceField(queryset=Session.objects.all(), required=True)
    scheme = forms.ModelChoiceField(queryset=Scheme.objects.all(), required=True)
    job_role = forms.ModelChoiceField(queryset=JobRole.objects.none(), required=True)
    batch = forms.ModelChoiceField(queryset=Batch.objects.none(), required=True)
    student = forms.ModelChoiceField(queryset=Student.objects.none(), required=True, label="Candidate ID")

    certificate_file = forms.FileField(required=True)
    marksheet_file = forms.FileField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'session' in self.data and 'scheme' in self.data:
            try:
                session_id = int(self.data.get('session'))
                scheme_id = int(self.data.get('scheme'))
                self.fields['job_role'].queryset = JobRole.objects.filter(session_id=session_id, scheme_id=scheme_id)
            except (ValueError, TypeError):
                pass
        elif self.initial.get('session') and self.initial.get('scheme'):
            self.fields['job_role'].queryset = JobRole.objects.filter(
                session=self.initial['session'], scheme=self.initial['scheme'])

        if 'job_role' in self.data:
            try:
                job_role_id = int(self.data.get('job_role'))
                self.fields['batch'].queryset = Batch.objects.filter(job_role_id=job_role_id)
            except (ValueError, TypeError):
                pass

        if 'batch' in self.data:
            try:
                batch_id = int(self.data.get('batch'))
                self.fields['student'].queryset = Student.objects.filter(batch_id=batch_id)
            except (ValueError, TypeError):
                pass
