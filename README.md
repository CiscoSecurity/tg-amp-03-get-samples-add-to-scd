[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/AMP-for-Endpoints "Gitter chat")

### Get samples from Threat Grid and add the SHA256 to AMP for Endpoint Simple Custom Detection

This is an example script for getting samples that score 95 or greater in Threat Grid and adding their SHA256's to a Simple Custom Detection in AMP for Endpoints. This script is intended to show the bare minimum required to query Threat Grid and POST to a Simple Custom Detection list. It is in no way production ready and should not be used in a production environment.

### Before using you must update the following:
- Line 4: tg_api_key
- Line 7: client_id
- Line 8: amp_api_key
- Line 11: scd_guid
