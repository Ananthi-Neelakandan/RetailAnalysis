import pytest
from lib.utils import get_spark_session

@pytest.fixture
def spark():
    print("Spark session is creating")
    spark_session = get_spark_session('LOCAL')
    yield spark_session
    print("Spark session has been created and started to stop spark session")
    spark_session.stop()
    print("stopped spark session")

@pytest.fixture
def expected_results(spark):
    expected_results_schema = 'state string, count integer'
    return spark.read\
        .format('csv')\
        .schema(expected_results_schema)\
        .load('data/state_aggregrate/test_results.csv')