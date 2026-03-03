Below is a production-grade DynamoDB schema optimized specifically for your retirement planning app.

🎯 DESIGN PRINCIPLES

Single-table design

Query by partition key

Avoid scans

Keep reads to 1 query per screen

Model access patterns first

📘 ACCESS PATTERNS (MOST IMPORTANT)

We design the schema based on what the app needs to do.

Required Access Patterns

Get user profile

Get all clients for a user

Get one client with all related data (inputs, assets, scenarios)

Get all scenarios for a client

Add/update assets

Add new scenario calculation

If schema doesn’t optimize these, it’s wrong.

🏗️ FINAL DYNAMODB DESIGN
Table Name: retirement_app
Primary Key

PK (Partition Key)
SK (Sort Key)

Both are STRING.

🧱 ITEM STRUCTURE

We store everything under a USER partition.

1️⃣ User Profile Item

PK: USER#<user_id>
SK: PROFILE

Attributes:

user_id

email

password_hash

role

created_at

2️⃣ Client Item

PK: USER#<user_id>
SK: CLIENT#<client_id>

Attributes:

client_id

name

current_age

retirement_age

life_expectancy

created_at

3️⃣ Financial Input Item

PK: USER#<user_id>
SK: CLIENT#<client_id>#INPUT

Attributes:

annual_expense

inflation_rate

pre_ret_return

post_ret_return

step_up_rate

lumpsum_available

updated_at

4️⃣ Asset Items

PK: USER#<user_id>
SK: CLIENT#<client_id>#ASSET#<asset_id>

Attributes:

asset_id

asset_type

current_value (Decimal)

expected_return

created_at

Multiple asset rows per client.

5️⃣ Scenario Items

PK: USER#<user_id>
SK: CLIENT#<client_id>#SCENARIO#<scenario_id>

Attributes:

scenario_id

corpus_required

future_assets

deficit

fixed_sip

stepup_sip

generated_at

📊 HOW DATA IS QUERIED
Get All Clients for a User

Query:
PK = USER#123
SK begins_with "CLIENT#"

Filter out INPUT/ASSET/SCENARIO via prefix logic.

Get Full Client Detail (Single Query)

Query:
PK = USER#123
SK begins_with "CLIENT#abc123"

This returns:

CLIENT

INPUT

ASSET items

SCENARIO items

One query. No joins. Perfect DynamoDB usage.

🧠 WHY THIS IS STRONG

1 query per client screen

No scans

No joins

Minimal RCU usage

Linear scaling

Cost efficient

This is how senior engineers design DynamoDB schemas.

💰 COST BENEFITS

Because:

No secondary tables

No relational joins

On-demand billing

Minimal queries

This keeps your monthly cost extremely low.

🔐 OPTIONAL: GLOBAL SECONDARY INDEX (GSI)

Only add if needed.

Example:

If you want:
Login via email

Add GSI:

GSI1PK = EMAIL#<email>
GSI1SK = USER#<user_id>

This allows:
Query by email to find user.

Only 1 GSI needed.

🧮 IMPORTANT: FINANCIAL PRECISION

Store numeric values as:

Decimal type (DynamoDB supports it)

Never float.

In Python:
Use Decimal from decimal module.

Interview gold line:

“All monetary values are stored using DynamoDB Decimal to prevent floating-point precision errors.”

🗂️ EXAMPLE RECORD SET

For user 123 and client abc:

PK: USER#123
SK: PROFILE

PK: USER#123
SK: CLIENT#abc

PK: USER#123
SK: CLIENT#abc#INPUT

PK: USER#123
SK: CLIENT#abc#ASSET#1

PK: USER#123
SK: CLIENT#abc#ASSET#2

PK: USER#123
SK: CLIENT#abc#SCENARIO#1