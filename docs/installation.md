# Installation

## From PyPI

```bash
pip install -U pyodx
```

## From Source

```bash
git clone https://github.com/WebODM/PyODX.git
cd PyODX
pip install -e .
```

## Running a NodeODX Instance

PyODX requires a running [NodeODX](https://github.com/WebODM/NodeODX) instance to process images. The easiest way to get one running is with Docker:

```bash
docker run -ti --rm -p 3000:3000 webodm/nodeodx
```

This will start a NodeODX instance on `localhost:3000`.

## Verifying the Installation

```python
from pyodx import Node

node = Node("localhost", 3000)
print(node.info())
```

If the node is running, this will print information about the NodeODX instance including its version, available memory, and CPU cores.
