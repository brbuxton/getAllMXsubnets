import requests
import os
import csv

# Load the API Key from an environment variable
API_KEY = os.getenv('MERAKI_DASHBOARD_API_KEY')
BASE_URL = 'https://api.meraki.com/api/v1'
HEADERS = {'X-Cisco-Meraki-API-Key': API_KEY, 'Content-Type': 'application/json'}


def get_network_appliance_vlans(network_id):
    """Fetch VLANs for a specific network's appliance."""
    url = f'{BASE_URL}/networks/{network_id}/appliance/vlans'
    response = requests.get(url, headers=HEADERS)
    return response.json()


def get_device_appliance_uplinks_settings(org_id):
    """Fetch uplink settings for a specific appliance."""
    url = f'{BASE_URL}/organizations/{org_id}/appliance/uplink/statuses'
    response = requests.get(url, headers=HEADERS)
    return response.json()


def get_organization_networks(org_id):
    """Fetch all networks for a given organization."""
    url = f'{BASE_URL}/organizations/{org_id}/networks'
    response = requests.get(url, headers=HEADERS)
    return response.json()


def get_network_devices(network_id):
    """Fetch devices for a specific network."""
    url = f'{BASE_URL}/networks/{network_id}/devices'
    response = requests.get(url, headers=HEADERS)
    return response.json()


def get_network_name(network_id):
    """Fetch network name for a specific network."""
    url = f'{BASE_URL}/networks/{network_id}'
    response = requests.get(url, headers=HEADERS)
    return response.json()['name']


def main():
    org_id = 'YOUR_ORG_ID'  # Replace 'YOUR_ORG_ID' with your actual Organization ID

    # Prepare the CSV file for writing
    with open('meraki_mx_vlans_uplinks.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Network Name', 'VLAN Name', 'Subnet'])

        #networks = get_organization_networks(org_id)
        mx_statuses = get_device_appliance_uplinks_settings(org_id)
        print(mx_statuses)
        for network in mx_statuses:
            # Fetch VLAN details
            try:
                check_error = get_network_appliance_vlans(network['networkId'])['errors']
                print(f'{get_network_name(network["networkId"])} has no VLANs')
            except:
                print('VLANs present')
                vlans = get_network_appliance_vlans(network['networkId'])
                #print(vlans)

                for vlan in vlans:
                    # Write details to CSV
                    print(get_network_name(vlan['networkId']), vlan['name'], vlan['subnet'])
                    writer.writerow([get_network_name(vlan['networkId']), vlan['name'], vlan['subnet']])


if __name__ == '__main__':
    main()
