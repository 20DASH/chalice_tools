
def no_cors_response(body:dict, status_code=200):
    from chalice import Response
    return Response(body=body, status_code=status_code,  headers={
        'Access-Control-Allow-Origin': '*', 
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, DELETE'
    })

def load_chalice_config(stage="dev"):
    import json
    import os
    with open(".chalice/config.json", "r") as config_file:
        config = json.load(config_file)

    for key, value in config.get('environment_variables', {}).items():
        os.environ[key] = value

    stage_env_vars = config.get('stages', {}).get(stage, {}).get('environment_variables', {})
    for key, value in stage_env_vars.items():
        os.environ[key] = value