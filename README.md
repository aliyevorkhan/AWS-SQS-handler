# AWS SQS Handler for Message Queues

### Summary

This is an example class for handling message queues in AWS SQS service.

### Requirements
- boto3
- python-environ

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip3 install -r requirements
```

## Get started
Rename *.env.example* file to *.env* .
```bash
mv .env.example .env
```

Then edit constants which *.env* file contains.

Mandatory defines:
```python
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""

#for region name example: us-east-1
REGION_NAME=""
```

## Usage
Define credentials and constant variables via environ.

```python
env = environ.Env()
environ.Env.read_env()

AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
REGION_NAME = env("REGION_NAME")
QUEUE_NAME = 'MyQueue'
```

Initialize SQSHandler instance for handling queue.
```python
sqs_handler = SQSHandler(
        AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,
        REGION_NAME, QUEUE_NAME)
```

Core methods:
```python
#show all available queues
sqs_handler.show_all_available_queues()
#send given message
sqs_handler.send_message("Hello")
#receive available message on most top
sqs_handler.receive_message()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)