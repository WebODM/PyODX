# API Reference

## Node

::: pyodx.api.Node
    options:
      members:
        - __init__
        - from_url
        - info
        - options
        - version_greater_or_equal_than
        - create_task
        - get_task
        - url

## Task

::: pyodx.api.Task
    options:
      members:
        - info
        - output
        - cancel
        - remove
        - restart
        - download_zip
        - download_assets
        - wait_for_completion

## Types

::: pyodx.types.NodeInfo

::: pyodx.types.NodeOption

::: pyodx.types.TaskInfo

::: pyodx.types.TaskStatus

## Exceptions

::: pyodx.exceptions.GenericError

::: pyodx.exceptions.NodeServerError

::: pyodx.exceptions.NodeConnectionError

::: pyodx.exceptions.NodeResponseError

::: pyodx.exceptions.TaskFailedError

::: pyodx.exceptions.RangeNotAvailableError
