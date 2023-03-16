# Data Object Model

This section provides an overview of how to use the data object model provided in the library. The data objects are designed to represent different types of entities, attributes, classifications, and other components in Aurelius Atlas.

## Usage

You can simply import any data object from the library to use it in your code. For example, to use the `Entity` data object:

```python
from m4i_atlas_core import Entity
```

### Serialization and deserialization

Each data object is a `dataclass` and is designed to be easily serialized and deserialized using the `dataclasses_json` library. This allows for convenient conversion between JSON and the corresponding data object instances.

The `dataclasses_json` library provides additional features such as camelCase letter conversion and other customizations.

Below are some examples of how to use a data object, such as `Entity`, to convert between its instance and JSON representation.

#### From JSON to Instance

Suppose you have the following JSON representation of an entity:

```json
{
  "classifications": [],
  "create_time": 1628769600.0,
  "created_by": "admin",
  "custom_attributes": { "example_key": "example_value" },
  "guid": "12345",
  "home_id": null,
  "is_incomplete": false,
  "labels": ["label1", "label2"],
  "meanings": [],
  "provenance_type": 0,
  "proxy": false,
  "relationship_attributes": {},
  "status": "ACTIVE",
  "update_time": 1628769600.0,
  "updated_by": "admin",
  "version": 0
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
