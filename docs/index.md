# PyODX

**A Python SDK for creating orthophotos, DEMs, 3D models and point clouds from aerial images via the [NodeODX API](https://github.com/WebODM/NodeODX/blob/master/docs/index.adoc).**

PyODX is an official [WebODM](https://webodm.org) project.

## Quick Start

To test these examples start a [NodeODX](https://github.com/WebODM/NodeODX) node via:

``docker run -ti --rm -p 3000:3000 webodm/nodeodx``

Then:

```bash
pip install pyodx
```

```python
from pyodx import Node

node = Node("localhost", 3000)

task = node.create_task(
    ["images/image_1.jpg", "images/image_2.jpg"],
    {"dsm": True}
)
task.wait_for_completion()
task.download_assets("./results")
```

## Features

- Create processing tasks from aerial images
- Monitor task progress with callbacks
- Download orthophotos, DEMs, point clouds and 3D models
- Parallel uploads and downloads
- Webhook support for task completion notifications

## Requirements

- Python 3.6+

## Next Steps

- [Examples](examples.md) — full code examples
- [API Reference](reference.md) — complete API documentation
