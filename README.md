[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/Lobby "Gitter chat")

### Get samples from Threat Grid and add the SHA256 to AMP for Endpoint Simple Custom Detection:
This is an example script for getting samples that score 95 or greater in Threat Grid and adding their SHA256's to a Simple Custom Detection in AMP for Endpoints. This script is intended to show the bare minimum required to query Threat Grid and POST to a Simple Custom Detection list. It is in no way production ready and should not be used in a production environment.

### Before using you must update the following:
- tg_api_key
- amp_client_id
- amp_api_key
- scd_guid

### Usage:
```
python get_samples_add_sha256_to_scd.py
```

### Example script output:
```
b6eab2191d00eac62989f7a0309e5c07cdf5dfc566756c4910dbc12664096480 - Successfully added to SCD
8a1a0c32f0cb66d5053d00e766d02b4db9443ccfd61e62ee62d921b27beeeb15 - Successfully added to SCD
08d1f13364d0545366318872894e8085758bb0cf69dd5755b9538c1fe0f9ff09 - Successfully added to SCD
```
