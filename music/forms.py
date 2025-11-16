from django import forms
from .models import Song
from django.core.exceptions import ValidationError
import os


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artists', 'album', 'audio_file', 'cover_image']

    def clean_audio_file(self):
        f = self.cleaned_data.get('audio_file')
        if not f:
            return f
        # limit 15 MB
        max_mb = 15
        if f.size > max_mb * 1024 * 1024:
            raise ValidationError(f'Fișierul este prea mare (max {max_mb}MB).')
        # check extension
        valid_ext = ['.mp3', '.wav', '.ogg', '.m4a']
        ext = os.path.splitext(f.name)[1].lower()
        if ext not in valid_ext:
            raise ValidationError('Format audio neacceptat. Folosește mp3, wav, ogg sau m4a.')
        return f
