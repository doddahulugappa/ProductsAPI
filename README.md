# ProductsAPI

## Setup

```
git clone https://github.com/doddahulugappa/ProductsAPI.git

cd ProductsAPI


pip install -r requirements.txt

python api\products.api

python api\api.py

```
##### Open the browser and type the url where service is running and explore all API endpoints

#Products REST API

The REST API to the products app is described below.

## Get a list of Products

### Request

`GET /products`

    curl -i -H 'Accept: application/json' http://localhost:8000/products

### Response
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    
    {
        "Products": [
            {
                "currency": "USD",
                "id": 1,
                "name": "Banana",
                "price": 65.99
            }
        ]
    }

## Create a new Product

### Request

`POST /products`

    curl --location --request POST "http://localhost:8000/products" \
    --header "Content-Type: application/json" \
    --data-raw "{
        "name":"Apple",
        "price":89.99,
        "currency":"USD"
    }"

### Response

    Status: 201 Created
    Connection: close
    Content-Type: application/json

    Product added

## Get a specific Product by ID

### Request

`GET /products/id`

    curl --location --request GET "http://localhost:8000/products/1" \
    --header "Content-Type: application/json"

### Response

    Status: 200 OK
    Connection: close
    Content-Type: application/json

    [
        {
            "currency": "USD",
            "id": 1,
            "name": "Banana",
            "price": 65.99
        }
    ]

## Change a Product by ID

### Request

`PUT /products/id`

    curl --location --request PUT 'http://localhost:8000/products/1' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "name":"Orange",
        "price":89.99,
        "currency":"USD"
    }'
### Response

    Status: 200 OK
    Connection: close
    Content-Type: application/json
    
    Product Updated
    
## Delete a Product by ID

### Request

`DELETE /products/id`

    curl --location --request DELETE 'http://localhost:8000/products/1' \
    --header 'Content-Type: application/json'
### Response


    Status: 20O OK
    Connection: close
    
    Product Deleted
