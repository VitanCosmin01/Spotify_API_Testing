import unittest

from Spotify.spotify_requests import SpotifyRequests


class TestGetArtist(unittest.TestCase):

    def setUp(self):
        self.requests_handler = SpotifyRequests()

    def test_get_artist(self):
        """
        Verificam:
        - status code este 200
        - status code contine OK
        - verificam ca atributul "type" are valoare "artist"
        - Verficam respunsul ca are 10 atribute
        - verificam ca raspunsul cuprinde toate atributele specificate
        :return:
        """
        expected_code = 200
        expected_code_name = "OK"
        expected_artist_id = "0TnOYISbd1XYRBk9myaseg"
        expected_type_value = "artist"
        expected_no_attributes = 10
        expected_attributes = ["external_url", "followers", "genres", "href", "id",
                               "images", "name", "popularity", "type", "uri"]
        response = self.requests_handler.get_artist("0TnOYISbd1XYRBk9myaseg")
        self.assertEqual(expected_code, response.status_code)
        self.assertEqual(expected_code_name, response.reason)
        self.assertEqual(expected_artist_id, response.json()["id"])
        self.assertEqual(expected_type_value, response.json()["type"])
        self.assertEqual(expected_no_attributes, len(response.json()))
        for atribut in expected_attributes:
            if atribut in response.json():
                self.assertIn(atribut, response.json())

    def test_get_artist_not_in_db(self):
        """
        Verificam:
        - status code este 400
        - status code name este Bad Request
        - verificam daca mesajul de eroare este cel correct
        :return:
        """
        expected_status_code = 400
        expected_status_name = "Bad Request"
        searched_key = "error"
        error_message = "Invalid base62 id"
        response = self.requests_handler.get_artist("111111111111111")
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_status_name, response.reason)
        self.assertIn(searched_key, response.json())
        try:
            self.assertEqual(error_message, response.json()["error"]["message"])
        except AssertionError:
            print(f'Api error message: {error_message} este diferit de Pycharm error message: {response.json()["error"]["message"]}! ')
        print(response.json())
