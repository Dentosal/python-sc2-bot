import json
from pathlib import Path

import sc2

class MyBot(sc2.BotAI):
    with open(Path(__file__).parent / "../botinfo.json") as f:
        NAME = json.load(f)["name"]

    async def on_step(self, iteration):
        if iteration == 0:
            await self.chat_send(f"Name: {self.NAME}")

            for worker in self.workers:
                await self.do(worker.attack(self.enemy_start_locations[0]))
