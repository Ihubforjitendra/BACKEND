from django.shortcuts import render, redirect, get_object_or_404
from .models import Batch, Trainer, JobRole, Student
from .forms import BatchForm, TrainerForm, JobRoleForm, CertificateUploadForm

#Main Dashboard Views
def dashboard(request):
    return render(request, 'core/dashboard.html')


# ---------------- BATCH VIEWS ----------------
def create_batch(request):
    if request.method == 'POST':
        form = BatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_batches')
    else:
        form = BatchForm()
    return render(request, 'core/create_batch.html', {'form': form})

def list_batches(request):
    batches = Batch.objects.all()
    return render(request, 'core/list_batches.html', {'batches': batches})


# ---------------- Edit Batch ----------------
def edit_batch(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    if request.method == 'POST':
        form = BatchForm(request.POST, instance=batch)
        if form.is_valid():
            form.save()
            return redirect('list_batches')
    else:
        form = BatchForm(instance=batch)
    return render(request, 'core/edit_batch.html', {'form': form})


#upload certificate for student by admin
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Session, Scheme, JobRole, Batch
from django.contrib import messages

def upload_certificate_admin(request):
    sessions = Session.objects.all()
    schemes = Scheme.objects.all()
    job_roles = JobRole.objects.all()
    batches = Batch.objects.all()
    students = Student.objects.none()  # Default empty until filters are selected

    if request.method == 'POST':
        session_id = request.POST.get('session')
        scheme_id = request.POST.get('scheme')
        job_role_id = request.POST.get('job_role')
        batch_id = request.POST.get('batch')
        student_id = request.POST.get('candidate_id')

        if student_id:
            student = get_object_or_404(Student, id=student_id)

            if 'certificate' in request.FILES:
                student.certificate = request.FILES['certificate']
            if 'marksheet' in request.FILES:
                student.marksheet = request.FILES['marksheet']
            student.save()

            messages.success(request, f'Certificate & Marksheet uploaded for {student.candidate_id}')
            return redirect('upload_certificate_admin')
        else:
            messages.error(request, 'Please select a valid candidate.')

        # Reload students if form submission fails
        if batch_id:
            students = Student.objects.filter(batch_id=batch_id)

    context = {
        'sessions': sessions,
        'schemes': schemes,
        'job_roles': job_roles,
        'batches': batches,
        'students': students,
    }
    return render(request, 'core/upload_certificate.html', context)



# ---------------- TRAINER CRUD (Create, List, Edit only) ----------------
def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_trainers')
    else:
        form = TrainerForm()
    return render(request, 'core/add_trainer.html', {'form': form})

def list_trainers(request):
    trainers = Trainer.objects.all()
    return render(request, 'core/list_trainers.html', {'trainers': trainers})

def edit_trainer(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('list_trainers')
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'core/edit_trainer.html', {'form': form})

# ---------------- JOB ROLE CRUD (Create, List, Edit only) ----------------
def add_jobrole(request):
    if request.method == 'POST':
        form = JobRoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_jobroles')
    else:
        form = JobRoleForm()
    return render(request, 'core/add_jobrole.html', {'form': form})

def list_jobroles(request):
    jobroles = JobRole.objects.all()
    return render(request, 'core/list_jobroles.html', {'jobroles': jobroles})

def edit_jobrole(request, pk):
    jobrole = get_object_or_404(JobRole, pk=pk)
    if request.method == 'POST':
        form = JobRoleForm(request.POST, instance=jobrole)
        if form.is_valid():
            form.save()
            return redirect('list_jobroles')
    else:
        form = JobRoleForm(instance=jobrole)
    return render(request, 'core/edit_jobrole.html', {'form': form})
