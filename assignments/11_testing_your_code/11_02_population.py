import os
import sys


city_country = None
try:
    # first try a normal import by name
    import importlib
    city_mod = importlib.import_module("city_functions")
except Exception:
    # if that fails, try loading city_functions.py from the same directory
    city_mod = None
    module_path = os.path.join(os.path.dirname(__file__), "city_functions.py")
    if os.path.isfile(module_path):
        import importlib.util
        spec = importlib.util.spec_from_file_location("city_functions", module_path)
        if spec and spec.loader:
            city_mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(city_mod)
if city_mod and hasattr(city_mod, "city_country"):
    city_country = city_mod.city_country
def read_file_and_print(filename):
    try:
        with open(filename) as file:
            contents = file.read()
            print(contents.lower().count('at'))
    except FileNotFoundError:
        pass