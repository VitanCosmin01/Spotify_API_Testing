import unittest
import HtmlTestRunner

from tests.test_get_album import TestGetAlbum
from tests.test_get_several_albums import TestGetSeveralAlbums
from tests.test_get_album_track import TestGetAlbumTracks
from tests.test_get_artist import TestGetArtist
from tests.test_get_several_artists import TestGetSeveralArtists
from tests.test_get_artists_albums import TestGetArtistsAlbums
from tests.test_get_artists_top_tracks import TestGetArtistsTopTracks
from tests.test_get_artists_related_artists import TestGetArtistsRelatedArtists


class TestSuite(unittest.TestCase):

    def test_suite(self):
        tests_to_run = unittest.TestSuite()

        tests_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetAlbum),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetSeveralAlbums),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetAlbumTracks),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetArtist),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetSeveralArtists),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetArtistsAlbums),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetArtistsTopTracks),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetArtistsRelatedArtists)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,  # daca avem mai multe clase de test, rezultatele vor fi puse in acelasi raport
            report_title='TestReport',
            report_name='Spotify Test Result'
           )

        runner.run(tests_to_run)

