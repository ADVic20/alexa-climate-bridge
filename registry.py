from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er


class AlexaRegistry:
    """Obtiene información de los dispositivos Alexa."""

    def __init__(self, hass: HomeAssistant):
        self.hass = hass
        self.device_registry = dr.async_get(hass)
        self.entity_registry = er.async_get(hass)

    def get_echo_devices(self) -> list[dict]:
        """Devuelve todos los Echo registrados por alexa_devices."""

        devices = []

        for device in self.device_registry.devices.values():

            if not device.identifiers:
                continue

            found = False

            for domain, identifier in device.identifiers:
                if domain == "alexa_devices":
                    found = True
                    break

            if not found:
                continue

            devices.append(
                {
                    "id": device.id,
                    "name": device.name,
                    "manufacturer": device.manufacturer,
                    "model": device.model,
                }
            )

        devices.sort(key=lambda d: d["name"])

        return devices

    def get_voice_event(self, device_id: str) -> str | None:
        """Obtiene la entidad voice_event del Echo."""

        entities = er.async_entries_for_device(
            self.entity_registry,
            device_id,
        )

        for entity in entities:

            if entity.domain != "event":
                continue

            if entity.entity_id.endswith("_voice_event"):
                return entity.entity_id

        return None

    def get_media_player(self, device_id: str) -> str | None:
        """Obtiene el media_player del Echo."""

        entities = er.async_entries_for_device(
            self.entity_registry,
            device_id,
        )

        for entity in entities:

            if entity.domain == "media_player":
                return entity.entity_id

        return None

    def get_echo_info(self, device_id: str) -> dict | None:
        """Devuelve toda la información necesaria."""

        device = self.device_registry.async_get(device_id)

        if device is None:
            return None

        return {
            "device_id": device.id,
            "name": device.name,
            "manufacturer": device.manufacturer,
            "model": device.model,
            "voice_event": self.get_voice_event(device.id),
            "media_player": self.get_media_player(device.id),
        }
