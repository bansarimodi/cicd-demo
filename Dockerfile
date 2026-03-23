# Lambda Python base image
FROM public.ecr.aws/lambda/python:3.12

# Copy application code
COPY lambda_function.py .

# Lambda handler
CMD ["lambda_function.lambda_handler"]