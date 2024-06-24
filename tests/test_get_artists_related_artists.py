import unittest
import time

from Spotify.spotify_requests import SpotifyRequests


class TestGetArtistsRelatedArtists(unittest.TestCase):

    def setUp(self):
        self.request_handler = SpotifyRequests()

    def test_get_artists_related_artists(self):
        """
        Verificam:
        - status code este 200
        - status code name este "OK"
        - performanta request-ului
        - prezenta cheii 'artists'
        - cheia 'artists' are o valoare de tip lista
        - cheia 'total' este de tip numeric
        - cheia 'followers' este de tip dictionar
        - verificam faptul ca fiecare artist este descris de atributele corecte
        :return:
        """
        expected_status_code = 200
        expected_status_name = "OK"
        searched_key = "artists"
        expected_no_of_attributes_first_artist = 10
        list_of_attributes = ["external_urls", "followers", "genres", "href", "id", "images", "name", "popularity", "type", "uri"]
        start_time = time.time()
        response = self.request_handler.get_artists_related_artists(artist_id="0TnOYISbd1XYRBk9myaseg")
        end_time = time.time()
        lasting_time = (end_time - start_time) * 1000
        print(lasting_time)
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_status_name, response.reason)
        self.assertIn(searched_key, response.json())
        self.assertIsInstance(response.json()["artists"], list)
        self.assertIsInstance(response.json()["artists"][0]["followers"]["total"], int)
        self.assertIsInstance(response.json()["artists"][0]["followers"], dict)
        self .assertEqual(expected_no_of_attributes_first_artist, len(response.json()["artists"][0]))
        for artist in response.json()["artists"]:
            for attribut in list_of_attributes:
                if attribut in artist:
                    self.assertIn(attribut, artist)

    def test_get_artists_related_artists_with_invalid_id(self):
        """
        Verificam:
        - status code este 400
        - status code name este Bad Request
        - prezenta cheii "error"
        - mesajul de eroare este cel asteptat
        :return:
        """
        expected_status_code = 400
        expected_status_name = "Bad Request"
        key_error = "error"
        expected_error_message = "Invalid base62 id"
        response = self.request_handler.get_artists_related_artists(artist_id="111111111111111")
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_status_name, response.reason)
        self.assertIn(key_error, response.json())
        try:
            self.assertEqual(expected_error_message, response.json()["error"]["message"])
        except AssertionError:
            print(f' Mesajul API: {expected_error_message} este diferit de cel redat de cod: {response.json()["error"]["message"]}')

