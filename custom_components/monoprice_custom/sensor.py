"""Support for interfacing with Monoprice 6 zone home audio controller."""
from code import interact
import logging

from serial import SerialException

from homeassistant import core
try:
    from homeassistant.components.sensor import (
        SensorEntity as SensorEntity,
    )
except ImportError:
    from homeassistant.components.sensor import SensorEntity

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_PORT
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv, entity_platform, service
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import (
    CONF_SOURCES,
    DOMAIN,
    FIRST_RUN,
    MONOPRICE_OBJECT
)

_LOGGER = logging.getLogger(__name__)
PARALLEL_UPDATES = 1


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Monoprice 6-zone amplifier platform."""
    port = config_entry.data[CONF_PORT]
    monoprice = hass.data[DOMAIN][config_entry.entry_id][MONOPRICE_OBJECT]

    entities = []
    for i in range(1, 4):
        for j in range(1, 7):
            zone_id = (i * 10) + j
            _LOGGER.info("Adding zone %d for port %s", zone_id, port)
            entities.append(MonopriceZone(monoprice, "Keypad", config_entry.entry_id, zone_id))
            entities.append(MonopriceZone(monoprice, "Public Anouncement", config_entry.entry_id, zone_id))
            entities.append(MonopriceZone(monoprice, "Do Not Disturb", config_entry.entry_id, zone_id))

    # only call update before add if it's the first run so we can try to detect zones
    first_run = hass.data[DOMAIN][config_entry.entry_id][FIRST_RUN]
    async_add_entities(entities, first_run)

    platform = entity_platform.async_get_current_platform()


    @service.verify_domain_control(hass, DOMAIN)
    async def async_service_handle(service_call: core.ServiceCall) -> None:
        """Handle for services."""
        entities = await platform.async_extract_from_service(service_call)

        if not entities:
            return


class MonopriceZone(SensorEntity):
    """Representation of a Monoprice amplifier zone."""


    def __init__(self, monoprice, sensor_type, namespace, zone_id):
        """Initialize new zone sensors."""
        self._monoprice = monoprice
        self._sensor_type = sensor_type
        self._zone_id = zone_id
        self._unique_id = f"{namespace}_{self._zone_id}"
        self._name = f"Zone {self._zone_id} {sensor_type}"
        self._state = None

        if(sensor_type == "Keypad"):
            self._icon = "mdi:dialpad"
        elif(sensor_type == "Public Anouncement"):
            self._icon = "mdi:bullhorn"
        elif(sensor_type == "Do Not Disturb"):
            self._icon = "mdi:weather-night"
            
        self._update_success = True

    def update(self):
        """Retrieve latest value."""
        try:
            state = self._monoprice.zone_status(self._zone_id)
        except SerialException:
            self._update_success = False
            _LOGGER.warning("Could not update zone %d", self._zone_id)
            return

        if not state:
            self._update_success = False
            return

        if(self._sensor_type == "Keypad"):
            self._state = '{}'.format('Connected' if state.keypad else 'Disconnected')
        elif(self._sensor_type == "Public Anouncement"):
            self._state = '{}'.format('On' if state.pa else 'Off')
        elif(self._sensor_type == "Do Not Disturb"):
            self._state = '{}'.format('On' if state.do_not_disturb else 'Off')

    @property
    def entity_registry_enabled_default(self):
        """Return if the entity should be enabled when first added to the entity registry."""
        return self._zone_id < 20 or self._update_success

    @property
    def device_info(self) -> DeviceInfo:
        """Return device info for this device."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._unique_id)},
            manufacturer="Monoprice",
            model="6-Zone Amplifier",
            name="Zone " + str(self._zone_id)
        )

    @property
    def unique_id(self):
        """Return unique ID for this device."""
        return self._unique_id + "_" + self._sensor_type

    @property
    def name(self):
        """Return the name of the zone."""
        return self._name

    @property
    def native_value(self) -> str:
        """Return the state of the zone."""
        return self._state

    @property
    def icon(self):
        """Return the icon of the zone."""
        return self._icon