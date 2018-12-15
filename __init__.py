# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

import requests

__author__ = 'wddler'

LOGGER = getLogger(__name__)


class CoffeeOrderSkill(MycroftSkill):
    def __init__(self):
        super(CoffeeOrderSkill, self).__init__(name="CoffeeOrderSkill")

    def initialize(self):
        coffee_order_intent = IntentBuilder("CoffeeOrderIntent"). \
            require("CoffeeOrderKeyword").build()
        self.register_intent(coffee_order_intent, self.handle_coffee_order_intent)

    def handle_coffee_order_intent(self, message):
        self.speak_dialog("coffee.order")
        r = requests.get('http://192.168.42.11:8001')
        print(r.status_code)
        
    def stop(self):
        pass


def create_skill():
    return CoffeeOrderSkill()
