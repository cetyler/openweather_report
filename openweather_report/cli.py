"""Console script to get data from OpenWeatherMap."""

from .__init__ import __version__
import click
from .openweather import OpenWeatherMap
from datetime import datetime, timedelta, date
from pathlib import Path

API_TYPES = [
    "one_call",
    "current",
    "forecast",
    "historical",
]

SAVE_TYPES = [
    "json",
    "postgresql",
]


@click.command(context_settings={"ignore_unknown_options": True})
@click.argument(
    "api_type",
    type=click.Choice(
        API_TYPES,
        case_sensitive=False,
    ),
)
@click.argument(
    "latitude",
    type=float,
)
@click.argument(
    "longitude",
    type=float,
)
@click.argument(
    "api_key",
    type=str,
)
@click.option(
    "--weather_date",
    type=click.DateTime(formats=["%Y-%m-%d %H:%M"]),
    default=f"{(datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M')}",
    help="Put in the date to get the weather for a particular day.",
)
@click.option(
    "--save",
    type=click.Choice(SAVE_TYPES, case_sensitive=False),
    default="json",
)
@click.option(
    "--save_path",
    type=str,
    default=f"{datetime.today().strftime('%y%m%d-%H%M')}_data.json",
)
@click.version_option(__version__)
def main(
    api_type: str,
    latitude: float,
    longitude: float,
    api_key: str,
    weather_date: datetime,
    save: str,
    save_path: str,
) -> int:
    """Take user inputs and save to either file or database."""

    weather_data = OpenWeatherMap(
        longitude=longitude, latitude=latitude, api_key=api_key
    )

    weather_types = {
        # "current": weather_data.by_current(),
        "one_call": weather_data.by_one_call(),
        # "forecast": weather_data.by_forecast(),
        # "historical": weather_data.by_history(weather_data),
    }

    weather_types.get(api_type)

    if save == "json":
        with open(Path(save_path), "w") as file:
            file.write(weather_data.raw_data)
    elif save == "postgresql":
        pass

    return 0
