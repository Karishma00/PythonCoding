# encoding: utf-8
# module markupsafe._speedups
# from /usr/lib/python3/dist-packages/markupsafe/_speedups.cpython-37m-x86_64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# functions

def escape(s): # real signature unknown; restored from __doc__
    """
    escape(s) -> markup
    
    Convert the characters &, <, >, ', and " in string s to HTML-safe
    sequences.  Use this if you need to display text that might contain
    such characters in HTML.  Marks return value as markup string.
    """
    pass

def escape_silent(s): # real signature unknown; restored from __doc__
    """
    escape_silent(s) -> markup
    
    Like escape but converts None to an empty string.
    """
    pass

def soft_unicode(p_object): # real signature unknown; restored from __doc__
    """
    soft_unicode(object) -> string
    
    Make a string unicode if it isn't already.  That way a markup
    string is not converted back to unicode.
    """
    return ""

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f2b68affbe0>'

__spec__ = None # (!) real value is "ModuleSpec(name='markupsafe._speedups', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f2b68affbe0>, origin='/usr/lib/python3/dist-packages/markupsafe/_speedups.cpython-37m-x86_64-linux-gnu.so')"

