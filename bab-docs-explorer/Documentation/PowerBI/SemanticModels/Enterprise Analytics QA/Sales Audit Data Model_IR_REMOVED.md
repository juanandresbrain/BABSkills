# Sales Audit Data Model_IR_REMOVED

**Workspace:** Enterprise Analytics QA  
**Dataset ID:** 2424a6a8-fc6b-456b-a7df-a26924c85bdb  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| Calendar | 47 | 0 |  |
| DateTableTemplate_e114f3e2-1436-4fde-85b3-c26a63948797 | 8 | 0 |  |
| Locations (Store MDM) | 42 | 0 |  |
| LocalDateTable_93238a4d-3b84-4f59-be36-5ff69cd43d4e | 8 | 0 |  |
| LocalDateTable_5c168f80-25a0-4efa-bf12-7e60a5e48a8e | 8 | 0 |  |
| LocalDateTable_96e4d140-fa2d-4e56-b7de-334a44a64da4 | 8 | 0 |  |
| Product Images | 5 | 0 |  |
| Transactions (JumpMind) | 36 | 0 |  |
| LocalDateTable_e60a4d41-cac0-48db-97a2-d983bc81d3d0 | 8 | 0 |  |
| LocalDateTable_3d5229f5-4fe7-4b35-bcee-e6627e744a8b | 8 | 0 |  |
| LocalDateTable_4e98b083-f78d-424d-99f6-7928ae69c16f | 8 | 0 |  |
| LocalDateTable_d7529a08-6398-426c-a772-644494cce77d | 8 | 0 |  |
| Business Units (JumpMind) | 4 | 0 |  |
| Users (JumpMind) | 13 | 0 |  |
| LocalDateTable_b4b70347-805d-4ca2-8d32-4fa167522777 | 8 | 0 |  |
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
| LocalDateTable_5c26535c-2005-449c-bab9-ba36531e9c6d | 8 | 0 |  |
| LocalDateTable_e402dd30-9f43-4d4f-a4fb-db08f436e975 | 8 | 0 |  |
| LocalDateTable_f9c3d338-cbb0-41fb-86dc-21dc0f34e12b | 8 | 0 |  |
| LocalDateTable_a2f29b70-36e2-4209-aa2b-d342e1e0f8c6 | 8 | 0 |  |
| LocalDateTable_bbd477ee-7054-427a-998e-b90a9310acd8 | 8 | 0 |  |
| Global Products (JumpMind) | 9 | 0 |  |
| LocalDateTable_db9f588e-3a3b-4808-9922-3c9443a2e153 | 8 | 0 | Yes |
| LocalDateTable_f84ef23a-3840-4b6e-99ba-dd3ef26f713e | 8 | 0 | Yes |
| LocalDateTable_cb103ba7-2fb4-402a-895c-2b84dc3f5dbd | 8 | 0 | Yes |
| LocalDateTable_561eb354-c83a-4fad-8bed-dff84b95c91b | 8 | 0 | Yes |
| LocalDateTable_12349c08-94b3-429b-ab24-c10ba82ff847 | 8 | 0 | Yes |
| LocalDateTable_dab62035-2669-4a22-aaec-2632fabcb287 | 8 | 0 | Yes |
| LocalDateTable_7860c2a2-378f-46bb-b7a0-5185b792d99e | 8 | 0 | Yes |
| LocalDateTable_f2bca1c6-828c-4094-bbfb-4763519fe956 | 8 | 0 | Yes |
| LocalDateTable_b03143ec-a3af-4798-a56d-95139da8728a | 8 | 0 | Yes |
| LocalDateTable_a4dcc117-e9b4-4b16-adee-f4f9946a165d | 8 | 0 | Yes |
| LocalDateTable_49ea6d5f-fb07-4da6-9fb1-51d02a2bc45a | 8 | 0 | Yes |
| LocalDateTable_c696f59a-66cf-41b7-8b07-5195859bcbaa | 8 | 0 | Yes |
| LocalDateTable_389f283c-edb3-40f4-ac2f-a231a1db0d91 | 8 | 0 | Yes |
| LocalDateTable_252fac6a-2c05-4ea6-811c-020b777cc24e | 8 | 0 | Yes |
| LocalDateTable_61a52116-af4f-4f93-b42a-bae69dfe4c27 | 8 | 0 | Yes |
| LocalDateTable_9d389bc1-31cd-4452-87ee-b48b7c91fa60 | 8 | 0 | Yes |

## Measures

### Retail Transactions (JumpMind).GAAP Flash Sales

```sql

CALCULATE(
    SUM('Retail Transactions (JumpMind)'[Total]),
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Retail Transactions (JumpMind).Endless Aisle Flash Sales

```sql

CALCULATE(
    SUM('Retail Transactions (JumpMind)'[Total]),
    'Retail Lines (JumpMind)'[Line Item Type] = "Order In Store",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Retail Lines (JumpMind).Returned Tender Amount | Without Loyalty Card Numbers (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Returned] = TRUE(),
    ISBLANK('Retail Transactions (JumpMind)'[Loyalty Card Number]) = TRUE(),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Retail Lines (JumpMind).Returned Tender Amount | With Loyalty Card Numbers (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Returned] = TRUE(),
    ISBLANK('Retail Transactions (JumpMind)'[Customer Id]) = FALSE(),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Retail Lines (JumpMind).Returned Tender Amount (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Returned] = TRUE(),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Retail Lines (JumpMind).Modification Amount TE (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Discount Amount TE (Native Currency)]),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Retail Lines (JumpMind).Modification Amount TE (Native) | Sales

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Discount Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Returned] = FALSE(),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Retail Lines (JumpMind).Modification Amount TE (Native) | Returns

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Discount Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Returned] = TRUE(),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Retail Line Discounts (JumpMind).Modification Amount (Native)

```sql

CALCULATE(
    SUM('Retail Line Discounts (JumpMind)'[Modification Total (Native Currency)]),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Retail Line Discounts (JumpMind).Modification Amount (Native) | Returns

```sql

CALCULATE(
    SUM('Retail Line Discounts (JumpMind)'[Modification Total (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Returned] = TRUE(),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Retail Line Discounts (JumpMind).Modification Amount (Native) | Sales

```sql

CALCULATE(
    SUM('Retail Line Discounts (JumpMind)'[Modification Total (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Returned] = FALSE(),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Tender Settlement Lines (JumpMind).Safe Amount

```sql

CALCULATE(
    SUM('Tender Settlement Lines (JumpMind)'[Open Session Amount]),
    'Tender Settlement Lines (JumpMind)'[Reason Code] = "Open Store Bank",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Tender Settlement Lines (JumpMind).Till Amount

```sql

CALCULATE(
    SUM('Tender Settlement Lines (JumpMind)'[Open Session Amount]),
    'Tender Settlement Lines (JumpMind)'[Reason Code] = "Open Till",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Tender Settlement Lines (JumpMind).Store Funds Amount

```sql
[Safe Amount] + [Till Amount]
```

### Tender Settlement Lines (JumpMind).Over/Short Amount (Native)

```sql

CALCULATE(
    SUM('Tender Settlement Lines (JumpMind)'[Over Under Session Amount]),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Tender Lines (JumpMind).Total Tender Amount (Native)

```sql

CALCULATE(
    SUM('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Tender Lines (JumpMind).Total Tender Amount (Native) | Store Sales

```sql

CALCULATE(
    SUM('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]),
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Tender Lines (JumpMind).Total Tender Amount (Native) | Order In Store

```sql

CALCULATE(
    SUM('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]),
    'Retail Lines (JumpMind)'[Line Item Type] = "Order In Store",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Tender Lines (JumpMind).Debit Tender Amount (Native)

```sql

CALCULATE(
    SUM('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]),
    'Tender Lines (JumpMind)'[Charge Type] = "Debit",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Tender Lines (JumpMind).Credit Tender Amount (Native)

```sql

CALCULATE(
    SUM('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]),
    'Tender Lines (JumpMind)'[Charge Type] = "Credit",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Tender Lines (JumpMind).Balance Tender Amount (Native)

```sql
ABS([Debit Tender Amount (Native)]) - ABS([Credit Tender Amount (Native)])
```

### Measure Table.Retail Transactions

```sql

CALCULATE(
    DISTINCTCOUNTNOBLANK('Retail Lines (JumpMind)'[Transaction Key]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Donation Amount (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Type] = "Donation",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Units

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Regular Unit Price (Native Currency)] <> 0,
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Donation Units

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Item Type] = "Donation",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Sales TE | Actual (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Discount Amount TE (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Discount Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.AUR (Native)

```sql
[Retail Sales TE | Actual (Native)] / [Retail Units]
```

### Measure Table.DPT (Native)

```sql
[Retail Sales TE | Actual (Native)] / [Retail Transactions]
```

### Measure Table.UPT

```sql
[Retail Units] / [Retail Transactions]
```

### Measure Table.Retail Sales TE | Actual (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount TE (USD Converted)]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.AUR (USD)

```sql
[Retail Sales TE | Actual (USD)] / [Retail Units]
```

### Measure Table.Retail Discount Amount TE (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Discount Amount TE (USD Converted)]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Donation Amount (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount TE (USD Converted)]),
    'Retail Lines (JumpMind)'[Item Type] = "Donation",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.DPT (USD)

```sql
[Retail Sales TE | Actual (USD)] / [Retail Transactions]
```

### Measure Table.Retail Transactions | Loyalty Members

```sql

CALCULATE(
    DISTINCTCOUNTNOBLANK('Retail Lines (JumpMind)'[Transaction Key]),
    'Retail Lines (JumpMind)'[Item Type] = "Loyalty",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Bonus Club Capture Rate

```sql
[Retail Transactions | Loyalty Members] / [Retail Transactions]
```

### Measure Table.Average Retail Discount Amount TE Per Unit (Native)

```sql

CALCULATE(
    AVERAGE('Retail Lines (JumpMind)'[Discount Amount Per Unit TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Average Retail Discount Amount TE Per Unit (USD)

```sql

CALCULATE(
    AVERAGE('Retail Lines (JumpMind)'[Discount Amount Per Unit TE (USD Converted)]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Average Retail Discount Amount TE Per Transaction (Native)

```sql

CALCULATE(
    AVERAGE('Retail Lines (JumpMind)'[Discount Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Average Retail Discount Amount TE Per Transaction (USD)

```sql

CALCULATE(
    AVERAGE('Retail Lines (JumpMind)'[Discount Amount TE (USD Converted)]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Discount Percentage TE

```sql
[Retail Discount Amount TE (Native)] / [Retail Sales TE | Full-Price (Native)]
```

### Measure Table.Retail Sales TE | Full-Price (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Regular Sales Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Sales TE | Full-Price (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Regular Sales Amount TE (USD Converted)]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Units | Accessories

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] = "Accessories",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Units | Clothes

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] = "Clothes",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Units | Footwear

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] = "Footwear",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Units | Friend

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] = "Friend",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Units | Human

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] = "Human",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Units | Human Clothes

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] = "Human Clothes",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Units | Stuffed

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] = "Stuffed",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Units | Stuffers

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] = "Stuffers",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Units | Unstuffed

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] = "Unstuffed",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Units | Stuffers | Scents

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] = "Stuffers",
    'Products (PLM)','Products (PLM)'[Class] = "Scents",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Units | Stuffers | Sounds

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] = "Stuffers",
    'Products (PLM)','Products (PLM)'[Class] = "Sound",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Transactions | Party Packages

```sql

CALCULATE(
    DISTINCTCOUNTNOBLANK('Retail Lines (JumpMind)'[Transaction Key]),
    'Retail Lines (JumpMind)'[Item Type] = "Party Package",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Total Sales TE | Full-Price (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Regular Sales Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Total Sales TE | Actual (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Total Sales TE | Actual (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount TE (USD Converted)]),
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Total Sales TE | Full-Price (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Regular Sales Amount TE (USD Converted)]),
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Non-Retail Units

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Regular Unit Price (Native Currency)] <> 0,
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    NOT('Retail Lines (JumpMind)'[Item Type] IN {"Gift Card", "Donation", "Loyalty", "Military", "Party Package"}),
    NOT('Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"}),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Non-Retail Sales TE | Actual (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Regular Unit Price (Native Currency)] <> 0,
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    NOT('Retail Lines (JumpMind)'[Item Type] IN {"Gift Card", "Donation", "Loyalty", "Party Package"}),
    NOT('Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"}),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Non-Retail Sales TE | Actual (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount TE (USD Converted)]),
    'Retail Lines (JumpMind)'[Regular Unit Price (Native Currency)] <> 0,
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    NOT('Retail Lines (JumpMind)'[Item Type] IN {"Gift Card", "Donation", "Loyalty", "Party Package"}),
    NOT('Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"}),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Transactions | Military Discounts

```sql

CALCULATE(
    DISTINCTCOUNTNOBLANK('Retail Lines (JumpMind)'[Transaction Key]),
    'Retail Lines (JumpMind)'[Item Type] = "Military",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Profit TE (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Retail Line Profit TE (USD)]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Non-Retail Profit TE (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Retail Line Profit TE (USD)]),
    'Retail Lines (JumpMind)'[Regular Unit Price (Native Currency)] <> 0,
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    NOT('Retail Lines (JumpMind)'[Item Type] IN {"Gift Card", "Donation", "Loyalty", "Party Package"}),
    NOT('Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"}),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Cash (Deposit)

```sql

VAR _GLAmountExpected = 
CALCULATE(
    SUM('Tender Settlement Lines (JumpMind)'[Pickup Amount]),
    'Tender Settlement Lines (JumpMind)'[Repository Transfer Type] = "From Store Bank to External Bank",
    'Tender Settlement Lines (JumpMind)'[Tender Type Code] = "Cash",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)

VAR _TotalOverUnderSessionAmount = 
CALCULATE(
    SUM('Tender Settlement Lines (JumpMind)'[Over Under Session Amount]),
    'Tender Settlement Lines (JumpMind)'[Tender Type Code] = "Cash",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)


RETURN
CALCULATE(
    _GLAmountExpected - _TotalOverUnderSessionAmount
)
```

### Measure Table.Bank (Deposit)

```sql

CALCULATE(
    SUM('Tender Settlement Lines (JumpMind)'[Pickup Amount]),
    'Tender Settlement Lines (JumpMind)'[Repository Transfer Type] = "From Store Bank to External Bank",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.FBR (Over)/Short

```sql

CALCULATE(
    -1 * SUM('Tender Settlement Lines (JumpMind)'[Over Under Session Amount]),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Total Visa Payment Amount (Native)

```sql

CALCULATE(
    SUM('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]),
    'Tender Card Lines (JumpMind)'[Brand] = "Visa",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Total MasterCard Payment Amount (Native)

```sql

CALCULATE(
    SUM('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]),
    'Tender Card Lines (JumpMind)'[Brand] IN {"MasterCard","Maestro"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Total Visa/MasterCard Payment Amount (Native)

```sql

CALCULATE(
    SUM('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]),
    'Tender Card Lines (JumpMind)'[Brand] IN {"Visa","MasterCard","Maestro"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Total Debit & Credit Payment Amount (Native)

```sql

CALCULATE(
    SUM('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]),
    'Tender Card Lines (JumpMind)'[Tender Type Code] IN {"Credit","Debit"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Total Electronic Payment Amount (Native)

```sql

CALCULATE(
    SUM('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]),
    'Tender Card Lines (JumpMind)'[Tender Type Code] IN {"Credit","Debit","E-Wallet"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Total E-Wallet Payment Amount (Native)

```sql

CALCULATE(
    SUM('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]),
    'Tender Card Lines (JumpMind)'[Tender Type Code] = "E-Wallet",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Activated Gift Cards Gross Amount TE (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Regular Sales Amount TE (USD Converted)]),
    'Retail Lines (JumpMind)'[Item Type] = "Gift Card",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Activated Gift Card Units

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Item Type] = "Gift Card",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Activated Gift Cards Gross Amount TE (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Regular Sales Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Type] = "Gift Card",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Activated Gift Cards Net Amount TE (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Type] = "Gift Card",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Activated Gift Cards Net Amount TE (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount TE (USD Converted)]),
    'Retail Lines (JumpMind)'[Item Type] = "Gift Card",
    'Retail Lines (JumpMind)'[Line Item Type] = "Store Sale",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Redeemed Gift Card Units

```sql

CALCULATE(
    COUNT('Tender Lines (JumpMind)'[Transaction Line Key]),
    'Tender Lines (JumpMind)'[Tender Type Code] = "Gift Card",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Redeemed Gift Card Tender Amount (Native)

```sql

CALCULATE(
    -1 * SUM('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]),
    'Tender Lines (JumpMind)'[Tender Type Code] = "Gift Card",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Money Tax Amount (Native)

```sql

CALCULATE(
    SUM('Tax Lines (JumpMind)'[Money Tax Amount (Native Currency)]),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Non-Taxable Amount (Native)

```sql

CALCULATE(
    SUM('Tax Lines (JumpMind)'[Tax Exempt Amount (Native Currency)]),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Non-Taxable Amount (Native) | Merchandise

```sql

CALCULATE(
    SUM('Tax Lines (JumpMind)'[Tax Exempt Amount (Native Currency)]),
    'Tax Lines (JumpMind)'[Tax Category] = "Merchandise",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Non-Taxable Amount (Native) | Fees

```sql

CALCULATE(
    SUM('Tax Lines (JumpMind)'[Tax Exempt Amount (Native Currency)]),
    'Tax Lines (JumpMind)'[Tax Category] = "Fee",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Tax Amount (Native)

```sql

CALCULATE(
    SUM('Tax Lines (JumpMind)'[Tax Amount (Native Currency)]),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Tax Variance (Native)

```sql
[Money Tax Amount (Native)] - [Tax Amount (Native)]
```

### Measure Table.Taxable Amount (Native)

```sql

CALCULATE(
    SUM('Tax Lines (JumpMind)'[Taxable Amount (Native Currency)]),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Taxable Amount (Native) | Merchandise

```sql

CALCULATE(
    SUM('Tax Lines (JumpMind)'[Taxable Amount (Native Currency)]),
    'Tax Lines (JumpMind)'[Tax Category] = "Merchandise",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Taxable Amount (Native) | Fees

```sql

CALCULATE(
    SUM('Tax Lines (JumpMind)'[Taxable Amount (Native Currency)]),
    'Tax Lines (JumpMind)'[Tax Category] = "Fee",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Check (Deposit)

```sql

VAR _GLAmountExpected = 
CALCULATE(
    SUM('Tender Settlement Lines (JumpMind)'[Pickup Amount]),
    'Tender Settlement Lines (JumpMind)'[Repository Transfer Type] = "From Store Bank to External Bank",
    'Tender Settlement Lines (JumpMind)'[Tender Type Code] = "Check",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)

VAR _TotalOverUnderSessionAmount = 
CALCULATE(
    SUM('Tender Settlement Lines (JumpMind)'[Over Under Session Amount]),
    'Tender Settlement Lines (JumpMind)'[Tender Type Code] = "Check",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)


RETURN
CALCULATE(
    _GLAmountExpected - _TotalOverUnderSessionAmount
)
```

### Measure Table.Travelers Checks (Null)

```sql

IF(
    [GL Amount Expected] > 0,
    0
)
```

### Measure Table.Total American Express Payment Amount (Native)

```sql

CALCULATE(
    SUM('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]),
    'Tender Card Lines (JumpMind)'[Brand] = "American Express",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.GL Amount Expected

```sql

IF(
    [Bank (Deposit)] = 0,
    [FBR (Over)/Short],
    [Bank (Deposit)]
)
```

### Measure Table.Total Discover Payment Amount (Native)

```sql

CALCULATE(
    SUM('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]),
    'Tender Card Lines (JumpMind)'[Brand] = "Discover",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Receipt Quantity

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Item Type] <> "Donation",
    'Retail Lines (JumpMind)'[Regular Unit Price (Native Currency)] <> 0,
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Donation Quantity

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Item Type] = "Donation",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Mall Gift Cards (Null)

```sql

IF(
    [GL Amount Expected] > 0,
    0
)
```

### Measure Table.Cash Deposit Expected

```sql

VAR _GLAmountExpected = 
CALCULATE(
    SUM('Tender Settlement Lines (JumpMind)'[Pickup Amount]),
    'Tender Settlement Lines (JumpMind)'[Repository Transfer Type] = "From Store Bank to External Bank",
    'Tender Settlement Lines (JumpMind)'[Tender Type Code] IN {"Cash", "Check"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)

VAR _TotalOverUnderSessionAmount = 
CALCULATE(
    SUM('Tender Settlement Lines (JumpMind)'[Over Under Session Amount]),
    'Tender Settlement Lines (JumpMind)'[Tender Type Code] IN {"Cash", "Check"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)


RETURN
CALCULATE(
    _GLAmountExpected - _TotalOverUnderSessionAmount
)
```

### Measure Table.Total Register (Over)/Short

```sql

VAR _GLAmountExpected = 
CALCULATE(
    SUM('Tender Settlement Lines (JumpMind)'[Pickup Amount]),
    'Tender Settlement Lines (JumpMind)'[Repository Transfer Type] = "From Store Bank to External Bank",
    'Tender Settlement Lines (JumpMind)'[Tender Type Code] IN {"Cash", "Check"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)

VAR _TotalOverUnderSessionAmount = 
CALCULATE(
    SUM('Tender Settlement Lines (JumpMind)'[Over Under Session Amount]),
    'Tender Settlement Lines (JumpMind)'[Tender Type Code] IN {"Cash", "Check"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)


RETURN
CALCULATE(
    _GLAmountExpected - _TotalOverUnderSessionAmount
)
```

### Measure Table.Float Variance (Null)

```sql

IF(
    [GL Amount Expected] > 0,
    0
)
```

### Measure Table.Foreign Currency (Null)

```sql

IF(
    [GL Amount Expected] > 0,
    0
)
```

### Measure Table.Exchange Amount (Null)

```sql

IF(
    [GL Amount Expected] > 0,
    0
)
```

### Measure Table.Foreign Total (Null)

```sql

IF(
    [GL Amount Expected] > 0,
    0
)
```

### Measure Table.Total Register Counts (Null)

```sql

IF(
    [GL Amount Expected] > 0,
    0
)
```

## Power Query Source (per table)

### Calendar

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Mart", [CreateNavigationProperties=false]),
    dbo_date_dim = Source{[Schema="dbo",Item="date_dim"]}[Data],
    #"Renamed Columns" = Table.RenameColumns(dbo_date_dim,{{"actual_date", "Actual Datetime"}, {"fiscal_year", "Fiscal Year"}, {"season", "Season"}, {"fiscal_quarter", "Fiscal Quarter"}, {"fiscal_period", "Fiscal Month"}, {"fiscal_week", "Fiscal Week"}, {"month", "Calendar Month Id"}, {"year", "Calendar Year"}, {"month_name", "Calendar Month Name"}, {"day_of_month", "Day of Calendar Month"}, {"day_of_year", "Day of Calendar Year"}, {"day_name", "Day Name"}, {"weekend_y_n", "Is Weekend"}, {"day_of_week", "Day of Week"}, {"day_id", "Running Fiscal Day Id"}, {"week_of_period", "Week of Fiscal Month"}, {"week_of_quarter", "Week of Fiscal Quarter"}, {"period_of_quarter", "Month of Fiscal Quarter"}, {"holiday_period_code", "Holiday Period Code"}, {"week_id", "Running Fiscal Week Id"}, {"period_id", "Running Fiscal Month Id"}, {"quarter_id", "Running Fiscal Quarter Id"}, {"org_fiscal_quarter", "Fiscal Quarter 2"}, {"org_fiscal_period", "Fiscal Month 2"}, {"org_fiscal_week", "Fiscal Week 2"}, {"org_week_of_period", "Week of Fiscal Month 2"}, {"org_week_of_quarter", "Week of Fiscal Quarter 2"}, {"org_period_of_quarter", "Month of Fiscal Quarter 2"}}),
    #"Filtered Rows | Fiscal Year > 2018" = Table.SelectRows(#"Renamed Columns", each ([Fiscal Year] > 2018)),
    #"Inserted Date | Actual Date" = Table.AddColumn(#"Filtered Rows | Fiscal Year > 2018", "Actual Date", each Date.From([Actual Datetime]), type date),
    #"Removed Columns | Duplicates" = Table.RemoveColumns(#"Inserted Date | Actual Date",{"Fiscal Quarter 2", "Fiscal Month 2", "Fiscal Week 2", "Week of Fiscal Month 2", "Week of Fiscal Quarter 2", "Month of Fiscal Quarter 2", "Calendar Month Name", "Calendar Month Id"}),
    #"Sorted Rows | Actual Datetime ASC" = Table.Sort(#"Removed Columns | Duplicates",{{"Actual Datetime", Order.Ascending}}),
    #"Added Custom | Fiscal Year (Header)" = Table.AddColumn(#"Sorted Rows | Actual Datetime ASC", "Fiscal Year (Header)", each "FY" & Text.From([Fiscal Year])),
    #"Added Custom | Fiscal Quarter (Header)" = Table.AddColumn(#"Added Custom | Fiscal Year (Header)", "Fiscal Quarter (Header)", each "FQ" & Text.From([Fiscal Quarter])),
    #"Added Conditional Column | Fiscal Month (Name)" = Table.AddColumn(#"Added Custom | Fiscal Quarter (Header)", "Fiscal Month (Name)", each if [Fiscal Month] = 1 then "Febuary" else if [Fiscal Month] = 2 then "March" else if [Fiscal Month] = 3 then "April" else if [Fiscal Month] = 4 then "May" else if [Fiscal Month] = 5 then "June" else if [Fiscal Month] = 6 then "July" else if [Fiscal Month] = 7 then "August" else if [Fiscal Month] = 8 then "September" else if [Fiscal Month] = 9 then "October" else if [Fiscal Month] = 10 then "November" else if [Fiscal Month] = 11 then "December" else if [Fiscal Month] = 12 then "January" else null),
    #"Inserted Month Name | Calendar Month (Name)" = Table.AddColumn(#"Added Conditional Column | Fiscal Month (Name)", "Calendar Month (Name)", each Date.MonthName([Actual Datetime]), type text),
    #"Inserted Month | Calendar Month INT" = Table.AddColumn(#"Inserted Month Name | Calendar Month (Name)", "Calendar Month", each Date.Month([Actual Datetime]), Int64.Type),
    #"Added Custom | Fiscal Month (Header)" = Table.AddColumn(#"Inserted Month | Calendar Month INT", "Fiscal Month (Header)", each Text.PadStart(Text.From([Fiscal Month]),2,"0") & "-" & [#"Fiscal Month (Name)"]),
    #"Added Custom | Calendar Month (Header)" = Table.AddColumn(#"Added Custom | Fiscal Month (Header)", "Calendar Month (Header)", each Text.PadStart(Text.From([#"Calendar Month"]),2,"0") & "-" & [#"Calendar Month (Name)"]),
    #"Added Custom | Fiscal Week (Header)" = Table.AddColumn(#"Added Custom | Calendar Month (Header)", "Fiscal Week (Header)", each "FW" & Text.PadStart(Text.From([Fiscal Week]),2,"0")),
    #"Inserted Quarter | Calendar Quarter INT" = Table.AddColumn(#"Added Custom | Fiscal Week (Header)", "Calendar Quarter", each Date.QuarterOfYear([Actual Datetime]), Int64.Type),
    #"Added Custom | Calendar Quarter (Header)" = Table.AddColumn(#"Inserted Quarter | Calendar Quarter INT", "Calendar Quarter (Header)", each "CQ" & Text.From([#"Calendar Quarter"])),
    #"Added Custom | Calendar Year (Header)" = Table.AddColumn(#"Added Custom | Calendar Quarter (Header)", "Calendar Year (Header)", each "CY" & Text.From([Calendar Year])),
    #"Inserted Week of Year | Calendar Week INT" = Table.AddColumn(#"Added Custom | Calendar Year (Header)", "Calendar Week", each Date.WeekOfYear([Actual Datetime]), Int64.Type),
    #"Added Custom | Calendar Week (Header)" = Table.AddColumn(#"Inserted Week of Year | Calendar Week INT", "Calendar Week (Header)", each "CW" & Text.PadStart(Text.From([Calendar Week]),2,"0")),
    #"Replaced Value | """" with NULL" = Table.ReplaceValue(#"Added Custom | Calendar Week (Header)","",null,Replacer.ReplaceValue,{"Holiday Period Code"}),
    #"Reordered Columns" = Table.ReorderColumns(#"Replaced Value | """" with NULL",{"date_key", "Actual Datetime", "Actual Date", "Fiscal Year", "Fiscal Quarter", "Fiscal Month", "Fiscal Month (Name)", "Fiscal Week", "Calendar Year", "Calendar Quarter", "Calendar Month", "Calendar Month (Name)", "Calendar Week", "Day Name", "Is Weekend", "Holiday Period Code", "Season", "Day of Week", "Day of Calendar Month", "Day of Calendar Year", "Week of Fiscal Month", "Week of Fiscal Quarter", "Month of Fiscal Quarter", "Running Fiscal Day Id", "Running Fiscal Week Id", "Running Fiscal Month Id", "Running Fiscal Quarter Id", "Fiscal Year (Header)", "Fiscal Quarter (Header)",  "Fiscal Month (Header)", "Fiscal Week (Header)", "Calendar Year (Header)", "Calendar Quarter (Header)", "Calendar Month (Header)", "Calendar Week (Header)"}),
    #"Changed Type" = Table.TransformColumnTypes(#"Reordered Columns",{{"Fiscal Month (Name)", type text}, {"Fiscal Year (Header)", type text}, {"Fiscal Quarter (Header)", type text}, {"Fiscal Month (Header)", type text}, {"Fiscal Week (Header)", type text}, {"Calendar Year (Header)", type text}, {"Calendar Quarter (Header)", type text}, {"Calendar Month (Header)", type text}, {"Calendar Week (Header)", type text}})
in
    #"Changed Type"
```

### DateTableTemplate_e114f3e2-1436-4fde-85b3-c26a63948797

```sql
Calendar(Date(2015,1,1), Date(2015,1,1))
```

### Locations (Store MDM)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Mart", [CreateNavigationProperties=false]),
    dbo_store_dim = Source{[Schema="dbo",Item="store_dim"]}[Data],
    #"Renamed Columns" = Table.RenameColumns(dbo_store_dim,{{"store_id", "Location Number"}, {"bearea", "Bearea"}, {"store_name", "Location Name"}, {"bearritory", "District"}, {"address1", "Address line 1"}, {"store_name_abbrv", "Abbrev"}, {"region", "Region"}, {"zone", "Zone"}, {"address2", "Address line 2"}, {"state_province_name", "State/Province name"}, {"business_type", "Business type"}, {"city", "City"}, {"division", "Division"}, {"state_province", "State/Province"}, {"county", "County"}, {"business_unit", "Business unit"}, {"country", "Country"}, {"country_name", "Country name"}, {"postal_code", "Postal code"}, {"phone", "Phone"}, {"email", "Email"}, {"opening_date", "Opening date"}, {"active", "Active"}, {"latitude", "Latitude"}, {"longitude", "Longitude"}, {"volume_group", "Volume group"}, {"store_mgr", "Store manager"}, {"bearea_mgr", "Bearea manager"}, {"bearitory_mgr", "Bearritory manager"}, {"region_mgr", "Region manager"}, {"store_type", "Store type"}, {"closing_date", "Closing date"}, {"comp_date", "Comp date"}, {"store_group_id", "Store group Id"}, {"address3", "Address line 3"}, {"address4", "Address line 4"}, {"square_feet", "Square feet"}, {"num_of_pos", "POS count"}, {"num_of_kiosks", "Kiosk count"}, {"postal_plus4", "Postal +4"}, {"Legal_Description", "Legal description"}, {"comp_week_id", "Comp week Id"}, {"bearea_id", "Bearea Id"}, {"bearitory_id", "Bearittory Id"}, {"region_id", "Region Id"}, {"division_code", "Division code"}, {"language", "Language"}, {"demographics_bg_key", "Demographics key"}, {"fax", "Fax"}}),
    #"Filtered Rows | ETL_LOG_ID <> -1" = Table.SelectRows(#"Renamed Columns", each ([ETL_LOG_ID] <> -1)),
    #"Filtered Rows | Store Key > 0" = Table.SelectRows(#"Filtered Rows | ETL_LOG_ID <> -1", each [store_key] > 0),
    #"Removed Columns | System Fields" = Table.RemoveColumns(#"Filtered Rows | Store Key > 0",{"INS_DT", "UPDT_DT", "ETL_LOG_ID", "ETL_EVNT_ID"}),
    #"Removed Columns | Empty Columns" = Table.RemoveColumns(#"Removed Columns | System Fields",{"Zone", "Business type", "County", "Business unit", "Fax", "Address line 3", "Address line 4", "Kiosk count", "Postal +4", "Bearea Id", "Bearittory Id", "Region Id", "Division code", "Language"}),
    #"Filtered Rows | Remove DC Bypass, Locked-Held, Transfer" = Table.SelectRows(#"Removed Columns | Empty Columns", each not Text.Contains([Location Name], "DC Bypass") and not Text.Contains([Location Name], "Locked-Held") and not Text.Contains([Location Name], "Transfer") and not Text.Contains([Location Name], "RZ") and not Text.Contains([Location Name], "Ridemakerz")),
    #"Filtered Rows | Address line 1 IS NOT NULL" = Table.SelectRows(#"Filtered Rows | Remove DC Bypass, Locked-Held, Transfer", each ([Address line 1] <> null)),
    #"Replaced Value | 980 with 9980" = Table.ReplaceValue(#"Filtered Rows | Address line 1 IS NOT NULL",980,9980,Replacer.ReplaceValue,{"Location Number"}),
    #"Replaced Value | 960 with 9960" = Table.ReplaceValue(#"Replaced Value | 980 with 9980",960,9960,Replacer.ReplaceValue,{"Location Number"}),
    #"Filtered Rows | Toys R US" = Table.SelectRows(#"Replaced Value | 960 with 9960", each not Text.Contains([Location Name], "Toys R US")),
    #"Added Custom | Location Number (Standard)" = Table.AddColumn(#"Filtered Rows | Toys R US", "Location Number (Standard)", each Text.PadStart(Text.PadStart(Number.ToText([Location Number]),3,"0"),4,"1")),
    #"Added Custom | Location Line" = Table.AddColumn(#"Added Custom | Location Number (Standard)", "Location Line", each [#"Location Number (Standard)"] & " | " & [Location Name]),
    #"Added Conditional Column | Legal Entity (D365)" = Table.AddColumn(#"Added Custom | Location Line", "Legal Entity (D365)", each if [Country] = "US" then 1100 else if [Country] = "CA" then 1700 else if [Country] = "IE" then 2110 else if [Country] = "UK" then 2110 else null),
    #"Cleaned Text" = Table.TransformColumns(#"Added Conditional Column | Legal Entity (D365)",{{"Location Name", Text.Clean, type text}, {"Abbrev", Text.Clean, type text}, {"District", Text.Clean, type text}, {"Address line 1", Text.Clean, type text}, {"Bearea", Text.Clean, type text}, {"Region", Text.Clean, type text}, {"Address line 2", Text.Clean, type text}, {"State/Province name", Text.Clean, type text}, {"City", Text.Clean, type text}, {"Division", Text.Clean, type text}, {"State/Province", Text.Clean, type text}, {"Country", Text.Clean, type text}, {"Country name", Text.Clean, type text}, {"Postal code", Text.Clean, type text}, {"Phone", Text.Clean, type text}, {"Email", Text.Clean, type text}, {"Store manager", Text.Clean, type text}, {"Bearea manager", Text.Clean, type text}, {"Bearritory manager", Text.Clean, type text}, {"Region manager", Text.Clean, type text}, {"Store type", Text.Clean, type text}, {"Abbreviation", Text.Clean, type text}, {"Legal description", Text.Clean, type text}}),
    #"Trimmed Text" = Table.TransformColumns(#"Cleaned Text",{{"Location Name", Text.Trim, type text}, {"Abbrev", Text.Trim, type text}, {"District", Text.Trim, type text}, {"Address line 1", Text.Trim, type text}, {"Bearea", Text.Trim, type text}, {"Region", Text.Trim, type text}, {"Address line 2", Text.Trim, type text}, {"State/Province name", Text.Trim, type text}, {"City", Text.Trim, type text}, {"Division", Text.Trim, type text}, {"State/Province", Text.Trim, type text}, {"Country", Text.Trim, type text}, {"Country name", Text.Trim, type text}, {"Postal code", Text.Trim, type text}, {"Phone", Text.Trim, type text}, {"Email", Text.Trim, type text}, {"Store manager", Text.Trim, type text}, {"Bearea manager", Text.Trim, type text}, {"Bearritory manager", Text.Trim, type text}, {"Region manager", Text.Trim, type text}, {"Store type", Text.Trim, type text}, {"Abbreviation", Text.Trim, type text}, {"Legal description", Text.Trim, type text}}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Trimmed Text",{{"State/Province name", Text.Proper, type text}}),
    #"Added Custom | City State" = Table.AddColumn(#"Capitalized Each Word", "City, State", each [City] & ", " & [#"State/Province name"]),
    #"Replaced Value | ? with NULL" = Table.ReplaceValue(#"Added Custom | City State","?","",Replacer.ReplaceText,{"State/Province name"}),
    #"Replaced Value | """" with NULL" = Table.ReplaceValue(#"Replaced Value | ? with NULL","",null,Replacer.ReplaceValue,{"Address line 2", "Legal description", "Demographics key","State/Province name"}),
    #"Replaced Value | ( with NULL" = Table.ReplaceValue(#"Replaced Value | """" with NULL","(","",Replacer.ReplaceText,{"Phone"}),
    #"Replaced Value | ) with NULL" = Table.ReplaceValue(#"Replaced Value | ( with NULL",")","",Replacer.ReplaceText,{"Phone"}),
    #"Replaced Value | - with NULL" = Table.ReplaceValue(#"Replaced Value | ) with NULL","-","",Replacer.ReplaceText,{"Phone"}),
    #"Changed Type" = Table.TransformColumnTypes(#"Replaced Value | - with NULL",{{"Legal Entity (D365)", type text}, {"Active", type logical}, {"Location Number (Standard)", type text}, {"Location Line", type text}, {"City, State", type text}}),
    #"Renamed Columns1" = Table.RenameColumns(#"Changed Type",{{"Location Number", "Location Number (MDM)"}, {"Location Number (Standard)", "Location Number (D365)"}}),
    #"Sorted Rows" = Table.Sort(#"Renamed Columns1",{{"District", Order.Descending}}),
    #"Removed Duplicates" = Table.Distinct(#"Sorted Rows", {"Location Number (D365)"}),
    #"Sorted Rows1" = Table.Sort(#"Removed Duplicates",{{"Location Number (D365)", Order.Ascending}})
in
    #"Sorted Rows1"
```

### LocalDateTable_93238a4d-3b84-4f59-be36-5ff69cd43d4e

```sql
Calendar(Date(Year(MIN('Locations (Store MDM)'[Opening date])), 1, 1), Date(Year(MAX('Locations (Store MDM)'[Opening date])), 12, 31))
```

### LocalDateTable_5c168f80-25a0-4efa-bf12-7e60a5e48a8e

```sql
Calendar(Date(Year(MIN('Locations (Store MDM)'[Closing date])), 1, 1), Date(Year(MAX('Locations (Store MDM)'[Closing date])), 12, 31))
```

### LocalDateTable_96e4d140-fa2d-4e56-b7de-334a44a64da4

```sql
Calendar(Date(Year(MIN('Locations (Store MDM)'[Comp date])), 1, 1), Date(Year(MAX('Locations (Store MDM)'[Comp date])), 12, 31))
```

### Product Images

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [CreateNavigationProperties=false]),
    dbo_productimageurl = Source{[Schema="dbo",Item="productimageurl"]}[Data],
    #"Renamed Columns" = Table.RenameColumns(dbo_productimageurl,{{"ImageURL", "Image URL"}, {"isPrimary", "Primary Image"}}),
    #"Filtered Rows | isPrimary = 1" = Table.SelectRows(#"Renamed Columns", each ([Primary Image] = 1)),
    #"Added Custom | Core SKU" = Table.AddColumn(#"Filtered Rows | isPrimary = 1", "Core SKU", each Text.End([ItemNumber],5)),
    #"Changed Type" = Table.TransformColumnTypes(#"Added Custom | Core SKU",{{"Primary Image", type logical}, {"Core SKU", type text}}),
    #"Removed Duplicates | Core SKU" = Table.Distinct(#"Changed Type", {"Core SKU"})
in
    #"Removed Duplicates | Core SKU"
```

### Transactions (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source"),
    dbo_jumpmind_sls_trans = Source{[Schema="dbo",Item="jumpmind_sls_trans"]}[Data],
    #"Filtered Rows | Incremental Refresh" = Table.SelectRows(dbo_jumpmind_sls_trans, each [last_update_time] >= RangeStart and [last_update_time] < RangeEnd),
    #"Filtered Rows | Remove Web Merge" = Table.SelectRows(#"Filtered Rows | Incremental Refresh", each ([create_by] = "openpos-sls")),
    #"Inserted Text After Delimiter | Till Id" = Table.AddColumn(#"Filtered Rows | Remove Web Merge", "Till Id", each Text.AfterDelimiter([device_id], "-"), type text),
    #"Duplicated Column | Sequence Number" = Table.DuplicateColumn(#"Inserted Text After Delimiter | Till Id", "sequence_number", "sequence_number - Copy"),
    #"Merged Columns | Transaction Key" = Table.CombineColumns(Table.TransformColumnTypes(#"Duplicated Column | Sequence Number", {{"sequence_number", type text}}, "en-US"),{"device_id", "business_date", "sequence_number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Transaction Key"),
    #"Renamed Columns" = Table.RenameColumns(#"Merged Columns | Transaction Key",{{"trans_type", "Transaction Type"}, {"trans_status", "Transaction Status"}, {"business_unit_id", "Business Unit Id"}, {"username", "Username Id"}, {"begin_time", "Begin Datetime"}, {"end_time", "End Datetime"}, {"local_offset", "Local Offset"}, {"client_offset", "Client Offset"}, {"keyed_offline", "Keyed Offline"}, {"override_user_id", "Override User Id"}, {"barcode", "Barcode"}, {"training_mode", "Training Mode"}, {"session_id", "Session Id"}, {"trans_pin", "Transaction PIN"}, {"till_id", "BusinessUnitTillId"}, {"app_id", "App Id"}, {"app_version", "App Version"}, {"create_time", "Created Datetime"}, {"create_by", "Created By"}, {"last_update_time", "Last Updated Datetime"}, {"sequence_number - Copy", "Sequence Number"}, {"last_update_by", "Last Updated By"}}),
    #"Added Custom | Username Key" = Table.AddColumn(#"Renamed Columns", "Username Key", each [Business Unit Id] & "-" & [Username Id]),
    #"Replaced Value | _ with SPACE" = Table.ReplaceValue(#"Added Custom | Username Key","_"," ",Replacer.ReplaceText,{"Transaction Type", "Transaction Status"}),
    #"Added Custom | Override Username Key" = Table.AddColumn(#"Replaced Value | _ with SPACE", "Override Username Key", each [Business Unit Id] & "-" & [Override User Id]),
    #"Inserted Date | Transaction Date" = Table.AddColumn(#"Added Custom | Override Username Key", "Transaction Date", each Date.From([Last Updated Datetime]), type date),
    #"Inserted Time | Begin Time" = Table.AddColumn(#"Inserted Date | Transaction Date", "Begin Time", each Time.From([Begin Datetime]), type time),
    #"Inserted Time | End Time (Transaction Time)" = Table.AddColumn(#"Inserted Time | Begin Time", "Transaction Time", each Time.From([End Datetime]), type time),
    #"Capitalized Each Word" = Table.TransformColumns(#"Inserted Time | End Time (Transaction Time)",{{"Transaction Type", Text.Proper, type text}, {"Transaction Status", Text.Proper, type text}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Capitalized Each Word",{{"Keyed Offline", type logical}, {"Training Mode", type logical}, {"Username Key", type text}, {"Override Username Key", type text}}),
    #"Reordered Columns" = Table.ReorderColumns(#"Changed Type",{"Transaction Status", "Transaction Key", "Transaction Type", "Barcode", "Business Unit Id", "Till Id", "Training Mode", "Begin Datetime", "End Datetime", "Local Offset", "Client Offset", "Username Id", "Username Key", "Override User Id", "Override Username Key", "Keyed Offline", "Session Id", "Transaction PIN", "BusinessUnitTillId", "App Id", "App Version", "Created Datetime", "Created By", "Last Updated Datetime", "Last Updated By"}),
    #"Merged Queries | Users" = Table.NestedJoin(#"Reordered Columns", {"Username Key"}, #"Users (JumpMind)", {"Username Key"}, "Users (JumpMind)", JoinKind.LeftOuter),
    #"Expanded Users (JumpMind)" = Table.ExpandTableColumn(#"Merged Queries | Users", "Users (JumpMind)", {"Username", "Work Group"}, {"Username", "Work Group"}),
    #"Merged Queries | Users (Override)" = Table.NestedJoin(#"Expanded Users (JumpMind)", {"Override Username Key"}, #"Users (JumpMind)", {"Username Key"}, "Users (JumpMind)", JoinKind.LeftOuter),
    #"Expanded Users (JumpMind) | Override Users" = Table.ExpandTableColumn(#"Merged Queries | Users (Override)", "Users (JumpMind)", {"Username", "Work Group"}, {"Users (JumpMind).Username", "Users (JumpMind).Work Group"}),
    #"Renamed Columns | Users" = Table.RenameColumns(#"Expanded Users (JumpMind) | Override Users",{{"Users (JumpMind).Username", "Override Associate Name"}, {"Users (JumpMind).Work Group", "Override Associate Work Group"}, {"Username", "Associate Name"}, {"Work Group", "Associate Work Group"}})
in
    #"Renamed Columns | Users"
```

### LocalDateTable_e60a4d41-cac0-48db-97a2-d983bc81d3d0

```sql
Calendar(Date(Year(MIN('Transactions (JumpMind)'[Begin Datetime])), 1, 1), Date(Year(MAX('Transactions (JumpMind)'[Begin Datetime])), 12, 31))
```

### LocalDateTable_3d5229f5-4fe7-4b35-bcee-e6627e744a8b

```sql
Calendar(Date(Year(MIN('Transactions (JumpMind)'[End Datetime])), 1, 1), Date(Year(MAX('Transactions (JumpMind)'[End Datetime])), 12, 31))
```

### LocalDateTable_4e98b083-f78d-424d-99f6-7928ae69c16f

```sql
Calendar(Date(Year(MIN('Transactions (JumpMind)'[Created Datetime])), 1, 1), Date(Year(MAX('Transactions (JumpMind)'[Created Datetime])), 12, 31))
```

### LocalDateTable_d7529a08-6398-426c-a772-644494cce77d

```sql
Calendar(Date(Year(MIN('Transactions (JumpMind)'[Last Updated Datetime])), 1, 1), Date(Year(MAX('Transactions (JumpMind)'[Last Updated Datetime])), 12, 31))
```

### Business Units (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="SELECT DISTINCT#(lf)#(lf)       [business_unit_id]#(lf)      --,[geo_code]#(lf)      ,[business_unit_name]#(lf)      --,[government_id]#(lf)      --,[create_time]#(lf)      --,[create_by]#(lf)      --,[last_update_time]#(lf)      --,[last_update_by]#(lf)#(lf)  FROM#(tab)#(tab)[dbo].[jumpmind_ctx_business_unit]#(lf)#(lf)  ORDER BY#(tab)[business_unit_id]#(tab)ASC", CreateNavigationProperties=false]),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"business_unit_id", "Business Unit Id"}, {"business_unit_name", "Business Unit Name"}}),
    #"Added Custom | Location Line" = Table.AddColumn(#"Renamed Columns", "Location Line", each [Business Unit Id] & " | " & [Business Unit Name]),
    #"Changed Type" = Table.TransformColumnTypes(#"Added Custom | Location Line",{{"Location Line", type text}})
in
    #"Changed Type"
```

### Users (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="SELECT DISTINCT#(lf)#(lf)       [business_unit_id]#(lf)      ,[username]#(lf)      ,[last_name]#(lf)      ,[first_name]#(lf)      ,[last_login]#(lf)      ,[locked_out_flag]#(lf)      ,[alternate_id]#(lf)      ,[workgroup_id]#(lf)      ,[user_active_flag]#(lf)      --,[create_time]#(lf)      --,[create_by]#(lf)      --,[last_update_time]#(lf)      --,[last_update_by]#(lf)#(lf)  FROM#(tab)#(tab)[dbo].[jumpmind_bab_active_user]#(lf)#(lf)  ORDER BY#(tab)[business_unit_id]#(tab)ASC,#(lf)#(tab)#(tab)#(tab)[workgroup_id]#(tab)#(tab)ASC,#(lf)#(tab)#(tab)#(tab)[user_active_flag]#(tab)DESC,#(lf)#(tab)#(tab)#(tab)[username]#(tab)#(tab)ASC", CreateNavigationProperties=false]),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"alternate_id", "Alternate Id"}, {"business_unit_id", "Business Unit Id"},  {"first_name", "First Name"}, {"last_login", "Last Login"}, {"last_name", "Last Name"},  {"locked_out_flag", "Locked Out Flag"}, {"user_active_flag", "User Active Flag"}, {"username", "Username Id"}, {"workgroup_id", "Workgroup Id"}}),
    #"Added Custom | Username Key" = Table.AddColumn(#"Renamed Columns", "Username Key", each [Business Unit Id] & "-" & [Username Id]),
    #"Removed Duplicates | Username Key" = Table.Distinct(#"Added Custom | Username Key", {"Username Key"}),
    #"Inserted Merged Column | Username" = Table.AddColumn(#"Removed Duplicates | Username Key", "Username", each Text.Combine({[First Name], [Last Name]}, " "), type text),
    #"Added Conditional Column | Work Group" = Table.AddColumn(#"Inserted Merged Column | Username", "Work Group", each if Text.Contains([Workgroup Id], "BB") then "Bear Builder" else if Text.Contains([Workgroup Id], "SL") then "Sales Lead" else if Text.Contains([Workgroup Id], "AWM") then "Assistant Workshop Manager" else if Text.Contains([Workgroup Id], "CWM") then "Chief Workshop Manager" else if Text.Contains([Workgroup Id], "Bear Builder") then "Bear Builder" else if Text.Contains([Workgroup Id], "Sales Lead") then "Sales Lead" else if Text.Contains([Workgroup Id], "Assistant Workshop Manager") then "Assistant Workshop Manager" else if Text.Contains([Workgroup Id], "Chief Workshop Manager") then "Chief Workshop Manager" else if Text.Contains([Workgroup Id], "WM") then "Workshop Manager (Other)" else if Text.Contains([Workgroup Id], "DM") then "District Manager" else if Text.Contains([Workgroup Id], "SRVDSK") then "Service Desk" else if [Workgroup Id] = null then null else "Other"),
    #"Replaced Errors" = Table.ReplaceErrorValues(#"Added Conditional Column | Work Group", {{"Work Group", null}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Replaced Errors",{{"Locked Out Flag", type logical}, {"User Active Flag", type logical}, {"Username Key", type text}, {"Work Group", type text}})
in
    #"Changed Type"
```

### LocalDateTable_b4b70347-805d-4ca2-8d32-4fa167522777

```sql
Calendar(Date(Year(MIN('Users (JumpMind)'[Last Login])), 1, 1), Date(Year(MAX('Users (JumpMind)'[Last Login])), 12, 31))
```

### Retail Transactions (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source"),
    dbo_jumpmind_sls_retail_trans = Source{[Schema="dbo",Item="jumpmind_sls_retail_trans"]}[Data],
    #"Filtered Rows | Incremental Refresh" = Table.SelectRows(dbo_jumpmind_sls_retail_trans, each [last_update_time] >= RangeStart and [last_update_time] < RangeEnd),
    #"Filtered Rows | Remove Web Merge" = Table.SelectRows(#"Filtered Rows | Incremental Refresh", each ([create_by] = "openpos-sls")),
    #"Renamed Columns" = Table.RenameColumns(#"Filtered Rows | Remove Web Merge",{{"business_date", "Business Date"}, {"age_restricted_date_of_birth", "Age Restricted Date of Birth"}, {"create_by", "Created By"}, {"create_time", "Created Datetime"}, {"customer_callout", "Customer Callout"}, {"customer_id", "Customer Id"}, {"customer_name", "Customer Name"}, {"device_id", "Device Id"}, {"customer_entry_method_code", "Customer Entry Method Code"}, {"cust_other_id", "Customer Id (Other)"}, {"discount_total", "Discount Total"}, {"employee_id_for_discount", "Employee Id for Discount"}, {"employee_name_for_discount", "Employee Name for Discount"}, {"entry_mode_code", "Entry Mode Code"}, {"event_id", "Event Id"}, {"event_invoice", "Event Invoice"}, {"fiscal_control_number", "Fiscal Control Number"}, {"fiscal_processor_code", "Fiscal Processor Code"}, {"gift_receipt_print_type", "Gift Receipt Print Type"}, {"iso_currency_code", "ISO Currency Code"}, {"idle_elapsed_time_in_secs", "Idle Elapsed Time (in Seconds)"}, {"item_count", "Item Count"}, {"last_update_by", "Last Updated By"}, {"last_update_time", "Last Updated Datetime"}, {"line_item_count", "Line Item Count"}, {"lock_elapsed_time_in_secs", "Lock Elapsed Time (in Seconds)"}, {"loyalty_card_number", "Loyalty Card Number"}, {"loyalty_points_earned", "Loyalty Points Earned"}, {"non_rcpt_rtn_count", "Non-Receipt Return Count"}, {"non_rcpt_rtn_total", "Non-Receipt Return Total"}, {"order_id", "Order Id"}, {"party_id", "Party Id"}, {"pre_tender_balance_due", "Pre-Tender Balance Due"}, {"rcpt_rtn_count", "Receipt Return Count"}, {"rcpt_rtn_total", "Receipt Return Total"}, {"ring_elapsed_time_in_secs", "Ring Elapsed Time (in Seconds)"}, {"selling_channel_code", "Selling Channel Code"}, {"sequence_number", "Sequence Number"}, {"subtotal", "Subtotal"}, {"suspended_note", "Suspended Note"}, {"suspended_reason_code", "Suspended Reason Code"}, {"tax_exempt_certificate", "Tax Exempt Certificate"}, {"tax_exempt_code", "Tax Exempt Code"}, {"tax_exempt_customer_id", "Tax Exempt Customer Id"}, {"tax_geo_code_origin", "Tax Geo Code Origin"}, {"tax_total", "Tax Total"}, {"tax_total_for_display", "Tax Total for Display"}, {"tender_elapsed_time_in_secs", "Tender Elapsed Time (in Seconds)"}, {"tender_type_codes", "Tender Type Codes"}, {"total", "Total"}, {"voidable_flag", "Voidable Flag"}}),
    #"Merged Columns | Transaction Key" = Table.CombineColumns(Table.TransformColumnTypes(#"Renamed Columns", {{"Sequence Number", type text}}, "en-US"),{"Device Id", "Business Date", "Sequence Number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Transaction Key"),
    #"Added Custom | Tender Type Count" = Table.AddColumn(#"Merged Columns | Transaction Key", "Tender Type Count", each List.Count(Text.Split([Tender Type Codes]," "))),
    #"Replaced Errors | Tender Type Count NULL" = Table.ReplaceErrorValues(#"Added Custom | Tender Type Count", {{"Tender Type Count", null}}),
    #"Cleaned Text" = Table.TransformColumns(#"Replaced Errors | Tender Type Count NULL",{{"Customer Name", Text.Clean, type text}}),
    #"Trimmed Text" = Table.TransformColumns(#"Cleaned Text",{{"Customer Name", Text.Trim, type text}}),
    #"Replaced Value | blank with NULL" = Table.ReplaceValue(#"Trimmed Text","",null,Replacer.ReplaceValue,{"Customer Name"}),
    #"Replaced Value | _ with SPACE" = Table.ReplaceValue(#"Replaced Value | blank with NULL","_"," ",Replacer.ReplaceText,{"Gift Receipt Print Type"}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Replaced Value | _ with SPACE",{{"Customer Name", Text.Proper, type text}, {"Gift Receipt Print Type", Text.Proper, type text}, {"Customer Entry Method Code", Text.Proper, type text}, {"Selling Channel Code", Text.Proper, type text}, {"Employee Name for Discount", Text.Proper, type text}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Capitalized Each Word",{{"Voidable Flag", type logical}, {"Tender Type Count", Int64.Type}}),
    #"Removed Columns | Redundant Columns" = Table.RemoveColumns(#"Changed Type",{"Created Datetime", "Created By", "Last Updated By"}),
    #"Removed Columns | Empty Columns" = Table.RemoveColumns(#"Removed Columns | Redundant Columns",{"Age Restricted Date of Birth", "Suspended Note", "Fiscal Control Number", "Fiscal Processor Code"}),
    #"Removed Columns | Unneeded Columns" = Table.RemoveColumns(#"Removed Columns | Empty Columns",{"Tax Geo Code Origin"})
in
    #"Removed Columns | Unneeded Columns"
```

### Retail Transaction Discounts (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source"),
    dbo_jumpmind_sls_retail_trans_price_mod = Source{[Schema="dbo",Item="jumpmind_sls_retail_trans_price_mod"]}[Data],
    #"Filtered Rows | Incremental Refresh" = Table.SelectRows(dbo_jumpmind_sls_retail_trans_price_mod, each [last_update_time] >= RangeStart and [last_update_time] < RangeEnd),
    #"Filtered Rows | Remove Voided Lines" = Table.SelectRows(#"Filtered Rows | Incremental Refresh", each [voided] = 0),
    #"Renamed Columns" = Table.RenameColumns(#"Filtered Rows | Remove Voided Lines",{{"business_date", "Business Date"}, {"calc_method", "Calculation Method"}, {"create_by", "Created By"}, {"create_time", "Created Datetime"}, {"device_id", "Device Id"}, {"entry_method_code", "Entry Method Code"}, {"iso_currency_code", "ISO Currency Code"}, {"last_update_by", "Last Updated By"}, {"last_update_time", "Last Updated Datetime"}, {"line_sequence_number", "Line Sequence Number"}, {"mod_by_amount", "Modification by Amount (Native Currency)"}, {"mod_by_percentage", "Modification by Percentage"}, {"mod_line_sequence_number", "Mod Line Sequence Number"}, {"override_user_id", "Override User Id"}, {"price_mod_source_type_code", "Price Mod Source Type Code"}, {"price_mod_type_code", "Price Mod Type Code"}, {"reason_code", "Reason Code"}, {"rounding_amount", "Rounding Amount (Native Currency)"}, {"sequence_number", "Sequence Number"}, {"username", "Username"}, {"voided", "Voided"}}),
    #"Merged Columns | Transaction Key" = Table.CombineColumns(Table.TransformColumnTypes(#"Renamed Columns", {{"Sequence Number", type text}}, "en-US"),{"Device Id", "Business Date", "Sequence Number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Transaction Key"),
    #"Changed Type" = Table.TransformColumnTypes(#"Merged Columns | Transaction Key",{{"Modification by Percentage", Percentage.Type}, {"Voided", type logical}}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Changed Type",{{"Calculation Method", Text.Proper, type text}, {"Price Mod Type Code", Text.Proper, type text}, {"Price Mod Source Type Code", Text.Proper, type text}}),
    #"Removed Columns | Redundant Columns" = Table.RemoveColumns(#"Capitalized Each Word",{"Created Datetime", "Created By", "Last Updated By"})
in
    #"Removed Columns | Redundant Columns"
```

### Retail Lines (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source"),
    dbo_jumpmind_sls_retail_line_item = Source{[Schema="dbo",Item="jumpmind_sls_retail_line_item"]}[Data],
    #"Filtered Rows | Incremental Refresh" = Table.SelectRows(dbo_jumpmind_sls_retail_line_item, each [last_update_time] >= RangeStart and [last_update_time] < RangeEnd),
    #"Filtered Rows | Remove Web Merge" = Table.SelectRows(#"Filtered Rows | Incremental Refresh", each ([create_by] = "openpos-sls")),
    #"Filtered Rows | Remove Voided Lines" = Table.SelectRows(#"Filtered Rows | Remove Web Merge", each ([voided] = 0)),
    #"Renamed Columns" = Table.RenameColumns(#"Filtered Rows | Remove Voided Lines",{{"actual_unit_price", "Actual Unit Price (Native Currency)"}, {"additional_classifiers", "Additional Classifiers"}, {"business_date", "Business Date"}, {"classifier_brand", "Brand"}, {"classifier_class", "JM Class"}, {"classifier_department", "JM Department"}, {"classifier_style", "Style"}, {"coupon_allowed", "Coupon Allowed"}, {"coupon_multiply_allowed", "Coupon Multiply Allowed"}, {"create_by", "Created By"}, {"create_time", "Created Datetime"}, {"damage_discount_applied", "Damage Discount Applied"}, {"device_id", "Device Id"}, {"discount_amount", "Discount Amount (Native Currency)"}, {"discount_applied", "Discount Applied"}, {"disposition_code", "Disposition Code"}, {"eletronic_coupon_allowed", "Electronic Coupon Allowed"}, {"employee_discount_allowed", "Employee Discount Allowed"}, {"extended_amount", "Regular Sales Amount (Native Currency)"}, {"entry_method_code", "Entry Method Code"}, {"extended_discounted_amount", "Actual Sales Amount (Native Currency)"}, {"external_system_id", "External System Id"}, {"family_code", "Family Code"}, {"find_a_bear_id", "Find A Bear Id"}, {"gift_receipt", "Gift Receipt"}, {"inquiry_method_code", "Inquiry Method Code"}, {"iso_currency_code", "ISO Currency Code"}, {"item_description", "Item Description"}, {"item_discountable", "Item Discountable"}, {"item_id", "Item Id"}, {"item_length", "Item Length"}, {"item_long_description", "Item Long Description"}, {"item_name", "Item Name"}, {"item_price_overridable", "Item Price Overridable"}, {"item_returnable", "Item Returnable"}, {"item_returned", "Item Returned"}, {"item_taxable", "Item Taxable"}, {"item_type", "Item Type"}, {"item_weight", "Item Weight"}, {"item_weight_plus_tare", "Item Weight Plus Tare"}, {"last_update_by", "Last Updated By"}, {"last_update_time", "Last Updated Datetime"}, {"length_unit_of_measure", "Length Unit of Measure"}, {"line_item_type", "Line Item Type"}, {"line_sequence_number", "Line Sequence Number"}, {"loyalty_unit_price", "Loyalty Unit Price (Native Currency)"}, {"order_id", "Order Id"}, {"order_line_number", "Order Line Number"}, {"orig_business_date", "Orig_Business Date"}, {"orig_business_unit_id", "Orig_Business Unit Id"}, {"orig_device_id", "Orig_Device Id"}, {"orig_line_sequence_number", "Orig_Line Sequence Number"}, {"orig_order_id", "Orig_Order Id"}, {"orig_sequence_number", "Orig_Sequence Number"}, {"orig_username", "Orig_Username"}, {"override_user_id", "Override User Id"}, {"pos_item_id", "POS Item Id"}, {"product_id", "Product Id"}, {"quantity", "Quantity"}, {"quantity_avail_for_return", "Quantity Available for Return"}, {"quantity_modifiable", "Quantity Modifiable"}, {"reason_code", "Reason Code"}, {"reason_code_group_id", "Reason Code Group Id"}, {"regular_unit_price", "Regular Unit Price (Native Currency)"}, {"return_policy_id", "Return Policy Id"}, {"rtn_extended_discounted_amount", "Return Value Amount (Native Currency)"}, {"save_value", "Save Value"}, {"save_value_type", "Save Value Type"}, {"sequence_number", "Sequence Number"}, {"serialized_coupon_barcode", "Serialized Coupon Barcode"}, {"stuff_info", "Stuff Info"}, {"tare_weight", "Tare Weight"}, {"tax_amount", "Tax Amount (Native Currency)"}, {"tax_group_id", "Tax Group Id"}, {"tax_included_in_price", "Tax Included in Price"}, {"username", "Username"}, {"voided", "Voided"}, {"weight_entry_method_code", "Weight Entry Method Code"}, {"weight_unit_of_measure", "Weight Unit of Measure"}}),
    #"Removed Columns | Redundant Columns" = Table.RemoveColumns(#"Renamed Columns",{"tender_auth_method_code", "Created By", "Created Datetime", "Last Updated By"}),
    #"Removed Columns | Empty Columns" = Table.RemoveColumns(#"Removed Columns | Redundant Columns",{"Additional Classifiers", "Brand", "Family Code", "External System Id", "Loyalty Unit Price (Native Currency)", "Style", "JM Class", "JM Department", "Item Length", "Length Unit of Measure", "Item Weight", "Weight Entry Method Code", "Weight Unit of Measure", "Tare Weight", "Save Value Type", "Save Value", "Disposition Code"}),
    #"Merged Columns | Transaction Key" = Table.CombineColumns(Table.TransformColumnTypes(#"Removed Columns | Empty Columns", {{"Sequence Number", type text}}, "en-US"),{"Device Id", "Business Date", "Sequence Number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Transaction Key"),
    #"Added Custom | Transaction Line Key" = Table.AddColumn(#"Merged Columns | Transaction Key", "Transaction Line Key", each [Transaction Key] & "-" & Text.From([Line Sequence Number])),
    #"Added Conditional Column | Endless Aisle" = Table.AddColumn(#"Added Custom | Transaction Line Key", "Endless Aisle", each if [Line Item Type] = "STORE_SALE" then false else if [Line Item Type] = "ORDER_IN_STORE" then true else null),
    #"Added Custom | Item Key" = Table.AddColumn(#"Added Conditional Column | Endless Aisle", "Item Key", each [ISO Currency Code] & [Item Id]),
    #"Added Custom | Item Line" = Table.AddColumn(#"Added Custom | Item Key", "Item Line", each [Item Id] & " - " & [Item Description]),
    #"Added Custom | Actual Sales Amount TE" = Table.AddColumn(#"Added Custom | Item Line", "Actual Sales Amount TE (Native Currency)", each if [#"ISO Currency Code"] = "GBP" or [#"ISO Currency Code"] = "EUR" then (Number.Abs([#"Actual Sales Amount (Native Currency)"]) - Number.Abs([#"Tax Amount (Native Currency)"])) * Number.Sign([#"Quantity"]) else [#"Actual Sales Amount (Native Currency)"]),
    #"Added Custom | Tax Percentage" = Table.AddColumn(#"Added Custom | Actual Sales Amount TE", "Tax Percentage", each [#"Tax Amount (Native Currency)"] / [#"Actual Sales Amount TE (Native Currency)"]),
    #"Added Custom | Discount Amount TE" = Table.AddColumn(#"Added Custom | Tax Percentage", "Discount Amount TE (Native Currency)", each if [#"ISO Currency Code"] = "GBP" or [#"ISO Currency Code"] = "EUR" then (Number.Abs([#"Discount Amount (Native Currency)"]) - (Number.Abs([#"Discount Amount (Native Currency)"])*[Tax Percentage])) * Number.Sign([#"Quantity"]) else [#"Discount Amount (Native Currency)"]),
    #"Added Custom | Regular Sales Amount TE" = Table.AddColumn(#"Added Custom | Discount Amount TE", "Regular Sales Amount TE (Native Currency)", each if [ISO Currency Code] = "GBP" or [ISO Currency Code] = "EUR" then (Number.Abs([#"Actual Sales Amount (Native Currency)"]) - Number.Abs([#"Tax Amount (Native Currency)"]) + Number.Abs([#"Discount Amount TE (Native Currency)"])) * Number.Sign([#"Quantity"]) else [#"Regular Sales Amount (Native Currency)"]),
    #"Added Custom | Actual Unit Price TE" = Table.AddColumn(#"Added Custom | Regular Sales Amount TE", "Actual Unit Price TE (Native Currency)", each [#"Actual Sales Amount TE (Native Currency)"] / [Quantity]),
    #"Added Custom | Regular Unit Price TE" = Table.AddColumn(#"Added Custom | Actual Unit Price TE", "Regular Unit Price TE (Native Currency)", each [#"Regular Sales Amount TE (Native Currency)"] / [Quantity]),
    #"Added Custom | Discount Amount Per Unit TE" = Table.AddColumn(#"Added Custom | Regular Unit Price TE", "Discount Amount Per Unit TE (Native Currency)", each [#"Discount Amount TE (Native Currency)"] / [Quantity] * Number.Sign([#"Quantity"])),
    #"Added Custom | Item Line (SKU5)" = Table.AddColumn(#"Added Custom | Discount Amount Per Unit TE", "Item Line (SKU5)", each Text.End([Item Id],5) & " - " & [Item Description]),
    #"Added Custom | Total Tender Amount (Native Currency)" = Table.AddColumn(#"Added Custom | Item Line (SKU5)", "Total Tender Amount (Native Currency)", each [#"Actual Sales Amount TE (Native Currency)"] + [#"Tax Amount (Native Currency)"]),
    #"Changed Type" = Table.TransformColumnTypes(#"Added Custom | Total Tender Amount (Native Currency)",{{"Coupon Multiply Allowed", type logical}, {"Electronic Coupon Allowed", type logical}, {"Coupon Allowed", type logical}, {"Quantity Modifiable", type logical}, {"Item Returned", type logical}, {"Item Price Overridable", type logical}, {"Discount Applied", type logical}, {"Damage Discount Applied", type logical}, {"Tax Included in Price", type logical}, {"Item Returnable", type logical}, {"Item Taxable", type logical}, {"Item Discountable", type logical}, {"Employee Discount Allowed", type logical}, {"Gift Receipt", type logical}, {"Endless Aisle", type logical}, {"Actual Unit Price TE (Native Currency)", type number}, {"Actual Sales Amount TE (Native Currency)", type number}, {"Quantity", Int64.Type}, {"Voided", type logical}, {"Transaction Line Key", type text}, {"Item Line", type text}, {"Regular Unit Price TE (Native Currency)", type number}, {"Regular Sales Amount TE (Native Currency)", type number}, {"Discount Amount Per Unit TE (Native Currency)", type number}, {"Item Line (SKU5)", type text}, {"Item Key", type text}, {"Tax Percentage", Percentage.Type}, {"Discount Amount TE (Native Currency)", type number}, {"Total Tender Amount (Native Currency)", type number}}),
    #"Replaced Errors" = Table.ReplaceErrorValues(#"Changed Type", {{"Tax Percentage", null}}),
    #"Replaced Value | _ with SPACE" = Table.ReplaceValue(#"Replaced Errors","_"," ",Replacer.ReplaceText,{"Item Type", "Line Item Type", "Inquiry Method Code", "Entry Method Code"}),
    #"Replaced Value | GIFTCARD with GIFT CARD" = Table.ReplaceValue(#"Replaced Value | _ with SPACE","GIFTCARD","GIFT CARD",Replacer.ReplaceText,{"Item Type"}),
    #"Replaced Value | loyalty with loyaltySPACE" = Table.ReplaceValue(#"Replaced Value | GIFTCARD with GIFT CARD","loyalty","loyalty ",Replacer.ReplaceText,{"Return Policy Id"}),
    #"Replaced Value | nonreceipted with non-Receipted" = Table.ReplaceValue(#"Replaced Value | loyalty with loyaltySPACE","nonreceipted","non-Receipted",Replacer.ReplaceText,{"Return Policy Id"}),
    #"Replaced Value | returns with returnsSPACE" = Table.ReplaceValue(#"Replaced Value | nonreceipted with non-Receipted","returns","returns ",Replacer.ReplaceText,{"Return Policy Id"}),
    #"Replaced Value | orders with ordersSPACE" = Table.ReplaceValue(#"Replaced Value | returns with returnsSPACE","orders","orders ",Replacer.ReplaceText,{"Return Policy Id"}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Replaced Value | orders with ordersSPACE",{{"Item Type", Text.Proper, type text}, {"Line Item Type", Text.Proper, type text}, {"Return Policy Id", Text.Proper, type text}, {"Inquiry Method Code", Text.Proper, type text}, {"Entry Method Code", Text.Proper, type text}}),
    #"Reordered Columns" = Table.ReorderColumns(#"Capitalized Each Word",{"Transaction Key", "Transaction Line Key", "Line Item Type", "Item Type", "Voided", "POS Item Id", "Item Id", "Item Description", "Item Long Description", "Item Name", "Item Line", "ISO Currency Code", "Quantity", "Regular Unit Price (Native Currency)", "Regular Unit Price TE (Native Currency)", "Regular Sales Amount (Native Currency)", "Regular Sales Amount TE (Native Currency)", "Discount Amount (Native Currency)", "Discount Amount TE (Native Currency)", "Discount Amount Per Unit TE (Native Currency)", "Tax Amount (Native Currency)", "Tax Percentage", "Actual Unit Price (Native Currency)", "Actual Unit Price TE (Native Currency)", "Actual Sales Amount (Native Currency)", "Actual Sales Amount TE (Native Currency)", "Item Taxable", "Tax Group Id", "Tax Included in Price", "Endless Aisle", "Order Id", "Order Line Number", "Item Price Overridable", "Coupon Allowed", "Coupon Multiply Allowed", "Electronic Coupon Allowed", "Serialized Coupon Barcode", "Item Discountable", "Item Weight Plus Tare", "Damage Discount Applied", "Discount Applied", "Employee Discount Allowed", "Find A Bear Id", "Gift Receipt", "Product Id", "Stuff Info", "Quantity Modifiable", "Item Returnable", "Item Returned", "Quantity Available for Return", "Return Policy Id", "Return Value Amount (Native Currency)", "Reason Code Group Id", "Reason Code", "Inquiry Method Code", "Entry Method Code", "Orig_Business Date", "price_type", "list_unit_price", "retail_unit_price", "item_tax_group_id", "tax_group_type", "tax_exempted", "tender_group", "serial_number", "cart_line_item_uuid", "related_line_sequence_number", "Orig_Business Unit Id", "Orig_Device Id", "Orig_Line Sequence Number", "Orig_Order Id", "Orig_Sequence Number", "Orig_Username", "Line Sequence Number", "Username", "Override User Id", "Item Key", "Item Line (SKU5)"})
in
    #"Reordered Columns"
```

### Retail Line Discounts (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source"),
    dbo_jumpmind_sls_retail_line_item_price_mod = Source{[Schema="dbo",Item="jumpmind_sls_retail_line_item_price_mod"]}[Data],
    #"Filtered Rows | Incremental Refresh" = Table.SelectRows(dbo_jumpmind_sls_retail_line_item_price_mod, each [last_update_time] >= RangeStart and [last_update_time] < RangeEnd),
    #"Filtered Rows | Remove Voided Lines" = Table.SelectRows(#"Filtered Rows | Incremental Refresh", each [voided] = 0),
    #"Renamed Columns" = Table.RenameColumns(#"Filtered Rows | Remove Voided Lines",{{"applied_coupon_item_ids", "Applied Coupon Item Ids"}, {"business_date", "Business Date"}, {"calc_method", "Calculation Method"}, {"create_by", "Created By"}, {"create_time", "Created Datetime"}, {"description", "Description"}, {"device_id", "Device Id"}, {"entry_method_code", "Entry Method Code"}, {"iso_currency_code", "ISO Currency Code"}, {"last_update_by", "Last Updated By"}, {"last_update_time", "Last Updated Datetime"}, {"line_sequence_number", "Line Sequence Number"}, {"loyalty_promotion_id", "Loyalty Promotion Id"}, {"mod_by_amount", "Modification Amount (Native Currency)"}, {"mod_by_percentage", "Modification Percentage"}, {"modification_total", "Modification Total (Native Currency)"}, {"override_user_id", "Override User Id"}, {"price_mod_source_sub_type_code", "Price Mod Source Sub-Type Code"}, {"price_mod_source_type_code", "Price Mod Source Type Code"}, {"price_mod_type_code", "Price Mod Type Code"}, {"promotion_id", "Promotion Id"}, {"promotion_reward_quantity", "Promotion Reward Quantity"}, {"promotion_type", "Promotion Type"}, {"reason_code", "Reason Code"}, {"ref_line_sequence_number", "Ref Line Sequence Number"}, {"sequence_number", "Sequence Number"}, {"username", "Username Id"}, {"voided", "Voided"}, {"promo_code_id", "Promo Code Id"}, {"reward_base_price_type_code", "Reward Base Price Type Code"}, {"vendor_funded_flag", "Vendor Funded Flag"}, {"quantity_index", "Quantity Index"}, {"rtn_device_id", "Return Device Id"}, {"rtn_business_date", "Return Business Date"}, {"rtn_sequence_number", "Return Sequence Number"}, {"returned_flag", "Returned Flag"}, {"external_id", "External Id"}}),
    #"Removed Columns | Redundant Columns" = Table.RemoveColumns(#"Renamed Columns",{"Created Datetime", "Created By", "Last Updated By"}),
    #"Merged Columns | Transaction Line Key" = Table.CombineColumns(Table.TransformColumnTypes(#"Removed Columns | Redundant Columns", {{"Sequence Number", type text}, {"Line Sequence Number", type text}}, "en-US"),{"Device Id", "Business Date", "Sequence Number", "Line Sequence Number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Transaction Line Key"),
    #"Merged Columns | Return Transaction Key" = Table.CombineColumns(Table.TransformColumnTypes(#"Merged Columns | Transaction Line Key", {{"Return Sequence Number", type text}}, "en-US"),{"Return Device Id", "Return Business Date", "Return Sequence Number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Return Transaction Key"),
    #"Replaced Value | _ with SPACE" = Table.ReplaceValue(#"Merged Columns | Return Transaction Key","_"," ",Replacer.ReplaceText,{"Promotion Type"}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Replaced Value | _ with SPACE",{{"Calculation Method", Text.Proper, type text}, {"Promotion Type", Text.Proper, type text}, {"Price Mod Type Code", Text.Proper, type text}, {"Price Mod Source Type Code", Text.Proper, type text}, {"Price Mod Source Sub-Type Code", Text.Proper, type text}}),
    #"Replaced Value | blank with NULL" = Table.ReplaceValue(#"Capitalized Each Word","",null,Replacer.ReplaceValue,{"Applied Coupon Item Ids"}),
    #"Replaced Value | Trans with Transaction" = Table.ReplaceValue(#"Replaced Value | blank with NULL","Trans","Transaction",Replacer.ReplaceText,{"Promotion Type", "Price Mod Type Code"}),
    #"Added Conditional Column | Promo Calculation" = Table.AddColumn(#"Replaced Value | Trans with Transaction", "Promo Calculation", each if [Promotion Id] = "addPennyToExchange" then "Exchange fix" else if Text.Contains([Description], "%") then "Percent Off" else if Text.Contains([Promotion Type], "Employee Discount") then "Percent Off" else if Text.Contains([Description], "$") then "Amount Off" else if Text.Contains([Description], "£") then "Amount Off" else if Text.Contains([Description], "€") then "Amount Off" else if Text.Contains([Description], "off") then "Amount Off" else if Text.Contains([Description], "OFF") then "Amount Off" else if Text.Contains([Description], "Off") then "Amount Off" else if Text.Contains([Description], "Reward") then "Amount Off" else "Other Discounts"),
    #"Replaced Value | -- with NULL" = Table.ReplaceValue(#"Added Conditional Column | Promo Calculation","--",null,Replacer.ReplaceValue,{"Return Transaction Key"}),
    #"Added Custom | Discount Line Object" = Table.AddColumn(#"Replaced Value | -- with NULL", "Discount Line Object", each [Promo Calculation] & " | " & [Price Mod Type Code] & "s"),
    #"Added Custom | Discount Line Type" = Table.AddColumn(#"Added Custom | Discount Line Object", "Discount Line Type", each [Price Mod Type Code] & "s" & " | " & [Promo Calculation]),
    #"Changed Type" = Table.TransformColumnTypes(#"Added Custom | Discount Line Type",{{"Modification Percentage", Percentage.Type}, {"Voided", type logical},  {"Returned Flag", type logical}, {"Vendor Funded Flag", type logical}})
in
    #"Changed Type"
```

### Retail Return Lines (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source"),
    dbo_jumpmind_sls_rtn_event_line_item = Source{[Schema="dbo",Item="jumpmind_sls_rtn_event_line_item"]}[Data],
    #"Filtered Rows | Incremental Refresh" = Table.SelectRows(dbo_jumpmind_sls_rtn_event_line_item, each [last_update_time] >= RangeStart and [last_update_time] < RangeEnd),
    #"Filtered Rows | Remove Voided Lines" = Table.SelectRows(#"Filtered Rows | Incremental Refresh", each [voided] = 0),
    #"Changed Type" = Table.TransformColumnTypes(#"Filtered Rows | Remove Voided Lines",{{"voided", type logical}}),
    #"Renamed Columns" = Table.RenameColumns(#"Changed Type",{{"business_date", "Business Date"}, {"create_by", "Created By"}, {"create_time", "Created Datetime"}, {"device_id", "Device Id"}, {"entry_method_code", "Entry Method Code"}, {"entry_mode_code", "Entry Mode Code"}, {"item_id", "Item Id"}, {"last_update_by", "Last Updated By"}, {"last_update_time", "Last Updated Datetime"}, {"line_sequence_number", "Line Sequence Number"}, {"orig_business_date", "Original Business Date"}, {"orig_device_id", "Original Device Id"}, {"orig_line_sequence_number", "Original Line Sequence Number"}, {"orig_order_id", "Original Order Id"}, {"orig_sequence_number", "Original Sequence Number"}, {"override_user_id", "Override User Id"}, {"pos_item_id", "POS Item Id"}, {"rtn_event_type_code", "Return Event Type Code"}, {"rtn_policy_id", "Return Policy Id"}, {"rtn_rejection_code", "Return Rejection Code"}, {"sequence_number", "Sequence Number"}, {"voided", "Voided"}}),
    #"Removed Columns | Redundant Columns" = Table.RemoveColumns(#"Renamed Columns",{"Created Datetime", "Created By", "Last Updated By"}),
    #"Merged Columns | Transaction Key" = Table.CombineColumns(Table.TransformColumnTypes(#"Removed Columns | Redundant Columns", {{"Sequence Number", type text}}, "en-US"),{"Device Id", "Business Date", "Sequence Number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Transaction Key"),
    #"Replaced Value | receipted with SPACEreceipted" = Table.ReplaceValue(#"Merged Columns | Transaction Key","receipted"," receipted",Replacer.ReplaceText,{"Return Policy Id"}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Replaced Value | receipted with SPACEreceipted",{{"Return Policy Id", Text.Proper, type text}, {"Entry Method Code", Text.Proper, type text}}),
    #"Replaced Value | nonSPACE with SPACENon-" = Table.ReplaceValue(#"Capitalized Each Word","non "," Non-",Replacer.ReplaceText,{"Return Policy Id"})
in
    #"Replaced Value | nonSPACE with SPACENon-"
```

### Tax Lines (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source"),
    dbo_jumpmind_sls_tax_retail_line_item = Source{[Schema="dbo",Item="jumpmind_sls_tax_retail_line_item"]}[Data],
    #"Filtered Rows | Incremental Refresh" = Table.SelectRows(dbo_jumpmind_sls_tax_retail_line_item, each [last_update_time] >= RangeStart and [last_update_time] < RangeEnd),
    #"Filtered Rows | Remove Web Merge" = Table.SelectRows(#"Filtered Rows | Incremental Refresh", each ([create_by] = "openpos-sls")),
    #"Filtered Rows | Remove Voided Lines" = Table.SelectRows(#"Filtered Rows | Remove Web Merge", each [voided] = 0),
    #"Renamed Columns" = Table.RenameColumns(#"Filtered Rows | Remove Voided Lines",{{"authority_id", "Authority Id"}, {"authority_type", "Authority Type"}, {"business_date", "Business Date"}, {"calculation_source", "Calculation Source"}, {"create_by", "Created By"}, {"create_time", "Created Datetime"}, {"device_id", "Device Id"}, {"entry_method_code", "Entry Method Code"}, {"group_id", "Group Id"}, {"iso_currency_code", "ISO Currency Code"}, {"last_update_by", "Last Updated By"}, {"last_update_time", "Last Updated Datetime"}, {"line_sequence_number", "Line Sequence Number"}, {"money_tax_amount", "Money Tax Amount (Native Currency)"}, {"override_amount", "Override Amount (Native Currency)"}, {"override_applied", "Override Applied"}, {"override_percent", "Override Percent"}, {"override_reason_code", "Override Reason Code"}, {"override_user_id", "Override User Id"}, {"rate_rule_sequence_number", "Rate Rule Sequence Number"}, {"rule_name", "Rule Name"}, {"sequence_number", "Sequence Number"}, {"tax_amount", "Tax Amount (Native Currency)"}, {"tax_exempt", "Tax Exempt"}, {"tax_exempt_amount", "Tax Exempt Amount (Native Currency)"}, {"tax_exempt_id", "Tax Exempt Id"}, {"tax_holiday_indicator", "Tax Holiday Indicator"}, {"tax_included_in_price", "Tax Included in Price"}, {"tax_line_sequence_number", "Tax Line Sequence Number"}, {"tax_percentage", "Tax Percentage"}, {"tax_type", "Tax Type"}, {"taxable_amount", "Taxable Amount (Native Currency)"}, {"voided", "Voided"}, {"rule_description", "Rule Description"}}),
    #"Removed Columns | Empty Columns" = Table.RemoveColumns(#"Renamed Columns",{"Entry Method Code"}),
    #"Merged Columns | Transaction Line Key" = Table.CombineColumns(Table.TransformColumnTypes(#"Removed Columns | Empty Columns", {{"Sequence Number", type text}, {"Line Sequence Number", type text}}, "en-US"),{"Device Id", "Business Date", "Sequence Number", "Line Sequence Number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Transaction Line Key"),
    #"Divided Column | Percentages by 100" = Table.TransformColumns(#"Merged Columns | Transaction Line Key", {{"Override Percent", each _ / 100, type number}, {"Tax Percentage", each _ / 100, type number}}),
    #"Added Conditional Column | Tax Category" = Table.AddColumn(#"Divided Column | Percentages by 100", "Tax Category", each if [Tax Type] = "Fee" then "Fee" else if [Tax Type] = "Surcharge" then "Fee" else "Merchandise"),
    #"Replaced Value | IndigenousTaxExemption" = Table.ReplaceValue(#"Added Conditional Column | Tax Category","IndigenousTaxExemption","Indigenous Tax Exemption",Replacer.ReplaceText,{"Rule Name"}),
    #"Changed Type" = Table.TransformColumnTypes(#"Replaced Value | IndigenousTaxExemption",{{"Voided", type logical}, {"Tax Holiday Indicator", type logical}, {"Override Applied", type logical}, {"Tax Exempt", type logical}, {"Tax Included in Price", type logical}, {"Override Percent", Percentage.Type}, {"Tax Percentage", Percentage.Type}, {"Tax Category", type text}})
in
    #"Changed Type"
```

### Tender Settlement Lines (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source"),
    dbo_jumpmind_sls_tender_settlement_line_itm = Source{[Schema="dbo",Item="jumpmind_sls_tender_settlement_line_itm"]}[Data],
    #"Filtered Rows | Incremental Refresh" = Table.SelectRows(dbo_jumpmind_sls_tender_settlement_line_itm, each [last_update_time] >= RangeStart and [last_update_time] < RangeEnd),
    #"Filtered Rows | Remove Voided Lines" = Table.SelectRows(#"Filtered Rows | Incremental Refresh", each [voided] = 0),
    #"Renamed Columns" = Table.RenameColumns(#"Filtered Rows | Remove Voided Lines",{{"business_date", "Business Date"}, {"close_media_quantity", "Close Media Quantity"}, {"close_session_amount", "Close Session Amount"}, {"counted_media_quantity", "Counted Media Quantity"}, {"counted_session_amount", "Counted Session Amount"}, {"create_by", "Created By"}, {"create_time", "Created Datetime"}, {"device_id", "Device Id"}, {"difference_reason", "Difference Reason"}, {"entry_method_code", "Entry Method Code"}, {"from_repository", "From Repository"}, {"iso_currency_code", "ISO Currency Code"}, {"last_update_by", "Last Updated By"}, {"last_update_time", "Last Updated Datetime"}, {"line_sequence_number", "Line Sequence Number"}, {"open_media_quantity", "Open Media Quantity"}, {"open_session_amount", "Open Session Amount"}, {"over_under_media_quantity", "Over Under Media Quantity"}, {"over_under_session_amount", "Over Under Session Amount"}, {"override_user_id", "Override User Id"}, {"pickup_amount", "Pickup Amount"}, {"reason_code", "Reason Code"}, {"sequence_number", "Sequence Number"}, {"session_id", "Session Id"}, {"store_bank_id", "Store Bank Id"}, {"tender_code", "Tender Code"}, {"tender_type_code", "Tender Type Code"}, {"till_id", "Till Id"}, {"to_repository", "To Repository"}, {"voided", "Voided"}}),
    #"Removed Columns | Redundant Columns" = Table.RemoveColumns(#"Renamed Columns",{"Created Datetime", "Created By", "Last Updated By"}),
    #"Removed Columns | Empty Columns" = Table.RemoveColumns(#"Removed Columns | Redundant Columns",{"Entry Method Code"}),
    #"Merged Columns | Transaction Key" = Table.CombineColumns(Table.TransformColumnTypes(#"Removed Columns | Empty Columns", {{"Sequence Number", type text}}, "en-US"),{"Device Id", "Business Date", "Sequence Number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Transaction Key"),
    #"Replaced Value | _ with SPACE" = Table.ReplaceValue(#"Merged Columns | Transaction Key","_"," ",Replacer.ReplaceText,{"Tender Type Code", "Tender Code", "From Repository", "To Repository", "Reason Code"}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Replaced Value | _ with SPACE",{{"Tender Type Code", Text.Proper, type text}, {"From Repository", Text.Proper, type text}, {"To Repository", Text.Proper, type text}}),
    #"Added Prefix | FromSPACE" = Table.TransformColumns(#"Capitalized Each Word", {{"From Repository", each "From " & _, type text}}),
    #"Added Prefix | toSPACE" = Table.TransformColumns(#"Added Prefix | FromSPACE", {{"To Repository", each "to " & _, type text}}),
    #"Merged Columns | Repository Transfer Type" = Table.CombineColumns(#"Added Prefix | toSPACE",{"From Repository", "To Repository"},Combiner.CombineTextByDelimiter(" ", QuoteStyle.None),"Repository Transfer Type"),
    #"Replaced Value | E WALLET with E-Wallet" = Table.ReplaceValue(#"Merged Columns | Repository Transfer Type","E WALLET","E-Wallet",Replacer.ReplaceText,{"Reason Code"}),
    #"Replaced Value | Open with OpenSPACE" = Table.ReplaceValue(#"Replaced Value | E WALLET with E-Wallet","Open","Open ",Replacer.ReplaceText,{"Reason Code"}),
    #"Replaced Value | Close with CloseSPACE" = Table.ReplaceValue(#"Replaced Value | Open with OpenSPACE","Close","Close ",Replacer.ReplaceText,{"Reason Code"}),
    #"Replaced Value | Store with StoreSPACE" = Table.ReplaceValue(#"Replaced Value | Close with CloseSPACE","Store","Store ",Replacer.ReplaceText,{"Reason Code"}),
    #"Replaced Value | NonCounted with Non-Counted" = Table.ReplaceValue(#"Replaced Value | Store with StoreSPACE","NonCounted","Non-Counted ",Replacer.ReplaceText,{"Reason Code"}),
    #"Replaced Value | TenderUnitCount with Tender Unit Count" = Table.ReplaceValue(#"Replaced Value | NonCounted with Non-Counted","TenderUnitCount"," Tender Unit Count",Replacer.ReplaceText,{"Reason Code"}),
    #"Capitalized Each Word1" = Table.TransformColumns(#"Replaced Value | TenderUnitCount with Tender Unit Count",{{"Reason Code", Text.Proper, type text}}),
    #"Replaced Value | E Wallet with E-Wallet" = Table.ReplaceValue(#"Capitalized Each Word1","E Wallet","E-Wallet",Replacer.ReplaceText,{"Tender Type Code"}),
    #"Capitalized Each Word2" = Table.TransformColumns(#"Replaced Value | E Wallet with E-Wallet",{{"Tender Code", Text.Proper, type text}}),
    #"Replaced Value | Usd with USD" = Table.ReplaceValue(#"Capitalized Each Word2","Usd","USD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Cad with CAD" = Table.ReplaceValue(#"Replaced Value | Usd with USD","Cad","CAD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Eur with EUR" = Table.ReplaceValue(#"Replaced Value | Cad with CAD","Eur","EUR",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Gbp with GBP" = Table.ReplaceValue(#"Replaced Value | Eur with EUR","Gbp","GBP",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Hkd with HKD" = Table.ReplaceValue(#"Replaced Value | Gbp with GBP","Hkd","HKD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Mxn with MXN" = Table.ReplaceValue(#"Replaced Value | Hkd with HKD","Mxn","MXN",Replacer.ReplaceText,{"Tender Code"}),
    #"Changed Type" = Table.TransformColumnTypes(#"Replaced Value | Mxn with MXN",{{"Voided", type logical}}),
    #"Reordered Columns" = Table.ReorderColumns(#"Changed Type",{"Transaction Key", "Line Sequence Number", "Session Id", "Till Id", "Store Bank Id", "Tender Type Code", "Tender Code", "ISO Currency Code", "Repository Transfer Type", "Reason Code", "Open Session Amount", "Close Session Amount", "Counted Session Amount", "Over Under Session Amount", "Pickup Amount", "Difference Reason", "Open Media Quantity", "Close Media Quantity", "Counted Media Quantity", "Over Under Media Quantity", "Voided", "Override User Id"}),
    #"Replaced Value | Amex with American Express" = Table.ReplaceValue(#"Reordered Columns","Amex","American Express",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Mastercard with MasterCard" = Table.ReplaceValue(#"Replaced Value | Amex with American Express","Mastercard","MasterCard",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Globale with Global-e" = Table.ReplaceValue(#"Replaced Value | Mastercard with MasterCard","Globale","Global-e",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Applepay with Apple Pay" = Table.ReplaceValue(#"Replaced Value | Globale with Global-e","Applepay","Apple Pay",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Giftcard with Gift Card" = Table.ReplaceValue(#"Replaced Value | Applepay with Apple Pay","Giftcard","Gift Card",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Paypal with PayPal" = Table.ReplaceValue(#"Replaced Value | Giftcard with Gift Card","Paypal","PayPal",Replacer.ReplaceText,{"Tender Code"})
in
    #"Replaced Value | Paypal with PayPal"
```

### Tender Lines (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source"),
    dbo_jumpmind_sls_tender_line_item = Source{[Schema="dbo",Item="jumpmind_sls_tender_line_item"]}[Data],
    #"Filtered Rows | Incremental Refresh" = Table.SelectRows(dbo_jumpmind_sls_tender_line_item, each [last_update_time] >= RangeStart and [last_update_time] < RangeEnd),
    #"Filtered Rows | Remove Web Merge" = Table.SelectRows(#"Filtered Rows | Incremental Refresh", each [create_by] = "openpos-sls"),
    #"Filtered Rows | Remove Voided Lines" = Table.SelectRows(#"Filtered Rows | Remove Web Merge", each [voided] = 0),
    #"Renamed Columns" = Table.RenameColumns(#"Filtered Rows | Remove Voided Lines",{{"business_date", "Business Date"}, {"cash_back_amount", "Cash Back Amount (Native Currency)"}, {"certificate_number", "Certificate Number"}, {"change_flag", "Change Flag"}, {"create_by", "Created By"}, {"create_time", "Created Datetime"}, {"customer_account_number", "Customer Account Number"}, {"device_id", "Device Id"}, {"entry_method_code", "Entry Method Code"}, {"exchange_rate", "Exchange Rate"}, {"foreign_currency_amount", "Foreign Currency Amount"}, {"iso_currency_code", "ISO Currency Code"}, {"iso_foreign_currency_code", "ISO Foreign Currency Code"}, {"last_update_by", "Last Updated By"}, {"last_update_time", "Last Updated Datetime"}, {"line_sequence_number", "Line Sequence Number"}, {"override_user_id", "Override User Id"}, {"overtendered", "Overtendered"}, {"partially_approved", "Partially Approved"}, {"post_void", "Post Void"}, {"sequence_number", "Sequence Number"}, {"tender_account_number", "Tender Account Number"}, {"tender_amount", "Tender Amount (Native Currency)"}, {"tender_code", "Tender Code"}, {"tender_finance_id", "Tender Finance Id"}, {"tender_type_code", "Tender Type Code"}, {"voided", "Voided"}}),
    #"Removed Columns | Empty Columns" = Table.RemoveColumns(#"Renamed Columns",{"Entry Method Code", "Tender Finance Id", "Certificate Number", "ISO Foreign Currency Code", "Foreign Currency Amount", "Customer Account Number", "Tender Account Number"}),
    #"Merged Columns | Transaction Key" = Table.CombineColumns(Table.TransformColumnTypes(#"Removed Columns | Empty Columns", {{"Sequence Number", type text}}, "en-US"),{"Device Id", "Business Date", "Sequence Number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Transaction Key"),
    #"Added Custom | Transaction Line Key" = Table.AddColumn(#"Merged Columns | Transaction Key", "Transaction Line Key", each [Transaction Key] & "-" & Text.From([Line Sequence Number])),
    #"Replaced Value | _ with SPACE" = Table.ReplaceValue(#"Added Custom | Transaction Line Key","_"," ",Replacer.ReplaceText,{"Tender Code", "Tender Type Code"}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Replaced Value | _ with SPACE",{{"Tender Code", Text.Proper, type text}, {"Tender Type Code", Text.Proper, type text}}),
    #"Replaced Value | Usd with USD" = Table.ReplaceValue(#"Capitalized Each Word","Usd","USD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Cad with CAD" = Table.ReplaceValue(#"Replaced Value | Usd with USD","Cad","CAD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Eur with EUR" = Table.ReplaceValue(#"Replaced Value | Cad with CAD","Eur","EUR",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Gbp with GBP" = Table.ReplaceValue(#"Replaced Value | Eur with EUR","Gbp","GBP",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Amex with American Express" = Table.ReplaceValue(#"Replaced Value | Gbp with GBP","Amex","American Express",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Giftcard with Gift Card" = Table.ReplaceValue(#"Replaced Value | Amex with American Express","Giftcard","Gift Card",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Mastercard with MasterCard" = Table.ReplaceValue(#"Replaced Value | Giftcard with Gift Card","Mastercard","MasterCard",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | American Express with American Express Credit" = Table.ReplaceValue(#"Replaced Value | Mastercard with MasterCard","American Express","American Express Credit",Replacer.ReplaceValue,{"Tender Code"}),
    #"Replaced Value | E Wallet with E-Wallet" = Table.ReplaceValue(#"Replaced Value | American Express with American Express Credit","E Wallet","E-Wallet",Replacer.ReplaceText,{"Tender Type Code"}),
    #"Added Conditional Column | Charge Type" = Table.AddColumn(#"Replaced Value | E Wallet with E-Wallet", "Charge Type", each if [#"Tender Amount (Native Currency)"] < 0 then "Credit" else if [#"Tender Amount (Native Currency)"] >= 0 then "Debit" else null),
    #"Added Custom | Tender Object-Action" = Table.AddColumn(#"Added Conditional Column | Charge Type", "Tender Object-Action", each if [Charge Type] = "Debit" then [Tender Code] & " charged" else [Tender Code] & " credited"),
    #"Changed Type" = Table.TransformColumnTypes(#"Added Custom | Tender Object-Action",{{"Change Flag", type logical}, {"Voided", type logical}, {"Overtendered", type logical}, {"Partially Approved", type logical}, {"Post Void", type logical}, {"Charge Type", type text}, {"Tender Object-Action", type text}})
in
    #"Changed Type"
```

### Tender Card Lines (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source"),
    dbo_jumpmind_sls_card_line_item = Source{[Schema="dbo",Item="jumpmind_sls_card_line_item"]}[Data],
    #"Filtered Rows | Incremental Refresh" = Table.SelectRows(dbo_jumpmind_sls_card_line_item, each [last_update_time] >= RangeStart and [last_update_time] < RangeEnd),
    #"Filtered Rows | Remove Web Merge" = Table.SelectRows(#"Filtered Rows | Incremental Refresh", each [create_by] = "openpos-sls"),
    #"Merged Columns | Transaction Line Key" = Table.CombineColumns(Table.TransformColumnTypes(#"Filtered Rows | Remove Web Merge", {{"sequence_number", type text}, {"ref_line_sequence_number", type text}}, "en-US"),{"device_id", "business_date", "sequence_number", "ref_line_sequence_number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Transaction Line Key"),
    #"Removed Duplicates | Remove Errors from Stores Not Closing Properly" = Table.Distinct(#"Merged Columns | Transaction Line Key", {"Transaction Line Key"}),
    #"Renamed Columns" = Table.RenameColumns(#"Removed Duplicates | Remove Errors from Stores Not Closing Properly",{{"brand", "Brand"}, {"card_name", "Card Name"}, {"card_number", "Card Number"}, {"code", "Tender Code"}, {"create_by", "Created By"}, {"create_time", "Created Datetime"}, {"entry_mode", "Entry Mode"}, {"expiration_date", "Expiration Date"}, {"last_update_by", "Last Updated By"}, {"last_update_time", "Last Updated Datetime"}, {"masked_card_number", "Masked Card Number"}, {"payment_provider_code", "Payment Provider Code"}, {"line_sequence_number", "Line Sequence Number"}, {"service_code", "Service Code"}, {"type_code", "Tender Type Code"}}),
    #"Removed Columns | Redundant Columns" = Table.RemoveColumns(#"Renamed Columns",{"Created Datetime", "Created By", "Last Updated By"}),
    #"Removed Columns | Empty Columns" = Table.RemoveColumns(#"Removed Columns | Redundant Columns",{"Payment Provider Code", "Service Code"}),
    #"Replaced Value | _ with SPACE" = Table.ReplaceValue(#"Removed Columns | Empty Columns","_"," ",Replacer.ReplaceText,{"Brand", "Card Name", "Tender Code", "Tender Type Code"}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Replaced Value | _ with SPACE",{{"Brand", Text.Proper, type text}, {"Card Name", Text.Proper, type text}, {"Tender Code", Text.Proper, type text}, {"Entry Mode", Text.Proper, type text}, {"Tender Type Code", Text.Proper, type text}}),
    #"Replaced Value | E Wallet with E-Wallet" = Table.ReplaceValue(#"Capitalized Each Word","E Wallet","E-Wallet",Replacer.ReplaceText,{"Tender Type Code"}),
    #"Replaced Value | Credit Card with Credit" = Table.ReplaceValue(#"Replaced Value | E Wallet with E-Wallet","Credit Card","Credit",Replacer.ReplaceText,{"Tender Type Code"}),
    #"Replaced Value | Giftcard with Gift Card" = Table.ReplaceValue(#"Replaced Value | Credit Card with Credit","Giftcard","Gift Card",Replacer.ReplaceText,{"Brand", "Card Name", "Tender Code", "Tender Type Code"}),
    #"Replaced Value | Amex with American Express" = Table.ReplaceValue(#"Replaced Value | Giftcard with Gift Card","Amex","American Express",Replacer.ReplaceText,{"Brand", "Card Name", "Tender Code"}),
    #"Replaced Value | Applepay with Apple Pay" = Table.ReplaceValue(#"Replaced Value | Amex with American Express","Applepay","Apple Pay",Replacer.ReplaceText,{"Brand", "Card Name", "Tender Code"}),
    #"Replaced Value | Globale with Global-e" = Table.ReplaceValue(#"Replaced Value | Applepay with Apple Pay","Globale","Global-e",Replacer.ReplaceText,{"Brand", "Card Name", "Tender Code"}),
    #"Replaced Value | Jcb with JCB" = Table.ReplaceValue(#"Replaced Value | Globale with Global-e","Jcb","JCB",Replacer.ReplaceText,{"Brand", "Card Name", "Tender Code"}),
    #"Replaced Value | Mc with Mastercard" = Table.ReplaceValue(#"Replaced Value | Jcb with JCB","Mc","Mastercard",Replacer.ReplaceText,{"Brand", "Card Name", "Tender Code"}),
    #"Replaced Value | Mastercard with MasterCard" = Table.ReplaceValue(#"Replaced Value | Mc with Mastercard","Mastercard","MasterCard",Replacer.ReplaceText,{"Brand", "Card Name", "Tender Code"}),
    #"Replaced Value | Paypal with PayPal" = Table.ReplaceValue(#"Replaced Value | Mastercard with MasterCard","Paypal","PayPal",Replacer.ReplaceText,{"Brand", "Card Name", "Tender Code"}),
    #"Replaced Value | Uk with UK" = Table.ReplaceValue(#"Replaced Value | Paypal with PayPal","Uk","UK",Replacer.ReplaceText,{"Brand", "Card Name", "Tender Code"}),
    #"Replaced Value | Valuelink with ValueLink" = Table.ReplaceValue(#"Replaced Value | Uk with UK","Valuelink","ValueLink",Replacer.ReplaceText,{"Brand"}),
    #"Replaced Value | Vpay with V Pay" = Table.ReplaceValue(#"Replaced Value | Valuelink with ValueLink","Vpay","V Pay",Replacer.ReplaceText,{"Brand", "Card Name", "Tender Code"}),
    #"Replaced Value | Uspindebit with US PIN Debit" = Table.ReplaceValue(#"Replaced Value | Vpay with V Pay","Uspindebit","US PIN Debit",Replacer.ReplaceText,{"Brand", "Card Name", "Tender Code"}),
    #"Replaced Value | credit with SPACECredit" = Table.ReplaceValue(#"Replaced Value | Uspindebit with US PIN Debit","credit"," Credit",Replacer.ReplaceText,{"Card Name"}),
    #"Replaced Value | debit with SPACEDebit" = Table.ReplaceValue(#"Replaced Value | credit with SPACECredit","debit"," Debit",Replacer.ReplaceText,{"Card Name"}),
    #"Replaced Value | commercial with SPACECommercial" = Table.ReplaceValue(#"Replaced Value | debit with SPACEDebit","commercial"," Commercial",Replacer.ReplaceText,{"Card Name"}),
    #"Replaced Value | corporate with SPACECorporate" = Table.ReplaceValue(#"Replaced Value | commercial with SPACECommercial","corporate"," Corporate",Replacer.ReplaceText,{"Card Name"}),
    #"Replaced Value | fleet with SPACEFleet" = Table.ReplaceValue(#"Replaced Value | corporate with SPACECorporate","fleet"," Fleet",Replacer.ReplaceText,{"Card Name"}),
    #"Replaced Value | premium with SPACEPremium" = Table.ReplaceValue(#"Replaced Value | fleet with SPACEFleet","premium"," Premium",Replacer.ReplaceText,{"Card Name"}),
    #"Replaced Value | standard with SPACEStandard" = Table.ReplaceValue(#"Replaced Value | premium with SPACEPremium","standard"," Standard",Replacer.ReplaceText,{"Card Name"}),
    #"Replaced Value | super with SPACESuper" = Table.ReplaceValue(#"Replaced Value | standard with SPACEStandard","super"," Super",Replacer.ReplaceText,{"Card Name"}),
    #"Replaced Value | purchasing with SPACEPurchasing" = Table.ReplaceValue(#"Replaced Value | super with SPACESuper","purchasing"," Purchasing",Replacer.ReplaceText,{"Card Name"}),
    #"Replaced Value | prepaidanonymous with SPACEPrepaid Anonymous" = Table.ReplaceValue(#"Replaced Value | purchasing with SPACEPurchasing","prepaidanonymous"," Prepaid Anonymous",Replacer.ReplaceText,{"Card Name"}),
    #"Replaced Value | American Express with American Express Credit" = Table.ReplaceValue(#"Replaced Value | prepaidanonymous with SPACEPrepaid Anonymous","American Express","American Express Credit",Replacer.ReplaceValue,{"Tender Code"}),
    #"Replaced Value | Cad with CAD" = Table.ReplaceValue(#"Replaced Value | American Express with American Express Credit","Cad","CAD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Eur with EUR" = Table.ReplaceValue(#"Replaced Value | Cad with CAD","Eur","EUR",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Gbp with GBP" = Table.ReplaceValue(#"Replaced Value | Eur with EUR","Gbp","GBP",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Hkd with HKD" = Table.ReplaceValue(#"Replaced Value | Gbp with GBP","Hkd","HKD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Mxn with MXN" = Table.ReplaceValue(#"Replaced Value | Hkd with HKD","Mxn","MXN",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Usd with USD" = Table.ReplaceValue(#"Replaced Value | Mxn with MXN","Usd","USD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Cup with CUP" = Table.ReplaceValue(#"Replaced Value | Usd with USD","Cup","CUP",Replacer.ReplaceText,{"Brand", "Card Name"}),
    #"Reordered Columns" = Table.ReorderColumns(#"Replaced Value | Cup with CUP",{"Transaction Line Key", "Line Sequence Number", "Brand", "Card Name", "Tender Code", "Tender Type Code", "Masked Card Number", "Card Number", "Expiration Date", "Entry Mode", "gift_card_action_code"})
in
    #"Reordered Columns"
```

### Measure Table

```sql
let
    Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("i44FAA==", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [Column1 = _t]),
    #"Changed Type" = Table.TransformColumnTypes(Source,{{"Column1", type text}}),
    #"Removed Columns" = Table.RemoveColumns(#"Changed Type",{"Column1"})
in
    #"Removed Columns"
```

### Activated Gift Cards (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="SELECT DISTINCT#(lf)#(lf)       jumpmind_sls_card_line_item.[device_id]#(lf)      ,jumpmind_sls_card_line_item.[business_date]#(lf)      ,jumpmind_sls_card_line_item.[sequence_number]#(lf)      ,jumpmind_sls_card_line_item.[line_sequence_number]#(lf)      ,jumpmind_sls_card_line_item.[brand]#(lf)      ,jumpmind_sls_card_line_item.[card_name]#(lf)      ,jumpmind_sls_card_line_item.[code]#(lf)      ,jumpmind_sls_card_line_item.[type_code]#(lf)      ,jumpmind_sls_card_line_item.[payment_provider_code]#(lf)      ,jumpmind_sls_card_line_item.[masked_card_number]#(lf)      ,jumpmind_sls_card_line_item.[entry_mode]#(lf)      ,jumpmind_sls_card_line_item.[service_code]#(lf)      ,jumpmind_sls_card_line_item.[expiration_date]#(lf)      ,jumpmind_sls_card_line_item.[ref_line_sequence_number]#(lf)      ,jumpmind_sls_card_line_item.[card_number]#(lf)      ,jumpmind_sls_card_line_item.[gift_card_action_code]#(lf)#(tab)  --,jumpmind_sls_card_line_item.[create_time]#(lf)      ,jumpmind_sls_card_line_item.[last_update_time]#(lf)      --,jumpmind_sls_card_line_item.[create_by]#(lf)      --,jumpmind_sls_card_line_item.[last_update_by]#(lf)#(lf)#(lf)#(tab)FROM#(tab)#(tab)#(tab)#(tab)#(tab)[dbo].[jumpmind_sls_card_line_item]#(lf)#(lf)#(lf)#(tab)-----------------------------------------------#(lf)#(tab)--REQUIRED FILTERS#(tab)-#(tab)DO NOT REMOVE#(tab)#(tab)#(tab)#(tab)#(tab)#(lf)#(tab)-----------------------------------------------#(tab)#(lf)#(lf)#(tab)WHERE#(tab)#(tab)#(tab)#(tab)#(tab)jumpmind_sls_card_line_item.[type_code]#(tab)#(tab)#(tab)#(tab)=#(tab)'GIFTCARD'#(tab)#(lf)#(lf)#(tab)ORDER BY#(tab)#(tab)#(tab)#(tab)jumpmind_sls_card_line_item.[business_date]#(tab)#(tab)#(tab)ASC,#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)jumpmind_sls_card_line_item.[device_id]#(tab)#(tab)#(tab)ASC,#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)jumpmind_sls_card_line_item.[sequence_number]#(tab)#(tab)ASC,#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)jumpmind_sls_card_line_item.[line_sequence_number]#(tab)ASC#(tab)", CreateNavigationProperties=false]),
    #"Filtered Rows | Incremental Refresh" = Table.SelectRows(Source, each [last_update_time] >= RangeStart and [last_update_time] < RangeEnd),
    #"Filtered Rows | Type Code = GIFTCARD" = Table.SelectRows(#"Filtered Rows | Incremental Refresh", each ([type_code] = "GIFTCARD")),
    #"Merged Columns | Transaction Line Key" = Table.CombineColumns(Table.TransformColumnTypes(#"Filtered Rows | Type Code = GIFTCARD", {{"sequence_number", type text}, {"ref_line_sequence_number", type text}}, "en-US"),{"device_id", "business_date", "sequence_number", "ref_line_sequence_number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Transaction Line Key"),
    #"Reordered Columns" = Table.ReorderColumns(#"Merged Columns | Transaction Line Key",{"Transaction Line Key", "line_sequence_number", "brand", "card_name", "code", "type_code", "payment_provider_code", "masked_card_number", "entry_mode", "service_code", "expiration_date", "card_number", "last_update_time"}),
    #"Renamed Columns" = Table.RenameColumns(#"Reordered Columns",{{"brand", "Brand"}, {"card_name", "Card Name"}, {"card_number", "Card Number"}, {"code", "Code"}, {"entry_mode", "Entry Mode"}, {"expiration_date", "Expiration Date"},  {"last_update_time", "Last Updated Datetime"}, {"masked_card_number", "Masked Card Number"}, {"payment_provider_code", "Payment Provider Code"}, {"line_sequence_number", "Line Sequence Number"}, {"service_code", "Service Code"}, {"type_code", "Type Code"}, {"gift_card_action_code", "Gift Card Action Code"}}),
    #"Replaced Value | GIFTCARD with Gift Card" = Table.ReplaceValue(#"Renamed Columns","GIFTCARD","Gift Card",Replacer.ReplaceText,{"Brand", "Code", "Type Code"}),
    #"Removed Duplicates | Transaction Line Key" = Table.Distinct(#"Replaced Value | GIFTCARD with Gift Card", {"Transaction Line Key"}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Removed Duplicates | Transaction Line Key",{{"Card Name", Text.Proper, type text}, {"Entry Mode", Text.Proper, type text}})
in
    #"Capitalized Each Word"
```

### Tax Authorities (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="SELECT DISTINCT#(lf)#(lf)       [id]#(lf)      ,[auth_name]#(lf)      ,[rounding_code]#(lf)      ,[rounding_digits_quantity]#(lf)      ,[auth_type_name]#(lf)      --,[category]#(lf)      --,[create_time]#(lf)      --,[create_by]#(lf)      --,[last_update_time]#(lf)      --,[last_update_by]#(lf)#(lf)  FROM#(tab)#(tab)[dbo].[jumpmind_tax_authority]#(lf)#(lf)  ORDER BY#(tab)[id]#(tab)ASC", CreateNavigationProperties=false]),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"auth_name", "Authorization Name"}, {"id", "Id"}, 
{"rounding_code", "Rounding Code"}, {"rounding_digits_quantity", "Rounding Digits Quantity"}, {"auth_type_name", "Authorization Type Name"}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Renamed Columns",{{"Rounding Code", Int64.Type}})
in
    #"Changed Type"
```

### Tax Groups (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="SELECT DISTINCT#(lf)#(lf)       [id]#(lf)      ,[group_name]#(lf)      ,[description]#(lf)      --,[category]#(lf)      --,[receipt_print_code]#(lf)      --,[create_time]#(lf)      --,[create_by]#(lf)      --,[last_update_time]#(lf)      --,[last_update_by]#(lf)#(lf)  FROM [dbo].[jumpmind_tax_group]#(lf)#(lf)  ORDER BY#(tab)[id]#(tab)ASC#(lf)", CreateNavigationProperties=false]),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"description", "Description"}, {"group_name", "Group Name"}, {"id", "Id"}}),
    #"Replaced Value | """" with NULL" = Table.ReplaceValue(#"Renamed Columns","",null,Replacer.ReplaceValue,{"Group Name"})
in
    #"Replaced Value | """" with NULL"
```

### Tenders (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="SELECT DISTINCT#(lf)#(lf)       [tender_code]#(lf)      ,[tender_type_code]#(lf)      ,[iso_currency_code]#(lf)      ,[description]#(lf)      ,[cash_drawer_open_required]#(lf)      ,[till_unit_count_required]#(lf)      ,[till_amount_count_required]#(lf)      ,[return_tender_type_code]#(lf)      --,[create_time]#(lf)      --,[create_by]#(lf)      --,[last_update_time]#(lf)      --,[last_update_by]#(lf)      --,[check_number]#(lf)#(lf)  FROM#(tab)#(tab)[dbo].[jumpmind_sls_tender]#(lf)#(lf)  ORDER BY#(tab)[tender_code]#(tab)ASC", CreateNavigationProperties=false]),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"cash_drawer_open_required", "Cash Drawer Open Required"}, {"description", "Description"}, {"iso_currency_code", "ISO Currency Code"}, {"return_tender_type_code", "Return Tender Type Code"}, {"tender_code", "Tender Code"}, {"tender_type_code", "Tender Type Code"}, {"till_amount_count_required", "Till Amount Count Required"}, {"till_unit_count_required", "Till Unit Count Required"}}),
    #"Replaced Value | _ with SPACE" = Table.ReplaceValue(#"Renamed Columns","_"," ",Replacer.ReplaceText,{"Tender Code", "Tender Type Code", "Return Tender Type Code"}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Replaced Value | _ with SPACE",{{"Tender Code", Text.Proper, type text}, {"Return Tender Type Code", Text.Proper, type text}, {"Tender Type Code", Text.Proper, type text}}),
    #"Replaced Value | Cad with CAD" = Table.ReplaceValue(#"Capitalized Each Word","Cad","CAD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Eur with EUR" = Table.ReplaceValue(#"Replaced Value | Cad with CAD","Eur","EUR",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Gbp with GBP" = Table.ReplaceValue(#"Replaced Value | Eur with EUR","Gbp","GBP",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Hkd with HKD" = Table.ReplaceValue(#"Replaced Value | Gbp with GBP","Hkd","HKD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Mxn with MXN" = Table.ReplaceValue(#"Replaced Value | Hkd with HKD","Mxn","MXN",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Usd with USD" = Table.ReplaceValue(#"Replaced Value | Mxn with MXN","Usd","USD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Amex with American Express" = Table.ReplaceValue(#"Replaced Value | Usd with USD","Amex","American Express",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Applepay with Apple Pay" = Table.ReplaceValue(#"Replaced Value | Amex with American Express","Applepay","Apple Pay",Replacer.ReplaceText,{"Tender Code", "Description"}),
    #"Replaced Value | Globale with Global-e" = Table.ReplaceValue(#"Replaced Value | Applepay with Apple Pay","Globale","Global-e",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Paypal with PayPal" = Table.ReplaceValue(#"Replaced Value | Globale with Global-e","Paypal","PayPal",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | E Wallet with E-Wallet" = Table.ReplaceValue(#"Replaced Value | Paypal with PayPal","E Wallet","E-Wallet",Replacer.ReplaceText,{"Tender Type Code", "Return Tender Type Code"}),
    #"Replaced Value | Apply pay with Apple Pay" = Table.ReplaceValue(#"Replaced Value | E Wallet with E-Wallet","Apply pay","Apple Pay",Replacer.ReplaceText,{"Description"}),
    #"Changed Type" = Table.TransformColumnTypes(#"Replaced Value | Apply pay with Apple Pay",{{"Cash Drawer Open Required", type logical}, {"Till Unit Count Required", type logical}, {"Till Amount Count Required", type logical}})
in
    #"Changed Type"
```

### Transaction Summaries (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source"),
    dbo_jumpmind_sls_trans_summary = Source{[Schema="dbo",Item="jumpmind_sls_trans_summary"]}[Data],
    #"Filtered Rows | Incremental Refresh" = Table.SelectRows(dbo_jumpmind_sls_trans_summary, each [last_update_time] >= RangeStart and [last_update_time] < RangeEnd),
    #"Merged Columns | Transaction Key" = Table.CombineColumns(Table.TransformColumnTypes(#"Filtered Rows | Incremental Refresh", {{"sequence_number", type text}}, "en-US"),{"device_id", "business_date", "sequence_number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Transaction Key"),
    #"Renamed Columns" = Table.RenameColumns(#"Merged Columns | Transaction Key",{{"barcode", "Barcode"}, {"begin_time", "Begin Time"},  {"business_unit_id", "Business Unit Id"}, {"client_offset", "Client Offset"}, {"create_by", "Created By"}, {"create_time", "Created Datetime"}, {"customer_id", "Customer Id"}, {"customer_name", "Customer Name"}, {"device_type", "Device Type"}, {"discount_total", "Discount Total"}, {"employee_id_for_discount", "Employee Id for Discount"}, {"end_time", "End Time"}, {"iso_currency_code", "ISO Currency Code"}, {"item_count", "Item Count"}, {"last_update_by", "Last Updated By"}, {"last_update_time", "Last Updated Datetime"}, {"local_offset", "Local Offset"}, {"loyalty_card_number", "Loyalty Card Number"}, {"loyalty_rewards_count", "Loyalty Rewards Count"}, {"loyalty_rewards_total", "Loyalty Rewards Total"}, {"mfr_coupons_count", "Manufacturer Coupons Count"}, {"mfr_coupons_non_taxable_count", "Manufacturer Coupons Non-taxable Count"}, {"mfr_coupons_non_taxable_total", "Manufacturer Coupons Non-taxable Total"}, {"mfr_coupons_taxable_count", "Manufacturer Coupons Taxable Count"}, {"mfr_coupons_taxable_total", "Manufacturer Coupons Taxable Total"}, {"mfr_coupons_total", "Manufacturer Coupons Total"}, {"non_rcpt_rtn_count", "Non-Receipt Return Count"}, {"paid_to", "Paid To"}, {"pre_tender_balance_due", "Pre-tender Balance Due"}, {"rcpt_rtn_count", "Receipt Return Count"}, {"resumed_device_id", "Resumed Device Id"}, {"resumed_sequence_number", "Resumed Sequence Number"}, {"session_id", "Session Id"}, {"store_bank_id", "Store Bank Id"}, {"store_electronic_promos_count", "Store Electronic Promos Count"}, {"store_electronic_promos_total", "Store Electronic Promos Total"}, {"store_physical_coupons_count", "Store Physical Coupons Count"}, {"store_physical_coupons_total", "Store Physical Coupons Total"}, {"store_promos_count", "Store Promos Count"}, {"store_promos_non_taxable_count", "Store Promos Non-taxable Count"}, {"store_promos_non_taxable_total", "Store Promos Non-taxable Total"}, {"store_promos_taxable_count", "Store Promos Taxable Count"}, {"store_promos_taxable_total", "Store Promos Taxable Total"}, {"store_promos_total", "Store Promos Total"}, {"suspended_device_id", "Suspended Device Id"}, {"suspended_sequence_number", "Suspended Sequence Number"}, {"tax_total", "Tax Total"}, {"tender_type_codes", "Tender Type Codes"}, {"tender1_amount", "Tender1 Amount"}, {"tender1_auth_code", "Tender1 Authorization Code"}, {"tender1_card_type_code", "Tender1 Card Type Code"}, {"tender1_masked_card_number", "Tender1 Masked Card Number"}, {"tender1_type_code", "Tender1 Type Code"}, {"tender2_amount", "Tender2 Amount"}, {"tender2_auth_code", "Tender2 Authorization Code"}, {"tender2_card_type_code", "Tender2 Card Type Code"}, {"tender2_masked_card_number", "Tender2 Masked Card Number"}, {"tender2_type_code", "Tender2 Type Code"}, {"tender3_amount", "Tender3 Amount"}, {"tender3_auth_code", "Tender3 Authorization Code"}, {"tender3_card_type_code", "Tender3 Card Type Code"}, {"tender3_masked_card_number", "Tender3 Masked Card Number"}, {"tender3_type_code", "Tender3 Type Code"}, {"tender4_amount", "Tender4 Amount"}, {"tender4_auth_code", "Tender4 Authorization Code"}, {"tender4_card_type_code", "Tender4 Card Type Code"}, {"tender4_masked_card_number", "Tender4 Masked Card Number"}, {"tender4_type_code", "Tender4 Type Code"}, {"tender5_amount", "Tender5 Amount"}, {"tender5_auth_code", "Tender5 Authorization Code"}, {"tender5_card_type_code", "Tender5 Card Type Code"}, {"tender5_masked_card_number", "Tender5 Masked Card Number"}, {"tender5_type_code", "Tender5 Type Code"}, {"till_id", "Till Id"}, {"total", "Total"}, {"total_physical_coupons_count", "Total Physical Coupons Count"}, {"training_mode", "Training Mode"}, {"trans_status_code", "Transaction Status Code"}, {"transaction_duration_in_sec", "Transaction Duration (in Seconds)"}, {"username", "Username"}, {"voidable_flag", "Voidable Flag"}, {"voided_sequence_number", "Voided Sequence Number"}, {"trans_type_code", "Transaction Type Code"}, {"reason_code", "Reason Code"}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Renamed Columns",{{"Training Mode", type logical}, {"Voidable Flag", type logical}}),
    #"Removed Columns | Redundant Columns" = Table.RemoveColumns(#"Changed Type",{"Business Unit Id", "Username", "Begin Time", "End Time", "Local Offset", "Training Mode", "Barcode", "Session Id", "Till Id", "Customer Id", "Loyalty Card Number", "Customer Name", "Employee Id for Discount", "Voidable Flag", "Item Count", "Receipt Return Count", "Non-Receipt Return Count", "Total", "Pre-tender Balance Due", "Tax Total", "Discount Total", "Tender Type Codes", "Created Datetime", "Created By", "Last Updated By", "Transaction Type Code", "Transaction Status Code"}),
    #"Removed Columns | Empty Columns" = Table.RemoveColumns(#"Removed Columns | Redundant Columns",{"Device Type"})
in
    #"Removed Columns | Empty Columns"
```

### Exchange rates (Dynamics)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_D365", [Query="/*#(lf)____________________________________________________________________________________________________#(lf)****************************************************************************************************#(lf)#(tab)#(tab)#(tab)#(tab)-----------------------#(tab)#(tab)#(tab)#(tab)#(lf)ENTITY#(tab)#(tab)|   (D365FO) Exchange rates#(lf)#(tab)#(tab)#(tab)#(tab)-----------------------#(lf)#(tab)#(tab)#(tab)#(tab)Datasource ID:#(tab)#(tab)#(tab)D365FO#(lf)#(tab)#(tab)#(tab)#(tab)Datasource name:#(tab)#(tab)Dynamics 365 Finance & Operations#(lf)#(tab)#(tab)#(tab)#(tab)Datasource publisher:#(tab)Microsoft#(lf)#(tab)#(tab)#(tab)#(tab)Schema last updated:#(tab)2025-MAY-01#(lf)#(tab)#(tab)#(tab)#(tab)Schema updated by:#(tab)#(tab)V King#(lf)#(lf)____________________________________________________________________________________________________#(lf)#(lf)TABLES#(tab)#(tab)|   Complete list of tables contained within this entity#(lf)#(lf)#(tab)#(tab)#(tab)#(tab)Primary table name:#(tab)#(tab)[ExchangeRate]#(lf)#(tab)#(tab)#(tab)#(tab)Table name:#(tab)#(tab)#(tab)#(tab)[ExchangeRateCurrencyPair]#(lf)#(tab)#(tab)#(tab)#(tab)Table name:#(tab)#(tab)#(tab)#(tab)[ExchangeRateType]#(lf)#(tab)#(tab)#(tab)#(tab)Table name:#(tab)#(tab)#(tab)#(tab)[GlobalOptionsetMetadata]#(lf)#(lf)#(tab)#(tab)#(tab)#(tab)#(lf)#(tab)#(tab)#(tab)#(tab)**See footnotes for references to datasource documentation#(lf)____________________________________________________________________________________________________#(lf)****************************************************************************************************#(lf)*/#(lf)#(lf)SELECT DISTINCT#(lf)#(tab)#(tab)#(tab)#(tab)#(lf)#(tab)#(tab)#(tab)#(tab)#(lf)#(tab)--------------------------------------------------------------------------------#(lf)#(tab)--#(tab)PRIMARY#(tab)TABLE#(tab)|#(tab)[ExchangeRate]#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab) #(lf)#(tab)-------------------------------------------------------------------------------- #(lf)#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)-- exchangerate.[Id] AS [exchangerate_Id]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[SinkCreatedOn] AS [exchangerate_SinkCreatedOn]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[SinkModifiedOn] AS [exchangerate_SinkModifiedOn]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[sysdatastatecode] AS [exchangerate_sysdatastatecode]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab) exchangerate.[exchangerate] AS [exchangerate_exchangerate]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[exchangeratecurrencypair] AS [exchangerate_exchangeratecurrencypair]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab),exchangerate.[validfrom] AS [exchangerate_validfrom]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab),exchangerate.[validto] AS [exchangerate_validto]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[modifieddatetime] AS [exchangerate_modifieddatetime]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[modifiedby] AS [exchangerate_modifiedby]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[modifiedtransactionid] AS [exchangerate_modifiedtransactionid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[createddatetime] AS [exchangerate_createddatetime]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[createdby] AS [exchangerate_createdby]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[createdtransactionid] AS [exchangerate_createdtransactionid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[dataareaid] AS [exchangerate_dataareaid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[recversion] AS [exchangerate_recversion]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[partition] AS [exchangerate_partition]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[sysrowversion] AS [exchangerate_sysrowversion]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[recid] AS [exchangerate_recid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[tableid] AS [exchangerate_tableid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[versionnumber] AS [exchangerate_versionnumber]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[createdon] AS [exchangerate_createdon]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[modifiedon] AS [exchangerate_modifiedon]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[IsDelete] AS [exchangerate_IsDelete]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[createdonpartition] AS [exchangerate_createdonpartition]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[PartitionId] AS [exchangerate_PartitionId]#(lf)#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(lf)#(tab)--------------------------------------------------------------------------------#(lf)#(tab)--#(tab)#(tab)#(tab)TABLE#(tab)|#(tab)[ExchangeRateCurrencyPair]#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab) #(lf)#(tab)-------------------------------------------------------------------------------- #(lf)#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[Id] AS [exchangeratecurrencypair_Id]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[SinkCreatedOn] AS [exchangeratecurrencypair_SinkCreatedOn]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[SinkModifiedOn] AS [exchangeratecurrencypair_SinkModifiedOn]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab),exchangeratecurrencypair.[exchangeratedisplayfactor] AS [exchangeratecurrencypair_exchangeratedisplayfactor]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[sysdatastatecode] AS [exchangeratecurrencypair_sysdatastatecode]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[exchangeratetype] AS [exchangeratecurrencypair_exchangeratetype]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab),exchangeratecurrencypair.[fromcurrencycode] AS [exchangeratecurrencypair_fromcurrencycode]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab),exchangeratecurrencypair.[tocurrencycode] AS [exchangeratecurrencypair_tocurrencycode]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[modifieddatetime] AS [exchangeratecurrencypair_modifieddatetime]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[modifiedby] AS [exchangeratecurrencypair_modifiedby]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[modifiedtransactionid] AS [exchangeratecurrencypair_modifiedtransactionid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[createddatetime] AS [exchangeratecurrencypair_createddatetime]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[createdby] AS [exchangeratecurrencypair_createdby]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[createdtransactionid] AS [exchangeratecurrencypair_createdtransactionid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[dataareaid] AS [exchangeratecurrencypair_dataareaid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[recversion] AS [exchangeratecurrencypair_recversion]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[partition] AS [exchangeratecurrencypair_partition]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[sysrowversion] AS [exchangeratecurrencypair_sysrowversion]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[recid] AS [exchangeratecurrencypair_recid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[tableid] AS [exchangeratecurrencypair_tableid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[versionnumber] AS [exchangeratecurrencypair_versionnumber]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[createdon] AS [exchangeratecurrencypair_createdon]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[modifiedon] AS [exchangeratecurrencypair_modifiedon]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[IsDelete] AS [exchangeratecurrencypair_IsDelete]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[createdonpartition] AS [exchangeratecurrencypair_createdonpartition]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[PartitionId] AS [exchangeratecurrencypair_PartitionId]#(lf)#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(lf)#(tab)--------------------------------------------------------------------------------#(lf)#(tab)--#(tab)#(tab)#(tab)TABLE#(tab)|#(tab)[ExchangeRateType]#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab) #(lf)#(tab)-------------------------------------------------------------------------------- #(lf)#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[Id] AS [exchangeratetype_Id]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[SinkCreatedOn] AS [exchangeratetype_SinkCreatedOn]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[SinkModifiedOn] AS [exchangeratetype_SinkModifiedOn]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[sysdatastatecode] AS [exchangeratetype_sysdatastatecode]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab),exchangeratetype.[description] AS [exchangeratetype_description]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab),exchangeratetype.[name] AS [exchangeratetype_name]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[calendarid] AS [exchangeratetype_calendarid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[modifieddatetime] AS [exchangeratetype_modifieddatetime]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[modifiedby] AS [exchangeratetype_modifiedby]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[modifiedtransactionid] AS [exchangeratetype_modifiedtransactionid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[createddatetime] AS [exchangeratetype_createddatetime]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[createdby] AS [exchangeratetype_createdby]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[createdtransactionid] AS [exchangeratetype_createdtransactionid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[dataareaid] AS [exchangeratetype_dataareaid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[recversion] AS [exchangeratetype_recversion]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[partition] AS [exchangeratetype_partition]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[sysrowversion] AS [exchangeratetype_sysrowversion]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[recid] AS [exchangeratetype_recid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[tableid] AS [exchangeratetype_tableid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[versionnumber] AS [exchangeratetype_versionnumber]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[createdon] AS [exchangeratetype_createdon]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[modifiedon] AS [exchangeratetype_modifiedon]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[IsDelete] AS [exchangeratetype_IsDelete]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[createdonpartition] AS [exchangeratetype_createdonpartition]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[PartitionId] AS [exchangeratetype_PartitionId]#(lf)#(lf)#(lf)#(lf)  FROM#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)[exchangerate]#(lf)#(lf)  LEFT JOIN#(tab)#(tab)#(tab)#(tab)#(tab)[exchangeratecurrencypair]#(lf)  ON#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)exchangerate.[exchangeratecurrencypair]#(tab)#(tab)=#(tab)exchangeratecurrencypair.[recid]#(lf)#(lf)  LEFT JOIN#(tab)#(tab)#(tab)#(tab)#(tab)[exchangeratetype]#(lf)  ON#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)exchangeratecurrencypair.[exchangeratetype]#(tab)#(tab)=#(tab)exchangeratetype.[recid]#(lf)#(lf)#(lf)#(lf)#(tab)--------------------------------------------------------------------------------#(lf)#(tab)--#(tab)#(tab)#(tab)FILTER#(tab)|#(tab)Query optimization#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab) #(lf)#(tab)-------------------------------------------------------------------------------- #(lf)#(lf)  WHERE#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)exchangeratecurrencypair.[tocurrencycode]#(tab)#(tab)=#(tab)'USD'#(lf)  AND#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)exchangeratecurrencypair.[fromcurrencycode]#(tab)#(tab)IN#(tab)('CAD','GBP','EUR')#(lf)  AND#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)exchangeratetype.[description]#(tab)#(tab)#(tab)#(tab)#(tab)=#(tab)'Income Statement'#(lf)  AND#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)exchangerate.[validfrom]#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)>=#(tab)'2019-02-03'#(lf)#(lf)#(tab)--------------------------------------------------------------------------------#(lf)#(tab)--#(tab)#(tab)#(tab)FILTER#(tab)|#(tab)Remove deleted lines#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)  #(lf)#(tab)-------------------------------------------------------------------------------- #(lf)#(lf)  AND#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)(exchangerate.[IsDelete]#(tab)#(tab)#(tab)#(tab)IS NULL#(tab)OR#(tab)exchangerate.[IsDelete]#(tab)#(tab)#(tab)#(tab)= 0)#(lf)  AND#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)(exchangeratecurrencypair.[IsDelete]#(tab)IS NULL#(tab)OR#(tab)exchangeratecurrencypair.[IsDelete]#(tab)= 0)#(lf)  AND#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)(exchangeratetype.[IsDelete]#(tab)#(tab)#(tab)IS NULL#(tab)OR#(tab)exchangeratetype.[IsDelete]#(tab)#(tab)#(tab)= 0)#(lf)#(lf)#(lf)  ORDER BY#(tab)#(tab)#(tab)#(tab)#(tab)exchangerate.[validfrom]#(tab)#(tab)#(tab)#(tab)ASC#(lf)#(lf)#(lf)/*#(lf)____________________________________________________________________________________________________#(lf)****************************************************************************************************#(lf)#(lf)REFERENCES#(tab)|   Datasource documentation#(lf)#(lf)#(tab)#(tab)#(tab)#(tab)Entity name:#(tab)#(tab)#(tab)[ExchangeRateEntity]#(lf)#(tab)#(tab)#(tab)#(tab)Schema last updated:#(tab)2025-MAY-01#(lf)#(tab)#(tab)#(tab)#(tab)Schema updated by:#(tab)#(tab)V King#(lf)#(tab)#(tab)#(tab)#(tab)Microsoft schema:#(tab)#(tab)https://learn.microsoft.com/en-us/common-data-model/schema/core/operationscommon/entities/system/systemadministration/exchangerateentity#(lf)#(tab)#(tab)#(tab)#(tab)JSON definition:#(tab)#(tab)https://github.com/microsoft/CDM/blob/master/schemaDocuments/core/operationsCommon/Entities/System/SystemAdministration/ExchangeRateEntity.cdm.json#(lf)#(lf)#(tab)#(tab)#(tab)#(tab)Primary table name:#(tab)#(tab)[ExchangeRate]#(lf)#(tab)#(tab)#(tab)#(tab)Schema last updated:#(tab)2025-MAY-01#(lf)#(tab)#(tab)#(tab)#(tab)Schema updated by:#(tab)#(tab)V King#(lf)#(tab)#(tab)#(tab)#(tab)Microsoft schema:#(tab)#(tab)https://learn.microsoft.com/en-us/common-data-model/schema/core/operationscommon/tables/common/currency/reference/exchangerate#(lf)#(tab)#(tab)#(tab)#(tab)JSON definition:#(tab)#(tab)https://github.com/microsoft/CDM/blob/master/schemaDocuments/core/operationsCommon/Tables/Common/Currency/Reference/ExchangeRate.cdm.json#(lf)#(lf)#(tab)#(tab)#(tab)#(tab)Table name:#(tab)#(tab)#(tab)#(tab)[ExchangeRateCurrencyPair]#(lf)#(tab)#(tab)#(tab)#(tab)Schema last updated:#(tab)2025-MAY-01#(lf)#(tab)#(tab)#(tab)#(tab)Schema updated by:#(tab)#(tab)V King#(lf)#(tab)#(tab)#(tab)#(tab)Microsoft schema:#(tab)#(tab)https://learn.microsoft.com/en-us/common-data-model/schema/core/operationscommon/tables/common/currency/group/exchangeratecurrencypair#(lf)#(tab)#(tab)#(tab)#(tab)JSON definition:#(tab)#(tab)https://github.com/Microsoft/CDM/tree/master/schemaDocuments/core/operationsCommon/Tables/Common/Currency/Group/ExchangeRateCurrencyPair.cdm.json#(lf)#(lf)#(tab)#(tab)#(tab)#(tab)Table name:#(tab)#(tab)#(tab)#(tab)[ExchangeRateType]#(lf)#(tab)#(tab)#(tab)#(tab)Schema last updated:#(tab)2025-MAY-01#(lf)#(tab)#(tab)#(tab)#(tab)Schema updated by:#(tab)#(tab)V King#(lf)#(tab)#(tab)#(tab)#(tab)Microsoft schema:#(tab)#(tab)https://learn.microsoft.com/en-us/common-data-model/schema/core/operationscommon/tables/common/currency/group/exchangeratetype#(lf)#(tab)#(tab)#(tab)#(tab)JSON definition:#(tab)#(tab)https://github.com/Microsoft/CDM/tree/master/schemaDocuments/core/operationsCommon/Tables/Common/Currency/Group/ExchangeRateType.cdm.json#(lf)#(lf)#(tab)#(tab)#(tab)#(tab)Table name:#(tab)#(tab)#(tab)#(tab)[OptionSetMetadata]#(lf)#(tab)#(tab)#(tab)#(tab)Schema last updated:#(tab)2025-MAY-01#(lf)#(tab)#(tab)#(tab)#(tab)Schema updated by:#(tab)#(tab)V King#(lf)#(tab)#(tab)#(tab)#(tab)Microsoft schema:#(tab)#(tab)https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/optionsetmetadata?view=dataverse-latest#(lf)#(lf)____________________________________________________________________________________________________#(lf)****************************************************************************************************#(lf)*/", CreateNavigationProperties=false]),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"exchangeratecurrencypair_fromcurrencycode", "From Currency Code"}, {"exchangeratecurrencypair_tocurrencycode", "To Currency Code"}, {"exchangerate_validfrom", "Valid From"}, {"exchangerate_validto", "Valid To"}, {"exchangerate_exchangerate", "Exchange rate"}, {"exchangeratetype_name", "Exchange rate type"}, {"exchangeratetype_description", "Name"}, {"exchangeratecurrencypair_exchangeratedisplayfactor", "Conversion factor"} })
in
    #"Renamed Columns"
```

### Products (PLM)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Mart", [Query="SELECT DISTINCT#(lf)#(lf)       products.[product_key] AS [ProductKey]#(lf)      ,products.[style_code] AS [Style Code]#(lf)      ,products.[INLINE_CD] AS [Inline CD]#(lf)      ,products.[style_desc] AS [Style Description]#(lf)      ,products.[jurisdiction_code] AS [Jurisdiction Code]#(lf)      ,attributes.[ProductSellingGeography] AS [Product Selling Geography]#(lf)      ,products.[jurisdiction_id] AS [Jurisdiction Id]#(lf)      ,attributes.[ProductCountry] AS [Product Country]#(lf)      ,products.[original_retail] AS [Original Retail]#(lf)      ,products.[current_retail] AS [Current Retail]#(lf)      ,products.[current_selling_retail_home] AS [Current Selling Retail Home]#(lf)      ,products.[cdn_value] AS [CDN Value]#(lf)      ,products.[euro_value] AS [Euro Value]#(lf)      ,products.[price_with_vat] AS [Price with VAT]#(lf)      ,products.[priceline_code] AS [Priceline Code]#(lf)      ,products.[ScorecardCategory] AS [Scorecard Category]#(lf)      ,products.[department] AS [Department]#(lf)      ,products.[department_code] AS [Department Code]#(lf)      ,attributes.[DepartmentHierarchyGroupID] AS [Department Hierarchy Group ID]#(lf)      ,products.[class] AS [Class]#(lf)      ,products.[class_code] AS [Class Code]#(lf)      ,attributes.[ClassHierarchyGroupID] AS [Class Hierarchy Group ID]#(lf)      ,attributes.[ClassParentGroupID] AS [Class Parent Group ID]#(lf)      ,products.[subclass] AS [Subclass]#(lf)      ,products.[subclass_code] AS [Subclass Code]#(lf)      ,attributes.[SubClassHierarchyGroupID] AS [Subclass Hierarchy Group ID]#(lf)      ,attributes.[SubClassParentGroupID] AS [Subclass Parent Group ID]#(lf)      ,attributes.[StyleParentGroupID] AS [Style Parent Group ID]#(lf)      ,products.[division] AS [Division]#(lf)      ,attributes.[DivisionCode] AS [Division Code]#(lf)      ,attributes.[ConsumerGroup] AS [Consumer Group]#(lf)      ,products.[concept] AS [Concept]#(lf)      ,products.[chain] AS [Chain]#(lf)      ,attributes.[ChainCode] AS [Chain Code]#(lf)      ,attributes.[ItemType] AS [Item Type]#(lf)      ,attributes.[isBundleSKU] AS [Is Bundle SKU]#(lf)      ,attributes.[WebExclusive] AS [Web Exclusive]#(lf)      ,attributes.[Web] AS [Web]#(lf)      ,attributes.[KeyStory] AS [Key Story]#(lf)      ,attributes.[LICEN] AS [Licensed]#(lf)      ,attributes.[LicensedCollection] AS [Licensed Collection]#(lf)      ,attributes.[occasion] AS [Occasion]#(lf)      ,attributes.[OccasionCode] AS [Occasion Code]#(lf)      ,attributes.[Sound] AS [Sound]#(lf)      ,products.[color_code] AS [Color Code]#(lf)      ,products.[color_desc] AS [Color Description]#(lf)      ,products.[color_id] AS [Color Id]#(lf)      ,attributes.[sportsTeam] AS [Sports Team]#(lf)      ,products.[merch_status] AS [Merch Status]#(lf)      ,attributes.[SellingStatus] AS [Selling Status]#(lf)      ,attributes.[AvailB] AS [AvailB]#(lf)      ,products.[activation_date] AS [Activation Date]#(lf)      ,attributes.[MerchInDate] AS [Merch In Date]#(lf)      ,attributes.[merchOutDate] AS [Merch Out Date]#(lf)      ,attributes.[ODATE] AS [ODate]#(lf)      ,attributes.[ONOTE] AS [Out Date Note]#(lf)      ,attributes.[isOutOfStock] AS [Is Out Of Stock]#(lf)      ,products.[reorder_flag] AS [Reorder Flag]#(lf)      ,attributes.[OnOrderFlag] AS [On Order Flag]#(lf)      ,attributes.[isWebEligible] AS [Is Web Eligible]#(lf)      ,attributes.[WMSTAT] AS [WMSTAT]#(lf)      ,attributes.[OMSTAT] AS [OMSTAT]#(lf)      ,attributes.[OrderMultiple] AS [Order Multiple]#(lf)      ,attributes.[DistributionMultiple] AS [Distribution Multiple]#(lf)      ,attributes.[InnerCasePack] AS [Inner Case Pack]#(lf)      ,attributes.[ManufacturerCountry] AS [Manufacturer Country]#(lf)      ,products.[primary_vendor_name] AS [Primary Vendor Name]#(lf)      ,products.[primary_vendor_code] AS [Primary Vendor Code]#(lf)      ,products.[alt_primary_vendor_code] AS [Alt Primary Vendor Code]#(lf)      ,attributes.[InventoryBuffer] AS [Inventory Buffer]#(lf)      ,attributes.[CommodityCode] AS [Commodity Code]#(lf)      ,attributes.[QuantityRestriction] AS [Quantity Restriction]#(lf)      ,attributes.[AccessoryEligible] AS [Accessory Eligible]#(lf)      ,attributes.[AccessoryType] AS [Accessory Type]#(lf)      ,attributes.[AnimalSoldSeparately] AS [Animal Sold Separately]#(lf)      ,attributes.[AsthmaFriendly] AS [Asthma Friendly]#(lf)      ,attributes.[BirthCertificateRequired] AS [Birth Certificate Required]#(lf)      ,attributes.[BodyType] AS [Body Type]#(lf)      ,attributes.[Bottoms] AS [Bottoms]#(lf)      ,attributes.[Boy] AS [Boy]#(lf)      ,attributes.[BRF] AS [Back Room Fulfillment]#(lf)      ,attributes.[CompSetName] AS [Comp Set Name]#(lf)      ,products.[CORE_FASH_CD] AS [Core Fashion CD]#(lf)      ,attributes.[DisplayOnAmazon] AS [Display On Amazon]#(lf)      ,attributes.[EmbroideryProductList] AS [Embroidery Product List]#(lf)      ,attributes.[EyeColor] AS [Eye Color]#(lf)      ,attributes.[fourLeggedAnimal] AS [Four Legged Animal]#(lf)      ,attributes.[FriendHeight] AS [Friend Height]#(lf)      ,attributes.[FriendWeight] AS [Friend Weight]#(lf)      ,products.[GENDER] AS [Gender]#(lf)      ,attributes.[GiftBoxType] AS [Gift Box Type]#(lf)      ,attributes.[giftCardType] AS [Gift Card Type]#(lf)      ,attributes.[Girl] AS [Girl]#(lf)      ,attributes.[isCashierEnterQty] AS [Is Cashier Enters Quantity]#(lf)      ,attributes.[isCashierEntersPrice] AS [Is Cashier Enters Price]#(lf)      ,attributes.[isCouponEligible] AS [Is Coupon Eligible]#(lf)      ,attributes.[isEmployeeDiscountEligible] AS [Is Employee Discount Eligible]#(lf)      ,attributes.[isEndlessAisleEligible] AS [Is Endless Aisle Eligible]#(lf)      ,attributes.[isLoyaltyRewardsDiscountEligible] AS [Is Loyalty Rewards Discount Eligible]#(lf)      ,attributes.[isQtyRestricted] AS [Is Quantity Restricted]#(lf)      ,attributes.[isReturnEligible] AS [Is Return Eligible]#(lf)      ,attributes.[isTaxExempt] AS [Is Tax Exempt]#(lf)      ,attributes.[Mini] AS [Mini]#(lf)      ,attributes.[MLBTeams] AS [MLB Teams]#(lf)      ,attributes.[Music] AS [Music]#(lf)      ,attributes.[NBATeams] AS [NBA Teams]#(lf)      ,attributes.[Neutral] AS [Neutral]#(lf)      ,attributes.[NFLTeams] AS [NFL Teams]#(lf)      ,attributes.[NHLTeams] AS [NHL Teams]#(lf)      ,attributes.[NoInternationalShipping] AS [No International Shipping]#(lf)      ,attributes.[Outfits] AS [Outfits]#(lf)      ,attributes.[Outlet] AS [Outlet]#(lf)      ,attributes.[PackageOption] AS [Package Option]#(lf)      ,attributes.[ProductCanBeEmbroidered] AS [Product Can Be Embroidered]#(lf)      ,attributes.[ProductMustBeEmbroidered] AS [Product Must Be Embroidered]#(lf)      ,attributes.[Purses] AS [Purses]#(lf)      ,attributes.[RefundEligible] AS [Refund Eligible]#(lf)      ,attributes.[Seasonal] AS [Seasonal]#(lf)      ,attributes.[ShippingClass] AS [Shipping Class]#(lf)      ,attributes.[Shoes] AS [Shoes]#(lf)      ,attributes.[SkinType] AS [Skin Type]#(lf)      ,attributes.[SoundEligible] AS [Sound Eligible]#(lf)      ,attributes.[StoreFrontEligible] AS [Store Front Eligible]#(lf)      ,attributes.[Stuffable] AS [Stuffable]#(lf)      ,attributes.[SAC] AS [Stuffed-And-Closed]#(lf)      ,attributes.[SNC] AS [Stuffed-Not-Closed]#(lf)      ,attributes.[ThirdPartySiteEligible] AS [Third Party Site Eligible]#(lf)      ,attributes.[Tops] AS [Tops]#(lf)      ,attributes.[UKFootball] AS [UK Football]#(lf)      ,attributes.[UPC] AS [UPC]#(lf)      ,attributes.[WarningLabel] AS [Warning Label]#(lf)      ,products.[wss_reportable] AS [WSS Reportable]#(lf)      ,products.[UPDT_DT] AS [Last Update Datetime]#(lf)#(lf)#(lf)  FROM#(tab)#(tab)#(tab)[dbo].[product_dim] products#(lf)#(lf)  LEFT JOIN#(tab)#(tab)[dbo].[productcatalogmasterattributes] attributes#(lf)  ON#(tab)#(tab)#(tab)products.[jurisdiction_code] = attributes.[ProductSellingGeography]#(lf)  AND#(tab)#(tab)#(tab)products.[style_code] = attributes.[StyleCode]#(tab)#(lf)#(lf)  WHERE#(tab)#(tab)#(tab)products.[style_code] IS NOT NULL#(lf)  AND#(tab)#(tab)#(tab)products.[product_key] > 0#(lf)#(lf)  ORDER BY#(tab)#(tab)products.[style_code] ASC", CreateNavigationProperties=false]),
    #"Added Custom | Core SKU" = Table.AddColumn(Source, "Core SKU", each Text.End([Style Code],5)),
    #"Added Custom | Item Line" = Table.AddColumn(#"Added Custom | Core SKU", "Item Line", each [Style Code] & " - " & [Style Description]),
    #"Added Conditional | Primary Selling Currency" = Table.AddColumn(#"Added Custom | Item Line", "Primary Selling Currency", each if [Jurisdiction Code] = "CA" then "CAD" else if [Jurisdiction Code] = "IE" then "EUR" else if [Jurisdiction Code] = "UK" then "GBP" else if [Jurisdiction Code] = "US" then "USD" else [Jurisdiction Code]),
    #"Added Custom | CurrencyItemKey" = Table.AddColumn(#"Added Conditional | Primary Selling Currency", "CurrencyItemKey", each [Primary Selling Currency] & [Style Code]),
    #"Added Conditional Column | Web Eligible" = Table.AddColumn(#"Added Custom | CurrencyItemKey", "Web Eligible", each if [Web] = "WEBYES" then true else if [Web] = "WEBNO" then false else if [Web] = "WEBNYC" then true else null),
    #"Added Conditional Column | Web Eligible NYC Only" = Table.AddColumn(#"Added Conditional Column | Web Eligible", "Web Eligible - NYC Only", each if [Web] = "WEBNYC" then true else false),
    #"Inserted Date | Out Date" = Table.AddColumn(#"Added Conditional Column | Web Eligible NYC Only", "Out Date", each Date.From([ODate]), type date),
    #"Replaced Errors | Out Date" = Table.ReplaceErrorValues(#"Inserted Date | Out Date", {{"Out Date", null}}),
    #"Added Conditional Column | Merch Out Date" = Table.AddColumn(#"Replaced Errors | Out Date", "Merchandise Out Date", each if [Merch Out Date] <> null then [Merch Out Date] else [Out Date]),
    #"Added Custom | Item Line Core SKU" = Table.AddColumn(#"Added Conditional Column | Merch Out Date", "Item Line (Core SKU)", each [Core SKU] & " - " & [Style Description]),
    #"Replaced Value | Y > TRUE" = Table.ReplaceValue(#"Added Custom | Item Line Core SKU","Y","true",Replacer.ReplaceText,{"WSS Reportable","Outlet"}),
    #"Replaced Value | N > FALSE" = Table.ReplaceValue(#"Replaced Value | Y > TRUE","N","false",Replacer.ReplaceText,{"WSS Reportable","Outlet"}),
    #"Replaced Value | NULL > null" = Table.ReplaceValue(#"Replaced Value | N > FALSE","NULL",null,Replacer.ReplaceValue,{"Alt Primary Vendor Code"}),
    #"Replaced Value | NO > FALSE" = Table.ReplaceValue(#"Replaced Value | NULL > null","NO","false",Replacer.ReplaceText,{"Licensed"}),
    #"Replaced Value | 0 > FALSE" = Table.ReplaceValue(#"Replaced Value | NO > FALSE","0","false",Replacer.ReplaceText,{"Is Cashier Enters Quantity", "Is Cashier Enters Price", "Is Quantity Restricted", "Is Return Eligible", "Outlet"}),
    #"Replaced Value | 1 > TRUE" = Table.ReplaceValue(#"Replaced Value | 0 > FALSE","1","true",Replacer.ReplaceText,{"Is Cashier Enters Quantity", "Is Cashier Enters Price", "Is Quantity Restricted", "Is Return Eligible", "Outlet"}),
    #"Added Conditional Column | D365 Legal Entity" = Table.AddColumn(#"Replaced Value | 1 > TRUE", "D365 Legal Entity", each if [CurrencyItemKey] = "USD8" then 1200 else if [CurrencyItemKey] = "USD9" then 3001 else if [Primary Selling Currency] = "CAD" then 1700 else if [Primary Selling Currency] = "EUR" then 2110 else if [Primary Selling Currency] = "GBP" then 2110 else if [Primary Selling Currency] = "USD" then 1100 else null),
    #"Changed Type" = Table.TransformColumnTypes(#"Added Conditional Column | D365 Legal Entity",{{"Embroidery Product List", type logical}, {"Product Can Be Embroidered", type logical}, {"Product Must Be Embroidered", type logical}, {"Asthma Friendly", type logical}, {"Back Room Fulfillment", type logical}, {"Music", type logical}, {"Animal Sold Separately", type logical}, {"Stuffed-And-Closed", type logical}, {"Bottoms", type logical}, {"Outfits", type logical}, {"Mini", type logical}, {"Tops", type logical}, {"Purses", type logical}, {"Stuffed-Not-Closed", type logical}, {"Boy", type logical}, {"Girl", type logical}, {"Neutral", type logical}, {"Birth Certificate Required", type logical}, {"Refund Eligible", type logical}, {"Third Party Site Eligible", type logical}, {"AvailB", type logical}, {"Stuffable", type logical}, {"No International Shipping", type logical}, {"Display On Amazon", type logical}, {"Web Exclusive", type logical}, {"Accessory Eligible", type logical}, {"Sound Eligible", type logical}, {"Store Front Eligible", type logical}, {"Merch Out Date", type date}, {"On Order Flag", type logical}, {"Shoes", type logical}, {"Sound", type logical}, {"Four Legged Animal", type logical}, {"Merch In Date", type date}, {"Activation Date", type date}, {"Item Line", type text}, {"Primary Selling Currency", type text}, {"CurrencyItemKey", type text}, {"Core SKU", type text}, {"ProductKey", type text}, {"Is Bundle SKU", type logical}, {"Web Eligible", type logical}, {"Web Eligible - NYC Only", type logical}, {"Licensed", type logical}, {"Is Out Of Stock", type logical}, {"Is Web Eligible", type logical}, {"Is Cashier Enters Quantity", type logical}, {"Is Cashier Enters Price", type logical}, {"Is Coupon Eligible", type logical}, {"Is Employee Discount Eligible", type logical}, {"Is Loyalty Rewards Discount Eligible", type logical}, {"Is Quantity Restricted", type logical}, {"Is Return Eligible", type logical}, {"Is Tax Exempt", type logical}, {"WSS Reportable", type logical}, {"Outlet", type logical}, {"Merchandise Out Date", type date}, {"Item Line (Core SKU)", type text}, {"D365 Legal Entity", type text}}),
    #"Added Custom | ItemKey" = Table.AddColumn(#"Changed Type", "ItemKey", each [D365 Legal Entity] & "-" & [Style Code]),
    #"Changed Type | ItemKey" = Table.TransformColumnTypes(#"Added Custom | ItemKey",{{"ItemKey", type text}}),
    #"Renamed Columns" = Table.RenameColumns(#"Changed Type | ItemKey",{{"Merch Out Date", "Out Date 1"}, {"Out Date", "Out Date 2"}, {"Merchandise Out Date", "Merch Out Date"}}),
    #"Sorted Rows | Last Update Datetime DESC" = Table.Sort(#"Renamed Columns",{{"Last Update Datetime", Order.Descending}}),
    #"Removed Duplicates | CurrencyItemKey" = Table.Distinct(#"Sorted Rows | Last Update Datetime DESC", {"CurrencyItemKey"}),
    #"Filtered Rows | Primary Selling Currency {CAD,EUR,GBP,USD}" = Table.SelectRows(#"Removed Duplicates | CurrencyItemKey", each ([Primary Selling Currency] <> "CN" and [Primary Selling Currency] <> "DK" and [Primary Selling Currency] <> "FR")),
    #"Sorted Rows | Primary Selling Currrency DESC" = Table.Sort(#"Filtered Rows | Primary Selling Currency {CAD,EUR,GBP,USD}",{{"Primary Selling Currency", Order.Descending}}),
    #"Removed Duplicates | ItemKey" = Table.Distinct(#"Sorted Rows | Primary Selling Currrency DESC", {"ItemKey"}),
    #"Sorted Rows | Style Code ASC" = Table.Sort(#"Removed Duplicates | ItemKey",{{"Style Code", Order.Ascending}})
in
    #"Sorted Rows | Style Code ASC"
```

### LocalDateTable_5c26535c-2005-449c-bab9-ba36531e9c6d

```sql
Calendar(Date(Year(MIN('Products (PLM)'[Activation Date])), 1, 1), Date(Year(MAX('Products (PLM)'[Activation Date])), 12, 31))
```

### LocalDateTable_e402dd30-9f43-4d4f-a4fb-db08f436e975

```sql
Calendar(Date(Year(MIN('Products (PLM)'[Merch In Date])), 1, 1), Date(Year(MAX('Products (PLM)'[Merch In Date])), 12, 31))
```

### LocalDateTable_f9c3d338-cbb0-41fb-86dc-21dc0f34e12b

```sql
Calendar(Date(Year(MIN('Products (PLM)'[Out Date 1])), 1, 1), Date(Year(MAX('Products (PLM)'[Out Date 1])), 12, 31))
```

### LocalDateTable_a2f29b70-36e2-4209-aa2b-d342e1e0f8c6

```sql
Calendar(Date(Year(MIN('Products (PLM)'[Out Date 2])), 1, 1), Date(Year(MAX('Products (PLM)'[Out Date 2])), 12, 31))
```

### LocalDateTable_bbd477ee-7054-427a-998e-b90a9310acd8

```sql
Calendar(Date(Year(MIN('Products (PLM)'[Merch Out Date])), 1, 1), Date(Year(MAX('Products (PLM)'[Merch Out Date])), 12, 31))
```

### Global Products (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="SELECT DISTINCT #(lf)#(lf)       [item_id]#(tab)#(tab)#(tab)AS [Item ID]#(lf)      ,RIGHT([item_id],5)#(tab)AS [Core SKU]#(lf)      ,[item_description]#(tab)AS [Item Description]#(lf)      ,[iso_currency_code]#(tab)AS [Currency]#(lf)      ,[item_type]#(tab)#(tab)#(tab)AS [Item Type]#(lf)#(tab)  ,CASE#(lf)#(tab)#(tab)#(tab)WHEN#(tab)[iso_currency_code] =#(tab)'USD'#(lf)#(tab)#(tab)#(tab)THEN#(tab)[item_description]#(lf)#(tab)#(tab)#(tab)END AS#(tab)'Item Name (US)'#(lf)#(tab)  ,CASE#(lf)#(tab)#(tab)#(tab)WHEN#(tab)[iso_currency_code] =#(tab)'CAD'#(lf)#(tab)#(tab)#(tab)THEN#(tab)[item_description]#(lf)#(tab)#(tab)#(tab)END AS#(tab)'Item Name (CA)'#(lf)#(tab)  ,CASE#(lf)#(tab)#(tab)#(tab)WHEN#(tab)[iso_currency_code] =#(tab)'GBP'#(lf)#(tab)#(tab)#(tab)THEN#(tab)[item_description]#(lf)#(tab)#(tab)#(tab)END AS#(tab)'Item Name (UK)'#(lf)#(tab)  ,CASE#(lf)#(tab)#(tab)#(tab)WHEN#(tab)[iso_currency_code] =#(tab)'EUR'#(lf)#(tab)#(tab)#(tab)THEN#(tab)[item_description]#(lf)#(tab)#(tab)#(tab)END AS#(tab)'Item Name (IE)'#(lf)#(lf)#(lf)  FROM#(tab)#(tab)[dbo].[jumpmind_sls_retail_line_item]#(lf)#(lf)  WHERE#(tab)#(tab)[item_description]#(tab)IS NOT NULL#(lf)  AND#(tab)#(tab)LEN(item_id)#(tab)#(tab)=#(tab)6#(lf)#(lf)  ORDER BY#(tab)RIGHT([item_id],5)#(tab)ASC", CreateNavigationProperties=false]),
    #"Removed Columns" = Table.RemoveColumns(Source,{"Item ID", "Item Description", "Currency"}),
    #"Grouped Rows" = Table.Group(#"Removed Columns", {"Core SKU", "Item Type"}, {{"Item Name (US)", each List.Max([#"Item Name (US)"]), type nullable text}, {"Item Name (CA)", each List.Max([#"Item Name (CA)"]), type nullable text}, {"Item Name (UK)", each List.Max([#"Item Name (UK)"]), type nullable text}, {"Item Name (IE)", each List.Max([#"Item Name (IE)"]), type nullable text}}),
    #"Added Conditional Column | Global Item Name" = Table.AddColumn(#"Grouped Rows", "Global Item Name", each if [#"Item Name (US)"] <> null then [#"Item Name (US)"] else if [#"Item Name (CA)"] <> null then [#"Item Name (CA)"] else if [#"Item Name (UK)"] <> null then [#"Item Name (UK)"] else if [#"Item Name (IE)"] <> null then [#"Item Name (IE)"] else null),
    #"Added Custom | Global Item Line" = Table.AddColumn(#"Added Conditional Column | Global Item Name", "Global Item Line", each [Core SKU] & " | " & [Global Item Name]),
    #"Changed Type" = Table.TransformColumnTypes(#"Added Custom | Global Item Line",{{"Global Item Name", type text}, {"Global Item Line", type text}}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Changed Type",{{"Item Type", Text.Proper, type text}})
in
    #"Capitalized Each Word"
```

### LocalDateTable_db9f588e-3a3b-4808-9922-3c9443a2e153

```sql
Calendar(Date(Year(MIN('Products (PLM)'[Last Update Datetime])), 1, 1), Date(Year(MAX('Products (PLM)'[Last Update Datetime])), 12, 31))
```

### LocalDateTable_f84ef23a-3840-4b6e-99ba-dd3ef26f713e

```sql
Calendar(Date(Year(MIN('Exchange rates (Dynamics)'[Valid From])), 1, 1), Date(Year(MAX('Exchange rates (Dynamics)'[Valid From])), 12, 31))
```

### LocalDateTable_cb103ba7-2fb4-402a-895c-2b84dc3f5dbd

```sql
Calendar(Date(Year(MIN('Exchange rates (Dynamics)'[Valid To])), 1, 1), Date(Year(MAX('Exchange rates (Dynamics)'[Valid To])), 12, 31))
```

### LocalDateTable_561eb354-c83a-4fad-8bed-dff84b95c91b

```sql
Calendar(Date(Year(MIN('Activated Gift Cards (JumpMind)'[Last Updated Datetime])), 1, 1), Date(Year(MAX('Activated Gift Cards (JumpMind)'[Last Updated Datetime])), 12, 31))
```

### LocalDateTable_12349c08-94b3-429b-ab24-c10ba82ff847

```sql
Calendar(Date(Year(MIN('Transaction Summaries (JumpMind)'[Last Updated Datetime])), 1, 1), Date(Year(MAX('Transaction Summaries (JumpMind)'[Last Updated Datetime])), 12, 31))
```

### LocalDateTable_dab62035-2669-4a22-aaec-2632fabcb287

```sql
Calendar(Date(Year(MIN('Retail Transactions (JumpMind)'[Last Updated Datetime])), 1, 1), Date(Year(MAX('Retail Transactions (JumpMind)'[Last Updated Datetime])), 12, 31))
```

### LocalDateTable_7860c2a2-378f-46bb-b7a0-5185b792d99e

```sql
Calendar(Date(Year(MIN('Retail Transaction Discounts (JumpMind)'[Last Updated Datetime])), 1, 1), Date(Year(MAX('Retail Transaction Discounts (JumpMind)'[Last Updated Datetime])), 12, 31))
```

### LocalDateTable_f2bca1c6-828c-4094-bbfb-4763519fe956

```sql
Calendar(Date(Year(MIN('Retail Lines (JumpMind)'[Last Updated Datetime])), 1, 1), Date(Year(MAX('Retail Lines (JumpMind)'[Last Updated Datetime])), 12, 31))
```

### LocalDateTable_b03143ec-a3af-4798-a56d-95139da8728a

```sql
Calendar(Date(Year(MIN('Retail Line Discounts (JumpMind)'[Last Updated Datetime])), 1, 1), Date(Year(MAX('Retail Line Discounts (JumpMind)'[Last Updated Datetime])), 12, 31))
```

### LocalDateTable_a4dcc117-e9b4-4b16-adee-f4f9946a165d

```sql
Calendar(Date(Year(MIN('Retail Return Lines (JumpMind)'[Last Updated Datetime])), 1, 1), Date(Year(MAX('Retail Return Lines (JumpMind)'[Last Updated Datetime])), 12, 31))
```

### LocalDateTable_49ea6d5f-fb07-4da6-9fb1-51d02a2bc45a

```sql
Calendar(Date(Year(MIN('Tax Lines (JumpMind)'[Created Datetime])), 1, 1), Date(Year(MAX('Tax Lines (JumpMind)'[Created Datetime])), 12, 31))
```

### LocalDateTable_c696f59a-66cf-41b7-8b07-5195859bcbaa

```sql
Calendar(Date(Year(MIN('Tax Lines (JumpMind)'[Last Updated Datetime])), 1, 1), Date(Year(MAX('Tax Lines (JumpMind)'[Last Updated Datetime])), 12, 31))
```

### LocalDateTable_389f283c-edb3-40f4-ac2f-a231a1db0d91

```sql
Calendar(Date(Year(MIN('Tender Lines (JumpMind)'[Created Datetime])), 1, 1), Date(Year(MAX('Tender Lines (JumpMind)'[Created Datetime])), 12, 31))
```

### LocalDateTable_252fac6a-2c05-4ea6-811c-020b777cc24e

```sql
Calendar(Date(Year(MIN('Tender Lines (JumpMind)'[Last Updated Datetime])), 1, 1), Date(Year(MAX('Tender Lines (JumpMind)'[Last Updated Datetime])), 12, 31))
```

### LocalDateTable_61a52116-af4f-4f93-b42a-bae69dfe4c27

```sql
Calendar(Date(Year(MIN('Tender Settlement Lines (JumpMind)'[Last Updated Datetime])), 1, 1), Date(Year(MAX('Tender Settlement Lines (JumpMind)'[Last Updated Datetime])), 12, 31))
```

### LocalDateTable_9d389bc1-31cd-4452-87ee-b48b7c91fa60

```sql
Calendar(Date(Year(MIN('Tender Card Lines (JumpMind)'[Last Updated Datetime])), 1, 1), Date(Year(MAX('Tender Card Lines (JumpMind)'[Last Updated Datetime])), 12, 31))
```

## Shared Expressions

### RangeStart (0)

```sql
#datetime(2025, 5, 31, 0, 0, 0) meta [IsParameterQuery=true, Type="DateTime", IsParameterQueryRequired=true]
```

### RangeEnd (0)

```sql
#datetime(2025, 6, 1, 0, 0, 0) meta [IsParameterQuery=true, Type="DateTime", IsParameterQueryRequired=true]
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com | LH_Mart | [4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/LH_Mart](../../../4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/DataDictionary/LH_Mart/) |
| 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com | LH_Source | [4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/LH_Source](../../../4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/DataDictionary/LH_Source/) |
| 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com | LH_D365 | [4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/LH_D365](../../../4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/DataDictionary/LH_D365/) |
