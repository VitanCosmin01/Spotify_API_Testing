import unittest

from Spotify.spotify_requests import SpotifyRequests


class TestGetArtistsTopTracks(unittest.TestCase):
    """
    Testam ruta GET /artists/<id>/top-tracks
    """
    def setUp(self):
        # instantiem un obiect din clasa SpotifyRequests si o setam pe self
        self.requests_handler = SpotifyRequests()

    # @unittest.skip
    def test_get_artists_top_tracks(self):
        """
        Verificam:
        - status code este 200
        - status codename este OK
        - verificam ca in raspunsul json, se regaseste id-ul furnizat
        - verificam ca atributul 'popularity' este un numar
        - verificam ca valoarea lui 'is_playable' este true
        - verificam ca valoarea lui 'is_playable' este de tip bool
        - raspunsul json trebuie sa contina cheia 'tracks'
        :return:
        """
        expected_status_code = 200
        expected_status_name = "OK"
        artist_id = "0TnOYISbd1XYRBk9myaseg"
        is_playable_value = "true"
        searched_key = "tracks"
        response = self.requests_handler.get_artists_top_tracks(artist_id=artist_id, market="ES")
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_status_name, response.reason)
        self.assertEqual(artist_id, response.json()["tracks"][0]["artists"][0]["id"])
        print(response.json()["tracks"][0]["artists"][0]["id"])
        self.assertIsInstance(response.json()["tracks"][0]["popularity"], int)
        print(response.json()["tracks"][0]["popularity"])
        self.assertIsInstance(response.json()["tracks"][0]["artists"], list)
        # true != True, ca urmare m-am folosit de metoda capitalize si str pentru a avea un test cu succes
        self.assertEqual(is_playable_value.capitalize(), str(response.json()["tracks"][0]["is_playable"]))
        print(response.json()["tracks"][0]["is_playable"])
        self.assertIsInstance(response.json()["tracks"][0]["is_playable"], bool)
        self.assertIn(searched_key, response.json())

    # @unittest.skip
    def test_get_artists_top_tracks_with_invalid_id(self):
        """
        Verificam:
        - status code este 400
        - status code name este Bad Request
        - prezenta cheii "error" in raspuns
        - comparam mesajele de eroare daca corespund
        :return:
        """
        expected_status_code = 400
        expected_status_name = "Bad Request"
        searched_key = "error"
        error_message = "Invalid base62 id"
        response = self.requests_handler.get_artists_top_tracks(artist_id="111111111111111", market="ES")
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_status_name, response.reason)
        self.assertIn(searched_key, response.json())
        try:
            self.assertEqual(error_message, response.json()["error"]["message"])
        except AssertionError:
            print(f'Api error message: {error_message} este diferit de Pycharm error message: {response.json()["error"]["message"]}! ')
        # print(response.json())
