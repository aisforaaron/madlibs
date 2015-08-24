from django.db import models

class Story(models.Model):
    # title
    story_title = models.CharField(max_length=255)
    # body
    story_body_help_text = "Enter your story and use {token} as values you want to replace. Use dashes instead of spaces. For example, {noun}, {plural-noun} and {verb}."
    story_body = models.TextField(help_text = story_body_help_text)
    # better admin object titles
    def __str__(self):              # __unicode__ on Python 2
        return self.story_title