#!/bin/sh

# IMPORTANT: This script was created and tested on Ubnutun Linux only!
# To install pybabel, run: sudo apt-get install python-pybabel


# See for these steps at http://tlphoto.googlecode.com/git/jinja2_i18n_howto.txt
# 0. Create the folder structure
#mkdir -pv ./lang/de_DE/LC_MESSAGES/
#mkdir -pv ./lang/en_US/LC_MESSAGES/
#mkdir -pv ./lang/es_VE/LC_MESSAGES/
#mkdir -pv ./lang/fa_IR/LC_MESSAGES/
#mkdir -pv ./lang/ja_JP/LC_MESSAGES/
#mkdir -pv ./lang/fr_FR/LC_MESSAGES/
#mkdir -pv ./lang/zh_CN/LC_MESSAGES/


# 1. Extracts strings in {{ _("string") }} to be translated to file messages.pot (Portable Object Template)
# File babel.config specifies from which files to extract. 
pybabel extract -F babel.config -o lang/messages.pot .


# 2. Initializes/Updates the concrete languaged-related pot file
# Language_contry code list: http://www.fincher.org/Utilities/CountryLanguageList.shtml

# 2.1 Initialize (Once is enough, or all the existing translation will be GONE!)
#pybabel init -l de_DE -d ./lang -i ./lang/messages.pot
#pybabel init -l en_US -d ./lang -i ./lang/messages.pot
#pybabel init -l es_VE -d ./lang -i ./lang/messages.pot
#pybabel init -l fa_IR -d ./lang -i ./lang/messages.pot
#pybabel init -l fr_FR -d ./lang -i ./lang/messages.pot
#pybabel init -l ja_JP -d ./lang -i ./lang/messages.pot
#pybabel init -l zh_CN -d ./lang -i ./lang/messages.pot

# 2.2 Update (Once initialized, the frequent work is to update them in order to keep the existing translation.)
#pybabel update -l de_DE -d ./lang -i ./lang/messages.pot
#pybabel update -l en_US -d ./lang -i ./lang/messages.pot
#pybabel update -l es_VE -d ./lang -i ./lang/messages.pot
#pybabel update -l fa_IR -d ./lang -i ./lang/messages.pot
#pybabel update -l fr_FR -d ./lang -i ./lang/messages.pot
#pybabel update -l ja_JP -d ./lang -i ./lang/messages.pot
pybabel update -l zh_CN -d ./lang -i ./lang/messages.pot

# 2.3 Optional: clean up the po files to strip the commentary to reduce the
# file size. (Contributed by Michael.X at https://github.com/xx-net)
#sed -i -e '/#.*$/d'  lang/de_DE/LC_MESSAGES/messages.po
#sed -i -e '/#.*$/d'  lang/en_US/LC_MESSAGES/messages.po
#sed -i -e '/#.*$/d'  lang/es_VE/LC_MESSAGES/messages.po
#sed -i -e '/#.*$/d'  lang/fa_IR/LC_MESSAGES/messages.po
#sed -i -e '/#.*$/d'  lang/ja_JP/LC_MESSAGES/messages.po
#sed -i -e '/#.*$/d'  lang/zh_CN/LC_MESSAGES/messages.po


# 3. Compiles the *.po (Portable Object) files after they're translated.
# If module simple_i18n.py is used, the step is not needed at all.
# 3.1 Use command msgfmt to compile one by one
#msgfmt lang/zh_CN/LC_MESSAGES/messages.po -o lang/zh_CN/LC_MESSAGES/messages.mo 
# 3.2 Use pybabel to compile all with a single command (recommended)
#pybabel compile -f -d ./lang
