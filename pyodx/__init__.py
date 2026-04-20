"""
PyODX is a library for easily creating orthophotos, DEMs, 3D models and point clouds from aerial images via the `NodeODX API`_. It's an official `WebODM`_ project.

Installation:
-------------

``pip install -U pyodx``

Simple usage:
-------------

   >>> import os
   >>> from pyodx import Node
   >>> n = Node('localhost', 3000)
   >>> task = n.create_task(['examples/images/image_1.jpg', 'examples/images/image_2.jpg'], {'dsm': True})
   >>> task.wait_for_completion()
   >>> os.listdir(task.download_assets("results"))[0:2]
   ['3d_tiles', 'cameras.json']

To test these examples you need to start a NodeODX node via:

``docker run -ti -p 3000:3000 webodm/nodeodx``

Code Samples:
-------------
 * `Create Task`_
 * `Get Node Info`_

Getting Help / Reporting Issues:
--------------------------------

PyODX is in active development. If you find an issue please `report it`_. We welcome contributions, see the `GitHub`_ page for more information.

License: BSD 3-Clause, see LICENSE for more details.

.. _NodeODX API:
   https://github.com/WebODM/NodeODX/blob/master/docs/index.adoc
.. _WebODM:
    https://webodm.org
.. _Create Task:
   https://github.com/WebODM/PyODX/blob/master/examples/create_task.py
.. _Get Node Info:
   https://github.com/WebODM/PyODX/blob/master/examples/get_node_info.py
.. _report it:
    https://github.com/WebODM/PyODX/issues
.. _`GitHub`:
    https://github.com/WebODM/PyODX
"""

name = "pyodx"
from .api import Node, Task