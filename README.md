# Project Name

Safygiphy is an updated Python wrapper for the Giphy API.

## Installation

Clone Repository
```
python setup.py install
```

PyPi registration is coming... soon(tm)

## Usage

To use:

```python
import safigiphy
c = safigiphy.Giphy()
r = c.random(tag="success")
# Will return a random GIF with the tag "success"
```

If you have an API token, you can specify it when calling the Giphy object.

```python
import safigiphy
c = safigiphy.Giphy(token=string)
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

2015/05/26 - Initial Commit and Readme

## Credits

Initial Author: TetraEtc (administrator@tetraetc.com)
