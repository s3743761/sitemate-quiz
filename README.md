# Sitemate REST API

This is a Python REST API to get, create, update and delete issues.

The data is stored in DyanmoDB and the service is deployed serverlessly to AWS Lambda

## Usage

1. To create an issue

```
POST /create

Body: {"id": 1, "title": "Test title", "description": "Test description"}
```

2. To read an issue

```
GET /read/<id>
```

2. To edit an issue

```
PUT /edit

Body: {"id": 1, "title": "Updated title", "description": "Updated description"}

```

4. To delete an issue

```
DELETE /delete/<id>
```

# Sitemate issues client 

This client side Node application, with a command line interface to create, read, update and delete issues. It interacts with issues
REST API 

## Usage

1. To start the program, run:

```
node index.js
```

2. Then select an option, 1 to create an issue, 2 to read an issue, 3 to update an issue and 4 to delete an issue. In this example, we will create an issue:

```
1
```

3. Lastly enter the issue attributes as a JSON object:
```
{"id": 1, "title": "Test", "description": "Test description"}
```
