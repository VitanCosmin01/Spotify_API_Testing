import unittest

from Spotify.spotify_requests import SpotifyRequests


class TestGetSeveralAlbums(unittest.TestCase):
    """
    Testam suta GET /albums/<ids>
    """
    def setUp(self):
        self.request_handler = SpotifyRequests()

    def test_get_several_albums(self):
        """
        Verificam:
        - status code este 200
        - status code name este OK
        - Numarul de albume din response este acelasi cu nr de ids furnizate in parametrul "ids"
        - Verificam ca sunt 15 piese in primul album
        - verificam ca id-urile fac parte din lista generata ca raspuns
        :return:
        """
        expected_status_code = 200
        ids = "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"
        expected_code_name = "OK"
        expected_album_ids = 3
        expected_tracks_number = 15  # pentru primul album
        response = self.request_handler.get_several_albums(ids, market="ES")    # functioneaza doar daca ii dau si parametrul market
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_code_name, response.reason)
        self.assertEqual(expected_album_ids, len(response.json()["albums"]))
        self.assertEqual(expected_tracks_number, response.json()["albums"][0]["total_tracks"])
        ids_list = list(ids.split(","))
        print(ids_list)
        for album_id in ids_list:
            if album_id in response.json()["albums"]:
                self.assertIn(album_id, response.json()["albums"])





