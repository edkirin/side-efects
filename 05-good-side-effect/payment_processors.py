from typing import List, Optional, Type

registry = None


class PaymentProcessor:
    name: str


class StripePaymentProcessor(PaymentProcessor):
    name = "Stripe"


class PaypalPaymentProcessor(PaymentProcessor):
    name = "Paypal"


class CorvusPaymentProcessor(PaymentProcessor):
    name = "Corvus"


class Registry(List[Type[PaymentProcessor]]):
    pass


if registry is None:
    registry = Registry()
    registry.append(StripePaymentProcessor)
    registry.append(PaypalPaymentProcessor)
    registry.append(CorvusPaymentProcessor)
