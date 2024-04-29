# API Documentation

This documentation provides information about the endpoints available in the BiogasCalculator API.

## Base URL

The base URL for all API endpoints is:

http://127.0.0.1:8000/


## Endpoints

### Calculate Percentage of Fat

Calculates the percentage of fat based on the provided input parameters.

- **URL:** `/calculate_percentage_of_fat/`
- **Method:** `POST`
- **Parameters:**
  - `weight_of_flask`: Weight of the flask (float)
  - `weight_of_oil`: Weight of the oil (float)
  - `weight_of_empty_flask`: Weight of the empty flask (float)
  - `weight_of_sample`: Weight of the sample (float)
- **Example Request Body:**
```json
{
    "weight_of_flask": 50.5,
    "weight_of_oil": 25.3,
    "weight_of_empty_flask": 30.1,
    "weight_of_sample": 10.0
}

```


- **Example Response:**
```json
{
    "percentage_of_fat": 35.2
}
```

### Calculate Percentage of Ash

Calculates the percentage of ash based on the provided input parameters.

- **URL:** /calculate_percentage_of_ash/
- **Method:** GET
- **Parameters:**
    - `weight_of_crucible:` Weight of the crucible (float)
    - `weight_of_ash:` Weight of the ash (float)
    - `weight_of_sample:` Weight of the sample (float)
- **Example Request Body:**
 ```json
 {
    "weight_of_crucible": 60.2,
    "weight_of_ash": 10.3,
    "weight_of_sample": 25.0
}

 ```
 - **Example Response:**
```json
{
    "percentage_of_fat": 8.12
}
```

## Calculate Percentage of Protein

Calculates the percentage of protein based on the provided input parameters.

- **URL:** `/calculate_percentage_of_protein/`
- **Method:** POST
- **Parameters:**
- **percentage_of_nitrogen:** Percentage of nitrogen (float)

**Example Request Body:**
```json
{
    "percentage_of_nitrogen": 4.5
}
```
**Example Response:**
```json
{
    "percentage_of_protein": 25.5
}

```
## Calculate Percentage of Moisture

Calculates the percentage of moisture based on the provided input parameters.

- **URL:** /calculate_percentage_of_moisture/
Method: POST
- **Parameters:**
`weight_of_crucible:` Weight of the crucible (float)
`weight_of_sample:` Weight of the sample (float)
`weight_of_drymatter:` Weight of the dry matter (float)

**Example Request Body:**
```json
{
    "weight_of_crucible": 70.2,
    "weight_of_sample": 30.5,
    "weight_of_drymatter": 15.0
}
```

**Example Response:**
```json
{
    "percentage_of_moisture": 72.0
}
```

## Calculate Determination of Total Solids

Calculates the determination of total solids based on the provided input parameters.

- **URL:** /calculate_determination_of_total_solids/
- **Method:** POST
- **Parameters:**
 `weight_of_crucible:` Weight of the crucible (float)
`weight_of_sample:` Weight of the sample (float)
`weight_of_dryresidue:` Weight of the dry residue (float)

**Example Request**
```json
{
    "weight_of_crucible": 80.2,
    "weight_of_sample": 40.5,
    "weight_of_dryresidue": 20.0
}
```
**Example Response**
```json
{
    "determination_of_total_solids": 16.0
}
```


## Calculate Determination of Volatile Solids

Calculates the determination of volatile solids based on the provided input parameters.

- **URL:** /calculate_determination_of_volatile_solids/
- **Method:** POST
- **Parameters:**
`weight_of_dryresidue:` Weight of the dry residue (float)
`weight_of_dryresidue_from_furnace:` Weight of the dry residue from the furnace (float)
`weight_of_sample:` Weight of the sample (float)
**Example Request Body:**
```json
{
    "weight_of_dryresidue": 25.0,
    "weight_of_dryresidue_from_furnace": 10.0,
    "weight_of_sample": 5.0
}
```
**Example Response:**
```json
{
    "determination_of_volatile_solids": 16.0
}
```


## Calculate Percentage of Fibre

Calculates the percentage of fibre based on the provided input parameters.

- **URL:** /calculate_percentage_of_fibre/
- **Method:** POST
- **Parameters:**
`weight_of_dryresidue:` Weight of the dry residue (float)
`weight_of_ash:` Weight of the ash (float)
`weight_of_sample:` Weight of the sample (float)

**Example Request:**
```json
{
    "weight_of_dryresidue": 30.0,
    "weight_of_ash": 5.0,
    "weight_of_sample": 10.0
}
```

**Example Response:**
```json
{
    "percentage_of_fibre": 25.0
}
```
