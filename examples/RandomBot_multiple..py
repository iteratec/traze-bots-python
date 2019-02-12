# -*- coding: utf-8 -*-
#
# Copyright 2018 The Traze Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
@author: Danny Lade
"""
import traze.log as log
from traze.client import World
from .RandomBot import RandomBot


# answers the question 'how to run multiple bots at once?'
# TODO - just a concept yet
if __name__ == "__main__":
    log.DEFAULT_LEVEL = log.DEBUG

    game = World().games[0]
    RandomBot(game).play(1)
#    RandomBot(game).play(1)
#    RandomBot(game).play(1)
