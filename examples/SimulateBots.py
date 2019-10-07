import random

random.seed(42)

MAX_BOTS = 5
MAX_BOT_LENGTH = 100
MAX_TICKS = 3 * MAX_BOT_LENGTH

BIRTH_PROBABILITY = 10 / MAX_BOT_LENGTH

SCORE_FACTOR = 100

if __name__ == '__main__':
    slot = [0 for _ in range(MAX_BOTS)]
    scores = [0 for _ in range(MAX_BOTS)]

    def birthOrGroth(bot):
        def death(bot):
            return 0 if rnd <= (1000000 ** ((bot / MAX_BOT_LENGTH) - 1)) else bot

        rnd = random.uniform(0.0, 1.0)
        if bot > 0 or rnd <= BIRTH_PROBABILITY:
            return death(bot + 1)
        return bot

    bot_count = 0
    for tick in range(MAX_TICKS):
        bot_count = 0
        for i in range(MAX_BOTS):
            bot = birthOrGroth(slot[i])
            if bot > 0:
                bot_count += 1

            slot[i] = bot

        for i in range(MAX_BOTS):
            scores[i] = MAX_BOT_LENGTH / bot_count if bot_count else 0

        for i in range(MAX_BOTS):
            scores[i] = int(SCORE_FACTOR * scores[i])

        print(tick, 'scores', slot, scores, bot_count)
