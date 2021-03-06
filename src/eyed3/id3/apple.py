# -*- coding: utf-8 -*-
################################################################################
#  Copyright (C) 2012  Travis Shirk <travis@pobox.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.
#
################################################################################
'''
Here lies Apple frames, all of which are non-standard. All of these would have
been standard user text frames by anyone not being a bastard, on purpose.
'''
from .frames import Frame, TextFrame

PCST_FID = b"PCST"
WFED_FID = b"WFED"
TKWD_FID = b"TKWD"
TDES_FID = b"TDES"
TGID_FID = b"TGID"


class PCST(Frame):
    '''Indicates a podcast. The 4 bytes of data is undefined, and is typically
    all 0.'''

    def __init__(self, id=PCST_FID):
        super(PCST, self).__init__(PCST_FID)

    def render(self):
        self.data = b"\x00" * 4
        return super(PCST, self).render()


class TKWD(TextFrame):
    '''Podcast keywords.'''

    def __init__(self, id=TKWD_FID):
        super(TKWD, self).__init__(TKWD_FID)


class TDES(TextFrame):
    '''Podcast description. One encoding byte followed by text per encoding.'''

    def __init__(self, id=TDES_FID):
        super(TDES, self).__init__(TDES_FID)


class TGID(TextFrame):
    '''Podcast URL of the audio file. This should be a W frame!'''

    def __init__(self, id=TGID_FID):
        super(TGID, self).__init__(TGID_FID)


class WFED(TextFrame):
    '''Another podcast URL, the feed URL it is said.'''

    def __init__(self, id=WFED_FID, url=""):
        super(WFED, self).__init__(WFED_FID, url)
