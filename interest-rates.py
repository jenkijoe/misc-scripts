from calendar import monthrange

def calculate_annual_interest(year, monthly_amount, annual_rate, starting_balance=0):
    """Calculate gross annual interest based on regular monthly payments.

    Args:
        year -- year of calculate (e.g. 2016), leap years are taken into consideration
        monthly_amount -- fixed notional monthly payment (e.g. 500)
        annual_rate -- annual gross interest rate as as a percentage (e.g. 5.0 is 5pc)
        starting_balance -- (optional) starting account balance (default: 0)
    """

    days_in_months = [monthrange(year, m)[1] for m in range(1,13)]
    monthly_balance = [starting_balance + m * monthly_amount for m in range(1,13)]
    totals = [d * mb for d, mb in zip(days_in_months, monthly_balance)]
    daily_rate = annual_rate / (100.0 * sum(days_in_months))
    gross_interest = sum(totals) * daily_rate
    print 'daily_rate: %.6lf%%, annual_rate: %d%%' % (100.0 * daily_rate, annual_rate)
    print 'gross interest for %d is %lf' % (year, gross_interest)
    return gross_interest

if __name__ == '__main__':
    calculate_annual_interest(2016, 500.0, 5.0)
