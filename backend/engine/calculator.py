from decimal import Decimal

# 5.1 Time Calculations
def get_years_to_retirement(current_age: Decimal, retirement_age: Decimal) -> Decimal:
    years = retirement_age - current_age
    if years <= 0:
        raise ValueError("Years to retirement must be > 0")
    return years

def get_retirement_years(retirement_age: Decimal, life_expectancy: Decimal) -> Decimal:
    years = life_expectancy - retirement_age
    if years <= 0:
        raise ValueError("Retirement years must be > 0")
    return years

# 5.2 Inflate Expense to Retirement
def calculate_inflated_expense(annual_expense: Decimal, inflation_rate: Decimal, years_to_retirement: Decimal) -> Decimal:
    return annual_expense * ((Decimal('1') + inflation_rate) ** years_to_retirement)

# 5.3 Corpus Required (Growing Annuity Model)
def calculate_corpus_required(inflated_expense: Decimal, post_ret_return: Decimal, inflation_rate: Decimal, retirement_years: Decimal) -> Decimal:
    r = post_ret_return
    g = inflation_rate
    n = retirement_years
    
    if r <= g:
        raise ValueError("Unsustainable withdrawal rate (r <= g)")
    
    term = Decimal('1') - ((Decimal('1') + g) / (Decimal('1') + r)) ** n
    return inflated_expense * (term / (r - g))

# 5.4 Future Value of Existing Assets
def calculate_asset_future_value(current_value: Decimal, pre_ret_return: Decimal, years_to_retirement: Decimal) -> Decimal:
    return current_value * ((Decimal('1') + pre_ret_return) ** years_to_retirement)

def calculate_future_assets(assets: list[Decimal], pre_ret_return: Decimal, years_to_retirement: Decimal) -> Decimal:
    return sum(
        calculate_asset_future_value(asset, pre_ret_return, years_to_retirement)
        for asset in assets
    )

# 5.5 Deficit
def calculate_deficit(corpus_required: Decimal, future_assets: Decimal, lumpsum_available: Decimal) -> Decimal:
    deficit = corpus_required - future_assets - lumpsum_available
    return max(deficit, Decimal('0'))

# 5.6 Fixed Monthly SIP
def calculate_fixed_sip(deficit: Decimal, pre_ret_return: Decimal, years_to_retirement: Decimal) -> Decimal:
    if deficit == Decimal('0'):
        return Decimal('0')
    
    monthly_rate = pre_ret_return / Decimal('12')
    months = years_to_retirement * Decimal('12')
    
    annuity_factor = (((Decimal('1') + monthly_rate) ** months) - Decimal('1')) / monthly_rate
    return deficit / annuity_factor

# 5.7 Step-Up SIP (Growing Annuity)
def calculate_stepup_sip(deficit: Decimal, pre_ret_return: Decimal, step_up_rate: Decimal, years_to_retirement: Decimal) -> Decimal:
    if deficit == Decimal('0'):
        return Decimal('0')
        
    r = pre_ret_return
    s = step_up_rate
    n = years_to_retirement
    
    if r != s:
        numerator = deficit * (r - s)
        denominator = ((Decimal('1') + r) ** n) - ((Decimal('1') + s) ** n)
        return numerator / denominator
    else:
        return deficit / (n * ((Decimal('1') + r) ** (n - Decimal('1'))))

# 6. WEALTH PROJECTION LOGIC
def project_wealth_pre_retirement(wealth: Decimal, pre_ret_return: Decimal, annual_contribution: Decimal) -> Decimal:
    return wealth * (Decimal('1') + pre_ret_return) + annual_contribution

def project_wealth_post_retirement(wealth: Decimal, post_ret_return: Decimal, expense: Decimal) -> Decimal:
    return wealth * (Decimal('1') + post_ret_return) - expense
