import requests
from requests_oauth2client import *


class SpotifyRequests:

    TOKEN_ENDPOINT = "https://accounts.spotify.com/api/token"
    REDIRECT_URI = "https://localhost:3000/"
    CLIENT_ID = "ed3c2eb5e6cf4694a49af1b6554bea9a"
    CLIENT_SECRET = "5ade79a0421843b484b0c9de0af0b496"
    AUTH_CREDENTIALS = (CLIENT_ID, CLIENT_SECRET)
    BASE_URL = "https://api.spotify.com/v1"

    def __init__(self):
        self.token = self.__get_token()

    def __get_token(self):
        oauth_client = OAuth2Client(token_endpoint=self.TOKEN_ENDPOINT, auth=self.AUTH_CREDENTIALS)
        return oauth_client.client_credentials(resource=self.REDIRECT_URI)

    # se implementeaza ENDPOINT-ul https://api.spotify.com/v1/albums/{id}
    def get_album(self, album_id, market=None):
        album_url = f'{self.BASE_URL}/albums/{album_id}'
        query_params = {}
        if market is not None:
            query_params.update({"market": market})
        response = requests.get(url=album_url,
                                params=query_params,
                                headers={"Authorization": f"Bearer {self.token}"})
        return response

    # ENDPOINT
    # https://api.spotify.com/v1/albums
    def get_several_albums(self, ids, market=None):
        several_albums_url = f'{self.BASE_URL}/albums'
        query_params = {"ids": ids}
        if market is not None:
            query_params.update({"market": market})
            response = requests.get(url=several_albums_url,
                                    params=query_params,
                                    headers={"Authorization": f"Bearer {self.token}"})
            return response

    # def get_album_tracks(self, id, limit=None, offset=None, market=None):
    #     album_tracks_url = f"{self.BASE_URL}/albums/{id}/tracks"
    #     query_params = {}
    #     if limit is not None:
    #         query_params.update({"limit": limit})
    #     if offset is not None:
    #         query_params.update({"offset": offset})
    #     if market is not None:
    #         query_params.update({"market": market})
    #     response = requests.get(url=album_tracks_url,
    #                             params=query_params,
    #                             headers={"Authorization": f'Bearer {self.token}'})
    #     return response

    # ENDPOINT
    # https: // api.spotify.com / v1 / albums / {id} / tracks
    def get_album_tracks(self, id, **kwargs):
        album_tracks_url = f"{self.BASE_URL}/albums/{id}/tracks"
        query_params = {"id": id}
        query_params.update(**kwargs)
        response = requests.get(url=album_tracks_url, params=query_params, headers={"Authorization": f'Bearer {self.token}'})
        return response

    # ENDPOINT
    # https: // api.spotify.com / v1 / artists / {id}
    def get_artist(self, artist_id):
        artist_url = f'{self.BASE_URL}/artists/{artist_id}'
        response = requests.get(url=artist_url,
                                headers={"Authorization": f'Bearer {self.token}'})
        return response
    # ENDPOINT
    # https://api.spotify.com/v1/artists
    def get_several_artists(self, ids):
        url = f'{self.BASE_URL}/artists'
        query_params = {"ids": ids}
        response = requests.get(url=url,
                                params=query_params,
                                headers={"Authorization": f'Bearer {self.token}'})
        return response

    # def get_artists_albums(self, artist_id, include_groups, market, limit, offset):
    #     url = f'{self.BASE_URL}/artists/{artist_id}/albums'
    #     query_params = {"id": artist_id}
    #     if include_groups is not None:
    #         query_params.update({"include_groups": include_groups})
    #     if market is not None:
    #         query_params.update({"market": market})
    #     if limit is not None:
    #         query_params.update({"limit": limit})
    #     if offset is not None:
    #         query_params.update({"offset": offset})
    #     response = requests.get(url=url,
    #                             params=query_params,
    #                             headers={"Authorization": f"Bearer {self.token}"})
    #     return response
    # ENDPOINT
    # https://api.spotify.com/v1/artists/{id}/albums
    "O varianta in care folosesc ca parametru **kwargs"
    def get_artists_albums(self, artist_id, **kwargs):
        url = f'{self.BASE_URL}/artists/{artist_id}/albums'
        query_params = {"artist_id": artist_id, **kwargs}
        response = requests.get(url=url, params=query_params, headers={"Authorization": f"Bearer {self.token}"})
        return response

    # ENDPOINT
    # https://api.spotify.com/v1/artists/{id}/top-tracks
    def get_artists_top_tracks(self, artist_id, market):
        # market nu este un parametru obligatoriu in documentatia API, dar se comporta ca si cum ar fi
        url = f'{self.BASE_URL}/artists/{artist_id}/top-tracks'
        query_params = {"market": market}
        response = requests.get(url=url,
                                params=query_params,
                                headers={"Authorization": f'Bearer {self.token}'})
        return response

    # ENDPOINT
    # https://api.spotify.com/v1/artists/{id}/related-artists
    def get_artists_related_artists(self, artist_id):
        url = f'{self.BASE_URL}/artists/{artist_id}/related-artists'
        response = requests.get(url=url, headers={"Authorization": f'Bearer {self.token}'})
        return response


obj1 = SpotifyRequests()

# token = obj1.token
# print(token)

# print(obj1.get_several_albums("382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"))
# print(obj1.get_album("4aawyAB9vmqN3uQ7FjRGTy"))
