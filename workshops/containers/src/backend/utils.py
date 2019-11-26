#
# Memento
# Backend
# Utilites
#


# reverse mapping - swap mappings ordering
# returns reverse mapping
def reverse_mapping(mapping):
    return [ (b, a) for a, b in mapping ]

# maps the given object to a dict using given mapping
# mapping is a list of (field, key)
# returns the mappped dictionary
def map_dict(obj, mapping):
    obj_dict = {}
    for field, key in mapping:
        if hasattr(obj, field):
            obj_dict[key] = getattr(obj, field)
    return obj_dict

# maps data from map_dict into object fields on the given object
# using the given mapping (a list of (key, field))
# returns the obj with the updated fields
def map_obj(obj, map_dict, mapping):
    for key, field in mapping:
        if key in map_dict:
            setattr(obj, field, map_dict[key])
    return obj

# maps the keys of the dict into the corresponding key in mapping
# returns a dict with the keys of mapping mapped
def map_keys(map_dict, mapping):
    alt_dict = {}
    for key, alt_key in mapping:
        if key in map_dict:
            alt_dict[alt_key] = map_dict[key]
    return alt_dict

# apply skip and limit to the given list of items
# returns the updated list
def apply_bound(items, skip=0, limit=None):
    items = items[skip:]
    if not limit is None: items = items[:limit]

    return items

# attempts to parse the given value as a boolean
# returns the value as True or False
def parse_bool(value):
    assert(type(value) == bool or type(value) == str)

    if type(value) == bool: return value
    elif type(value) == str:
        val_lower = value.lower()

        if val_lower == "true" or val_lower == "t" or val_lower == "1": return True
        elif val_lower == "false" or val_lower == "f" or val_lower == "0": return False
        else: raise NotImplementedError(f"Unparsable bool value: {value}")
