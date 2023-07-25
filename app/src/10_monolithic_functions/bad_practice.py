"""
10 — Monolithic Functions

Using monolithic functions is considered an anti-pattern because they tend to
combine multiple tasks into a single function, making the code less modular
and harder to maintain, test, and understand.

Breaking down functionality into smaller functions with single
responsibilities results in more organized, reusable, and comprehensible code.
Here is an example:
"""


def process_payment(user_id, amount):
    """
    Process a payment for a user and send payment notification

    Args:
        user_id (str): The ID of the user.
        amount (float): The amount to be processed.

    Returns:
        str: A message indicating the payment result.
    """
    # Step 1: Check if the user is valid
    if not is_valid_user(user_id):
        return "Invalid user."

    # Step 2: Deduct the amount from the user's account
    if not deduct_amount_from_account(user_id, amount):
        return "Insufficient funds."

    # Step 3: Process the payment
    if not process_payment_gateway(amount):
        return "Payment processing failed."

    # Step 4: Notify the user about the successful payment
    send_payment_notification(user_id, amount)

    return "Payment successful."


def is_valid_user(user_id):
    pass


def deduct_amount_from_account(user_id, amount):
    pass


def process_payment_gateway(amount):
    pass


def send_payment_notification(user_id, amount):
    pass
