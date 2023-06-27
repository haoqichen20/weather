### weather: a package to get weather information.
---

A general description of weather.

## Constructing the package.

**Bash**    Start a new project. Note the folder structure that is created.
```bash
Conda activate TechTalk
poetry new weather
cd weather
```

**Bash**    Create a new cli.py file in the weather directory. This will be our first "entry point" of the package.
```bash
touch weather/cli.py
open weather/cli.py
```

**Python**    Paste the following in cli.py. Note the following line, it judges whether the file is run by a Python interpreter.

if __name__ == "__main__":

```python
def cli():
  print("Hello world!")

if __name__ == "__main__":
  cli()
```

**Bash**    Try executing this as an independent Python script.
```bash
python weather/cli.py
```

**.toml**    Now let's start building a package for weather reporting. First, add the following to pyproject.toml file. This tells poetry that the cli.py will be turned into a console application (CLI software).
```bash
[tool.poetry.scripts]
weather = "weather.cli:cli"
```

**Bash**     Run the following to set up a virtual environment for the package. The VE isolate your package from everything else, even your conda environment. By default, the VE is stored in your home directory, but we don't care about that now.
```bash
poetry install
```

**Bash**    Congratulations! You now already have a minimal "package". Not useful, yet, but can be run (or even build and install).
```bash
# Make sure that you're running from where the pyproject.toml file is located.
poetry run weather
```

**Bash**    Now let's add useful things to the package. First, install the dependencies. Pay attention to what is changed in pyproject.toml.
```bash
poetry add requests #A python package for working with url
poetry add click #A python package for parsing user input from command line.
```

**Bash**    Create a "module" file that will store your python function:
```bash
touch weather/get_weather_metric.py
open weather/get_weather_metric.py
```

**Python**    Paste the following into get_weather_metric.py
```python
import requests

def get_weather_metric(metric: str, latitude: float, longitude: float):
    r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=' + str(latitude) + '&longitude=' + str(longitude) + '&current_weather=true')
    if r.status_code == 200:
        if metric in r.json()["current_weather"]:
            return(r.json()['current_weather'][metric])
        else:
            return("Metric not supported!")
    else:
        return("Open-Meteo is down!")
```

**Python**    Paste the following into cli.py, replace everything that was already in there. Note that we have "explicit relative importing", meaning we are importing from modules in the same package. Also note that we are taking three user input: metric, latitude, longitude.

```python
from .get_weather_metric import get_weather_metric
import click

@click.command()
@click.argument("metric", required=True)
@click.option("--latitude", "-lat", default=40.71, type=float, required=False, help="latitude (in degrees)")
@click.option("--longitude", "-lon", default=-74.01, type=float, required=False, help="longitude (in degrees)")
def cli(metric: str, latitude: float, longitude: float) -> None:
    output = get_weather_metric(metric=metric, 
                                latitude=latitude, 
                                longitude=longitude)
    print(output)

if __name__ == "__main__":
    cli()
```


## Testing the package.

**Bash**    Now, your package should be more useful. Try run the following, and it should give you the real-time temperature.
```bash
# Cambridge temperature
poetry run weather temperature --latitude=52.20 --longitude=0.13

# Guangzhou temperature
poetry run weather temperature --latitude=23.12 --longitude=113.26
```

**Bash**    Now, our package is largely complete. For best practice, create one more file:
```bash
touch weather/__main__.py
open weather/__main__.py
```

**Python**    Paste the following:
```python
"""
weather.__main__: executed when the weather directory is called as script.
"""

from .cli import cli

cli()
```

## Building and installing the package.

**Bash**    Now we can build our library:
```bash
poetry build
```

**Bash**    Two file will be created in the ./dist folder, one is a source code distribution, one is a binary wheel file. You can already install the package from the wheel file.
```bash
pip install weather-0.1.0-py3-none-any.whl #Your file might be named differently
```

**Bash**    Now your package is installed into your conda environment. Two things happen: you have made a CLI software that can directly be used:
```bash
# Guangzhou temperature
weather temperature --latitude=23.12 --longitude=113.26
```

**Python**    And you have make a "package" that can be imported.
```bash
touch test_weather.ipynb
```

```python
from weather import get_weather_metric
get_weather_metric("temperature", 52.19, 0.13)
```


## Publishing the package.

**Bash**    Finally, you need to register for a PyPI account, set up the credential stuff, and you can publish your package! Package name do need to be unique.
```bash
poetry publish
```