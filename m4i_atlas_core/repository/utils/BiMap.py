class BiMap(dict):
    """
    A `BiMap` (or "bidirectional map") is a map that preserves the uniqueness of its key-value mappings.
    """

    def __setitem__(self, key, value):
        # Remove any previous connections with these values
        if key in self:
            del self[key]
        # END IF

        if value in self:
            del self[value]
        # END IF

        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)
    # END __setitem__

    def __delitem__(self, key):
        dict.__delitem__(self, self[key])
        dict.__delitem__(self, key)
    # END __delitem__

    def __len__(self):
        return dict.__len__(self) // 2
    # END __len__
# END BiMap
