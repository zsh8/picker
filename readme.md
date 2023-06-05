# Product Feed Web Application

This web application allows you to receive, normalize, and store product feed data in a PostgreSQL database. It provides REST API endpoints to retrieve individual product information by code or fetch the entire range as an array if no argument is passed.

## Assumptions

While working on this challenge, the requirements were not explicitly defined. Based on the provided information, the following assumptions were made:

- When creating a new item, all the required information, including the amount, should be received by the API.
- When deleting an item, the entire item will be removed from the database.

## Requirements

- docker
- docker-compose

## Execution

To start the application server, navigate to the project's root directory and run the following command:

```sh
docker-compose up
```

This will start the necessary containers and set up the application.

After a few seconds, you can access the web server by opening your browser and visiting http://localhost:8000/.

The project provides both a set of REST API endpoints and a simple web form that can be accessed through the following URLs:

- http://localhost:8000/storag/ - Fetch all items
- http://localhost:8000/storag/create/ - Create a new item
- http://localhost:8000/storag/{typ}/{code}/ - Fetch a specific item
- http://localhost:8000/storag/{typ}/{code}/edit/ - Edit a specific item
- http://localhost:8000/storag/{typ}/{code}/delete/ - Delete a specific item

Note: Replace {typ} and {code} in the URLs with the appropriate values for the item you want to retrieve, edit, or delete.
