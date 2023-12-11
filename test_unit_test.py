import pytest
from lib.configReader import get_app_config
from lib.dataReader import read_customers, read_orders
from lib.dataManipulation import count_orders_state, count_all_order_status

def test_first_case():
    application_config_results = get_app_config('LOCAL')
    customer_path = application_config_results.get('customers.file.path')
    assert customer_path == 'data/customers.csv'

def test_third_case(spark, expected_results):
    customers_df = read_customers(spark, 'LOCAL')
    actual_count = count_orders_state(customers_df)
    assert actual_count.collect() == expected_results.collect()

## passing values based on generic values
@pytest.mark.latest()
@pytest.mark.parametrize(
    "status, count",
    [("CLOSED", 7556),
    ("PENDING_PAYMENT", 15030)]
)
def test_fourth_case(spark, status, count):
    orders_df = read_orders(spark, 'LOCAL')
    get_generic_status_count = count_all_order_status(orders_df, status)
    assert get_generic_status_count == count