import json
import os
import mercadopago

def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["MERCADOPAGO_TOKEN"])
    bodyGet = json.loads(event["body"])
    # TODO implement
    preference_data = {
       "items": bodyGet["items"]
    }

    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]

    return {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Headers': 'Content-type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": json.dumps(
            preference
        ),
    }