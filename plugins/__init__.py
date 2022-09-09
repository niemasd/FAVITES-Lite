#! /usr/bin/env python3
__all__ = list()

# import common functions
from . import common
for name, val in common.__dict__.items():
    if callable(val):
        vars()[name] = val; __all__.append(name)

# load plugin functions
from . import contact_network, transmission_network
PLUGIN_FUNCTIONS = {
    "Contact Network": contact_network.PLUGIN_FUNCTIONS,
    "Transmission Network": transmission_network.PLUGIN_FUNCTIONS,
}
