import shodan

# Shodan API key
API_KEY = "" # Enter your Shodan API key

# Public IP addresses to scan
ip_addresses = [
    "", # Enter the public IP addresses to be scanned
    "", # Enter the public IP addresses to be scanned
    "", # Enter the public IP addresses to be scanned
    ""  # Enter the public IP addresses to be scanned
# ...
]

# Function to scan open ports
def scan_ports(api_key, ip_address):
    api = shodan.Shodan(api_key)

    try:
        # Search for IP address information
        host = api.host(ip_address)

        # Display open ports
        print(f"Open ports for IP address {ip_address}:")
        for service in host['data']:
            print(f"  - Port: {service['port']}")
            print(f"    Service: {service['transport']}")
            print(f"    Produit: {service.get('product', 'Unknown')}")
            print(f"    Version: {service.get('version', 'Unknown')}")
            print("")
    except shodan.APIError as e:
        print(f"No open ports for IP address : {ip_address}")

# Loop over IP addresses
for ip_address in ip_addresses:
    scan_ports(API_KEY, ip_address)