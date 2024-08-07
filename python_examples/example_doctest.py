def calculate_bank_account_value(initial_investment, interest_rate, time_in_years):
    """
    This function calculates my money by adding the interest to it every year:
    >>> calculate_bank_account_value(100, 0.05, 1)
    105.0

    And also takes into account the interest on interest:
    >>> calculate_bank_account_value(100, 0.05, 2)
    110.25


    should actually be: 110.25
    """
    return initial_investment*(1+interest_rate)**time_in_years
