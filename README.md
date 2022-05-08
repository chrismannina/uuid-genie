# UUID Genie

***UUID Genie*** is a microservice application that generates random UUIDs. The application was created using flask and includes a simple API.

## What is a UUID?
**UUID** stands for **Universally Unique Identifier** (also referred to as *GUID* or *Globally Unique Identifiers*). UUIDs are 36-character alphanumeric strings that can be used to provide a unique identity to any collection or piece of information within a computing system. A UUID is a 128-bit value which is designed to be globally unique.

## API Documentation

### GET api/uuid/

Requests a randomly generated UUID. This method returns a JSON object that contains the generated UUID.

Example:    
```json
{
    "uuid": "2c315323-d9d4-4391-8545-17923a36c9d1"
}
```

### GET api/uuid/number

Requests multiple UUIDs based on number input. This method returns a JSON object that contains the generated UUIDs.

Example: 
```json
{
    "uuid-1": "69549be2-4c92-4e04-b898-b87caec61b98", 
    "uuid-2": "99a0e2b3-27f1-4846-88ab-27548f638c9f", 
    "uuid-3": "643cc82c-faf4-469c-9776-fcbae6a44008"
}
```

#### Other Information

All UUIDs generated from ***UUID Genie*** are version 4 (random). Read more about UUIDs and the different versions at [Wikipedia](https://en.wikipedia.org/wiki/Universally_unique_identifier).
