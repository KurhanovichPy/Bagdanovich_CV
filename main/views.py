from django.shortcuts import render
from .models import Project, ProjectImage, Visualization, VisualizationImage


def about(request):
    return render(request, 'main/templates/main/about.html')


def projects_page(request):
    projects = Project.objects.all()
    visuals = Visualization.objects.all()
    return render(request, 'main/templates/main/projects.html', {'projects': projects, 'visuals': visuals})


def contacts(request):
    return render(request, 'main/templates/main/contacts.html')


def project_info(request, pk):
    projects = Project.objects.filter(id=pk)
    projects_img = ProjectImage.objects.filter(project_id=pk)
    return render(request, 'main/templates/main/project.html', {'projects': projects, 'images': projects_img})


def visual_info(request, pk):
    visual_img = VisualizationImage.objects.filter(visual_id=pk)
    return render(request, 'main/templates/main/visual.html', {'images': visual_img})
