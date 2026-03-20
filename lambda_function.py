from service import process_request

def lambda_handler(event, context):

    result = process_request()

    return {
        "statusCode":200,
        "body":result
    }