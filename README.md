# Chalice Tools
chalice_tools is a utility package designed to simplify common tasks when working with the AWS Chalice framework. It provides helper functions for handling CORS responses and loading Chalice configuration.

## Installation
Add this line to your requirements.txt file:
    
    chalice_tools @ git+https://github.com/20DASH/chalice_tools

## Decorators

`@no_cors_route`

Defines a function as a chalice no-cors route. Similar to chalice's native @app.route, and can receive all the same named arguments except for 'cors'. The first positional argument is optional; if present, will define the endpoint, else the function name will be the endpoind.

All the examples below are equivalent:

```python
# simplest
@no_cors_route
def some_route():

# with parenthesis
@no_cors_route()
def some_route():

# endpoint specified
@no_cors_route("some_route")
def some_route():

# extra args
@no_cors_route(methods=["GET"])
def some_route():
```

## Functions

`no_cors_response(body: dict, status_code=200)`

Creates a Chalice Response object with CORS headers pre-configured for cross-origin requests.

### Parameters:
- `body` (dict): The response body to be returned.

- `status_code` (int, optional): The HTTP status code. Defaults to 200.

### Returns:

`chalice.Response`: A response object with CORS headers.

Example:

```python
from chalice_tools import no_cors_response

def my_view():
    return no_cors_response({"message": "Hello, world!"}, status_code=200)
```
`load_chalice_config(stage="dev")`

Loads environment variables from the .chalice/config.json file for the specified stage. Remember to do this before importing other packages.

### Parameters:
- `stage` (str, optional): The Chalice stage (e.g., dev, prod). Defaults to "dev".

Example:
```python
from chalice_tools import load_chalice_config
# Load environment variables for the 'dev' stage
load_chalice_config(stage="dev")

# Access environment variables
import os
print(os.getenv("MY_ENV_VAR"))
```

`get_current_stage(options=["prod", "dev"])`

Returns a str from the options argument if any of them is in the AWS lambda function name - meaning it is the current stage (unless it has a name that includes it). If any, like if running local, will return None

## Contributing
Contributions are welcome! If you'd like to contribute, please:

Fork the repository.

Create a new branch for your feature or bugfix.

Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.