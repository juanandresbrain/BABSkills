# test model report

**Workspace:** Enterprise Analytics QA  
**Dataset ID:** 7189254e-1977-48af-b618-cad24b1710cd  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| Calendar | 47 | 0 |  |
| Locations (Store MDM) | 42 | 0 |  |
| Product Images | 5 | 0 |  |
| Transactions (JumpMind) | 36 | 0 |  |
| Business Units (JumpMind) | 4 | 0 |  |
| Users (JumpMind) | 13 | 0 |  |
| Retail Transactions (JumpMind) | 46 | 2 |  |
| Retail Transaction Discounts (JumpMind) | 17 | 0 |  |
| Retail Lines (JumpMind) | 95 | 6 |  |
| Retail Line Discounts (JumpMind) | 34 | 3 |  |
| Retail Return Lines (JumpMind) | 18 | 0 |  |
| Tax Lines (JumpMind) | 33 | 0 |  |
| Tender Settlement Lines (JumpMind) | 26 | 4 |  |
| Tender Lines (JumpMind) | 26 | 6 |  |
| Tender Card Lines (JumpMind) | 13 | 0 |  |
| Measure Table | 1 | 85 |  |
| Activated Gift Cards (JumpMind) | 15 | 0 |  |
| Tax Authorities (JumpMind) | 6 | 0 |  |
| Tax Groups (JumpMind) | 4 | 0 |  |
| Tenders (JumpMind) | 9 | 0 |  |
| Transaction Summaries (JumpMind) | 58 | 0 |  |
| Exchange rates (Dynamics) | 10 | 0 |  |
| Products (PLM) | 145 | 0 |  |
| Global Products (JumpMind) | 9 | 0 |  |
| LocalDateTable_93238a4d-3b84-4f59-be36-5ff69cd43d4e | 8 | 0 |  |
| LocalDateTable_5c168f80-25a0-4efa-bf12-7e60a5e48a8e | 8 | 0 |  |
| LocalDateTable_96e4d140-fa2d-4e56-b7de-334a44a64da4 | 8 | 0 |  |
| LocalDateTable_e60a4d41-cac0-48db-97a2-d983bc81d3d0 | 8 | 0 |  |
| LocalDateTable_3d5229f5-4fe7-4b35-bcee-e6627e744a8b | 8 | 0 |  |
| LocalDateTable_4e98b083-f78d-424d-99f6-7928ae69c16f | 8 | 0 |  |
| LocalDateTable_d7529a08-6398-426c-a772-644494cce77d | 8 | 0 |  |
| LocalDateTable_b4b70347-805d-4ca2-8d32-4fa167522777 | 8 | 0 |  |
| LocalDateTable_dab62035-2669-4a22-aaec-2632fabcb287 | 8 | 0 |  |
| LocalDateTable_7860c2a2-378f-46bb-b7a0-5185b792d99e | 8 | 0 |  |
| LocalDateTable_f2bca1c6-828c-4094-bbfb-4763519fe956 | 8 | 0 |  |
| LocalDateTable_b03143ec-a3af-4798-a56d-95139da8728a | 8 | 0 |  |
| LocalDateTable_a4dcc117-e9b4-4b16-adee-f4f9946a165d | 8 | 0 |  |
| LocalDateTable_49ea6d5f-fb07-4da6-9fb1-51d02a2bc45a | 8 | 0 |  |
| LocalDateTable_c696f59a-66cf-41b7-8b07-5195859bcbaa | 8 | 0 |  |
| LocalDateTable_61a52116-af4f-4f93-b42a-bae69dfe4c27 | 8 | 0 |  |
| LocalDateTable_389f283c-edb3-40f4-ac2f-a231a1db0d91 | 8 | 0 |  |
| LocalDateTable_252fac6a-2c05-4ea6-811c-020b777cc24e | 8 | 0 |  |
| LocalDateTable_9d389bc1-31cd-4452-87ee-b48b7c91fa60 | 8 | 0 |  |
| LocalDateTable_561eb354-c83a-4fad-8bed-dff84b95c91b | 8 | 0 |  |
| LocalDateTable_12349c08-94b3-429b-ab24-c10ba82ff847 | 8 | 0 |  |
| LocalDateTable_f84ef23a-3840-4b6e-99ba-dd3ef26f713e | 8 | 0 |  |
| LocalDateTable_cb103ba7-2fb4-402a-895c-2b84dc3f5dbd | 8 | 0 |  |
| LocalDateTable_5c26535c-2005-449c-bab9-ba36531e9c6d | 8 | 0 |  |
| LocalDateTable_e402dd30-9f43-4d4f-a4fb-db08f436e975 | 8 | 0 |  |
| LocalDateTable_f9c3d338-cbb0-41fb-86dc-21dc0f34e12b | 8 | 0 |  |
| LocalDateTable_a2f29b70-36e2-4209-aa2b-d342e1e0f8c6 | 8 | 0 |  |
| LocalDateTable_bbd477ee-7054-427a-998e-b90a9310acd8 | 8 | 0 |  |
| LocalDateTable_db9f588e-3a3b-4808-9922-3c9443a2e153 | 8 | 0 |  |

## Measures

### Retail Transactions (JumpMind).GAAP Flash Sales

```sql
EXTERNALMEASURE("GAAP Flash Sales", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Retail Transactions (JumpMind).Endless Aisle Flash Sales

```sql
EXTERNALMEASURE("Endless Aisle Flash Sales", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Retail Lines (JumpMind).Returned Tender Amount | Without Loyalty Card Numbers (Native)

```sql
EXTERNALMEASURE("Returned Tender Amount | Without Loyalty Card Numbers (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Retail Lines (JumpMind).Returned Tender Amount | With Loyalty Card Numbers (Native)

```sql
EXTERNALMEASURE("Returned Tender Amount | With Loyalty Card Numbers (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Retail Lines (JumpMind).Returned Tender Amount (Native)

```sql
EXTERNALMEASURE("Returned Tender Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Retail Lines (JumpMind).Modification Amount TE (Native)

```sql
EXTERNALMEASURE("Modification Amount TE (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Retail Lines (JumpMind).Modification Amount TE (Native) | Sales

```sql
EXTERNALMEASURE("Modification Amount TE (Native) | Sales", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Retail Lines (JumpMind).Modification Amount TE (Native) | Returns

```sql
EXTERNALMEASURE("Modification Amount TE (Native) | Returns", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Retail Line Discounts (JumpMind).Modification Amount (Native)

```sql
EXTERNALMEASURE("Modification Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Retail Line Discounts (JumpMind).Modification Amount (Native) | Returns

```sql
EXTERNALMEASURE("Modification Amount (Native) | Returns", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Retail Line Discounts (JumpMind).Modification Amount (Native) | Sales

```sql
EXTERNALMEASURE("Modification Amount (Native) | Sales", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Tender Settlement Lines (JumpMind).Safe Amount

```sql
EXTERNALMEASURE("Safe Amount", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Tender Settlement Lines (JumpMind).Till Amount

```sql
EXTERNALMEASURE("Till Amount", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Tender Settlement Lines (JumpMind).Store Funds Amount

```sql
EXTERNALMEASURE("Store Funds Amount", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Tender Settlement Lines (JumpMind).Over/Short Amount (Native)

```sql
EXTERNALMEASURE("Over/Short Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Tender Lines (JumpMind).Total Tender Amount (Native)

```sql
EXTERNALMEASURE("Total Tender Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Tender Lines (JumpMind).Total Tender Amount (Native) | Store Sales

```sql
EXTERNALMEASURE("Total Tender Amount (Native) | Store Sales", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Tender Lines (JumpMind).Total Tender Amount (Native) | Order In Store

```sql
EXTERNALMEASURE("Total Tender Amount (Native) | Order In Store", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Tender Lines (JumpMind).Debit Tender Amount (Native)

```sql
EXTERNALMEASURE("Debit Tender Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Tender Lines (JumpMind).Credit Tender Amount (Native)

```sql
EXTERNALMEASURE("Credit Tender Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Tender Lines (JumpMind).Balance Tender Amount (Native)

```sql
EXTERNALMEASURE("Balance Tender Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Transactions

```sql
EXTERNALMEASURE("Retail Transactions", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Donation Amount (Native)

```sql
EXTERNALMEASURE("Donation Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Units

```sql
EXTERNALMEASURE("Retail Units", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Donation Units

```sql
EXTERNALMEASURE("Donation Units", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Sales TE | Actual (Native)

```sql
EXTERNALMEASURE("Retail Sales TE | Actual (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Discount Amount TE (Native)

```sql
EXTERNALMEASURE("Retail Discount Amount TE (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.AUR (Native)

```sql
EXTERNALMEASURE("AUR (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.DPT (Native)

```sql
EXTERNALMEASURE("DPT (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.UPT

```sql
EXTERNALMEASURE("UPT", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Sales TE | Actual (USD)

```sql
EXTERNALMEASURE("Retail Sales TE | Actual (USD)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.AUR (USD)

```sql
EXTERNALMEASURE("AUR (USD)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Discount Amount TE (USD)

```sql
EXTERNALMEASURE("Retail Discount Amount TE (USD)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Donation Amount (USD)

```sql
EXTERNALMEASURE("Donation Amount (USD)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.DPT (USD)

```sql
EXTERNALMEASURE("DPT (USD)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Transactions | Loyalty Members

```sql
EXTERNALMEASURE("Retail Transactions | Loyalty Members", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Bonus Club Capture Rate

```sql
EXTERNALMEASURE("Bonus Club Capture Rate", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Average Retail Discount Amount TE Per Unit (Native)

```sql
EXTERNALMEASURE("Average Retail Discount Amount TE Per Unit (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Average Retail Discount Amount TE Per Unit (USD)

```sql
EXTERNALMEASURE("Average Retail Discount Amount TE Per Unit (USD)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Average Retail Discount Amount TE Per Transaction (Native)

```sql
EXTERNALMEASURE("Average Retail Discount Amount TE Per Transaction (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Average Retail Discount Amount TE Per Transaction (USD)

```sql
EXTERNALMEASURE("Average Retail Discount Amount TE Per Transaction (USD)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Discount Percentage TE

```sql
EXTERNALMEASURE("Retail Discount Percentage TE", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Sales TE | Full-Price (Native)

```sql
EXTERNALMEASURE("Retail Sales TE | Full-Price (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Sales TE | Full-Price (USD)

```sql
EXTERNALMEASURE("Retail Sales TE | Full-Price (USD)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Units | Accessories

```sql
EXTERNALMEASURE("Retail Units | Accessories", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Units | Clothes

```sql
EXTERNALMEASURE("Retail Units | Clothes", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Units | Footwear

```sql
EXTERNALMEASURE("Retail Units | Footwear", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Units | Friend

```sql
EXTERNALMEASURE("Retail Units | Friend", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Units | Human

```sql
EXTERNALMEASURE("Retail Units | Human", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Units | Human Clothes

```sql
EXTERNALMEASURE("Retail Units | Human Clothes", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Units | Stuffed

```sql
EXTERNALMEASURE("Retail Units | Stuffed", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Units | Stuffers

```sql
EXTERNALMEASURE("Retail Units | Stuffers", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Units | Unstuffed

```sql
EXTERNALMEASURE("Retail Units | Unstuffed", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Units | Stuffers | Scents

```sql
EXTERNALMEASURE("Retail Units | Stuffers | Scents", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Units | Stuffers | Sounds

```sql
EXTERNALMEASURE("Retail Units | Stuffers | Sounds", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Transactions | Party Packages

```sql
EXTERNALMEASURE("Retail Transactions | Party Packages", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Total Sales TE | Full-Price (Native)

```sql
EXTERNALMEASURE("Total Sales TE | Full-Price (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Total Sales TE | Actual (Native)

```sql
EXTERNALMEASURE("Total Sales TE | Actual (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Total Sales TE | Actual (USD)

```sql
EXTERNALMEASURE("Total Sales TE | Actual (USD)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Total Sales TE | Full-Price (USD)

```sql
EXTERNALMEASURE("Total Sales TE | Full-Price (USD)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Non-Retail Units

```sql
EXTERNALMEASURE("Non-Retail Units", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Non-Retail Sales TE | Actual (Native)

```sql
EXTERNALMEASURE("Non-Retail Sales TE | Actual (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Non-Retail Sales TE | Actual (USD)

```sql
EXTERNALMEASURE("Non-Retail Sales TE | Actual (USD)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Transactions | Military Discounts

```sql
EXTERNALMEASURE("Retail Transactions | Military Discounts", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Retail Profit TE (USD)

```sql
EXTERNALMEASURE("Retail Profit TE (USD)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Non-Retail Profit TE (USD)

```sql
EXTERNALMEASURE("Non-Retail Profit TE (USD)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Cash (Deposit)

```sql
EXTERNALMEASURE("Cash (Deposit)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Bank (Deposit)

```sql
EXTERNALMEASURE("Bank (Deposit)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.FBR (Over)/Short

```sql
EXTERNALMEASURE("FBR (Over)/Short", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Total Visa Payment Amount (Native)

```sql
EXTERNALMEASURE("Total Visa Payment Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Total MasterCard Payment Amount (Native)

```sql
EXTERNALMEASURE("Total MasterCard Payment Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Total Visa/MasterCard Payment Amount (Native)

```sql
EXTERNALMEASURE("Total Visa/MasterCard Payment Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Total Debit & Credit Payment Amount (Native)

```sql
EXTERNALMEASURE("Total Debit & Credit Payment Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Total Electronic Payment Amount (Native)

```sql
EXTERNALMEASURE("Total Electronic Payment Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Total E-Wallet Payment Amount (Native)

```sql
EXTERNALMEASURE("Total E-Wallet Payment Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Activated Gift Cards Gross Amount TE (USD)

```sql
EXTERNALMEASURE("Activated Gift Cards Gross Amount TE (USD)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Activated Gift Card Units

```sql
EXTERNALMEASURE("Activated Gift Card Units", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Activated Gift Cards Gross Amount TE (Native)

```sql
EXTERNALMEASURE("Activated Gift Cards Gross Amount TE (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Activated Gift Cards Net Amount TE (Native)

```sql
EXTERNALMEASURE("Activated Gift Cards Net Amount TE (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Activated Gift Cards Net Amount TE (USD)

```sql
EXTERNALMEASURE("Activated Gift Cards Net Amount TE (USD)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Redeemed Gift Card Units

```sql
EXTERNALMEASURE("Redeemed Gift Card Units", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Redeemed Gift Card Tender Amount (Native)

```sql
EXTERNALMEASURE("Redeemed Gift Card Tender Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Money Tax Amount (Native)

```sql
EXTERNALMEASURE("Money Tax Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Non-Taxable Amount (Native)

```sql
EXTERNALMEASURE("Non-Taxable Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Non-Taxable Amount (Native) | Merchandise

```sql
EXTERNALMEASURE("Non-Taxable Amount (Native) | Merchandise", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Non-Taxable Amount (Native) | Fees

```sql
EXTERNALMEASURE("Non-Taxable Amount (Native) | Fees", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Tax Amount (Native)

```sql
EXTERNALMEASURE("Tax Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Tax Variance (Native)

```sql
EXTERNALMEASURE("Tax Variance (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Taxable Amount (Native)

```sql
EXTERNALMEASURE("Taxable Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Taxable Amount (Native) | Merchandise

```sql
EXTERNALMEASURE("Taxable Amount (Native) | Merchandise", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Taxable Amount (Native) | Fees

```sql
EXTERNALMEASURE("Taxable Amount (Native) | Fees", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Check (Deposit)

```sql
EXTERNALMEASURE("Check (Deposit)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Travelers Checks (Null)

```sql
EXTERNALMEASURE("Travelers Checks (Null)", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Total American Express Payment Amount (Native)

```sql
EXTERNALMEASURE("Total American Express Payment Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.GL Amount Expected

```sql
EXTERNALMEASURE("GL Amount Expected", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Total Discover Payment Amount (Native)

```sql
EXTERNALMEASURE("Total Discover Payment Amount (Native)", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Receipt Quantity

```sql
EXTERNALMEASURE("Receipt Quantity", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Donation Quantity

```sql
EXTERNALMEASURE("Donation Quantity", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Mall Gift Cards (Null)

```sql
EXTERNALMEASURE("Mall Gift Cards (Null)", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Cash Deposit Expected

```sql
EXTERNALMEASURE("Cash Deposit Expected", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Total Register (Over)/Short

```sql
EXTERNALMEASURE("Total Register (Over)/Short", DOUBLE, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Float Variance (Null)

```sql
EXTERNALMEASURE("Float Variance (Null)", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Foreign Currency (Null)

```sql
EXTERNALMEASURE("Foreign Currency (Null)", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Exchange Amount (Null)

```sql
EXTERNALMEASURE("Exchange Amount (Null)", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Foreign Total (Null)

```sql
EXTERNALMEASURE("Foreign Total (Null)", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

### Measure Table.Total Register Counts (Null)

```sql
EXTERNALMEASURE("Total Register Counts (Null)", INTEGER, "DirectQuery to AS - Sales Audit Data Model")
```

## Power Query Source (per table)

### Calendar

```sql
Calendar
```

### Locations (Store MDM)

```sql
Locations (Store MDM)
```

### Product Images

```sql
Product Images
```

### Transactions (JumpMind)

```sql
Transactions (JumpMind)
```

### Business Units (JumpMind)

```sql
Business Units (JumpMind)
```

### Users (JumpMind)

```sql
Users (JumpMind)
```

### Retail Transactions (JumpMind)

```sql
Retail Transactions (JumpMind)
```

### Retail Transaction Discounts (JumpMind)

```sql
Retail Transaction Discounts (JumpMind)
```

### Retail Lines (JumpMind)

```sql
Retail Lines (JumpMind)
```

### Retail Line Discounts (JumpMind)

```sql
Retail Line Discounts (JumpMind)
```

### Retail Return Lines (JumpMind)

```sql
Retail Return Lines (JumpMind)
```

### Tax Lines (JumpMind)

```sql
Tax Lines (JumpMind)
```

### Tender Settlement Lines (JumpMind)

```sql
Tender Settlement Lines (JumpMind)
```

### Tender Lines (JumpMind)

```sql
Tender Lines (JumpMind)
```

### Tender Card Lines (JumpMind)

```sql
Tender Card Lines (JumpMind)
```

### Measure Table

```sql
Measure Table
```

### Activated Gift Cards (JumpMind)

```sql
Activated Gift Cards (JumpMind)
```

### Tax Authorities (JumpMind)

```sql
Tax Authorities (JumpMind)
```

### Tax Groups (JumpMind)

```sql
Tax Groups (JumpMind)
```

### Tenders (JumpMind)

```sql
Tenders (JumpMind)
```

### Transaction Summaries (JumpMind)

```sql
Transaction Summaries (JumpMind)
```

### Exchange rates (Dynamics)

```sql
Exchange rates (Dynamics)
```

### Products (PLM)

```sql
Products (PLM)
```

### Global Products (JumpMind)

```sql
Global Products (JumpMind)
```

### LocalDateTable_93238a4d-3b84-4f59-be36-5ff69cd43d4e

```sql
LocalDateTable_93238a4d-3b84-4f59-be36-5ff69cd43d4e
```

### LocalDateTable_5c168f80-25a0-4efa-bf12-7e60a5e48a8e

```sql
LocalDateTable_5c168f80-25a0-4efa-bf12-7e60a5e48a8e
```

### LocalDateTable_96e4d140-fa2d-4e56-b7de-334a44a64da4

```sql
LocalDateTable_96e4d140-fa2d-4e56-b7de-334a44a64da4
```

### LocalDateTable_e60a4d41-cac0-48db-97a2-d983bc81d3d0

```sql
LocalDateTable_e60a4d41-cac0-48db-97a2-d983bc81d3d0
```

### LocalDateTable_3d5229f5-4fe7-4b35-bcee-e6627e744a8b

```sql
LocalDateTable_3d5229f5-4fe7-4b35-bcee-e6627e744a8b
```

### LocalDateTable_4e98b083-f78d-424d-99f6-7928ae69c16f

```sql
LocalDateTable_4e98b083-f78d-424d-99f6-7928ae69c16f
```

### LocalDateTable_d7529a08-6398-426c-a772-644494cce77d

```sql
LocalDateTable_d7529a08-6398-426c-a772-644494cce77d
```

### LocalDateTable_b4b70347-805d-4ca2-8d32-4fa167522777

```sql
LocalDateTable_b4b70347-805d-4ca2-8d32-4fa167522777
```

### LocalDateTable_dab62035-2669-4a22-aaec-2632fabcb287

```sql
LocalDateTable_dab62035-2669-4a22-aaec-2632fabcb287
```

### LocalDateTable_7860c2a2-378f-46bb-b7a0-5185b792d99e

```sql
LocalDateTable_7860c2a2-378f-46bb-b7a0-5185b792d99e
```

### LocalDateTable_f2bca1c6-828c-4094-bbfb-4763519fe956

```sql
LocalDateTable_f2bca1c6-828c-4094-bbfb-4763519fe956
```

### LocalDateTable_b03143ec-a3af-4798-a56d-95139da8728a

```sql
LocalDateTable_b03143ec-a3af-4798-a56d-95139da8728a
```

### LocalDateTable_a4dcc117-e9b4-4b16-adee-f4f9946a165d

```sql
LocalDateTable_a4dcc117-e9b4-4b16-adee-f4f9946a165d
```

### LocalDateTable_49ea6d5f-fb07-4da6-9fb1-51d02a2bc45a

```sql
LocalDateTable_49ea6d5f-fb07-4da6-9fb1-51d02a2bc45a
```

### LocalDateTable_c696f59a-66cf-41b7-8b07-5195859bcbaa

```sql
LocalDateTable_c696f59a-66cf-41b7-8b07-5195859bcbaa
```

### LocalDateTable_61a52116-af4f-4f93-b42a-bae69dfe4c27

```sql
LocalDateTable_61a52116-af4f-4f93-b42a-bae69dfe4c27
```

### LocalDateTable_389f283c-edb3-40f4-ac2f-a231a1db0d91

```sql
LocalDateTable_389f283c-edb3-40f4-ac2f-a231a1db0d91
```

### LocalDateTable_252fac6a-2c05-4ea6-811c-020b777cc24e

```sql
LocalDateTable_252fac6a-2c05-4ea6-811c-020b777cc24e
```

### LocalDateTable_9d389bc1-31cd-4452-87ee-b48b7c91fa60

```sql
LocalDateTable_9d389bc1-31cd-4452-87ee-b48b7c91fa60
```

### LocalDateTable_561eb354-c83a-4fad-8bed-dff84b95c91b

```sql
LocalDateTable_561eb354-c83a-4fad-8bed-dff84b95c91b
```

### LocalDateTable_12349c08-94b3-429b-ab24-c10ba82ff847

```sql
LocalDateTable_12349c08-94b3-429b-ab24-c10ba82ff847
```

### LocalDateTable_f84ef23a-3840-4b6e-99ba-dd3ef26f713e

```sql
LocalDateTable_f84ef23a-3840-4b6e-99ba-dd3ef26f713e
```

### LocalDateTable_cb103ba7-2fb4-402a-895c-2b84dc3f5dbd

```sql
LocalDateTable_cb103ba7-2fb4-402a-895c-2b84dc3f5dbd
```

### LocalDateTable_5c26535c-2005-449c-bab9-ba36531e9c6d

```sql
LocalDateTable_5c26535c-2005-449c-bab9-ba36531e9c6d
```

### LocalDateTable_e402dd30-9f43-4d4f-a4fb-db08f436e975

```sql
LocalDateTable_e402dd30-9f43-4d4f-a4fb-db08f436e975
```

### LocalDateTable_f9c3d338-cbb0-41fb-86dc-21dc0f34e12b

```sql
LocalDateTable_f9c3d338-cbb0-41fb-86dc-21dc0f34e12b
```

### LocalDateTable_a2f29b70-36e2-4209-aa2b-d342e1e0f8c6

```sql
LocalDateTable_a2f29b70-36e2-4209-aa2b-d342e1e0f8c6
```

### LocalDateTable_bbd477ee-7054-427a-998e-b90a9310acd8

```sql
LocalDateTable_bbd477ee-7054-427a-998e-b90a9310acd8
```

### LocalDateTable_db9f588e-3a3b-4808-9922-3c9443a2e153

```sql
LocalDateTable_db9f588e-3a3b-4808-9922-3c9443a2e153
```

## Shared Expressions

### DirectQuery to AS - Sales Audit Data Model (0)

```sql
let
    Source = AnalysisServices.Database("powerbi://api.powerbi.com/v1.0/myorg/Enterprise%20Analytics%20QA", "Sales Audit Data Model"),
    Cubes = Table.Combine(Source[Data]),
    Cube = Cubes{[Id="Model", Kind="Cube"]}[Data]
in
    Cube
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| powerbi://api.powerbi.com/v1.0/myorg/Enterprise%20Analytics%20QA | Sales Audit Data Model | _(not found in SQL documentation)_ |
