# op5-monitor-check-openweathermap
Monitor weather statistics from OpenWeatherMap with OP5 Monitor. <br/>
Requires access to OpenWeatherMap API. More info here: https://openweathermap.org/appid <br/>
Weather locations can be found at: https://openweathermap.org/find 

![alt text](https://github.com/bobkjell/op5-monitor-check-openweathermap/blob/main/openweathermap-checks.png "OpenWeatherMap service-checks")

## Requires
* python-requests
* OpenWeather API key

## Usage
Upload script to: `/opt/plugins/custom/` <br/>

Create a check_command for the plugin: <br/>
`command_name = check_openweathermap` <br/>
`command_line = $USER1$/custom/check_openweathermap.py -l $ARG1$ -k $ARG2$ -t $ARG3$` <br/>



Create service-objects for each type of weather metric: (Example for temperature) <br/>
`service_description = Temperature` <br/>
`check_command = check_openweathermap` <br/>
`check_command_args = <location>!<apikey>!temperature` <br/>

It's recommended to mask your API-key in: `/opt/monitor/etc/resource.cfg`

## 2021-03-11
Just an informal plugin for now. Thresholds are to be added later. <br/>
Supports the following metrics: Temperature (current, feels, min, max), Wind speed, Humidity, Pressure, Description.
