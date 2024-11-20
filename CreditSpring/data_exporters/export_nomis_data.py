from pandas import DataFrame
from datetime import datetime

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_parquet(df: DataFrame, **kwargs) -> None:
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filepath = f'data/bronze/raw_nomis_{timestamp}.parquet'
    df.to_parquet(filepath, engine='pyarrow')

