# med_NER
A Medical NER to extract drug name from the text and extract its data from the db.
This project makes use of spacy, scispacy for identifying the drug names from a given text. The APIs are created using the Django framework


## Prerequisties

- Create an env file with the following content -

> NAME = name_of_db
> USER = db_user_name
> PASSWORD = db_password
> HOST = host
> PORT = port

## APIs

- POST: BASE_URL/search
  
  This API returns the data corresponding for the identified drugs from the db.
  
  payload: 
  ```json
  {
    "data" : "take paracetamol 100mg for 10 days after having dinner"
  }
  ```
  
- POST: BASE_URL/insert

  This API can be used to insert the data to DB. There must a column called salt_name with names of compounds to be identified.
  
  ```json
  {
            "sku_id": "",
            "product_id": "",
            "sku_name": "ABC (500 mg)",
            "price": "15",
            "manufacturer_name": "XYZ",
            "salt_name": "Paracetamol",
            "drug_form": "Tablet",
            "pack_size": "10 Tablet",
            "strength": "500 mg",
            "product_banned_flag": "",
            "unit": "1 Tablet",
            "price_per_unit": "1.5"
        }
   ```



