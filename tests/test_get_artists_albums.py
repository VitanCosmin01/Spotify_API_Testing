import unittest

from Spotify.spotify_requests import SpotifyRequests


class TestGetArtistsAlbums(unittest.TestCase):

    def setUp(self):
        self.request_handler = SpotifyRequests()

    def test_get_artists_albums(self):
        """
        Verificam:
        - status code este 200
        - status code name este "OK"
        - verificam ca raspunsul cuprinde atributele corecte
        - verificam ca atributele au ca valori tipul de date necesar
        :return:
        """
        expected_status_code = 200
        expected_status_name = "OK"
        attributes = ["href", "limit", "next", "next", "offset", "previous", "total", "items"]

        response = self.request_handler.get_artists_albums(artist_id="0TnOYISbd1XYRBk9myaseg",
                                                           include_groups="single,appears_on",
                                                           market="ES",
                                                           limit=10,
                                                           offset=5)
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_status_name, response.reason)
        for attribut in attributes:
            if attribut in response.json():
                self.assertIn(attribut, response.json())
        self.assertIsInstance(response.json()["href"], str)
        self.assertIsInstance(response.json()["limit"], int)
        self.assertIsInstance(response.json()["next"], str)
        self.assertIsInstance(response.json()["offset"], int)
        self.assertIsInstance(response.json()["items"], list)
        self.assertIsInstance(response.json()["items"][0]["id"], str)
        self.assertIsInstance(response.json()["items"][0]["images"], list)
