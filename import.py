import json
import re

# Function to clean host and remove https:// and TLD
def clean_hostname(host):
    # Add https:// if no scheme is present
    if not re.match(r'^https?://', host):
        host = f"https://{host}"
    # Remove protocol (https://)
    clean_host = re.sub(r'https?://', '', host)
    # Remove TLD (the last .domain)
    clean_host = re.sub(r'\.[a-z]+$', '', clean_host)
    return host, clean_host

# Read hostnames from hosts.txt
def read_hosts_file(file_name):
    try:
        with open(file_name, 'r') as file:
            hosts = file.read().splitlines()
            return hosts
    except FileNotFoundError:
        print(f"Error: The file {file_name} does not exist.")
        return []

# Create monitor object
def create_monitor(id, host):
    host, clean_host = clean_hostname(host)
    return {
        "id": id,
        "name": clean_host,
        "description": None,
        "pathName": clean_host,
        "parent": None,
        "childrenIDs": [],
        "url": host,
        "method": "GET",
        "hostname": None,
        "port": None,
        "maxretries": 3,
        "weight": 2000,
        "active": True,
        "forceInactive": False,
        "type": "http",
        "timeout": 48,
        "interval": 60,
        "retryInterval": 60,
        "resendInterval": 0,
        "keyword": None,
        "invertKeyword": False,
        "expiryNotification": True,
        "ignoreTls": False,
        "upsideDown": False,
        "packetSize": 56,
        "maxredirects": 10,
        "accepted_statuscodes": [
            "200-299"
        ],
        "dns_resolve_type": "A",
        "dns_resolve_server": "1.1.1.1",
        "dns_last_result": None,
        "docker_container": "",
        "docker_host": None,
        "proxyId": None,
        "notificationIDList": {},
        "tags": [],
        "maintenance": False,
        "mqttTopic": "",
        "mqttSuccessMessage": "",
        "databaseQuery": None,
        "authMethod": None,
        "grpcUrl": None,
        "grpcProtobuf": None,
        "grpcMethod": None,
        "grpcServiceName": None,
        "grpcEnableTls": False,
        "radiusCalledStationId": None,
        "radiusCallingStationId": None,
        "game": None,
        "gamedigGivenPortOnly": True,
        "httpBodyEncoding": "json",
        "jsonPath": None,
        "expectedValue": None,
        "kafkaProducerTopic": None,
        "kafkaProducerBrokers": [],
        "kafkaProducerSsl": False,
        "kafkaProducerAllowAutoTopicCreation": False,
        "kafkaProducerMessage": None,
        "screenshot": None,
        "headers": None,
        "body": None,
        "grpcBody": None,
        "grpcMetadata": None,
        "basic_auth_user": None,
        "basic_auth_pass": None,
        "oauth_client_id": None,
        "oauth_client_secret": None,
        "oauth_token_url": None,
        "oauth_scopes": None,
        "oauth_auth_method": "client_secret_basic",
        "pushToken": None,
        "databaseConnectionString": None,
        "radiusUsername": None,
        "radiusPassword": None,
        "radiusSecret": None,
        "mqttUsername": "",
        "mqttPassword": "",
        "authWorkstation": None,
        "authDomain": None,
        "tlsCa": None,
        "tlsCert": None,
        "tlsKey": None,
        "kafkaProducerSaslOptions": {
            "mechanism": "None"
        },
        "includeSensitiveData": True
    }

# Main function to create the backup.json
def create_backup_json(hosts_file):
    hosts = read_hosts_file(hosts_file)
    if not hosts:
        return

    monitors = []
    for idx, host in enumerate(hosts, start=1):
        monitor = create_monitor(idx, host)
        monitors.append(monitor)

    # JSON structure
    backup_data = {
        "version": "1.23.13",
        "notificationList": [],
        "monitorList": monitors
    }

    # Write to backup.json
    with open("backup.json", "w") as json_file:
        json.dump(backup_data, json_file, indent=4)
    
    print("backup.json has been created successfully.")

# Get the hosts file from user input and create the backup
if __name__ == "__main__":
    hosts_file = input("Enter the hosts file name (e.g., hosts.txt): ")
    create_backup_json(hosts_file)

