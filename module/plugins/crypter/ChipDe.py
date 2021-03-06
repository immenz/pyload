# -*- coding: utf-8 -*-

import re
from module.plugins.Crypter import Crypter


class ChipDe(Crypter):
    __name__    = "ChipDe"
    __type__    = "crypter"
    __version__ = "0.10"

    __pattern__ = r'http://(?:www\.)?chip\.de/video/.+\.html'
    __config__  = [("use_subfolder", "bool", "Save package to subfolder", True),
                   ("subfolder_per_package", "bool", "Create a subfolder for each package", True)]

    __description__ = """Chip.de decrypter plugin"""
    __license__     = "GPLv3"
    __authors__     = [("4Christopher", "4Christopher@gmx.de")]


    def decrypt(self, pyfile):
        self.html = self.load(pyfile.url)
        try:
            f = re.search(r'"(http://video\.chip\.de/.+)"', self.html)
        except Exception:
            self.fail(_("Failed to find the URL"))
        else:
            self.urls = [f.group(1)]
            self.logDebug("The file URL is %s" % self.urls[0])
