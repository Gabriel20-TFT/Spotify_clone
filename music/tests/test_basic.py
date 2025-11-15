from django.test import TestCase
from django.urls import reverse
from .models import Artist, Song, Album
from django.contrib.auth.models import User

class BasicModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass123')
        self.artist = Artist.objects.create(name='Test Artist')
        self.album = Album.objects.create(title='Test Album')
        self.song = Song.objects.create(title='Test Song', album=self.album)
        self.song.artists.add(self.artist)

    def test_artist_str(self):
        self.assertEqual(str(self.artist), 'Test Artist')

    def test_song_list_view_requires_login(self):
        resp = self.client.get(reverse('song_list'))
        # should redirect to login
        self.assertIn(resp.status_code, (302, 301))

    def test_song_list_view_logged_in(self):
        self.client.login(username='tester', password='pass123')
        resp = self.client.get(reverse('song_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Test Song')
