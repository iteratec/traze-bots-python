import traze.log as log
from traze.client import World, Spectator

# watch the players behavior for 30 seconds
if __name__ == "__main__":
    log.DEFAULT_LEVEL = log.DEBUG

    Spectator(World().games[0]).watch()
