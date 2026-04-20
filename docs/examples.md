# Examples

## Get Node Info

Connect to a node and retrieve its information:

```python
from pyodx import Node, exceptions

node = Node.from_url("http://localhost:3000?token=abc")

try:
    print(node.info())
except exceptions.NodeConnectionError as e:
    print("Cannot connect: " + str(e))
```

## Create a Task

Upload images, process them, and download results:

```python
import os
from pyodx import Node, exceptions

node = Node("localhost", 3000)

try:
    # Start a task
    print("Uploading images...")
    task = node.create_task(
        ["images/image_1.jpg", "images/image_2.jpg"],
        {"dsm": True, "orthophoto-resolution": 4},
    )
    print(task.info())

    try:
        # Block until the task is finished
        task.wait_for_completion()

        print("Task completed, downloading results...")
        task.download_assets("./results")
        print("Assets saved in ./results (%s)" % os.listdir("./results"))

        # Restart task and this time compute dtm
        task.restart({"dtm": True})
        task.wait_for_completion()

        print("Task completed, downloading results...")
        task.download_assets("./results_with_dtm")
        print("Assets saved in ./results_with_dtm (%s)" % os.listdir("./results_with_dtm"))

    except exceptions.TaskFailedError as e:
        print("\n".join(task.output()))

except exceptions.NodeConnectionError as e:
    print("Cannot connect: %s" % e)
except exceptions.NodeResponseError as e:
    print("Error: %s" % e)
```

## Upload Progress Callback

Track upload progress with a callback:

```python
from pyodx import Node

node = Node("localhost", 3000)

def progress(percent):
    print("Upload: %.2f%%" % percent)

task = node.create_task(
    ["image_1.jpg", "image_2.jpg"],
    progress_callback=progress,
)
```

## Task Status Callback

Monitor task status while waiting for completion:

```python
from pyodx import Node

node = Node("localhost", 3000)

task = node.create_task(["image_1.jpg", "image_2.jpg"])

def status_update(info):
    print("Status: %s, Progress: %.1f%%" % (info.status, info.progress))

task.wait_for_completion(status_callback=status_update)
```
