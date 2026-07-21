from src.models.customer import Customer

def test_customer_model():
    customer = Customer(
        customerID="0001",
        gender="Male"
    )

    assert customer.customerID == "0001"
    assert customer.gender == "Male"