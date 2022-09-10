from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    area = models.CharField(max_length=5, blank=True, null=True)
    year = models.CharField(max_length=5)
    description = models.TextField()
    main_image = models.ImageField(upload_to='attachments')

    def __str__(self):
        return str(self.id)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='attachments')

    def __str__(self):
        return f'{str(self.project)} - {str(self.image)}'


class Visualization(models.Model):
    main_image = models.ImageField(upload_to='attachments')

    def __str__(self):
        return str(self.id)


class VisualizationImage(models.Model):
    visual = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='attachments')
    orientation = models.CharField(max_length=10, default='horizontal')

    def __str__(self):
        return f'{str(self.visual)} - {str(self.image)}'
