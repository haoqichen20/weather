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
