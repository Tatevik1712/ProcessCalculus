__author__ = "Саргсян Татев ИВТ-23"
"""
Анализ COVID-19 данных через pandas
"""

import pandas as pd
import matplotlib.pyplot as plt
import ssl

def load_data(url: str):
    """
    Загружает CSV данные (с отключенной SSL проверкой)
    """
    ssl._create_default_https_context = ssl._create_unverified_context

    df = pd.read_csv(url)
    df["Date_reported"] = pd.to_datetime(df["Date_reported"])

    return df


def filter_countries(df: pd.DataFrame, countries: list) -> pd.DataFrame:
    """
    Фильтрует данные по выбранным странам
    :param df: исходный DataFrame
    :param countries: список стран
    :return: отфильтрованный DataFrame
    """
    return df[df["Country"].isin(countries)]


def plot_cases(df: pd.DataFrame, countries: list):
    """
    Строит график заражений
    :param df: DataFrame
    :param countries: список стран
    """
    plt.figure()

    for country in countries:
        country_df = df[df["Country"] == country]

        plt.plot(
            country_df["Date_reported"],
            country_df["Cumulative_cases"],
            label=country
        )

    plt.title("COVID-19: Общее число заразившихся")
    plt.xlabel("Дата")
    plt.ylabel("Случаи заражения")
    plt.legend()
    plt.grid()

    plt.show()


def plot_deaths(df: pd.DataFrame, countries: list):
    """
    Строит график смертности
    :param df: DataFrame
    :param countries: список стран
    """
    plt.figure()

    for country in countries:
        country_df = df[df["Country"] == country]

        plt.plot(
            country_df["Date_reported"],
            country_df["Cumulative_deaths"],
            label=country
        )

    plt.title("COVID-19: Общее число смертей")
    plt.xlabel("Дата")
    plt.ylabel("Смерти")
    plt.legend()
    plt.grid()

    plt.show()


def main():
    url = "https://srhdpeuwpubsa.blob.core.windows.net/whdh/COVID/WHO-COVID-19-global-data.csv"

    df = load_data(url)

    print(df.head())

    countries = ["Estonia", "Germany", "United States", "Brazil", "China", "Iran", "Argentina", "Italy"]
    df_filtered = filter_countries(df, countries)

    plot_cases(df_filtered, countries)
    plot_deaths(df_filtered, countries)

if __name__ == "__main__":
    main()