import unittest
import timeit

from Spotify.spotify_requests import SpotifyRequests


class TestGetSeveralArtists(unittest.TestCase):

    def setUp(self):
        self.request_handler = SpotifyRequests()

    def test_get_several_artists(self):
        """
        Verificam:
        - status code este 200
        - status code name este OK
        - performanta testului
        - verificam ca fiecare artist_id se afla in raspunsul json
        - verificam daca in raspuns avem tot atatea ids cate am furnizat
        :return:
        """
        expected_status_code = 200
        expected_status_name = "OK"
        artists_ids = "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"
        expected_no_of_ids = 3
        start_time = timeit.default_timer()
        response = self.request_handler.get_several_artists(ids=artists_ids)
        end_time = timeit.default_timer()
        print(f"Timpul de execuție este {end_time - start_time} secunde.")
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_status_name, response.reason)
        artists_ids_list = artists_ids.split(",")
        for artist_id in artists_ids_list:
            if artist_id in response.json()["artists"]:
                self.assertIn(artists_ids, response.json()["artists"])
        self.assertEqual(expected_no_of_ids, len(response.json()["artists"]))



