import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# DATA SCIENCE AND VISUALIZATION
# covid_df = pd.read_csv("covid_data.csv")
# covid_df["date"] = pd.to_datetime(covid_df["date"])
#
# covid_df["day"] = pd.DatetimeIndex(covid_df["date"]).day
# covid_df["month"] = pd.DatetimeIndex(covid_df["date"]).month
# covid_df["year"] = pd.DatetimeIndex(covid_df["date"]).year

# SETTING THE DISPLAY OPTION TO BE 1000 ROWS

# covid_df = covid_df.at[200, "new_cases"]
# covid_df = covid_df[["date", "new_cases"]]
# covid_df = covid_df.iloc[997]
# covid_df = covid_df.new_tests.first_valid_index()
# covid_df = covid_df.new_cases.last_valid_index()
# covid_df = covid_df.samples(20)

# total_deaths = covid_df.new_deaths.sum()
# total_cases = covid_df.new_cases.sum()
#
# death_rate = total_deaths/total_cases
# pd.set_option("max_rows", 1000)
# print(type(total_cases))
# print("Total Deaths: {:,.2f}\nTotal Cases: {:,.2f}\nDeath Rate: {:,.2f}".format(total_deaths, total_cases,
# death_rate))
# covid_df["date"] = pd.to_datetime(covid_df["date"])
# covid_df["date"] = covid_df["date"].dt.strftime("%d-%m-%y")

# high_cases = covid_df.date > "12/12/2021"
# covid_df = covid_df[high_cases]
# covid_df['positive_rate'] = covid_df.new_cases/covid_df.new_tests
# covid_df = covid_df.fillna(0)
# covid_df = covid_df.drop("positive_rate", axis=1)

# covid_df["date"] = pd.to_datetime(covid_df["date"])
# covid_df["day"] = pd.DatetimeIndex(covid_df["date"]).day
# covid_df["week"] = pd.DatetimeIndex(covid_df["date"]).weekday
# covid_df["month"] = pd.DatetimeIndex(covid_df["date"]).month
# covid_df["year"] = pd.DatetimeIndex(covid_df["date"]).year
#
# # covid_month_report = covid_df[covid_df.month == 5][["new_cases", "new_deaths", "new_tests"]].sum().apply(lambda
# x: # "{:,.2f}".format(x)) covid_month_5 = covid_df[covid_df.month == 5]["new_cases"] covid_df = covid_month_5[
# "new_cases"]
#
# # covid_df = covid_df[covid_df.week == 6][["new_cases", "new_deaths", "new_tests"]]
# # may_month_record = covid_df[covid_df.date >= "11/11/2021"][["new_cases", "date"]]
# # may_month_record.set_index(may_month_record["date"])
# # may_month_record.plot()
# # plt.show()
#
# covid_df.set_index(covid_df["date"], inplace=True)
# covid_df = covid_df.loc["2021-02-01": "2021-02-10"][["new_cases", "new_deaths", "new_tests"]]
# death_df = covid_df.loc["2021-02-01": "2021-02-10"][["new_deaths"]]
# covid_df.plot(title="Graph of new cases, new death against date", kind="pie")
# plt.show()
# print(covid_df)

# DATA VISUALIZATION
yield_apples = [0.324, 0.234, 0.923, 0.534, 0.234, 0.8943]
plt.hist(yield_apples)
plt.title("Apple yield graph")
# path = "Images/"
# os.mkdir(path)
# file_name = input("Enter the file name")
# plt.savefig(f"{path}{file_name}")
plt.show()
