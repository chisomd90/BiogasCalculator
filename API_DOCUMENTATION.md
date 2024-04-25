# API Documentation

This documentation provides information about the endpoints available in the BiogasCalculator API.

## Base URL

The base URL for all API endpoints is:

http://127.0.0.1:8000/


## Endpoints

### Calculate Percentage of Fat

Calculates the percentage of fat based on the provided input parameters.

- **URL:** `/calculate_percentage_of_fat/`
- **Method:** `GET`
- **Parameters:**
  - `weight_of_flask`: Weight of the flask (float)
  - `weight_of_oil`: Weight of the oil (float)
  - `weight_of_empty_flask`: Weight of the empty flask (float)
  - `weight_of_sample`: Weight of the sample (float)
- **Example Request:**

GET /calculate_percentage_of_fat/?weight_of_flask=10&weight_of_oil=5&weight_of_empty_flask=2&weight_of_sample=50

- **Example Response:**
```json
{
    "percentage_of_fat": 15.0
}
```

### Calculate Percentage of Ash

Calculates the percentage of ash based on the provided input parameters.

- **URL:** /calculate_percentage_of_ash/
- **Method:** GET
- **Parameters:**
    - weight_of_crucible: Weight of the crucible (float)
    - weight_of_ash: Weight of the ash (float)
    - weight_of_sample: Weight of the sample (float)
- Example Request:
 bash

 GET /calculate_percentage_of_fat/?weight_of_flask=10&weight_of_oil=5&weight_of_empty_flask=2&weight_of_sample=50

 - **Example Response:**
```json
{
    "percentage_of_fat": 15.0
}
```

Calculate Percentage of Ash
Calculates the percentage of ash based on the provided input parameters.

URL: /calculate_percentage_of_ash/
Method: GET
Parameters:
weight_of_crucible: Weight of the crucible (float)
weight_of_ash: Weight of the ash (float)
weight_of_sample: Weight of the sample (float)

GET /calculate_percentage_of_ash/?weight_of_crucible=10&weight_of_ash=2&weight_of_sample=50

{
    "percentage_of_ash": 4.0
}

Calculate Percentage of Protein
Calculates the percentage of protein based on the provided input parameters.

URL: /calculate_percentage_of_protein/
Method: GET
Parameters:
percentage_of_nitrogen: Percentage of nitrogen (float)
Example Request:

GET /calculate_percentage_of_protein/?percentage_of_nitrogen=2.5

{
    "percentage_of_protein": 6.25
}



Certainly! Here's a template for your API documentation in markdown format:

markdown
Copy code
# API Documentation

This documentation provides information about the endpoints available in the BiogasCalculator API.

## Base URL

The base URL for all API endpoints is:

http://127.0.0.1:8000/

markdown
Copy code

## Endpoints

### Calculate Percentage of Fat

Calculates the percentage of fat based on the provided input parameters.

- **URL:** `/calculate_percentage_of_fat/`
- **Method:** `GET`
- **Parameters:**
  - `weight_of_flask`: Weight of the flask (float)
  - `weight_of_oil`: Weight of the oil (float)
  - `weight_of_empty_flask`: Weight of the empty flask (float)
  - `weight_of_sample`: Weight of the sample (float)
- **Example Request:**
GET /calculate_percentage_of_fat/?weight_of_flask=10&weight_of_oil=5&weight_of_empty_flask=2&weight_of_sample=50

css
Copy code
- **Example Response:**
```json
{
    "percentage_of_fat": 15.0
}
Calculate Percentage of Ash
Calculates the percentage of ash based on the provided input parameters.

URL: /calculate_percentage_of_ash/
Method: GET
Parameters:
weight_of_crucible: Weight of the crucible (float)
weight_of_ash: Weight of the ash (float)
weight_of_sample: Weight of the sample (float)
Example Request:
bash
Copy code
GET /calculate_percentage_of_ash/?weight_of_crucible=10&weight_of_ash=2&weight_of_sample=50
Example Response:
json
Copy code
{
    "percentage_of_ash": 4.0
}
Calculate Percentage of Protein
Calculates the percentage of protein based on the provided input parameters.

URL: /calculate_percentage_of_protein/
Method: GET
Parameters:
percentage_of_nitrogen: Percentage of nitrogen (float)
Example Request:
bash
Copy code
GET /calculate_percentage_of_protein/?percentage_of_nitrogen=2.5
Example Response:
json
Copy code
{
    "percentage_of_protein": 6.25
}
Calculate Percentage of Moisture
Calculates the percentage of moisture based on the provided input parameters.

URL: /calculate_percentage_of_moisture/
Method: GET
Parameters:
weight_of_crucible: Weight of the crucible (float)
weight_of_sample: Weight of the sample (float)
weight_of_drymatter: Weight of the dry matter (float)

Example Request:
bash
GET /calculate_percentage_of_moisture/?weight_of_crucible=10&weight_of_sample=50&weight_of_drymatter=2

{
    "percentage_of_moisture": 72.0
}



Certainly! Here's a template for your API documentation in markdown format:

markdown
Copy code
# API Documentation

This documentation provides information about the endpoints available in the BiogasCalculator API.

## Base URL

The base URL for all API endpoints is:

http://127.0.0.1:8000/

markdown
Copy code

## Endpoints

### Calculate Percentage of Fat

Calculates the percentage of fat based on the provided input parameters.

- **URL:** `/calculate_percentage_of_fat/`
- **Method:** `GET`
- **Parameters:**
  - `weight_of_flask`: Weight of the flask (float)
  - `weight_of_oil`: Weight of the oil (float)
  - `weight_of_empty_flask`: Weight of the empty flask (float)
  - `weight_of_sample`: Weight of the sample (float)
- **Example Request:**
GET /calculate_percentage_of_fat/?weight_of_flask=10&weight_of_oil=5&weight_of_empty_flask=2&weight_of_sample=50

css
Copy code
- **Example Response:**
```json
{
    "percentage_of_fat": 15.0
}
Calculate Percentage of Ash
Calculates the percentage of ash based on the provided input parameters.

URL: /calculate_percentage_of_ash/
Method: GET
Parameters:
weight_of_crucible: Weight of the crucible (float)
weight_of_ash: Weight of the ash (float)
weight_of_sample: Weight of the sample (float)
Example Request:
bash
Copy code
GET /calculate_percentage_of_ash/?weight_of_crucible=10&weight_of_ash=2&weight_of_sample=50
Example Response:
json
Copy code
{
    "percentage_of_ash": 4.0
}
Calculate Percentage of Protein
Calculates the percentage of protein based on the provided input parameters.

URL: /calculate_percentage_of_protein/
Method: GET
Parameters:
percentage_of_nitrogen: Percentage of nitrogen (float)
Example Request:
bash
Copy code
GET /calculate_percentage_of_protein/?percentage_of_nitrogen=2.5
Example Response:
json
Copy code
{
    "percentage_of_protein": 6.25
}
Calculate Percentage of Moisture
Calculates the percentage of moisture based on the provided input parameters.

URL: /calculate_percentage_of_moisture/
Method: GET
Parameters:
weight_of_crucible: Weight of the crucible (float)
weight_of_sample: Weight of the sample (float)
weight_of_drymatter: Weight of the dry matter (float)
Example Request:
bash
Copy code
GET /calculate_percentage_of_moisture/?weight_of_crucible=10&weight_of_sample=50&weight_of_drymatter=2
Example Response:
json
Copy code
{
    "percentage_of_moisture": 72.0
}
Calculate Determination of Total Solids
Calculates the determination of total solids based on the provided input parameters.

URL: /calculate_determination_of_total_solids/
Method: GET
Parameters:
weight_of_crucible: Weight of the crucible (float)
weight_of_sample: Weight of the sample (float)
weight_of_dryresidue: Weight of the dry residue (float)
Example Request

GET /calculate_determination_of_total_solids/?weight_of_crucible=10&weight_of_sample=50&weight_of_dryresidue=2

{
    "determination_of_total_solids": 16.0
}

Calculate Determination of Volatile Solids
Calculates the determination of volatile solids based on the provided input parameters.

URL: /calculate_determination_of_volatile_solids/
Method: GET
Parameters:
weight_of_dryresidue: Weight of the dry residue (float)
weight_of_dryresidue_from_furnace: Weight of the dry residue from the furnace (float)
weight_of_sample: Weight of the sample (float)
Example Request:
bash
GET /calculate_determination_of_volatile_solids/?weight_of_dryresidue=10&weight_of_dryresidue_from_furnace=2&weight_of_sample=50

{
    "determination_of_volatile_solids": 16.0
}


Calculate Percentage of Fibre
Calculates the percentage of fibre based on the provided input parameters.

URL: /calculate_percentage_of_fibre/
Method: GET
Parameters:
weight_of_dryresidue: Weight of the dry residue (float)
weight_of_ash: Weight of the ash (float)
weight_of_sample: Weight of the sample (float)
Example Request:
bash
GET /calculate_percentage_of_fibre/?weight_of_dryresidue=10&weight_of_ash=2&weight_of_sample=50


{
    "percentage_of_fibre": 16.0
}
