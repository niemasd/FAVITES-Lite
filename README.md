# FAVITES-Lite
FAVITES-Lite is a lightweight framework for viral transmission and evolution simulation. It is a spin-off of [FAVITES](https://github.com/niemasd/FAVITES) that is designed to be much simpler and faster, but at the expense of reduced flexibility. FAVITES-Lite was designed to incorporate the just key functionality of FAVITES that most users require. In general, we strongly recommend using FAVITES-Lite instead of FAVITES for epidemic simulation projects.

## Installation
FAVITES-Lite is written in Python and depends on the following Python packages:

* [NumPy](https://numpy.org/)
* [SciPy](https://scipy.org/)
* [TreeSAP](https://github.com/niemasd/treesap)
* [TreeSwift](https://github.com/niemasd/TreeSwift)

FAVITES-Lite also calls many command-line tools, which must be installed in your `PATH`:

* [CoaTran](https://github.com/niemasd/CoaTran)
* [GEMF_FAVITES](https://github.com/niemasd/GEMF)
* [NiemaGraphGen](https://github.com/niemasd/NiemaGraphGen)
* [Seq-Gen](https://github.com/rambaut/Seq-Gen)

To install FAVITES-Lite itself, you can either download the latest [release](https://github.com/niemasd/FAVITES-Lite/releases), or you can clone this GitHub repository:

```bash
git clone https://github.com/niemasd/FAVITES-Lite.git
```

For convenience, you can also use the [FAVITES-Lite Docker image](https://hub.docker.com/r/niemasd/favites_lite), or you can refer to the [`Dockerfile`](https://github.com/niemasd/FAVITES-Lite/blob/main/Dockerfile#L9-L42) for installation commands.

## Usage
There are two primary components to FAVITES-Lite: the [Config Designer](config_designer.py) and the [FAVITES-Lite executable](favites_lite.py).

### Config Designer
The [Config Designer (`config_designer.py`)](config_designer.py) is a tool that helps users design a FAVITES-Lite configuration file for their unique simulation experiment design. Unlike the original FAVITES, in which users had to navigate the documentation to manually design a configuration file, the FAVITES-Lite Config Designer guides the user and includes detailed information about all model choices for all steps of the simulation workflow.

To enter the Config Designer start page, which has a file navigator for creating a new config file or loading an existing one, simply execute the Config Designer without any arguments:

```bash
config_designer.py
```

If you already known the name of the new config file you wish to create or the existing config file you wish to view/modify, you can execute the Config Designer with the path to the desired config file as the only argument:

```bash
config_designer.py example/example.json
```

### FAVITES-Lite Executable
The [FAVITES-Lite executable (`favites_lite.py`)](favites_lite.py) actually executes a given simulation experiment, and it can be used as follows:

```
usage: favites_lite.py [-h] -c CONFIG -o OUTPUT [--overwrite] [--quiet] [--version]

  -h, --help                   show this help message and exit
  -c CONFIG, --config CONFIG   FAVITES-Lite Config File
  -o OUTPUT, --output OUTPUT   Output Directory
  --overwrite                  Overwrite output directory if it exists (default: False)
  --quiet                      Suppress Log Messages (default: False)
  --version                    Show FAVITES-Lite version (default: False)
```
