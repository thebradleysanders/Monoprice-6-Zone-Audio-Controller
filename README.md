# Home Assistant Custom Integration: Monoprice 6-Zone Amplifier
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)


 An Integration for the Monoprice 6-Zone Amplifier, with added sound mode, balance, treble & bass
 This is a modification of the <a href="https://www.home-assistant.io/integrations/monoprice/">existing Monoprice integration</a>.
 
 <b>Note:</b> if you your zones are slow to respond, make sure all entities in the zones you are not using are disabled in Home Assistant.

## How To:
* Add the monoprice folder to your /config/custom_components folder
* Restart Home Assistant
* Go to settings->integrations
* Click add->Monoprice 6-Zone Amplifier Custom
* Configure using your serial port & source names

<b>Note:</b> If the core integration is already configured, disable it before adding this custom one.


## Additional Features
These are features not included in the original Monoprice Integration.

 #### Zones
 * 10 - Used to control all zones on the master controller
 * 20 - Used to control all zones on the slave 1 controller
 * 30 - Used to control all zones on the slave 2 controller

 #### Services
 * <i>monoprice_custom.snapshot</i> 
 * <i>monoprice_custom.restore</i>
 * monoprice_custom.set_balance
 * monoprice_custom.set_bass
 * monoprice_custom.set_treble

 #### Sound Modes
 The sound modes can be controlled via a select dropdown on the media_player card.
 The sound modes are:
 * Normal
 * High Bass
 * Medium Bass
 * Low Bass

  #### Sensors
  * Keypad (Connected/Disconnected)
  * Do Not Disturb (On/Off)
  * Public Anouncement (On/Off)
  
  #### Sliders (Numbers)
  * Balance
  * Bass
  * Treble
