from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import CreateView, ListView
from .models import CV, Education, Skill, Experience
from .forms import CVForm, EducationForm, SkillForm, ExperienceForm
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.contrib import messages
class CVCreateView(CreateView):
   model = CV
   form_class = CVForm
   template_name = 'cv/create_cv.html'

   def post(self, request, *args, **kwargs):
       cv_form = CVForm(request.POST)
       education_form = EducationForm(request.POST)
       experience_form = ExperienceForm(request.POST)
       skill_form = SkillForm(request.POST)

       if all([cv_form  .is_valid(), education_form.is_valid(), experience_form.is_valid(), skill_form.is_valid()]):
          cv = cv_form.save()
          edu = education_form.save(commit=False)
          edu.cv = cv
          edu.save()
          exp = experience_form.save(commit=False)
          exp.cv = cv
          exp.save()
          skill = skill_form.save(commit=False)
          skill.cv = cv
          skill.save()
          messages.success(request, 'CV successfully created!')
          return redirect('cv_list')

       return render(request, self.template_name,{
             'cv_form' : cv_form,
             'education_form': education_form,
             'experience_form': experience_form,
             'skill_form': skill_form
           })


   def get(self, request, *args, **kwargs):
      return render(request, self.template_name, {
            'cv_form': CVForm(),
            'education_form': EducationForm(),
            'experience_form': ExperienceForm(),
            'skill_form': SkillForm()
      })
class CVListView(ListView):
      model = CV
      template_name = 'cv/cv_list.html'
      context_object_name = 'cvs'

def generate_pdf(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    educations = Education.objects.filter(cv=cv)
    experiences = Experience.objects.filter(cv=cv)
    skills = Skill.objects.filter(cv=cv)

    context = {
        'cv': cv,
        'educations': educations,
        'experiences': experiences,
        'skills': skills,
    }

    template = get_template('cv/cv_pdf.html')
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)
    return response

def welcome(request):
    return render(request, 'welcome.html')

def cv_view(request,pk):
    cv = get_object_or_404(CV, pk=pk)
    return render(request,'cv/view_cv.html',{'cv':cv})