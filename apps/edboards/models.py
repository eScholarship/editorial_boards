from django.db import models

class Journal(models.Model):
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    journal_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    orcid = models.CharField(max_length=19, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Institution(models.Model):
    name = models.CharField(max_length=255)
    ror_id = models.CharField(max_length=20, unique=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    is_uc = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Issue(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    volume = models.CharField(max_length=50)
    issue_number = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    source_url = models.URLField(max_length=500, blank=True, null=True)

    class Meta:
        unique_together = [('journal', 'issue_number', 'volume')]

    def __str__(self):
        return f"{self.journal} - Vol {self.volume}, Issue {self.issue_number}"

class EditorialBoardMember(models.Model):
    ROLES = [
        ('Executive Editor', 'Executive Editor'),
        ('Editor-in-Chief', 'Editor-in-Chief'),
        ('Co-Editor-in-Chief', 'Co-Editor-in-Chief'),
        ('Senior Editor', 'Senior Editor'),
        ('Associate Editor', 'Associate Editor'),
        ('Managing Editor', 'Managing Editor'),
        ('Handling Editor', 'Handling Editor'),
        ('Section Editor', 'Section Editor'),
        ('Review Editor', 'Review Editor'),
        ('Editorial Assistant', 'Editorial Assistant'),
        ('Editor', 'Editor'),
        ('Editorial Board Member', 'Editorial Board Member'),
        ('Advisory Board Member', 'Advisory Board Member'),
        ('Advisory Editor', 'Advisory Editor'),
        ('Honorary Editor', 'Honorary Editor'),
        ('Designer / Production Editor', 'Designer / Production Editor'),
        ('Writer', 'Writer'),
        ('Copyeditor', 'Copyeditor'),
        ('Publicity Editor', 'Publicity Editor'),
        ('Advisor', 'Advisor'),
    ]
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    affiliation = models.ForeignKey(Institution, on_delete=models.CASCADE, blank=True, null=True)
    role = models.CharField(max_length=255, choices=ROLES, default='Editorial Board Member')

    def __str__(self):
        return f"{self.person} - {self.issue} ({self.role})"

