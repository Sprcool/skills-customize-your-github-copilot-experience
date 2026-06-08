# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using the FastAPI framework. Implement endpoints, data models, validation, and basic CRUD logic to serve data over HTTP.

## 📝 Tasks

### 🛠️ Create a FastAPI Application

#### Description
Set up a FastAPI app in `starter-code.py` and define a data model for API resources.

#### Requirements
Completed program should:

- Create a FastAPI application instance.
- Define a Pydantic model named `Item` with fields for `id`, `name`, `description`, `price`, and `available`.
- Include a simple in-memory list to store items.
- Define a root endpoint (`/`) that returns a welcome message.

### 🛠️ Add REST API Endpoints

#### Description
Implement endpoints for reading and adding items.

#### Requirements
Completed program should:

- Provide a GET endpoint at `/items` that returns the list of items.
- Provide a GET endpoint at `/items/{item_id}` that returns a single item by `id`.
- Provide a POST endpoint at `/items` that accepts an `Item` and adds it to the list.
- Return a `404` error when an item is not found.

### 🛠️ Improve the API with Updates and Validation

#### Description
Extend the API with update and delete functionality.

#### Requirements
Completed program should:

- Provide a PUT endpoint at `/items/{item_id}` to update an existing item.
- Provide a DELETE endpoint at `/items/{item_id}` to remove an item.
- Validate that the item exists before updating or deleting.
- Return a clear message when actions are completed successfully.

### 🛠️ Test Your API

#### Description
Run the FastAPI app locally and verify endpoints with example requests.

#### Requirements
Completed program should:

- Run using `uvicorn starter-code:app --reload`.
- Return JSON responses for all endpoints.
- Allow easy testing with browser or API client tools.
