# MacAddress Company Tool

Docker tool that uses a python code to query the Mac Address Loopup API: https://api.macaddress.io and provides as an output the Company Name.

# Requirements

Before using this tool you must go to https://macaddress.io/signup and signup to get a token.

# Install the Tool

1. Clone this repo.

2. Edit endpoint_settings and change your token:

```sh
ENDPOINT="https://api.macaddress.io/v1"
TOKEN="XXXXXXXXXXXXXXXXXXXXX"
```

3. Build the container image

```sh
docker build -t companytool .
```

# Usage

The only require argument is a macaddress and you can run this as simple as running a docker run.
Provide MACADDRESS environment variable at docker run:

```sh
docker run --rm --env="MACADDRESS=44:38:39:ff:ef:57" companytool
```

# Debug

In case anything goes wrong you can use environment variable DEBUG:

```sh
docker run --rm --env="DEBUG=true" -env="MACADDRESS=44:38:39:ff:ef:57" companytool
```

# Security

Note: This tool has been created according to specific instructions. However a better secure approach should be using the tool locally and create a rest api as a service.
By creating the API as a service, credentials can be store in the cloud securely and only people using a VPN can only access this tool API.
Also I have created on the past API that are managed by token only provided by authentication service like cognito, which can work in an internal active directory.
