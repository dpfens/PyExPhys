import balance
import cardio
import composition
import mets
import model
import sport
import  strength

def get_include():
    """
    Extension modules that need to compile against PyFit should use this
    function to locate the appropriate include directory.
    Notes
    -----
    When using ``distutils``, for example in ``setup.py``.
    ::
        import pyfit
        ...
        Extension('extension_name', ...
                include_dirs=[pyfit.get_include()])
        ...
    """
    import pyfit
    import os
    dir_name = os.path.dirname(pyfit.__file__)
    d = os.path.join(os.path.dirname(dir_name))
    return d
