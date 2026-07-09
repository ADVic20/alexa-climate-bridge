from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.helpers import device_registry as dr
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
    """Config Flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None):

        if user_input is not None:
            return self.async_create_entry(
                title=user_input[CONF_NAME],
                data=user_input,
            )

        device_registry = dr.async_get(self.hass)

        echo_options = []

        for device in device_registry.devices.values():

            identifiers = list(device.identifiers)

            if not identifiers:
                continue

            found = False

            for identifier in identifiers:
                if identifier[0] == "alexa_devices":
                    found = True
                    break

            if not found:
                continue

            echo_options.append(
                selector.SelectOptionDict(
                    value=device.id,
                    label=device.name,
                )
            )

        echo_options.sort(key=lambda item: item["label"])

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_NAME): selector.TextSelector(),

                    vol.Required(
                        CONF_ECHO_DEVICE,
                    ): selector.SelectSelector(
                        selector.SelectSelectorConfig(
                            options=echo_options,
                            mode=selector.SelectSelectorMode.DROPDOWN,
                        )
                    ),

                    vol.Required(
                        CONF_CLIMATE_NAME,
                    ): selector.TextSelector(),
                }
            ),
        )
