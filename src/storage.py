import os
import boto3
from datetime import datetime

USE_DYNAMODB = os.environ.get("USE_DYNAMODB", "false").lower() == "true"

if USE_DYNAMODB:
    # Initialize DynamoDB client
    dynamodb = boto3.resource(
        "dynamodb",
        region_name=os.getenv("AWS_REGION", "us-east-1"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )
    table_name = os.getenv("DYNAMODB_TABLE_NAME", "dev-UniquePairsRequestLogs")
    table = dynamodb.Table(table_name)
else:
    in_memory_store = []


def log_request(data):
    # Log the request to either DynamoDB or the in-memory store."""
    timestamp = int(datetime.utcnow().timestamp())
    request_id = str(timestamp)

    if USE_DYNAMODB:
        log_to_dynamodb(data, request_id, timestamp)
    else:
        log_to_memory(data, request_id, timestamp)


def log_to_dynamodb(data, request_id, timestamp):
    table.put_item(
        Item={
            "RequestID": request_id,
            "Timestamp": timestamp,
            "RequestData": str(data),
        }
    )


def log_to_memory(data, request_id, timestamp):
    in_memory_store.append(
        {
            "RequestID": request_id,
            "Timestamp": timestamp,
            "RequestData": str(data),
        }
    )
