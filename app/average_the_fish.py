import pandas as pd


def average_the_fish(df_mon, df_tues, df_idk):  # Taking 3 dataframes as argument

    # This creates a dataframe called df_mon_avg out of df_mon. It is not yet averaged
    # columns just names the columns of the new dataframe
    df_mon_avg = pd.DataFrame(df_mon, columns=['Species', 'Weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width'])
    # Grouping by 'Species', because we want the average per species
    # .mean() because we want to calculate the mean
    # .reset_index and the previous line might not be totally necessary, but I'm not about to fix what ain't broke
    df_mon_avg = df_mon_avg.groupby('Species').mean().reset_index()

    df_tues_avg = pd.DataFrame(df_tues, columns=['Species', 'Weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width'])
    df_tues_avg = df_tues_avg.groupby('Species').mean().reset_index()

    df_idk_avg = pd.DataFrame(df_idk, columns=['Species', 'Weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width'])
    df_idk_avg = df_idk_avg.groupby('Species').mean().reset_index()

    # Here we append the dataframes for the tuesday and idk averages to the dataframe of the monday averages
    df_mon_avg = df_mon_avg.append(df_tues_avg)
    df_mon_avg = df_mon_avg.append(df_idk_avg)
    # Doing the same groupby() averaging calculation to average the 3 dataframes
    # Technically this doesn't weight for number of rows, which doesn't make a difference now, but could
    df_mon_avg = df_mon_avg.groupby('Species').mean().reset_index()

    # Returning the averages per species across the 3 days
    return df_mon_avg
