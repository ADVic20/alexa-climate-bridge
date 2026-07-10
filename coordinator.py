from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .alexa import AlexaController
from .listener import AlexaListener


class AlexaClimateCoordinator(DataUpdateCoordinator):
    """Coordinator."""

    def __init__(
        self,
        hass: HomeAssistant,
        device_id: str,
        climate_name: str,
        voice_event: str,
    ) -> None:

        super().__init__(
            hass,
            logger=None,
            name="Alexa Climate Bridge",
        )

        self.controller = AlexaController(
            hass,
            device_id,
            climate_name,
        )

        self.listener = AlexaListener(
            hass,
            voice_event,
            climate_name,
            self.async_refresh_state,
        )

        self.available = True

        self.is_on = False

        self.current_temperature = 24

        self.target_temperature = 24

        self.hvac_mode = "off"

        self.fan_mode = "Auto"

        self.swing_mode = "Off"

    async def async_start(self):
        """Iniciar listener."""
        await self.listener.async_start()

    async def async_stop(self):
        """Detener listener."""
        await self.listener.async_stop()

    async def async_turn_on(self):

        await self.controller.turn_on()

        self.is_on = True
        self.hvac_mode = "cool"

        self.async_update_listeners()

    async def async_turn_off(self):

        await self.controller.turn_off()

        self.is_on = False
        self.hvac_mode = "off"

        self.async_update_listeners()

    async def async_set_temperature(
        self,
        temperature: float,
    ):

        await self.controller.set_temperature(
            temperature,
        )

        self.target_temperature = temperature

        self.async_update_listeners()

    async def async_set_hvac_mode(
        self,
        mode: str,
    ):

        await self.controller.set_hvac_mode(
            mode,
        )

        self.hvac_mode = mode

        self.is_on = mode != "off"

        self.async_update_listeners()

    async def async_set_fan_mode(
        self,
        mode: str,
    ):

        await self.controller.set_fan_mode(
            mode,
        )

        self.fan_mode = mode

        self.async_update_listeners()

    async def async_set_swing_mode(
        self,
        mode: str,
    ):

        await self.controller.set_swing_mode(
            mode,
        )

        self.swing_mode = mode

        self.async_update_listeners()

    async def async_refresh_state(
        self,
        *,
        power=None,
        temperature=None,
        hvac_mode=None,
        fan_mode=None,
        swing_mode=None,
    ):

        if power is not None:
            self.is_on = power

            if not power:
                self.hvac_mode = "off"

        if temperature is not None:
            self.target_temperature = temperature

        if hvac_mode is not None:
            self.hvac_mode = hvac_mode

        if fan_mode is not None:
            self.fan_mode = fan_mode

        if swing_mode is not None:
            self.swing_mode = swing_mode

        self.async_update_listeners()
