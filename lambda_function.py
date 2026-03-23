import logging

# Create logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    logger.info("Lambda execution started")

    message = "CI/CD pipeline deployment successful"

    logger.info("Lambda execution completed successfully")

    return {
        "statusCode": 200,
        "body": message
    }