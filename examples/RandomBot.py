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
import random

import traze.log as log
from traze.bot import BotBase
from traze.client import World


class RandomBot(BotBase):
    """
    Very simple example bot to demonstrate the usage of traze framework.
    """
    def __init__(self, game):
        """
        Args:
            game (Game): The game object.

        Returns:
            ---
        """
        super().__init__(game)
        self._last_action = None

    def next_action(self, actions):
        """
        Args:
            actions (Tuple[Action]): All possible actions.

        Returns:
            Action: Next action.
        """
        # prefer the same action as far as possible
        if self._last_action not in actions:
            self._last_action = random.choice(actions)
        return self._last_action


if __name__ == "__main__":
    log.DEFAULT_LEVEL = log.DEBUG

    RandomBot(World().games[0]).play(1)
