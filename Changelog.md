7/30/26 - Bump pymonoprice to a reconnect-capable build (0.5.1) to fix permanent 'Broken pipe' failures on socket:// serial bridges. See PR for details.
4/24/22 - Fix balance controls on number entitys and monoprice_custom.set_balance
4/24/22 - Fix balance range monoprice_custom.set_balance from 1-19 to 0-20
4/24/22 - Disable zones 10, 20, 30 by default, there seems to be some issues with these zones. Enable with caution.