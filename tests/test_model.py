from src.models.customer import Customer

def test_customer_model():
    customer = Customer()

    assert customer is not None