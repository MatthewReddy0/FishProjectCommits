import app.fish_frame as ff
import app.average_the_fish as atf
import app.upload_fish as uf

df_mon, df_tues, df_idk = ff.get_fish_dataframes()
df_avg = atf.average_the_fish(df_mon, df_tues, df_idk)
uf.upload_the_fish(df_avg)
