from FishProjectCommits.app import average_the_fish as atf
from FishProjectCommits.app import fish_frame as ff
import pandas as pd
import numpy as np


def test_average_the_fish():
    monday, tuesday, umpday = ff.get_fish_dataframes()  # Getting the 3 dataframes
    df_avg = atf.average_the_fish(monday, tuesday, umpday)  # Getting the average dataframe

    assert isinstance(df_avg, pd.DataFrame)  # Checking one of them is a dataframe
    assert isinstance(df_avg.iat[1, 1], np.floating)  # Checking one of the numbers in the dataframe is a float
