import safygiphy

"""
Giphy object tests
Tests all (current) endpoints of the Giphy API
"""


def test_gif_by_id():
    g = safygiphy.Giphy()
    res = g.gif_by_id("Z34IiLkiwSbKw")
    assert res["data"]["embed_url"] == "https://giphy.com/embed/Z34IiLkiwSbKw"


def test_gifs_by_id():
    g = safygiphy.Giphy()
    ids = [
        'Hp8jtPPTWiH7O',
        '3o85xJS40GiTYwRLvG',
        'PVhrCQyyGzAru',
        '26BkN3EbWMliJvlsc',
        '3o6gaPlP1ZPn1qr6Ba'
    ]
    res = g.gifs_by_id(ids)
    assert len(res["data"]) == len(ids)


def test_random_no_tag():
    g = safygiphy.Giphy()
    res = g.random()
    assert res["meta"]["status"] == 200


def test_translate():
    g = safygiphy.Giphy()
    res = g.translate(s="Testing my wrapper")
    assert res["meta"]["status"] == 200


def test_format_overwitten():
    """
    The wrapper is designed to ignore any "fmt" arguments, and replace them with fmt="json"
    """
    g = safygiphy.Giphy()
    res = g.random(fmt="html")
    assert type(res) == dict


def test_random_tag():
    g = safygiphy.Giphy()
    res = g.random(tag="random")
    assert res["meta"]["status"] == 200


def test_invalid_method():
    """
    This tests an imaginary function that should return an error message
    """
    g = safygiphy.Giphy()
    res = g.invalid_method()
    assert res['meta']['status'] == 404

"""
Sticky object tests
"""


def test_sticker_search():
    s = safygiphy.Sticky()
    res = s.search(q="cat", limit=100)
    assert res["meta"]["status"] == 200
    assert res["pagination"]["count"] == 100
    assert len(res["data"]) == 100


def test_sticker_random_no_tag():
    s = safygiphy.Sticky()
    res = s.random()
    assert res["meta"]["status"] == 200


def test_sticker_random_tag():
    s = safygiphy.Sticky()
    res = s.random(tag="cats")
    assert res["meta"]["status"] == 200


def test_sticker_trending():
    s = safygiphy.Sticky()
    res = s.trending(limit=10)
    assert res["meta"]["status"] == 200
    assert len(res["data"]) == 10


def test_sticker_translate():
    s = safygiphy.Sticky()
    res = s.translate(s="hungry")
    assert res["meta"]["status"] == 200


def test_sticker_format_override():
    s = safygiphy.Sticky()
    res = s.random(fmt="html")
    assert type(res) == dict
    assert res["meta"]["status"] == 200


def test_sticker_invalid_endpoint():
    s = safygiphy.Sticky()
    res = s.invalid_method()
    assert res['meta']['status'] == 404

"""
Combined object tests
"""


def test_combined_gif_by_id():
    c = safygiphy.Combined()
    res = c.gif.gif_by_id("Z34IiLkiwSbKw")
    assert res["data"]["embed_url"] == "https://giphy.com/embed/Z34IiLkiwSbKw"


def test_combined_gifs_by_id():
    c = safygiphy.Combined()
    ids = [
        'Hp8jtPPTWiH7O',
        '3o85xJS40GiTYwRLvG',
        'PVhrCQyyGzAru',
        '26BkN3EbWMliJvlsc',
        '3o6gaPlP1ZPn1qr6Ba'
    ]
    res = c.gif.gifs_by_id(ids)
    assert len(res["data"]) == len(ids)


def test_combined_random_no_tag():
    c = safygiphy.Combined()
    res = c.gif.random()
    assert res["meta"]["status"] == 200


def test_combined_translate():
    c = safygiphy.Combined()
    res = c.gif.translate(s="Testing my wrapper")
    assert res["meta"]["status"] == 200


def test_combined_format_overwitten():
    """
    The wrapper is designed to ignore any "fmt" arguments, and replace them with fmt="json"
    """
    c = safygiphy.Combined()
    res = c.gif.random(fmt="html")
    assert type(res) == dict


def test_combined_random_tag():
    c = safygiphy.Combined()
    res = c.gif.random(tag="random")
    assert res["meta"]["status"] == 200


def test_combined_invalid_method():
    """
    This tests an imaginary function that should return an error message
    """
    c = safygiphy.Combined()
    res = c.gif.invalid_method()
    assert res["meta"]["status"] == 404
    

def test_combined_sticker_search():
    c = safygiphy.Combined()
    res = c.sticker.search(q="cat", limit=100)
    assert res["meta"]["status"] == 200
    assert res["pagination"]["count"] == 100
    assert len(res["data"]) == 100


def test_combined_sticker_random_no_tag():
    c = safygiphy.Combined()
    res = c.sticker.random()
    assert res["meta"]["status"] == 200


def test_combined_sticker_random_tag():
    c = safygiphy.Combined()
    res = c.sticker.random(tag="cats")
    assert res["meta"]["status"] == 200


def test_combined_sticker_trending():
    c = safygiphy.Combined()
    res = c.sticker.trending(limit=10)
    assert res["meta"]["status"] == 200
    assert len(res["data"]) == 10


def test_combined_sticker_translate():
    c = safygiphy.Combined()
    res = c.sticker.translate(s="hungry")
    assert res["meta"]["status"] == 200


def test_combined_sticker_format_override():
    c = safygiphy.Combined()
    res = c.sticker.random(fmt="html")
    assert type(res) == dict
    assert res["meta"]["status"] == 200


def test_combined_sticker_invalid_endpoint():
    c = safygiphy.Combined()
    res = c.sticker.invalid_method()
    assert res['meta']['status'] == 404
