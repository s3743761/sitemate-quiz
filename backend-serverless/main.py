
import json
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
import logging

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the logging level (INFO, DEBUG, ERROR, etc.)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)


def create(event, context):
    request_body = json.loads(event.get("body"))
    # request_body = event.get("body")
    id = request_body.get('id', "")
    title = request_body.get('title', "")
    description = request_body.get('description', "")

    try:
        dynamodb_client = boto3.client("dynamodb", region_name="us-west-2")

        # Create an item to add to the table
        item = {
            'id': {'S': id},
            'title': {'S': title},
            'description': {'S': description},
        }

        response = dynamodb_client.put_item(
            TableName='Issues',
            Item=item, ReturnConsumedCapacity='TOTAL')

        description = item['description']['S']
        id_value = item['id']['S']
        title = item['title']['S']

        item_response = {
            'id': id_value,
            'title': title,
            'description': description
        }

        logger.info(f"Reques to create issue: {json.dumps(item_response)}")

        return {
            'statusCode': 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Credentials": True,
            },
            'body': json.dumps({"Message": "Issue created successfully", "item": item_response})
        }

    except ClientError as e:
        logger.error(f"Error, Internal server error")
        return {
            'statusCode': 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Credentials": True,
            },
            'body': json.dumps(f'Error: {str(e)}')
        }

    except Exception as e:
        logger.error(f"Error, Internal server error")
        return {
            'statusCode': 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Credentials": True,
            },
            'body': json.dumps(f'Unexpected error: {str(e)}')
        }


def read(event, context):
    id = event['pathParameters']['id']

    try:
        dynamodb_client = boto3.client("dynamodb", region_name="us-west-2")

        # Create an item to add to the table

        response = dynamodb_client.get_item(
            Key={
                'id': {'S': id}
            },
            TableName="Issues"
        )

        # print(response['Item'])
        item = response['Item']
        description = item['description']['S']
        id_value = item['id']['S']
        title = item['title']['S']

        item = {
            'id': id_value,
            'title': title,
            'description': description
        }

        logger.info(f"Request to read issue with id: {id}")
        return {
            'statusCode': 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Credentials": True,
            },
            'body': json.dumps({"Message": "Issue fetched successfully", "item": item})
        }

    except ClientError as e:
        logger.error(f"Error, Internal server error")
        return {
            'statusCode': 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Credentials": True,
            },
            'body': json.dumps(f'Error: {str(e)}')
        }

    except Exception as e:
        logger.error(f"Error, Internal server error")
        return {
            'statusCode': 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Credentials": True,
            },
            'body': json.dumps(f'Unexpected error: {str(e)}')
        }


def update(event, context):
    request_body = json.loads(event.get("body"))
    # request_body = event.get("body")
    id = request_body.get('id', "")
    title = request_body.get('title', "")
    description = request_body.get('description', "")

    try:
        dynamodb_client = boto3.client("dynamodb", region_name="us-west-2")

        # Create an item to add to the table
        item = {
            'id': id,
            'title': title,
            'description': description,
        }

        dynamodb_client.update_item(
            TableName='Issues',
            Key={
                'id': {'S': id}
            },
            ExpressionAttributeNames={
                "#title": "title",
                "#description": "description"
            },
            ExpressionAttributeValues={
                ':title': {"S": title},
                ':description': {"S": description}
            },
            UpdateExpression="SET #title = :title, #description = :description",
            ReturnValues='ALL_NEW')

        logger.info(f"Request to update issue: {json.dumps(item)}")

        return {
            'statusCode': 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Credentials": True,
            },
            'body': json.dumps({"Message": "Issue updated successfully", "item": item})
        }

    except ClientError as e:
        logger.error(f"Error, Internal server error")
        return {
            'statusCode': 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Credentials": True,
            },
            'body': json.dumps(f'Error: {str(e)}')
        }

    except Exception as e:
        logger.error(f"Error, Internal server error")
        return {
            'statusCode': 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Credentials": True,
            },
            'body': json.dumps(f'Unexpected error: {str(e)}')
        }


def delete(event, context):
    request_body = json.loads(event.get("body"))
    # request_body = event.get("body")
    id = request_body.get('id', "")

    try:
        dynamodb_client = boto3.client("dynamodb", region_name="us-west-2")

        # Create an item to add to the table
        dynamodb_client.delete_item(
            TableName="Issues",
            Key={
                'id': {'S': id}
            }
        )

        logger.info(f"Request to delete issue with id: {id}")

        return {
            'statusCode': 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Credentials": True,
            },
            'body': json.dumps({"message": "Item deleted with id: " + id})
        }

    except ClientError as e:
        logger.error(f"Error, Internal server error")
        return {
            'statusCode': 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Credentials": True,
            },
            'body': json.dumps(f'Error: {str(e)}')
        }

    except Exception as e:
        logger.error(f"Error, Internal server error")
        return {
            'statusCode': 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Credentials": True,
            },
            'body': json.dumps(f'Unexpected error: {str(e)}')
        }


if __name__ == "__main__":
    # create({'body': {
    #     "id": "123",
    #     "title": "client@email2.com",
    #     "description": "client@email2.com"
    # }}, "")
    # read({'body': {
    #     "id": "123",
    # }}, "")
    # update({'body': {
    #     "id": "123",
    #     "title": "updated@email2.com",
    #     "description": "updated123@email22.com"
    # }}, "")
    delete({'body': {
        "id": "123",
    }}, "")
