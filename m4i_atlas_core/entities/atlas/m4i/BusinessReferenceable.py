from dataclasses import dataclass, field
from typing import Iterable, List

from dataclasses_json import LetterCase, dataclass_json
from ..core import (AttributeDef, Attributes, Entity, EntityBase,
                    EntityDef, EntityDefaultsBase, ObjectId,
                    TypeCategory, Cardinality)

from .M4IAttributes import M4IAttributesBase

# TypeDef for Entity & Relationships
m4i_referenceable_attributes_def = [
    AttributeDef(
        name="archimateReference",
        type_name="array<m4i_archimate_project>",
        cardinality=Cardinality.SET
    ),
    AttributeDef(
        name="source",
        type_name="array<m4i_source>",
        cardinality=Cardinality.SET
    )
]

m4i_referenceable_super_type = ["Referenceable"]

m4i_referenceable_def = EntityDef(
    category=TypeCategory.ENTITY,
    description="A type definition for a generic m4i Referenceable in the context of models4insight.com",
    name="m4i_referenceable",
    type_version="1.0",
    super_types=m4i_referenceable_super_type,
    attribute_defs=m4i_referenceable_attributes_def,
)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BusinessReferenceableAttributesBase(M4IAttributesBase):
    pass


# END BusinessReferenceableAttributesBase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BusinessReferenceableAttributesDefaultsBase(Attributes):
    archimate_reference: List[ObjectId] = field(default_factory=list)
    source: List[ObjectId] = field(default_factory=list)


# END BusinessReferenceableAttributesDefaultsBase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BusinessReferenceableAttributes(BusinessReferenceableAttributesDefaultsBase, BusinessReferenceableAttributesBase):
    pass


# END BusinessReferenceableAttributes


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BusinessReferenceableBase(EntityBase):
    attributes: BusinessReferenceableAttributes


# END BusinessReferenceableBase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BusinessReferenceableDefaultsBase(EntityDefaultsBase):
    pass


# END BusinessReferenceableDefaultsBase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BusinessReferenceable(Entity,
                            BusinessReferenceableDefaultsBase,
                            BusinessReferenceableBase):
    type_name: str = "m4i_referenceable"

    @classmethod
    def get_type_def(cls):
        return m4i_referenceable_def

    def get_referred_entities(self) -> Iterable[ObjectId]:
        """
        Returns the following references for this archimate project:
        * archimate_project
        * source
        """
        references = [
            *self.attributes.archimate_project,
            *self.attributes.source
        ]

        return filter(None, references)
    # END get_referred_entities

# END BusinessReferenceable
