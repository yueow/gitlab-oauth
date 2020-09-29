import json
import requests

from django.db import models
from django.conf import settings

import jsonfield


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    profile_url = models.URLField(blank=True, null=True)
    avatar_url = models.URLField(blank=True, null=True)
    suid = models.CharField(max_length=256, blank=True, null=True)
    location = models.CharField(max_length=256, blank=True, null=True)
    projects_json = jsonfield.JSONField()

    def __str__(self):
        return f'{self.user}'

    # I did not stick to creating separetad entity for repositories
    # So fetching user's repositories is implemented by this method
    # Returns a JSON of projects/repositories and saves it to JSONField 
    def get_projects(self, token):        
        projects = requests.get(f'https://gitlab.com/api/v4/users/{self.suid}/projects',
            headers={'Authorization': f'Bearer {token}'}).json()
        # print(projects)
        self.projects_json = projects
        self.save()
        return projects

