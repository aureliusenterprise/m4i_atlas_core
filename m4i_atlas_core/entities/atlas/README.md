# Data Object Model

This section provides an overview of how to use the data object model provided in the library. The data objects are designed to represent different types of entities, attributes, classifications, and other components in Aurelius Atlas.

The `entities` module is organized into two main submodules:

- `core`: This submodule includes data objects that correspond to the Apache Atlas API. These objects are used for representing entities, classifications, relationships, and other components as defined in Apache Atlas.
- `data_dictionary`: This submodule contains data objects that are specific to the Aurelius Atlas metamodel. These objects extend or customize the core data objects to better suit the requirements of the Aurelius Atlas platform.

Please find the table of contents for this `README` below.

- [Data Object Model](#data-object-model)
  - [Usage](#usage)
    - [Serialization and deserialization](#serialization-and-deserialization)
      - [From JSON to Instance](#from-json-to-instance)
      - [From Instance to JSON](#from-instance-to-json)
    - [Marshmallow Schema](#marshmallow-schema)
      - [Data Validation](#data-validation)
      - [Bulk Serialization and Deserialization](#bulk-serialization-and-deserialization)

## Usage

To use the data objects from the library in your code, you can easily import them. For example, if you want to work with the `Entity` data object, you can import it as follows:

```python
from m4i_atlas_core.entities import Entity
```

Once you have imported the desired data object, you can create instances, access their properties, and manipulate them as needed.

### Serialization and deserialization

Each data object is a `dataclass` and is designed to be easily serialized and deserialized using the `dataclasses_json` library. This allows for convenient conversion between JSON and the corresponding data object instances.

The `dataclasses_json` library provides additional features such as camelCase letter conversion and other customizations.

Below are some examples of how to use a data object, such as `Entity`, to convert between its instance and JSON representation.

#### From JSON to Instance

Suppose you have the following JSON representation of an entity:

```json
{
  "attributes": { "key": "value" },
  "created_by": "user",
  "guid": "12345"
}
```

You can convert it to an `Entity` instance using the following code:

```python
from m4i_atlas_core.entities import Entity

json_data = '''JSON string here'''
entity_instance = Entity.from_json(json_data)
```

#### From Instance to JSON

To convert an Entity instance back to its JSON representation, you can use the following code:

```python
json_data = entity_instance.to_json()
```

This will return a JSON string that represents the Entity instance.

### Marshmallow Schema

Each data object in the library is equipped with a built-in Marshmallow schema. These schemas are valuable tools for validating, serializing, and deserializing complex data structures. By utilizing Marshmallow schemas, you can ensure that the data being passed to or returned from the API adheres to the correct structure and data types.

To access the Marshmallow schema for any data object, use the `schema()` method:

```python
from m4i_atlas core import Entity

schema = Entity.schema()
```

#### Data Validation

Marshmallow schemas associated with the data objects in this library can be employed to perform data validation. The following example demonstrates how to use a Marshmallow schema to validate JSON input data:

```python
from m4i_atlas_core.entities import Entity

# Load the schema for the Entity data object
entity_schema = Entity.schema()

# Validate input data
input_data = {
    "guid": "123",
    "created_by": "user",
    "custom_attributes": {"key": "value"},
}

errors = entity_schema.validate(input_data)

if errors:
    print(f"Validation errors: {errors}")
else:
    print("Data is valid")
```

In this example, the `Entity` data object from the library is used to validate the `input_data` JSON using its associated Marshmallow schema. If the data is valid, the `validate` method will not return any errors, and the "Data is valid" message will be displayed. If the data is invalid, a dictionary containing the validation errors will be returned.

This approach can be applied to other data objects in the library for validating JSON input data using their respective Marshmallow schemas.

#### Bulk Serialization and Deserialization

Marshmallow schemas can be utilized for bulk serialization and deserialization of complex data structures. This is particularly useful when working with lists of data objects.

To serialize a list of data objects into a JSON format, you can use the dump method with the `many=True` option:

```python
from m4i_atlas_core import Entity

# Sample list of Entity data objects
entities = [
    Entity(guid="1", created_by="user1", custom_attributes={"key1": "value1"}),
    Entity(guid="2", created_by="user2", custom_attributes={"key2": "value2"}),
]

# Load the schema for the Entity data object
entity_schema = Entity.schema()

# Serialize the list of entities
serialized_data = entity_schema.dump(entities, many=True)

print("Serialized data:", serialized_data)
```

To deserialize a JSON list of data objects, you can use the load method with the `many=True` option:

```python
from m4i_atlas_core import Entity

# Sample JSON list of entity data
json_data = [
    {"guid": "1", "created_by": "user1", "custom_attributes": {"key1": "value1"}},
    {"guid": "2", "created_by": "user2", "custom_attributes": {"key2": "value2"}},
]

# Load the schema for the Entity data object
entity_schema = Entity.schema()

# Deserialize the JSON list of entities
deserialized_data = entity_schema.load(json_data, many=True)

print("Deserialized data:", deserialized_data)
```

In both examples, the `many=True` option is specified to indicate that the data being processed is a list. You can apply the same approach with other data objects in the library to perform bulk serialization and deserialization using their corresponding Marshmallow schemas.
