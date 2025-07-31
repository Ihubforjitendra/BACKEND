from django.urls import path
from . import views

urlpatterns = [
    # ---------------- Dashboard ----------------
    path('', views.dashboard, name='dashboard'),

    # ---------------- Batches ----------------
    path('batches/add/', views.create_batch, name='create_batch'),         # Add New Batch
    path('batches/', views.list_batches, name='list_batches'),             # View All Batches
    path('batches/edit/<int:pk>/', views.edit_batch, name='edit_batch'),   # ✅ Edit Batch

    # ---------------- Trainers ----------------
    path('trainers/add/', views.add_trainer, name='add_trainer'),
    path('trainers/', views.list_trainers, name='list_trainers'),
    path('trainers/edit/<int:pk>/', views.edit_trainer, name='edit_trainer'),

    # ---------------- Job Roles / Courses ----------------
    path('jobroles/add/', views.add_jobrole, name='add_jobrole'),
    path('jobroles/', views.list_jobroles, name='list_jobroles'),
    path('jobroles/edit/<int:pk>/', views.edit_jobrole, name='edit_jobrole'),

    # ---------------- Certificate Upload ----------------
    path('certificate/upload/', views.upload_certificate_admin, name='upload_certificate_admin'),  # ✅ Admin Upload
]
