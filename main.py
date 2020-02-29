# -*- coding: utf-8 -*-

from resources.lib import kodilogging
from resources.lib import script

import logging
import xbmcaddon

import os

# Keep this file to a minimum, as Kodi
# doesn't keep a compiled copy of this
ADDON = xbmcaddon.Addon()
kodilogging.config()

os.system('parsecd')

