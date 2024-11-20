import io
import pandas as pd
import requests
from pandas import DataFrame

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(**kwargs) -> DataFrame:
    url = 'https://www.nomisweb.co.uk/api/v01/dataset/NM_1037_1.data.csv?date=latest&geography=1157630013...1157630093&c_hlqpuk11=0&c_ethpuk11=0&measures=20100'
    response = requests.get(url)
    response.raise_for_status()
    df = pd.read_csv(io.StringIO(response.text))
    return df


@test
def test_output(df, *args) -> None:
    assert df is not None, 'The output is undefined'

@test 
def test_rows(df, *args) -> None:
    assert len(df.index) >= 80, 'Data should have at least 80 rows.'


