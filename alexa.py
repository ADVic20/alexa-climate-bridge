from __future__ import annotations

from homeassistant.core import HomeAssistant


class AlexaController:
    """Controlador de Alexa."""

    def __init__(
        self,
        hass: HomeAssistant,
        device_id: str,
        climate_name: str,
    ) -> None:
        self.hass = hass
        self.device_id = device_id
        self.climate_name = climate_name

    async def _send_command(self, command: str) -> None:
        """Enviar un comando de texto a Alexa."""
        await self.hass.services.async_call(
            "alexa_devices",
            "send_text_command",
            {
                "device_id": self.device_id,
                "text_command": command,
            },
            blocking=True,
        )

    async def turn_on(self):
        await self._send_command(
            f"enciende {self.climate_name}"
        )

    async def turn_off(self):
        await self._send_command(
            f"apaga {self.climate_name}"
        )

    async def set_temperature(self, temperature: float):
        await self._send_command(
            f"pon {self.climate_name} a {round(temperature)} grados"
        )

    async def set_hvac_mode(self, mode: str):

        modes = {
            "off": None,
            "cool": "enfriamiento",
            "heat": "calor",
            "dry": "deshumidificador",
            "fan_only": "ventilador",
            "auto": "automático",
        }

        if mode == "off":
            await self.turn_off()
            return

        if mode not in modes:
            return

        await self._send_command(
            f"pon {self.climate_name} en modo {modes[mode]}"
        )

    async def set_fan_mode(self, mode: str):
        await self._send_command(
            f"pon {self.climate_name} en velocidad {mode}"
        )

    async def set_swing_mode(self, mode: str):
        await self._send_command(
            f"pon {self.climate_name} con oscilación {mode}"
        )
