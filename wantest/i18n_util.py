# -*- coding: utf-8 -*-
# Ref 1: http://oz123.github.io/writings/2013-08-04-Localizing-with-gettext/
# Ref 2: https://wiki.maemo.org/Internationalize_a_Python_application
# A simplified version based on hello_gettext.py

# 0. Create the folder structure
# mkdir -pv lang/{de_DE,en_US,zh_CN}/LC_MESSAGES/

# 1. Create the template (domain_name = wantest)
# xgettext -k_ -kN_ -o lang/messages.pot wantest_main.py (a single file)
# xgettext -k_ -kN_ -o lang/messages.pot -f files-need-i10n.txt (file list)

# 2. Translate the template to different locales
# 2.1 Init
# msginit --input=lang/messages.pot --locale=en_US
#         --output=lang/en_US/LC_MESSAGES/messages.po
# msginit --input=lang/messages.pot --locale=zh_CN
#         --output=lang/zh_CN/LC_MESSAGES/messages.po
# 2.2 Update(python-pybabel needs to be installed!)
# pybabel update -l en_US -d ./lang -i ./lang/messages.pot
# pybabel update -l zh_CN -d ./lang -i ./lang/messages.pot
#
# 3. Compile the translations files
# msgfmt lang/en_US/LC_MESSAGES/messages.po -o lang/en_US/LC_MESSAGES/messages.mo
# msgfmt lang/zh_CN/LC_MESSAGES/messages.po -o lang/zh_CN/LC_MESSAGES/messages.mo

# 4. msgfmt "invalid multibyte sequence" error (*IMPORTANT)
# Edit zh_CN *.po file and change the Content-Type line to
# "Content-Type: text/plain; charset=UTF-8\n"
# (Changing the charset from ASCII to UTF-8)

import os
import sys
import locale
import gettext

# The shorthand for the translation method
global _
# Determines the language path (the i10n path), ./lang,
# to load the correct language
current_path = os.path.dirname(os.path.abspath(__file__))
#print("The current path: %s" % current_path)


def get_default_locale():
    # https://wiki.maemo.org/Internationalize_a_Python_application
    # Get the default locale, e.g., ['en_US', 'UTF-8']
    # lang_encoding = os.environ.get('LANG', '').split('.')
    # Linux/Unix only
    # tuple, e.g., ('en_US', 'UTF-8')
    default_locale, encoding = locale.getdefaultlocale()
    return default_locale


class I18NUtil(object):
    """An i18n utility class"""

    def __init__(self, domain_name, locale_dir, default_lang='en_US'):
        self.domain_name = domain_name
        self.locale_dir = locale_dir        
        self.default_lang = default_lang
        self.install()

    # http://www.wefearchange.org/2012/06/the-right-way-to-internationalize-your.html
    # Perhaps more usefully, you can use the gettext.install() function to put
    # _() into the built-in namespace,
    # so that all your other code can just use that function without doing
    # anything special.
    # Again, though we have to work around the boneheaded Python 2 API.  
    # Here's how to write code which works correctly in both Python 2 and 3.
    def install(self):
        kwargs = {}
        if sys.version_info[0] < 3:
            # In Python 2, ensure that the _() that gets installed into
            # built-ins always returns unicodes. This matches the default
            # behavior under Python 3, although that keyword argument is not
            # present in the Python 3 API.
            kwargs['unicode'] = True
        gettext.install(self.domain_name, **kwargs)


    def set_language(self, language='en_US'):
        t = gettext.translation(self.domain_name,
                                self.locale_dir, [language])
        global _ # or only the default locale used
        _ = t.ugettext


def test_me():
    print(_("*** ping tests started ***"))


# Tests with en_US, de_DE, and zh_CN
if __name__ == '__main__':
    locale_dir = os.path.join(current_path, 'lang')
    i18nu = I18NUtil(domain_name="messages", locale_dir=locale_dir,
                     default_lang='en_US')
    
    # The default language: en_US
    i18nu.set_language()
    test_me()

    default_lang = get_default_locale()
    i18nu.set_language(default_lang)
    test_me()
    
    i18nu.set_language('zh_CN')     
    test_me()
