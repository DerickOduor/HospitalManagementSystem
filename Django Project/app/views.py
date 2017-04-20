from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from .models import Records,Student_Database
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'all_students'
    
    def get_queryset(self):
        return Student_Database.objects.all()

class DetailView(generic.DetailView):
    model = Student_Database
    template_name = 'detail.html'
    context_object_name = 'all_students'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['students'] = Records.objects.all()
        return context

def success(request):
    return render(request, 'success.html')
class StudentAdd(CreateView):
    model = Student_Database
    template_name = 'student_form.html'
    fields = ['Image','Registration_No','Name','Faculty','Department','Course']
        
class RecordCreate(CreateView):
    model = Records
    template_name = 'student_form.html'
    fields = ['Student_Name','Student_Information','Date','Problem','Prescription','Maternity_Services','Lab_Results','Ward_Report']

class RecordUpdate(UpdateView):
    model = Records
    template_name = 'student_form.html'
    fields = ['Student_Name','Date','Problem','Prescription','Maternity_Services','Lab_Results','Ward_Report']

class StudentDelete(DeleteView):
    model = Records
    success_url = reverse_lazy('index')



