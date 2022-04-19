# Home Assistant Custom Integration: Monoprice 6-Zone Amplifier
 An Integration for the Monoprice 6-Zone Amplifier, with added sound mode, balance, treble & bass
 This is a modification of the existing Monoprice integration, when installed this will override it.

## How To:
* add the monoprice folder to your /config/custom_components folder
* restart Home Assistant
* Go to settings->integrations
* Click add->Monoprice 6-Zone Amplifier
* Configure using your serial port & zone names

 ## Services
 * monoprice.snapshot
 * monoprice.restore
 * monoprice.set_balance
 * monoprice.set_bass
 * monoprice.set_treble

 ## Sound Modes
 The sound modes can be controlled via a select dropdown on the media_player card
 The sound modes are:
 * Normal
 * High Bass
 * Medium Bass
 * Low Bass
