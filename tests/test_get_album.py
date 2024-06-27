import unittest

from Spotify.spotify_requests import SpotifyRequests


class TestGetAlbum(unittest.TestCase):
    """
    Testam ruta GET /album/<id>
    """

    def setUp(self):
        self.requests_handler = SpotifyRequests()

    # @unittest.skip
    def test_get_album(self):
        """
        Verificam:
        - ca status code este 200
        - Verificam ca in raspunsul primit se regaseste cuvantul "total_tracks"
        - Verificam ca in lista "available_markets" din raspuns contine ["RO", "FR", "PL"]
        """
        album_id = "4aawyAB9vmqN3uQ7FjRGTy"
        expected_status_code = 200
        expected_key = "total_tracks"

        response = self.requests_handler.get_album(album_id)
        self.assertEqual(expected_status_code, response.status_code)

        self.assertIn(expected_key, response.json())

        searched_contries = ["RO", "FR", "PL"]
        available_markets = response.json()["available_markets"]
        for countrie in searched_contries:
            if countrie in available_markets:
                # print(countrie, available_markets)
                self.assertIn(countrie, available_markets)

    # @unittest.skip
    def test_get_album_when_market_is_provided(self):
        """
        Verificam:
        - status code eeste 200
        - Verificam ca response body contine cheia "album_type"
        - Cheia available markets dispare din response
        - Verificam ca cheia "id" are valoarea furnizata in link "4aawyAB9vmqN3uQ7FjRGTy"
        :return:
        """
        expected_status_code = 200
        album_id = "4aawyAB9vmqN3uQ7FjRGTy"
        market = "ES"
        response = self.requests_handler.get_album(album_id=album_id, market=market)
        self.assertEqual(expected_status_code, response.status_code)
        #
        response = self.requests_handler.get_album(album_id=album_id, market=market)
        expected_key = "album_type"
        self.assertIn(expected_key, response.json())
        #
        missing_key = "available_markets"
        self.assertNotIn(missing_key, response.json())
        #
        self.assertEqual(album_id, response.json()["id"])


