import asyncio

from m4i_atlas_core import (connectors_types_def, data_dictionary_types_def, ConfigStore,
                            create_type_defs, process_types_def, kubernetes_types_def)

from config import config
from credentials import credentials

async def create_types():

    response = await asyncio.gather(
        create_type_defs(data_dictionary_types_def),
        create_type_defs(connectors_types_def)
    )

    return response
# END create_types


def main():
    store = ConfigStore.get_instance()

    store.load({
        **config,
        **credentials
    })

    asyncio.run(create_type_defs(data_dictionary_types_def))
    asyncio.run(create_type_defs(process_types_def))
    asyncio.run(create_type_defs(connectors_types_def))
    asyncio.run(create_type_defs(kubernetes_types_def))
# END main


if __name__ == "__main__":
    main()
# END IF
