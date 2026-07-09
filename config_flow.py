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


class AlexaClimateBridgeConfigFlow(
    config_entries.ConfigFlow,
    domain=DOMAIN,
):
    """Alexa Climate Bridge Config Flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None):

        if user_input is not None:
            return self.async_create_entry(
                title=user_input[CONF_NAME],
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_NAME): selector.TextSelector(),

                    vol.Required(CONF_ECHO_DEVICE): selector.DeviceSelector(
                        selector.DeviceSelectorConfig()
                    ),

                    vol.Required(CONF_CLIMATE_NAME): selector.TextSelector(),
                }
            ),
        )
