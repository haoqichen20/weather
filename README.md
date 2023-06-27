### weather: a package to get weather information.
---

A general description of weather.

## Constructing the package.

Start a new project

```bash
Conda activate TechTalk
poetry new weather
cd weather
```

Create a new cli.py file in the weather directory:

```bash
touch weather/cli.py
```

```python
def cli():
  print("Hello world!")

if __name__ == "__main__":
  cli()
```