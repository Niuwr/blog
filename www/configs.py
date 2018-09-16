# -*- coding: utf-8 -*-


import config_default


def merge(defaults, overrides):
    newDict = dict()
    for k, v in defaults.items():
        if k in overrides:
            if isinstance(v, dict):
                newDict[k] = merge(v, overrides[k])
            else:
                newDict[k] = overrides[k]
        else:
            newDict[k] = v
    for k1, v1 in overrides.items():
        if k1 not in newDict:
            newDict[k1] = v1
    return newDict


configs = config_default.configs

try:
    import config_override
    configs = merge(configs, config_override.configs)
except ImportError as e:
    print(e)
