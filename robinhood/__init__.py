import six

if six.PY3:
    from .Robinhood import Robinhood
    from . import exceptions
else:
    from robinhood import Robinhood
    from robinhood import exceptions
