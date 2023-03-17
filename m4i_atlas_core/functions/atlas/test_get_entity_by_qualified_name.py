import asyncio

from scripts.config import config
from scripts.credentials import credentials
from ... import ConfigStore, register_atlas_entity_types, data_dictionary_entity_types
from .get_entity_by_qualified_name import get_entity_by_qualified_name


def test_get_entity_by_qualified_name():
    """
    To test the get entity given the qualified Name and Type Name.

    This test assumes that a m4i_data_domain with name test_domain is in atlas

    """
    store = ConfigStore.get_instance()

    store.load({
        **config,
        **credentials
    })
    register_atlas_entity_types(data_dictionary_entity_types)
    qualified_name = "test_domain"
    type_name = "m4i_data_domain"

    entity = asyncio.run(get_entity_by_qualified_name(qualified_name=qualified_name, type_name=type_name))

    assert entity.type_name == type_name
    assert entity.attributes.qualified_name == qualified_name
    assert entity.attributes.definition is not None

# END test_get_entity_by_qualified_name
