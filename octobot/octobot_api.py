#  Drakkar-Software OctoBot
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
from tools.commands import stop_bot as command_stop, restart_bot as command_restart


class OctoBotAPI:

    def __init__(self, octobot):
        self._octobot = octobot

    def is_initialized(self) -> bool:
        return self._octobot.initialized

    def get_exchange_manager_ids(self) -> list:
        return self._octobot.exchange_factory.exchange_manager_ids

    def get_global_config(self) -> dict:
        return self._octobot.config

    def get_startup_config(self) -> dict:
        return self._octobot.startup_config

    def get_edited_config(self) -> dict:
        return self._octobot.edited_config

    def get_trading_mode(self) -> object:
        return self._octobot.get_trading_mode()

    def get_start_time(self) -> float:
        return self._octobot.start_time

    def get_matrix_id(self) -> str:
        return self._octobot.evaluator_factory.matrix_id

    def get_previous_states_manager(self) -> object:
        return self._octobot.exchange_factory.previous_trading_state_manager

    def get_aiohttp_session(self) -> object:
        return self._octobot.get_aiohttp_session()

    def run_in_main_asyncio_loop(self, coroutine):
        return self._octobot.run_in_main_asyncio_loop(coroutine)

    def stop_tasks(self) -> None:
        self._octobot.task_manager.stop_tasks()

    def stop_bot(self) -> None:
        command_stop(self._octobot)

    @staticmethod
    def restart_bot() -> None:
        command_restart()