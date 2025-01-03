""" Module to contain the utility functions for the gym tracker application. """

import os
from datetime import datetime


def export_daily_gym_plan_to_csv(
    gym_sets: dict, date: datetime = datetime.today()
) -> None:
    """
    Function that gets a dictionary of gym exercises and the number of sets for each exercise,
    and exports it to a CSV file with the given date as the filename.

    Args:
    -----
    gym_sets (dict): A dictionary of gym exercises and the number of sets for each exercise.
    date (datetime): The date to use for the filename. Defaults to today's date.
    """

    file_path: str = os.path.join(
        os.getcwd(),
        "gym_tracker/private_data",
        f"gym_plan_{date.strftime('%Y-%m-%d')}.csv",
    )
    with open(file_path, "w") as f:
        f.write("Exercise,Sets\n")
        for exercise, sets in gym_sets.items():
            f.write(f"{exercise},{sets}\n")


gym_plan = {}

export_daily_gym_plan_to_csv(gym_plan, datetime(2024, 12, 29))
