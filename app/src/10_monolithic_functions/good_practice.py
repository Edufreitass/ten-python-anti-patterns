def process_payment(user_id, amount):
    """
    Process a payment for a user.

    Args:
        user_id (str): The ID of the user.
        amount (float): The amount to be processed.

    Returns:
        str: A message indicating the payment result.
    """
    if not is_valid_user(user_id):
        return "Invalid user."

    if not deduct_amount_from_account(user_id, amount):
        return "Insufficient funds."

    if not process_payment_gateway(amount):
        return "Payment processing failed."

    return "Payment successful."


def is_valid_user(user_id):
    pass


def deduct_amount_from_account(user_id, amount):
    pass


def process_payment_gateway(amount):
    pass


def send_payment_notification(user_id, amount):
    """
    Send a payment notification to the user.

    Args:
        user_id (str): The ID of the user.
        amount (float): The amount that was processed.

    Returns:
        None
    """
    send_notification(user_id, f"Payment of {amount} processed successfully.")


def send_notification(user_id, param):
    pass


# Main function
def make_payment(user_id, amount):
    """
    Make a payment for a user and send a payment notification if successful.

    Args:
        user_id (str): The ID of the user.
        amount (float): The amount to be processed.

    Returns:
        str: A message indicating the payment result.
    """
    result = process_payment(user_id, amount)
    if result == "Payment successful.":
        send_payment_notification(user_id, amount)
    return result
