import requests
import urllib
import functools

version = "v1" #Current version of the Giphy API
base_url = "http://api.giphy.com/{}/gifs".format(version)
public_token="dc6zaTOxFJmzC"


class Giphy(object):

    def __init__(self, token=public_token):
        """
        Initialises your connection.
        :param token: Your API Token. If none supplied, usesthe Public API Key
        :return:
        """
        self.token=token

    def __str__(self):
        global public_token
        """
        Random String method, cause why not?
        :return: String describing the connection
        """
        if self.token == public_token:
            return "Giphy API Connection using the public API token."
        else:
            return "Giphy API Connection using the token: {}".format(self.token)

    def Post(self, endpoint = None, **kwargs):
        """
        Global command to post.
        :param endpoint: Endpoint that is going to be used to make the call. GifsByID has no endpoint, GifByID simply
        uses the ID as the endpoint. These methods are hardcoded though.
        :param kwargs: Options - Options for the call, such as Rating, Format and Search terms.
        :return: Returns the result of the call
        """
        global base_url
        if endpoint:
            if kwargs:
                if "fmt" in kwargs: # Don't try to change the format or you'll break stuff!
                    kwargs["fmt"]="json"
                params = urllib.urlencode(kwargs)
                url = "{}{}?api_key={}&{}".format(base_url,endpoint,self.token,params)
            else:
                url = "{}{}?api_key={}".format(base_url,endpoint,self.token)
        else:
            if "fmt" in kwargs:
                kwargs["fmt"]="json"
            params = urllib.urlencode(kwargs)
            url = "{}?api_key={}&{}".format(base_url,self.token,params)
        print url
        result = requests.get(url)
        return result.json()


    def gif_by_id(self, id):
        """
        Retrieves a specific GIF
        :param id: string -> ID of the GIF you wish to retrieve
        :return: GIF object
        """
        # Simplest call.
        return self.Post(endpoint="/"+id)


    def gifs_by_id(self, *ids):
        """
        Retrieves a specific set of GIFs
        :param id: list -> List of the IDs you want to get
        :return: Multi-Part GIF object.
        """
        return self.Post(ids=','.join(ids))


    def __getattr__(self, attr):
        """
        All other calls are much simpler, and done with this.
        :param attr: The endpoint of the call
        :return: Gif object
        """
        endpoint = "/{}".format(attr) # Appends the / to the URL
        return functools.partial(self.Post, endpoint) # calls the Post function





