#! /usr/bin/env python3
__all__ = list()

# import common functions
from . import common
for name, val in common.__dict__.items():
    if callable(val) or name in {'ZERO_THRESH'}:
        vars()[name] = val; __all__.append(name)

# load plugin functions
from . import contact_network, transmission_network, sample_times, viral_phylogeny_seeds, viral_phylogeny_trans, mutation_rates, ancestral_sequence, sequence_evolution
PLUGIN_FUNCTIONS = {
    "Contact Network": contact_network.PLUGIN_FUNCTIONS,
    "Transmission Network": transmission_network.PLUGIN_FUNCTIONS,
    "Sample Times": sample_times.PLUGIN_FUNCTIONS,
    "Viral Phylogeny (Seeds)": viral_phylogeny_seeds.PLUGIN_FUNCTIONS,
    "Viral Phylogeny (Transmissions)": viral_phylogeny_trans.PLUGIN_FUNCTIONS,
    "Mutation Rates": mutation_rates.PLUGIN_FUNCTIONS,
    "Ancestral Sequence": ancestral_sequence.PLUGIN_FUNCTIONS,
    "Sequence Evolution": sequence_evolution.PLUGIN_FUNCTIONS,
}
