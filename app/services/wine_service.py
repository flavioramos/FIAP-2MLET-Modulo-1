import os
import unicodedata

import pandas as pd
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from app.extensions import db
from app.models.wine_model import Comercio, ExpEspumantes, ExpSuco, ExpVinho, ImpEspumantes, ImpFrescas, \
    ImpPassas, ImpSuco, ImpVinhos, ProcessaAmericanas, ProcessaMesa, ProcessaViniferas, ProcessaSemclass, Producao

start_year = 1970
end_year = 2023

keys = {'Comercio': 'produto', 'ExpEspumantes': 'pais', 'ExpSuco': 'pais', 'ExpUva': 'pais', 'ExpVinho': 'pais',
        'ImpEspumantes': 'pais', 'ImpFrescas': 'pais', 'ImpPassas': 'pais', 'ImpSuco': 'pais', 'ImpVinhos': 'pais',
        'ProcessaAmericanas': 'cultivar', 'ProcessaMesa': 'cultivar', 'ProcessaSemclass': 'cultivar',
        'ProcessaViniferas': 'cultivar', 'Producao': 'produto'}

categories = [
    'Comercio',
    'ExpEspumantes',
    'ExpSuco',
    'ExpUva',
    'ExpVinho',
    'ImpEspumantes',
    'ImpFrescas',
    'ImpPassas',
    'ImpSuco',
    'ImpVinhos',
    'ProcessaAmericanas',
    'ProcessaMesa',
    'ProcessaSemclass',
    'ProcessaViniferas',
    'Producao'
]


def transform_string(input_string):
    normalized_string = unicodedata.normalize('NFKD', input_string)
    ascii_string = normalized_string.encode('ASCII', 'ignore').decode('utf-8')
    return ascii_string.lower()


def load_data(model, key_field, model_fields, delimiter):
    try:
        # Read CSV file into DataFrame
        df = pd.read_csv(os.path.join(os.getcwd(), 'cache', model.__name__), delimiter=delimiter)

        for _, row in df.iterrows():
            # Create a dictionary for the key field and dynamic year fields
            data = {transform_string(key_field): row[key_field]}
            year_data = {f'y_{year}': row[str(year)] for year in range(start_year, end_year + 1)}

            # Combine the key field data with the year data
            data.update(year_data)

            # Add any additional static data fields
            for field in model_fields:
                data[transform_string(field)] = row[field]

            # Create an instance of the model with the data
            entry = model(**data)

            if not db.session.query(model).filter_by(
                    **{transform_string(key_field): getattr(entry, transform_string(key_field))}).first():
                db.session.add(entry)

        db.session.commit()
        print(f"Data loaded successfully for model {model.__name__}")

    except (FileNotFoundError, pd.errors.ParserError) as e:
        print(f"Error reading the CSV file {model.__name__}.csv: {e}")
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error saving data to the database: {e}")


def load_all():
    load_data(Comercio, 'control', ['Produto'], ';')
    load_data(ExpEspumantes, 'País', [], ';')
    load_data(ExpSuco, 'País', [], ';')
    load_data(ExpVinho, 'País', [], ';')
    load_data(ImpEspumantes, 'País', [], ';')
    load_data(ImpFrescas, 'País', [], ';')
    load_data(ImpPassas, 'País', [], ';')
    load_data(ImpSuco, 'País', [], ';')
    load_data(ImpVinhos, 'País', [], ';')
    load_data(ProcessaAmericanas, 'control', ['cultivar'], '\t')
    load_data(ProcessaMesa, 'control', ['cultivar'], '\t')
    load_data(ProcessaSemclass, 'control', ['cultivar'], '\t')
    load_data(ProcessaViniferas, 'control', ['cultivar'], ';')
    load_data(Producao, 'control', ['produto'], ';')
    print("Wine CSV data loaded.")


def get_by_year(modelName, year):
    model = globals()[modelName]
    check_valid_year(year)
    year_column = getattr(model, f'y_{year}')
    query = select(getattr(model, keys[modelName]), year_column).filter(year_column.isnot(None))
    queryResult = db.session.execute(query).all()
    result = {}
    for row in queryResult:
        result[row[0]] = row[1]

    return result


def get_all_years(modelName):
    result = {}
    for year in range(start_year, end_year):
        result[year] = get_by_year(modelName, year)
    return result


def get_all():
    result = {}
    for year in range(start_year, end_year):
        yearData = {}
        for category in categories:
            yearData[year] = get_by_year(category, year)
        result[year] = yearData
    return result


def check_valid_year(year):
    if year < start_year or year > end_year:
        raise ValueError(f"Year must be between {start_year} and {end_year}")
