# Home Assistant Custom Integration: Monoprice 6-Zone Amplifier
 An Integration for the Monoprice 6-Zone Amplifier, with added sound mode, balance, treble & bass
 This is a modification of the <a href="https://www.home-assistant.io/integrations/monoprice/">existing Monoprice integration</a>, when installed this will override it.

## How To:
* Add the monoprice folder to your /config/custom_components folder
* Restart Home Assistant
* Go to settings->integrations
* Click add->Monoprice 6-Zone Amplifier Custom
* Configure using your serial port & source names

* <b>Note:</b> If the core integration is already configured, simply add this custom one to overwrite it, you should not need to delete & readd the integration.

 ## Services
 * monoprice_custom.snapshot
 * monoprice_custom.restore
 * monoprice_custom.set_balance
 * monoprice_custom.set_bass
 * monoprice_custom.set_treble

 ## Sound Modes
 The sound modes can be controlled via a select dropdown on the media_player card.
 The sound modes are:
 * Normal
 * High Bass
 * Medium Bass
 * Low Bass
