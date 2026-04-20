# Migrate from PyODM

[PyODM](https://pypi.org/project/pyodm/) continues to work fine for most use cases, but will no longer receive updates.

For new code, simply change your imports from pyodm to pyodx:

```python
# from pyodm import Node
from pyodx import Node
```

We also renamed `OdmError` to `GenericError`:

```python
# from pyodm.exceptions import OdmError
from pyodm.exceptions import GenericError
```

There are no other changes.