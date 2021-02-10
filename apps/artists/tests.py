from django.test import TestCase
from apps.artists.models import Album, Artist

class AlbumTestCase(TestCase):
    def setUp(self):
        album = Album.objects.create(title="Brazil Hits")
        album.artists.add(
            Artist.objects.create(name="Roberto Carlos"),
            Artist.objects.create(name="Djavan"),
            Artist.objects.create(name="Frejat"),
        )

    def test_album_with_multiple_artists(self):
        album = Album.objects.get(title="Brazil Hits")

        self.assertEqual(len(album.artists.all()), 3)
