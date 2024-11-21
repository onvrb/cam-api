# CAM-API

This is an implementation for a simple dashboard to get snapshots from a DVR system, specifically from a Safire SF-HTVR6208AP-HEVC.

# Requirements

- Docker

## Creating the `.env` file

| Name                  | Type         | Description                            |
|-----------------------|--------------|----------------------------------------|
| `API_USERNAME`        | `str`        | Username to authenticate with the DVR* |
| `API_PASSWORD`        | `str`        | Password to authenticate with the DVR* |
| `API_ENDPOINT`        | `str`        | API Endpoint before channel selection. Example `'http://192.168.0.100/ISAPI/Streaming/channels/'` |
| `API_PICTURE_CHANNELS`| `str` list   | List for the channels you want to get a snapshot from. Example: `'["101/picture","201/picture"]'` |
| `API_PARAMS`          | `str` object | Parameters for the GET request in the URL. Example: `'{"videoResolutionWidth": 1920, "videoResolutionHeight": 1080}'` |

*Make sure that for WEB Authentication (under Configuration -> System -> Security -> Authentication) is set to digest/basic, as the script will not work with digest only.

The full path for each channel ends up being `API_ENDPOINT` + `channel`, for example `http://192.168.0.100/ISAPI/Streaming/channels/101/picture`. Additionally, if possible, you can get a higher resolution image by adding `?videoResolutionWidth=1920&videoResolutionHeight=1080` to the end of the URL, which is passed as a parameter in `API_PARAMS` (see example above).

Because passing the environment variables from the `.env` is tricky, all parameters should be `str` in the `.env` as well as arguments for the script, which later on the are converted to the correct type.

# Usage

After the service is up and running, you can access the channel list at `http://localhost:8000/channels`.
