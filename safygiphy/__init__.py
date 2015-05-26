#Basic API wrapper for the Giphy API. Written by TetraEtc
#This software is free to use for non-commercial purposes.
#Uses __getattr__ blackmagic to perform all calls, except the get_by_id calls.

__author__ = 'Stewart Polley'

import requests
import json
import urllib
import functools

version = "v1" #Current version of the Giphy API
base_url = "http://api.giphy.com/{}/gifs".format(version)



class Giphy(object):

    def __init__(self, token="dc6zaTOxFJmzC"):
        """
        Initialises your connection.
        :param token: Your API Token. If none supplied, usesthe Public API Key
        :return:
        """
        self.token=token

    def __str__(self):
        """
        Random String method, cause why not?
        :return: String describing the connection
        """
        if self.token == "dc5zaTOxFJmzc":
            return "Giphy API Connection using the public API token."
        else:
            return "Giphy API Connection using the token: {}".format(self.token)

    def Post(self, endpoint=None, **kwargs):
        """
        Global command to post.
        :param endpoint: Endpoint that is going to be used to make the call. GifsByID has no endpoint, GifByID simply
        uses the ID as the endpoint. These methods are hardcoded though.
        :param kwargs: Options - Options for the call, such as Rating, Format and Search terms.
        :return: Returns the result of the call
        """
        global base_url

        if kwargs:
            params = urllib.urlencode(kwargs)
            url = "{}{}?api_key={}&{}".format(base_url,endpoint,self.token,params)
        else:
            url = "{}{}?api_key={}".format(base_url,endpoint,self.token)

        result = requests.get(url)
        return json.loads(result.text)


    def gif_by_id(self, id):
        """
        Retrieves a specific GIF
        :param id: string -> ID of the GIF you wish to retrieve
        :return: GIF object
        """
        # Simplest call.
        return self.Post(endpoint="/"+id)


    def gif_by_id(self, ids):
        """
        Retrieves a specific set of GIFs
        :param id: list -> List of the IDs you want to get
        :return: Multi-Part GIF object.
        """
        # Relace is used in the following line to remove commas and qoutation marks
        return self.Post(endpoint="?ids="+str(id)[1:-1].replace("'","").replace(" ",""))


    def __getattr__(self, attr):
        """
        All other calls are much simpler, and done with this.
        :param attr: The endpoint of the call
        :return: Gif object
        """
        endpoint = "/{}".format(attr) # Appends the / to the URL
        return functools.partial(self.Post, endpoint) # calls the Post function





