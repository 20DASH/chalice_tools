from chalice import CORSConfig


def no_cors_response(body: dict, status_code=200):
    from chalice import Response

    return Response(
        body=body,
        status_code=status_code,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "POST, GET, OPTIONS, DELETE",
        },
    )


cors_config = CORSConfig(
    allow_origin="*",
    allow_headers="*",
    max_age=600,
    expose_headers="*",
    allow_credentials=True,
)


def no_cors_route(*args, **kwargs):
    from functools import wraps

    # Remove 'cors' from kwargs to prevent conflicts
    kwargs.pop("cors", None)

    def decorator(func):
        # Determine the path
        if args and isinstance(args[0], str):
            path = args[0]
        else:
            path = f"/{func.__name__}"

        from app import app

        # Apply Chalice route with the determined path and remaining kwargs
        @app.route(path, cors=cors_config, **kwargs)
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            original_response = func(*args, **kwargs)
            # Handle cases where the function returns a tuple (body, status_code)
            if isinstance(original_response, tuple) and len(original_response) == 2:
                body, status_code = original_response
                return no_cors_response(body, status_code)
            else:
                return no_cors_response(original_response)

        return wrapped_function

    # Check if decorator is called without parentheses
    if not args or not isinstance(args[0], str):
        if args and callable(args[0]):
            # Case: @nocorsroute
            return decorator(args[0])
        else:
            # Case: @nocorsroute() with other parameters
            return decorator
    else:
        # Case: @nocorsroute('/path', methods=['GET'])
        return decorator


def load_chalice_config(stage="dev"):
    import json
    import os

    with open(".chalice/config.json", "r") as config_file:
        config = json.load(config_file)

    for key, value in config.get("environment_variables", {}).items():
        os.environ[key] = value

    stage_env_vars = (
        config.get("stages", {}).get(stage, {}).get("environment_variables", {})
    )
    for key, value in stage_env_vars.items():
        os.environ[key] = value


def get_current_stage(options=["prod", "dev"]):
    import os

    function_name = os.environ.get("AWS_LAMBDA_FUNCTION_NAME", "")
    for opt in options:
        if opt in function_name:
            return opt

    return None
