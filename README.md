# UUID Genie

***UUID Genie*** is a microservice application that generates random UUIDs. The application was created using flask and includes a simple API.

### Table of Contents

- [What is a UUID?](#what-is-a-uuid)
- [How to Use](#how-to-use)
- [API Documentation](#api-documentation)
- [Other Information](#other-information)

#### What is a UUID?
**UUID** stands for **Universally Unique Identifier** (also referred to as *GUID* or *Globally Unique Identifiers*). UUIDs are 36-character alphanumeric strings that can be used to provide a unique identity to any collection or piece of information within a computing system. A UUID is a 128-bit value which is designed to be globally unique.

## How to Use

#### *Local Deployment*

To run this application locally, please follow the instructions below.

##### Requirements
- Python 3
##### Installation
```
git clone https://github.com/chrismannina/uuid-genie.git
cd uuid-genie
pip install -r requirements.txt
```
##### Start Up
```
python wsgi.py
```
- The service will be hosted on http://localhost:1337/
- Press ctrl+c to end hosting

#### *Heroku Deployment*

If interested, this repository comes ready to deploy to [Heroku](https://www.heroku.com/). The necessary ```Procfile``` and ```wsgi.py``` files are included. Simply create an account, create a new app, and follow the instructions to deploy. 

Current deployment is found [here](https://uuid-genie.herokuapp.com/api/uuid/).

## API Documentation

#### GET api/uuid/

Requests a randomly generated UUID. This method returns a JSON object that contains the generated UUID.

Example:    
```json
{
    "uuid": "2c315323-d9d4-4391-8545-17923a36c9d1"
}
```

#### GET api/uuid/number

Requests multiple UUIDs based on number input. This method returns a JSON object that contains the generated UUIDs.

Example: 
```json
{
    "uuid-1": "69549be2-4c92-4e04-b898-b87caec61b98", 
    "uuid-2": "99a0e2b3-27f1-4846-88ab-27548f638c9f", 
    "uuid-3": "643cc82c-faf4-469c-9776-fcbae6a44008"
}
```

### Other Information

All UUIDs generated from ***UUID Genie*** are version 4 (random). Read more about UUIDs and the different versions at [Wikipedia](https://en.wikipedia.org/wiki/Universally_unique_identifier).
