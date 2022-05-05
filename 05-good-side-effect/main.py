from payment_processors import registry


def main():
    for payment_processor in registry:
        print(payment_processor.name)


if __name__ == "__main__":
    main()
