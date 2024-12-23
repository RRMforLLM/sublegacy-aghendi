from django.db import models
from django.contrib.auth.models import User

# Agenda Model: Represents an agenda, including its name, creator, and members.
class Agenda(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the agenda (must be unique)
    key = models.CharField(max_length=100)  # A key (used for agenda security or identification)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_agendas')  # Creator of the agenda
    editors = models.ManyToManyField(User, related_name="edited_agendas", blank=True)  # Users who can edit the agenda
    members = models.ManyToManyField(User, related_name='joined_agendas', blank=True)  # Members of the agenda

    def __str__(self):
        return self.name  # String representation of the agenda, displaying its name

# AgendaSection Model: Represents a section within an agenda.
class AgendaSection(models.Model):
    name = models.CharField(max_length=100)  # Section name
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, related_name='sections')  # The agenda this section belongs to

    def __str__(self):
        return f"{self.agenda.name} - {self.name}"  # String representation showing agenda name and section name

# AgendaElement Model: Represents an individual element within an agenda section.
class AgendaElement(models.Model):
    section = models.ForeignKey(AgendaSection, on_delete=models.CASCADE, related_name='elements')  # Section to which this element belongs
    subject = models.CharField(max_length=200)  # Subject or title of the agenda element
    details = models.TextField()  # Detailed description of the element
    deadline = models.DateField(null=True, blank=True)  # Deadline for the element (optional)
    emission = models.DateField(null=True, blank=True)  # Emission date for the element (optional)
    status = models.CharField(max_length=20, default='active', choices=[('active', 'Active'), ('expired', 'Expired')])
    completed = models.ManyToManyField(User, related_name='flagged_completed', blank=True)
    urgent = models.ManyToManyField(User, related_name='flagged_urgent', blank=True)
    nothing = models.ManyToManyField(User, related_name='not_flagged')

    def __str__(self):
        return self.subject  # String representation of the element, displaying its subject

# ElementComment Model: Represents a comment on an agenda element by a user.
class ElementComment(models.Model):
    element = models.ForeignKey(AgendaElement, on_delete=models.CASCADE, related_name='comments')  # The element this comment is related to
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who made the comment
    text = models.TextField()  # The text content of the comment
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the comment was created

    def __str__(self):
        return f"Comment by {self.user.username} on {self.element.subject}"  # String representation of the comment, showing the user and element subject