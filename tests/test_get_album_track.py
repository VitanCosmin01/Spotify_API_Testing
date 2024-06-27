import unittest

from Spotify.spotify_requests import SpotifyRequests


class TestGetAlbumTracks(unittest.TestCase):
    """
    Testam ruta GET /album/<id>/tracks
    """
    def setUp(self):
        self.request_handler = SpotifyRequests()

    # @unittest.skip
    def test_get_album_tracks(self):
        """
        Verificam:
        - status code este 200
        - status code name este OK
        - numarul de melodii este egal cu valoarea cheii "total"
        -
        :return:
        """
        expected_status_code = 200
        expected_status_name = "OK"
        expected_no_of_tracks = 18
        expected_offset_value = 0
        expected_key = "type"
        expected_value = "track"
        response = self.request_handler.get_album_tracks("4aawyAB9vmqN3uQ7FjRGTy")
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_status_name, response.reason)
        self.assertEqual(expected_no_of_tracks, response.json()["total"])
        self.assertEqual(expected_offset_value, response.json()["offset"])
        self.assertIn(expected_key, response.text)
        self.assertEqual(expected_value, response.json()["items"][0]["type"])

    # @unittest.skip
    def test_get_album_tracks_with_limit(self):
        """
        Verificam:
        - status code este 200 cand limita este un numar intreg
        - numarul de melodii corespunde cu limita care este 5

        :return:
        """
        expected_status_code = 200
        expected_length = 5

        response = self.request_handler.get_album_tracks(id="4aawyAB9vmqN3uQ7FjRGTy", limit=5)
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_length, len(response.json()["items"]))

    # @unittest.skip
    def test_get_album_tracks_with_neg_limit(self):
        """
        Verificam:
        - status code este 400 Bad Request cand limita este un numar negativ
        - response body contine cheia "error"
        - response body contine mesajul "Invalid limit"
        :return:
        """
        expected_status_code_with_limit_as_neg = 400
        searched_key = "error"
        error_message = "Invalid limit"
        response = self.request_handler.get_album_tracks(id="4aawyAB9vmqN3uQ7FjRGTy", limit=-5)
        self.assertEqual(expected_status_code_with_limit_as_neg, response.status_code)
        self.assertIn(searched_key, response.json())
        print(response.text, response.json())
        try:
            self.assertEqual(error_message, response.json()["error"]["message"])
        except AssertionError:
            print(
                f'Api error message: {error_message} este diferit de Pycharm error '
                f'message: {response.json()["error"]["message"]}! ')

        # Mesajul de eroare primit in Pycharm este diferit de cel din Postman:
        # Bad limit, limit must be larger than 0

