from __future__ import annotations

from homeassistant.components.climate import (
    ClimateEntity,
    ClimateEntityFeature,
    HVACMode,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import CONF_CLIMATE_NAME

from .coordinator import AlexaClimateCoordinator


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
):

    coordinator = AlexaClimateCoordinator(
        hass=hass,
        device_id=entry.data["echo_device_id"],
        climate_name=entry.data[CONF_CLIMATE_NAME],
        voice_event=entry.data["echo_event"],
    )

    async_add_entities(
        [
            AlexaClimateEntity(
                coordinator,
                entry,
            )
        ]
    )


class AlexaClimateEntity(
    CoordinatorEntity,
    ClimateEntity,
):

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: AlexaClimateCoordinator,
        entry: ConfigEntry,
    ):

        super().__init__(coordinator)

        self._attr_unique_id = entry.entry_id
        self._attr_name = entry.data["name"]

        self._attr_temperature_unit = UnitOfTemperature.CELSIUS
        self._attr_min_temp = 16
        self._attr_max_temp = 30

        self._attr_supported_features = (
            ClimateEntityFeature.TARGET_TEMPERATURE
            | ClimateEntityFeature.TURN_ON
            | ClimateEntityFeature.TURN_OFF
            | ClimateEntityFeature.FAN_MODE
            | ClimateEntityFeature.SWING_MODE
        )

        self._attr_hvac_modes = [
            HVACMode.OFF,
            HVACMode.COOL,
            HVACMode.HEAT,
            HVACMode.DRY,
            HVACMode.FAN_ONLY,
            HVACMode.AUTO,
        ]

        self._attr_fan_modes = [
            "Auto",
            "Low",
            "Medium",
            "High",
        ]

        self._attr_swing_modes = [
            "Off",
            "Vertical",
            "Horizontal",
            "Both",
        ]

    async def async_added_to_hass(self):
        """Cuando la entidad se agrega a Home Assistant."""

        await super().async_added_to_hass()
        await self.coordinator.async_start()

    async def async_will_remove_from_hass(self):
        """Cuando la entidad se elimina."""

        await self.coordinator.async_stop()
        await super().async_will_remove_from_hass()

    @property
    def available(self):
        return self.coordinator.available

    @property
    def current_temperature(self):
        return self.coordinator.current_temperature

    @property
    def target_temperature(self):
        return self.coordinator.target_temperature

    @property
    def hvac_mode(self):

        return HVACMode(self.coordinator.hvac_mode)

    @property
    def fan_mode(self):
        return self.coordinator.fan_mode

    @property
    def swing_mode(self):
        return self.coordinator.swing_mode

    async def async_turn_on(self):

        await self.coordinator.async_turn_on()

    async def async_turn_off(self):

        await self.coordinator.async_turn_off()

    async def async_set_temperature(self, **kwargs):

        temperature = kwargs.get("temperature")

        if temperature is None:
            return

        await self.coordinator.async_set_temperature(
            temperature
        )

    async def async_set_hvac_mode(
        self,
        hvac_mode,
    ):

        await self.coordinator.async_set_hvac_mode(
            hvac_mode.value
        )

    async def async_set_fan_mode(
        self,
        fan_mode,
    ):

        await self.coordinator.async_set_fan_mode(
            fan_mode
        )

    async def async_set_swing_mode(
        self,
        swing_mode,
    ):

        await self.coordinator.async_set_swing_mode(
            swing_mode
        )
