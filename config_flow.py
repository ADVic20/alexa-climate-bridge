from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.helpers import selector

from .const import (
    DOMAIN,
    CONF_NAME,
    CONF_ECHO_DEVICE,
    CONF_CLIMATE_NAME,
)
from .registry import AlexaRegistry


class AlexaClimateBridgeConfigFlow(
    config_entries.ConfigFlow,
    domain=DOMAIN,
):
    """Alexa Climate Bridge Config Flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None):

        registry = AlexaRegistry(self.hass)

        if user_input is not None:

            info = registry.get_echo_info(
                user_input[CONF_ECHO_DEVICE]
            )

            data = {
                CONF_NAME: user_input[CONF_NAME],
                CONF_CLIMATE_NAME: user_input[CONF_CLIMATE_NAME],
                "echo_device_id": info["device_id"],
                "echo_name": info["name"],
                "echo_event": info["voice_event"],
                "echo_media_player": info["media_player"],
            }

            return self.async_create_entry(
                title=user_input[CONF_NAME],
                data=data,
            )

        options = []

        for device in registry.get_echo_devices():

            options.append(
                selector.SelectOptionDict(
                    value=device["id"],
                    label=device["name"],
                )
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_NAME,
                    ): selector.TextSelector(),

                    vol.Required(
                        CONF_ECHO_DEVICE,
                    ): selector.SelectSelector(
                        selector.SelectSelectorConfig(
                            options=options,
                            mode=selector.SelectSelectorMode.DROPDOWN,
                        )
                    ),

                    vol.Required(
                        CONF_CLIMATE_NAME,
                    ): selector.TextSelector(),
                }
            ),
        )
