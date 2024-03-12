# Meraki Network VLANs and Uplinks Fetcher

This script automates the process of fetching VLAN details and uplink settings for devices across all networks within a specified Cisco Meraki organization. It utilizes the Meraki Dashboard API to retrieve information and saves the data to a CSV file for easy access and analysis.

## Features

- Fetch VLAN configurations for all networks within a Meraki organization.
- Retrieve uplink status and settings for devices within the organization.
- Save network name, VLAN name, and subnet information to a CSV file.

## Prerequisites

Before you run this script, make sure you have:

- Python 3 installed on your machine.
- `requests` library installed in your Python environment. You can install it using `pip install requests`.
- Access to a Cisco Meraki Dashboard with an API key.

## Configuration

1. Obtain an API key from your Meraki Dashboard:
   - Log into the Meraki Dashboard.
   - Navigate to `Organization > Settings`.
   - Scroll down to the section titled "Dashboard API access" and generate a new API key.

2. Set the API key as an environment variable on your machine:
   - On Windows: `set MERAKI_DASHBOARD_API_KEY=<Your-API-Key>`
   - On macOS/Linux: `export MERAKI_DASHBOARD_API_KEY=<Your-API-Key>`

3. Replace `'YOUR_ORG_ID'` in the script with your actual Organization ID. This can be found in the Meraki Dashboard URL or fetched via the Meraki API.

## Usage

To run the script, navigate to the directory containing the script and execute:

```bash
python meraki_network_info.py
```
This will generate a file named meraki_mx_vlans_uplinks.csv in the same directory, containing the fetched VLAN and uplink information.

## Output Format
The output CSV file will contain the following columns:

Network Name: The name of the network.  
VLAN Name: The name of the VLAN within the network.  
Subnet: The subnet associated with the VLAN.  

## License
https://github.com/CiscoSE/cisco-sample-code/blob/master/LICENSE