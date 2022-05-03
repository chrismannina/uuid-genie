# UUID Genie

***UUID Genie*** is a microservice application that generates random UUIDs. The application was created using flask and includes a simple API.

## What is a UUID?
**UUID** stands for **Universally Unique Identifier** (also referred to as *GUID* or *Globally Unique Identifiers*). UUIDs are 36-character alphanumeric strings that can be used to provide a unique identity to any collection or piece of information within a computing system. A UUID is a 128-bit value which is designed to be globally unique.

## API Documentation

### GET /uuid

Requests a randomly generated UUID. This method returns a JSON object that contains the generated UUID.

Example: {"UUID": "2c315323-d9d4-4391-8545-17923a36c9d1"}
