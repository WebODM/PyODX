import doctest

if __name__ == "__main__":
    import pyodx
    doctest.testmod(pyodx)

    from pyodx import api
    doctest.testmod(api)