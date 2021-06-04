from django.db import models
from django.utils.timezone import localtime, now


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(self):
      duration = now() - localtime(self.entered_at)
      if self.leaved_at:
        duration = self.leaved_at - self.entered_at
      return duration
    
    def is_visit_long(self, minutes=60):
      return self.get_duration().total_seconds() > minutes * 60 
    
    def serialize_visit(self):
      return {
          'who_entered': self.passcard.owner_name,
          'entered_at': self.entered_at,
          'duration': format_duration(self.get_duration()),
          'is_strange': self.is_visit_long(),
      }

    def __str__(self):
      return "{user} entered at {entered} {leaved}".format(
          user=self.passcard.owner_name,
          entered=self.entered_at,
          leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
      )

def format_duration(duration):
  splited_timedelta = str(duration).split(':')
  hours = splited_timedelta[0]
  minutes = splited_timedelta[1]
  return f'{hours}ч {minutes}мин'
