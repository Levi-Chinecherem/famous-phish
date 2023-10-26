from django.db import models


class PhishingAttempt(models.Model):
    attacker_ip = models.CharField(max_length=15)
    target_url = models.URLField()
    success = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # Add an attack_type field
    attack_type = models.CharField(max_length=255)
    
    def __str__(self):
        return f"PhishingAttempt - {self.attack_type} - {self.attacker_ip} - {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']  # Order by timestamp in descending order
        verbose_name = "Phising Attempt"
        verbose_name_plural = "Phising Attempt"
        
  