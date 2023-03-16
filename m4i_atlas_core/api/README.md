# API

This README provides documentation for the M4I Atlas Core `api` module, which is designed for interacting with the Apache Atlas API and retrieving authentication tokens from Keycloak.

The API module is divided into two submodules:

1. `atlas`: This submodule contains functions for interacting with the Apache Atlas API, enabling you to create, read, update, and delete entities and their related metadata.

2. `auth`: This submodule is responsible for retrieving authentication tokens from Keycloak, which are required for accessing and utilizing the Apache Atlas API.

## Atlas

The `atlas` submodule provides a collection of functions to interact with the Apache Atlas API. These functions allow you to create, retrieve, update, and delete various entities, types, and glossaries in Apache Atlas.

### Available Functions

Here is the list of available functions in the Atlas submodule:

- `create_entities`
- `create_glossary`
- `create_glossary_category`
- `create_glossary_term`
- `create_type_defs`
- `delete_entity_hard`
- `delete_entity_soft`
- `get_entities_by_attribute`
- `get_entities_by_type_name`
- `get_entity_audit_events`
- `get_entity_audit`
- `get_entity_by_guid`
- `get_type_def`
- `get_glossary`
- `get_glossary_by_guid`
- `get_glossary_category_by_guid`
- `get_glossary_term_by_guid`
- `get_type_defs`
- `get_lineage_by_guid`
- `get_lineage_by_qualified_name`
- `get_classification_defs`
- `update_type_defs`

To use any of these functions, import them from the Atlas submodule:

```python
from m4i_atlas_core import create_entities, create_glossary, ...
```

### Usage

This section includes examples on how to use each API function.

#### `create_entities`

The `create_entities` function allows you to create or update multiple entities in Apache Atlas in bulk. It takes in a variable number of `Entity` objects and an optional dictionary of referred entities. It also accepts an optional access token for authentication purposes.

Here's an example of how to use the `create_entities` function:

```python
from m4i_atlas_core import Entity, create_entities

entity1 = Entity(...)
entity2 = Entity(...)

mutations = await create_entities(entity1, entity2)

print(mutations)
```

This example creates the two given entities in Apache Atlas. The `create_entities` function returns an `EntityMutationResponse` object containing the details of the entities created or updated.

#### `create_glossary`

The `create_glossary` function allows you to create a new glossary in Apache Atlas. It takes in a `Glossary` object and an optional access token for authentication purposes.

Here's an example of how to use the `create_glossary` function:

```python

from m4i_atlas_core import Glossary, create_glossary

glossary = Glossary(...)

created_glossary = await create_glossary(glossary)

print(created_glossary)
```

This example creates the given glossary in Apache Atlas. The `create_glossary` function returns a `Glossary` object containing the details of the created glossary.

#### `create_glossary_category`

The `create_glossary_category` function allows you to create a new glossary category in Apache Atlas. It takes in a `GlossaryCategory` object and an optional access token for authentication purposes.

Here's an example of how to use the `create_glossary_category` function:

```python
from m4i_atlas_core import GlossaryCategory, create_glossary_category

category = GlossaryCategory(...)

created_category = await create_glossary_category(category)

print(created_category)
```

This example creates the given glossary category in Apache Atlas. The `create_glossary_category` function returns a `GlossaryCategory` object containing the details of the created category.

## Auth

The Auth submodule provides functionality for retrieving authentication tokens from Keycloak, which are required for accessing the Apache Atlas API.

### Usage

The `get_keycloak_token` function in the Auth submodule is responsible for retrieving an access token from a Keycloak instance.

To use the get_keycloak_token function, first import it:

```python
from m4i_atlas_core import get_keycloak_token
```

Next, call the function to retrieve an access token. You can provide your own Keycloak instance and credentials or rely on the pre-configured parameters from the ConfigStore. If you need to use multi-factor authentication, provide the one-time access token (TOTP) as well.

```python
# Example: Using pre-configured parameters
access_token = get_keycloak_token()

# Example: Using custom Keycloak instance and credentials
access_token = get_keycloak_token(keycloak=my_keycloak_instance, credentials=("my_username", "my_password"))

# Example: Using multi-factor authentication (TOTP)
access_token = get_keycloak_token(totp="123456")
```

The access_token can then be used to authenticate requests to the Apache Atlas API.

### ConfigStore

The `get_keycloak_token` function relies on the following values from the `ConfigStore`:

| Key                             | Description                                                                                                                                                                                                                                                      | Required |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `keycloak.server.url`           | The url of the Keycloak server. In case of a local connection, this includes the hostname and the port. E.g. `http://localhost:8180/auth`. In case of an external connection, provide a fully qualified domain name. E.g. `https://www.models4insight.com/auth`. | `True`   |
| `keycloak.client.id`            | The name of the Keycloak client.                                                                                                                                                                                                                                 | `True`   |
| `keycloak.realm.name`           | The name of the Keycloak realm.                                                                                                                                                                                                                                  | `True`   |
| `keycloak.client.secret.key`    | The public RS256 key associated with the Keycloak realm.                                                                                                                                                                                                         | `True`   |
| `keycloak.credentials.username` | The username of the Keycloak user.                                                                                                                                                                                                                               | `False`  |
| `keycloak.credentials.password` | The password of the Keycloak user.                                                                                                                                                                                                                               | `False`  |

[Please find more detailed documentation about `ConfigStore` here.](../config/README.md)
