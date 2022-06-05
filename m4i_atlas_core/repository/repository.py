from random import randrange
from typing import Optional, Union

from ..entities import Entity
from .utils import BiMap


class Repository:

    registry = BiMap()

    def generate_label(self):
        """
        Generates a unique label for use in the registry.
        """

        label = -len(self.registry) + 1

        while label in self.registry:
            label = randrange(-10000, -len(self.registry))
        # END LOOP

        return label
    # END generate_label

    def register(self, entity: Entity, label: Optional[Union[str, int]] = None, ignore_known=True, use_guid=True):
        """
        Adds the entity to the registry with the given `label`.
        If no `label` is given, one is generated.

        If the entity is already registered, assigns it the given `label` instead.

        If the label is already registered, assigns it the given `entity` instead.
        """

        if entity in self.registry and ignore_known:
            return
        # END IF

        if use_guid:
            label = entity.guid
        elif label is None:
            label = self.generate_label()
        # END IF

        self.registry[label] = entity
    # END register

# END Repository
