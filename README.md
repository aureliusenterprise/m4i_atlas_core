# M4I Atlas Core
This library contains all core functionality for connecting to atlas, defining type definitions, and their respective type class used to create and get atlas entities.
To push atlas entities of a certain type, the type must be defined in atlas and the request must be of a certain format. 
The type definitions can be found in their respective file under ``m4i_atlas_core/entities/atlas`` along with their atlas class that formats requests into the correct shape to send to the atlas api. 
The library currently holds type definitions that are used in the Aurelius Governance solution and are available here in 4 sets of definitions.
The following type definitions sets are available :
``
data_dictionary_types_def, process_types_def, connectors_types_def and kubernetes_types_def.
``
For more detail on this please look at the Atlas Type documentation.


## Installation

Please ensure your `Python` environment is on version `3.9`. Some dependencies do not work with any previous versions of `Python`.

To install `m4i-atlas-core` and all required dependencies to your active `Python` environment, please run the following command from the project root folder:

```
pip install -e .
```

## Configurations and Credentials
In the `scripts` directory.
Please make a copy of `config.sample.py` and `credentials.sample.py` and rename the files to `config.py` and `credentials.py` respectively.
Please set the configuration parameters and credentials for `atlas`.

| Name | Required | Description | 
|---|---|---|
| atlas.server.url | True |  The Server Url that Atlas runs on, with '/api/atlas' post fix. | 
| data.dictionary.path | False | The Path to the Data Dictionary to be loaded.| 
| atlas.credentials.username | True | The Username to be used to access the Atlas Instance. | 
| atlas.credentials.password | True |The Password to be used to access the Atlas Instance must correspond to the Username given. | 


## Execution
1. Create the Python Environment. How to do this can be found in this file under `Installation` 
2. Fill in the Configurations and Credentials as indicated in this file under `Configurations and Credentials` 
3. Run `scripts\load_type_defs.py` in the terminal to load the definitions.
The main function in `load_type_defs.py` can be adjusted to determine which set of type definitions to load.
Please note that if a subset of the set already exist, then the loading of the type definitions will fail. 

## Testing

This project uses `pytest` as its unit testing framework.
To run the unit tests, please install `pytest` and then execute the `pytest` command from the project root folder.

Unit tests are grouped per module.
Unit test modules are located in the same folder as their respective covered modules.
They can be recognized by the `test__` module name prefix, followed by the name of the covered module.




