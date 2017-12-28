# Author: Michael.X, the XX-Net creator
# A simple way to implement i18n. Here are his words:
# I try to read the source code of jinja2 and understand how it works, found out
# that jinja2 is a general template framework, not only for translation.
# Jinja2 can do the work that web_control.py do: generate html from
# index.html/menu.yaml and right content, and more powerful.
# We just need a simple key word/dictionary replacement.
# The standard to define translation is good enough for us, so I keep
# compatible with jinja2 and gettext.
# Also I remove the line comment in po file to keep git clean when we just
# change the line number.
# .pot files removed, too, we don't need them in git.
# We can remove the jinja2 libs if this works fine.

# Usage:
# Any textual file can act as a template file.
# 1. Get the translations ready. See the guide in pybabel_update.sh.
# 2. Calling function render(self, lang_path, template_file)
# returns the rendered template file.

import locale
import os
import sys
import subprocess

# Supports i18n/i10n
global _
global po_dict


class SimpleI18N():
    """
    A simple way to implement i18n without jinja2.

    Manipulates the translations in a dict object."""
    def __init__(self, lang=None):
        if lang:
            self.lang = lang
        else:
            self.lang = self.get_os_language()

    def get_os_language(self):
        try:
            lang_code, code_page = locale.getdefaultlocale()
            #('en_GB', 'cp1252'), en_US,
            self.lang_code = lang_code
            return lang_code
        except:
            #Mac fail to run this
            pass

        if sys.platform == "darwin":
            try:
                oot = os.pipe()
                p = subprocess.Popen(
                    ["/usr/bin/defaults", 'read', 'NSGlobalDomain', 'AppleLanguages'],
                    stdout=oot[1])
                p.communicate()
                lang_code = os.read(oot[0],10000)
                self.lang_code = lang_code
                return lang_code
            except:
                pass

        lang_code = 'Unknown'
        return lang_code

    def po_loader(self, file):
        global po_dict
        po_dict = {}

        fp = open(file, "r")
        while True:
            line = fp.readline()
            if not line:
                break

            if len(line) < 2:
                continue

            if line.startswith("#"):
                continue

            if line.startswith("msgid "):
                key = line[7:-2]
                value = ""
                while True:
                    line = fp.readline()
                    if not line:
                        break

                    if line.startswith("\""):
                        key += line[1:-2]
                    elif line.startswith("msgstr "):
                        value += line[8:-2]
                        break
                    else:
                        break

                while True:
                    line = fp.readline()
                    if not line:
                        break

                    if line.startswith("\""):
                        value += line[1:-2]
                    else:
                        break

                if key == "":
                    continue

                po_dict[key] = value

        return po_dict

    def _render(self, po_dict, file):
        fp = open(file, "r")
        content = fp.read()

        out_arr = []

        cp = 0
        while True:
            bp = content.find("{{", cp)
            if bp == -1:
                break

            ep = content.find("}}", bp)
            if ep == -1:
                print content[bp:]
                break

            b1p = content.find("_(", bp, ep)
            if b1p == -1:
                print content[bp:]
                continue
            b2p = content.find("\"", b1p+2, b1p + 4)
            if b2p == -1:
                print content[bp:]
                continue

            e1p = content.find(")", ep - 2, ep)
            if e1p == -1:
                print content[bp:]
                continue

            e2p = content.find("\"", e1p - 2, e1p)
            if e2p == -1:
                print content[bp:]
                continue

            out_arr.append(content[cp:bp])
            key = content[b2p+1:e2p]
            if key not in po_dict or po_dict[key] == "":
                out_arr.append(key)
            else:
                out_arr.append(po_dict[key])

            cp = ep + 2

        out_arr.append(content[cp:])

        return "".join(out_arr)

    def render(self, lang_path, template_file):
        """Renders a template file

        Translate with the provided language path from which to load
        the translations."""
        po_file = os.path.join(lang_path, self.lang, "LC_MESSAGES", "messages.po")
        if not os.path.isfile(po_file):
            return self._render(dict(), template_file)
        else:
            po_dict = self.po_loader(po_file)
            return self._render(po_dict, template_file)

    def render_message(self, input_msg):
        """Renders a single message."""
        rendered_msg = po_dict[input_msg]
        return rendered_msg


if __name__ == '__main__':
    """Works as tests. See the console for the translated output."""
    # Test cases. If not found, en_US is used instead.
    # Language_contry code list: 
    # http://www.fincher.org/Utilities/CountryLanguageList.shtml
    # Note: An underscore (underline) is used instead of a hyphen.
    #desired_lang = "de_DE" # Germany-Geman
    desired_lang = "en_US" # American-English
    #desired_lang = "es_VE" # Venezuelan-Spanish
    #desired_lang = "fa_IR" # Iran-Persian
    #desired_lang = "fr_FR" # France-French
    #desired_lang = "ja_JP" # Japan-Japanese
        
    # Creates a renderer object
    si18n = SimpleI18N(desired_lang)
    
    # Renders a file
    #print("--- templates/index.html ---")
    current_path = os.path.dirname(os.path.abspath(__file__))
    locale_dir = os.path.abspath(os.path.join(current_path, 'lang'))
    #template_file = os.path.abspath(os.path.join(current_path, 'templates',
    #                                             "index.html"))
    #print(si18n.render(locale_dir, template_file))

    # Renders a single message
    # Populates the global po_dict    
    po_file = os.path.join(locale_dir, desired_lang, "LC_MESSAGES",
                           "messages.po")
    si18n.po_loader(po_file)
    
    _ = si18n.render_message
    #rendered_msg = si18n.render_message("*** ping tests started ***")
    print(_("*** ping tests started ***"))

    # The simplified Chinese
    desired_lang = "zh_CN"
    po_file = os.path.join(locale_dir, desired_lang, "LC_MESSAGES",
                           "messages.po")
    si18n.po_loader(po_file)
    print(_("*** ping tests started ***"))
