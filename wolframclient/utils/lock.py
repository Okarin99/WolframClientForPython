from __future__ import absolute_import, print_function, unicode_literals

import warnings

try:
    import multithreading

    _lock = multithreading.Lock()

    def Lock():
        return _lock


except (ImportError, OSError):

    # JYTHON is raising an ImportError when running "import multithreading"
    # GVisor is raising an OSError when running "multithreading.Lock()" because the feature is not implemented

    from contextlib import contextmanager

    @contextmanager
    def Lock():
        warnings.warn("Lock is not implemented in the current interpreter.", RuntimeWarning)
        yield
