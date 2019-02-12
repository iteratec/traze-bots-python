import traze.log as log
from traze.bot import BotBase
from traze.client import World


class SpawnBot(BotBase):
    def __init__(self, game):
        """
        Args:
            game (Game): The game object.

        Returns:
            ---
        """
        super().__init__(game)

    def next_action(self, actions):
        """
        Args:
            actions (Set[Action]): All possible actions.

        Returns:
            Action: Next action.
        """
        return None


# answers the question 'what happens if no action is sent?'
if __name__ == "__main__":
    log.DEFAULT_LEVEL = log.DEBUG

    SpawnBot(World().games[0]).play(1, suppress_server_timeout=True)
