from __future__ import annotations

import re

from homeassistant.core import Event, HomeAssistant


class AlexaListener:
    """Escucha los eventos de voz de Alexa."""

    def __init__(
        self,
        hass: HomeAssistant,
        event_entity: str,
        climate_name: str,
        callback,
    ) -> None:
        self.hass = hass
        self.event_entity = event_entity
        self.climate_name = climate_name.lower()
        self.callback = callback
        self._remove_listener = None

    async def async_start(self):
        """Inicia el listener."""

        self._remove_listener = self.hass.bus.async_listen(
            "state_changed",
            self._state_changed,
        )

    async def async_stop(self):
        """Detiene el listener."""

        if self._remove_listener:
            self._remove_listener()

    async def _state_changed(self, event: Event):

        data = event.data

        if data.get("entity_id") != self.event_entity:
            return

        new_state = data.get("new_state")

        if new_state is None:
            return

        voice_command = (
            new_state.attributes.get("voice_command", "")
            .lower()
            .strip()
        )

        intent = new_state.attributes.get("intent", "")

        if self.climate_name not in voice_command:
            return

        if intent == "TurnOnApplianceIntent":
            await self.callback(
                power=True,
            )

        elif intent == "TurnOffApplianceIntent":
            await self.callback(
                power=False,
            )

        elif intent == "SetValueIntent":

            match = re.search(r"(\d+)", voice_command)

            if match:

                await self.callback(
                    temperature=int(match.group(1))
                )
