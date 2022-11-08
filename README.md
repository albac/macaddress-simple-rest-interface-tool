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
