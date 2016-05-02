import functools
import requests
import sys # Sys needed to determine python version
if sys.version_info[0] == 3:
    from urllib.parse import urlencode
else:
    from urllib import urlencode


version = "v1" #Current version of the Giphy API
base_url = "http://api.giphy.com/{0}/".format(version)
upload_url = "http://upload.giphy.com/{0}/".format(version)
public_token = "dc6zaTOxFJmzC"


class Giphy(object):
    def __init__(self, token=public_token):
        """
        Object that handles making GIF related calls
        :param token: Your GIF API Token. If none supplied, uses the Public GIF API Key
        :return:
        """
        global base_url
        self.token=token
        self.base = base_url + "gifs"


    def Post(self, endpoint = None, **kwargs):
        """
        Function that handles all calls for GIFs
        :param endpoint: Endpoint that is going to be used to make the call. GifsByID has no endpoint, GifByID simply
        uses the ID as the endpoint. These methods are hardcoded though.
        :param kwargs: Options - Options for the call, such as Rating and Search terms.
        :return: Returns the result of the call
        """
        if endpoint:
            if kwargs:
                if "fmt" in kwargs:
                    del(kwargs["fmt"])
                params = urlencode(kwargs)
                url = "{0}{1}?api_key={2}&{3}".format(self.base,endpoint,self.token,params)
            else:
                url = "{0}{1}?api_key={2}".format(self.base,endpoint,self.token)
        else:
            if "fmt" in kwargs:
                kwargs["fmt"]="json"

            params = urlencode(kwargs)
            url = "{0}?api_key={1}&{2}".format(self.base,self.token,params)
        result = requests.get(url)
        return result.json()

    def gif_by_id(self, id):
        """
        Retrieves a specific GIF
        :param id: string -> ID of the GIF you wish to retrieve
        :return: GIF object
        """
        # Simplest call.
        return self.Post(endpoint="/{0}".format(id))

    def gifs_by_id(self, ids):
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
        endpoint = "/{0}".format(attr) # Appends the / to the URL
        return functools.partial(self.Post, endpoint) # calls the Post function


class Sticky(object):
    def __init__(self, token=public_token):
        """
        Object that handles making STICKER related calls
        :param token: Your STICKER API Token. If none supplied uses the Public STICKER API Key
        :return:
        """
        global base_url
        self.token = token
        self.base = base_url + "stickers"

    def Post(self, endpoint = None, **kwargs):
        """
        Function that handles all calls for STICKERS
        :param endpoint: str - The chosen endpoint used to make the call
        :param kwargs: Options - Options for the call, such as Rating, Search Term, Tags etc
        :return: dict - Returns the result of the call
        """
        # TODO: Check if there's a STICKER endpoint that uses the base URL
        # TODO: Check if there's any options that we don't want to send out!
        if endpoint:
            if kwargs:
                if "fmt" in kwargs:
                    del(kwargs["fmt"])
                params = urlencode(kwargs)
                # TODO: Ensure this is a valid URL pattern
                url = "{0}{1}?api_key={2}&{3}".format(self.base, endpoint, self.token, params)
            else:
                url = "{0}{1}?api_key={2}".format(self.base, endpoint, self.token)
        else:
            params = urlencode(kwargs)
            url = "{0}?api_key={1}&{2}".format(self.base, self.token, params)
        result = requests.get(url)
        return result.json()

    # TODO: Check which API Endpoints need hardcoding, which can use __getattr__
    # TODO: Hardcode any endpoints that need hardcoding!

    def __getattr__(self, attr):
        """
        All calls that don't have hardcoded endpoints use lovely little system
        :param attr: The endpoint of the call
        :return: Sticker object
        """
        endpoint = "/{0}".format(attr)
        return functools.partial(self.Post, endpoint)


class Combined(object):
    def __init__(self, gif_token=public_token, sticker_token=public_token):
        """
        Object that has sub attributes that is capable of making EITHER calls using self.gifs.POST or
        self.stickers.post
        :return:
        """
        self.gif = Giphy(token=gif_token)
        self.sticker = Sticky(token=sticker_token)
