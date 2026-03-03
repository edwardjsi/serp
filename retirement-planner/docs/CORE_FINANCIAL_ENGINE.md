# 5. CORE FINANCIAL ENGINE (DETERMINISTIC)

All rates expressed as decimals (6% = 0.06)

---

## 5.1 Time Calculations

years_to_retirement = retirement_age - current_age
retirement_years = life_expectancy - retirement_age

Validation:

* years_to_retirement > 0
* retirement_years > 0

---

## 5.2 Inflate Expense to Retirement

inflated_expense = annual_expense × (1 + inflation_rate)^years_to_retirement

---

## 5.3 Corpus Required (Growing Annuity Model)

Let:
P = inflated_expense
r = post_ret_return
g = inflation_rate
n = retirement_years

If r ≠ g:

corpus_required =
P × [ (1 - ((1+g)/(1+r))^n ) / (r - g) ]

If r = g:

corpus_required = P × n / (1 + r)

Constraint:
If r ≤ g → raise warning (unsustainable withdrawal rate)

---

## 5.4 Future Value of Existing Assets

For each asset:

asset_future_value =
current_value × (1 + pre_ret_return)^years_to_retirement

future_assets = sum(asset_future_value)

---

## 5.5 Deficit

deficit = corpus_required - future_assets - lumpsum_available

If deficit < 0 → deficit = 0

---

## 5.6 Fixed Monthly SIP

monthly_rate = pre_ret_return / 12
months = years_to_retirement × 12

annuity_factor = ((1 + monthly_rate)^months - 1) / monthly_rate

fixed_sip = deficit / annuity_factor

If deficit = 0 → fixed_sip = 0

---

## 5.7 Step-Up SIP (Growing Annuity)

Let:
r = pre_ret_return
s = step_up_rate
n = years_to_retirement

If r ≠ s:

stepup_sip =
deficit × (r - s) /
((1 + r)^n - (1 + s)^n)

If r = s:

stepup_sip =
deficit / (n × (1 + r)^(n-1))

---

## 5.8 Real Return (Optional)

real_return = (1 + r) / (1 + g) - 1

Alternative corpus:

corpus_required =
inflated_expense ×
((1 - (1 + real_return)^(-n)) / real_return)

---

# 6. WEALTH PROJECTION LOGIC (FOR GRAPH)

Pre-retirement yearly loop:

wealth[t] =
wealth[t-1] × (1 + pre_ret_return)

* annual_contribution[t]

Post-retirement:

wealth[t] =
wealth[t-1] × (1 + post_ret_return)

* expense[t]

expense[t] grows at inflation.