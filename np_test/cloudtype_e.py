#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2010-2011.

# Author(s):
 
#   Martin Raspaud <martin.raspaud@smhi.se>

# This file is part of pytroll.

# Pytroll is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.

# Pytroll is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with
# pytroll.  If not, see <http://www.gnu.org/licenses/>.

"""A very stupid consumer.
"""

from posttroll.subscriber import Subscribe
from posttroll.publisher import Publish
#from posttroll.message import Message

try:
    with Publish("cloudtype_e", "msg lvl4", 9003) as pub:
        with Subscribe("HRIT lvl1.5", "NWCSAF", timeout=60) as sub1:
            print "ok, let's go"
            for msg in sub1.recv():
                
                if (msg is not None and
                    msg.data["type"] == "HRIT lvl1.5" and
                    msg.data["segment_number"] == "EPI"):
                    print "Consumer got", msg
                if (msg is not None and
                    msg.data["type"].startswith("NWCSAF")):
                    print "Consumer got", msg
                # if msg is not None and msg.type == "file":
                #     data = msg.data
                #     if data["type"] == "HRPT 2":
                #         data["type"] = "HRPT 3"
                #         data["format"] = "Pytroll's netcdf"
                #         print "publishing", Message('/dc/polar/gds', "file",
                #                                     data).encode()
                #         pub.send(Message('/dc/polar/gds', "file",
                #                          data).encode())
except KeyboardInterrupt:
    print "terminating consumer..."



