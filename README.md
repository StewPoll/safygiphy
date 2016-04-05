TODO: Add documentation about Sticky class
TODO: Add documentation about Combined class
TODO: Add date of next publication
# SafyGiphy

Safygiphy is an updated Python wrapper for the Giphy API.
Version 1.1.0

Full documentation of the Giphy API is [available here](https://github.com/Giphy/GiphyAPI).

## Installation

Clone Repository
```
python setup.py install
```

OR install with Pip

```
pip install safygiphy
```

## Usage

To use:

```python
import safygiphy
c = safigiphy.Giphy()
r = c.random(tag="success")
# Will return a random GIF with the tag "success"
```

If you have an API token, you can specify it when calling the Giphy object.

```python
import safigiphy
c = safigiphy.Giphy(token=string)
```

If you know the ID of a specific GIF you want to retrieve, you can use the `.gif_by_id` method to get the Gif.
```python
gif = g.gif_by_id("id")
```

If you have multiple IDs you need to get, you can use `gifs_by_id` to get these gifs. You can also use this method to get an individual gif as well, if you supply a single gif.
```python
gifs = g.gifs_by_id("id1","id2"..."idn")
```

For all othe endpoints, simply use the endpoint as the method name. Pythons `__getattr__` and `functools` do the rest for you. Simply specify the endpoint, and any kwargs.

```python
g.translate()
g.search()
g.random()
g.translate()
g.trending()
... Any other endpoints Giphy adds in the future.
```

Using the argument of `fmt="html"` in any calls will be ignored by the wrapper, as it won't work otherwise. 

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

v 1.1.0 - 2016/00/00 - Added Sticky and Combined objects. Added unit tests

v 1.0.3 - 2015/05/28 - Fixed minor issues

v 1.0.2 - 2015/05/27 - Further refinements on the code.

v 1.0.1 - 2015/05/27 - Fixed an issue with gifs_by_id, and improved code.

v 1.0.0 - 2015/05/26 - Initial Commit and Readme

## License
Copyright (c) 2016 Stewart Polley


Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.