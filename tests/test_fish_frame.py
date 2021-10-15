from FishProject.app import fish_frame as ff
import pandas as pd


def test_get_fish_dataframes():
    monday, tuesday, umpday = ff.get_fish_dataframes()  # Getting the 3 dataframes
    assert isinstance(monday, pd.DataFrame)  # Checking one of them is a dataframe
