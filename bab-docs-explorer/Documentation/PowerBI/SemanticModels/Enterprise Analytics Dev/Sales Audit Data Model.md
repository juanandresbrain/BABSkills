# Sales Audit Data Model

**Workspace:** Enterprise Analytics Dev  
**Dataset ID:** f5d320ff-8660-4a1f-970b-8c10444e0e0f  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| Calendar | 47 | 0 |  |
| Business Units (JumpMind) | 10 | 0 |  |
| Exchange rates (Dynamics) | 10 | 0 |  |
| Locations (Store MDM) | 43 | 0 |  |
| Product Images | 5 | 0 |  |
| Products (PLM) | 147 | 0 |  |
| Retail Line Discounts (JumpMind) | 42 | 3 |  |
| Global Products (JumpMind) | 9 | 0 |  |
| Retail Lines (JumpMind) | 103 | 1 |  |
| Retail Return Lines (JumpMind) | 22 | 0 |  |
| Retail Transaction Discounts (JumpMind) | 20 | 0 |  |
| Retail Transactions (JumpMind) | 91 | 0 |  |
| Tax Authorities (JumpMind) | 7 | 0 |  |
| Tax Groups (JumpMind) | 5 | 0 |  |
| Tax Lines (JumpMind) | 37 | 0 |  |
| Tender Card Lines (JumpMind) | 17 | 0 |  |
| Tender Lines (JumpMind) | 41 | 4 |  |
| Tender Settlement Lines (JumpMind) | 27 | 4 |  |
| Tenders (JumpMind) | 10 | 0 |  |
| Transaction Summaries (JumpMind) | 62 | 0 |  |
| Users (JumpMind) | 14 | 0 |  |
| Transactions (JumpMind) | 57 | 0 |  |
| Activated Gift Cards (JumpMind) | 19 | 0 |  |
| Measure Table | 2 | 94 |  |
| vwJumpMindEventReportingSummary | 15 | 0 |  |
| Gift Cards Details | 14 | 0 |  |
| Dict Payment Transaction Type | 4 | 0 |  |
| Transactions Extra Values | 57 | 0 |  |

## Measures

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

### Retail Lines (JumpMind).Returned Tender Amount (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Returned] = TRUE(),
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

### Tender Lines (JumpMind).Tender Amount with Currency Rounding

```sql

SUM('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]) + SUM('Tender Lines (JumpMind)'[currency Rounding adjustment])
```

### Tender Settlement Lines (JumpMind).Safe Amount

```sql

SUMX (
    VALUES ( 'Tender Settlement Lines (JumpMind)'[Store Bank Id] ), 
    VAR LastTimestamp = 
        CALCULATE (
            MAX ( 'Tender Settlement Lines (JumpMind)'[Last Updated Datetime] ),
            'Tender Settlement Lines (JumpMind)'[Reason Code] = "Open Store Bank",
            'Transactions (JumpMind)'[Training Mode] = FALSE (),
            'Transactions (JumpMind)'[Transaction Status] = "Completed"
        )
    RETURN
        CALCULATE (
            SUM ( 'Tender Settlement Lines (JumpMind)'[Open Session Amount] ),
            'Tender Settlement Lines (JumpMind)'[Last Updated Datetime] = LastTimestamp,
            'Tender Settlement Lines (JumpMind)'[Reason Code] = "Open Store Bank",
            'Transactions (JumpMind)'[Training Mode] = FALSE (),
            'Transactions (JumpMind)'[Transaction Status] = "Completed"
        )
)
```

### Tender Settlement Lines (JumpMind).Till Amount

```sql

SUMX (
    SUMMARIZE (
        'Tender Settlement Lines (JumpMind)',
        'Tender Settlement Lines (JumpMind)'[Store Bank Id],
        'Tender Settlement Lines (JumpMind)'[Till Id]
    ),
    VAR LastTimestamp = 
        CALCULATE (
            MAX ( 'Tender Settlement Lines (JumpMind)'[Last Updated Datetime] ),
            'Tender Settlement Lines (JumpMind)'[Reason Code] = "Open Till",
            'Transactions (JumpMind)'[Training Mode] = FALSE (),
            'Transactions (JumpMind)'[Transaction Status] = "Completed"
        )
    RETURN
        CALCULATE (
            SUM ( 'Tender Settlement Lines (JumpMind)'[Open Session Amount] ),
            'Tender Settlement Lines (JumpMind)'[Last Updated Datetime] = LastTimestamp,
            'Tender Settlement Lines (JumpMind)'[Reason Code] = "Open Till",
            'Transactions (JumpMind)'[Training Mode] = FALSE (),
            'Transactions (JumpMind)'[Transaction Status] = "Completed"
        )
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

### Measure Table.Donation Amount (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Type] = "Donation",
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Donation Units

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Item Type] = "Donation",
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Donation Amount (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount TE (USD Converted)]),
    'Retail Lines (JumpMind)'[Item Type] = "Donation",
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Transactions

```sql

CALCULATE(
    DISTINCTCOUNTNOBLANK('Retail Lines (JumpMind)'[Transaction Key]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Transactions | Loyalty Members

```sql

CALCULATE(
    DISTINCTCOUNTNOBLANK('Retail Lines (JumpMind)'[Transaction Key]),
    'Retail Lines (JumpMind)'[Item Type] = "Loyalty",
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Bonus Club Capture Rate

```sql
[Retail Transactions | Loyalty Members] / [Retail Transactions]
```

### Measure Table.Retail Transactions | Party Packages

```sql

CALCULATE(
    DISTINCTCOUNTNOBLANK('Retail Lines (JumpMind)'[Transaction Key]),
    'Retail Lines (JumpMind)'[Item Type] = "Party Package",
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Transactions | Military Discounts

```sql

CALCULATE(
    DISTINCTCOUNTNOBLANK('Retail Lines (JumpMind)'[Transaction Key]),
    'Retail Lines (JumpMind)'[Item Type] = "Military",
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Products (PLM)'[Department] = "Stuffers",
    'Products (PLM)','Products (PLM)'[Class] = "Sound",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Sales TE | Actual (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Sales TE | Actual (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount TE (USD Converted)]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Sales TE | Full-Price (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Regular Sales Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Profit TE (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Retail Line Profit TE (USD)]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Discount Amount TE (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Discount Amount TE (USD Converted)]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Average Retail Discount Amount TE Per Unit (Native)

```sql

CALCULATE(
    AVERAGE('Retail Lines (JumpMind)'[Discount Amount Per Unit TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Type] = "Stock",
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Retail Discount Percentage TE

```sql
[Retail Discount Amount TE (Native)] / [Retail Sales TE | Full-Price (Native)]
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

### Measure Table.AUR (USD)

```sql
[Retail Sales TE | Actual (USD)] / [Retail Units]
```

### Measure Table.DPT (USD)

```sql
[Retail Sales TE | Actual (USD)] / [Retail Transactions]
```

### Measure Table.Total Sales TE | Full-Price (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Regular Sales Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Total Sales TE | Actual (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Total Sales TE | Actual (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount TE (USD Converted)]),
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Total Sales TE | Full-Price (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Regular Sales Amount TE (USD Converted)]),
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Non-Retail Units

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Regular Unit Price (Native Currency)] <> 0,
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    NOT('Retail Lines (JumpMind)'[Item Type] IN {"Gift Card", "Donation", "Loyalty", "Party Package"}),
    NOT('Products (PLM)'[Department] IN {"Accessories","Clothes","Footwear","Friend","Human","Human Clothes","Stuffed","Stuffers","Unstuffed"}),
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Non-Retail Profit TE (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Retail Line Profit TE (USD)]),
    'Retail Lines (JumpMind)'[Regular Unit Price (Native Currency)] <> 0,
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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

### Measure Table.Activated Gift Cards Gross Amount TE (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Regular Sales Amount TE (USD Converted)]),
    'Retail Lines (JumpMind)'[Item Type] = "Gift Card",
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Activated Gift Card Units

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Quantity]),
    'Retail Lines (JumpMind)'[Item Type] = "Gift Card",
    'Retail Lines (JumpMind)'[Line Item Type] IN {"Store Sale", "Web Sale"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Activated Gift Cards Gross Amount TE (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Regular Sales Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Type] = "Gift Card",
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Activated Gift Cards Net Amount TE (Native)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount TE (Native Currency)]),
    'Retail Lines (JumpMind)'[Item Type] = "Gift Card",
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)
```

### Measure Table.Activated Gift Cards Net Amount TE (USD)

```sql

CALCULATE(
    SUM('Retail Lines (JumpMind)'[Actual Sales Amount TE (USD Converted)]),
    'Retail Lines (JumpMind)'[Item Type] = "Gift Card",
    'Retail Lines (JumpMind)'[Line Item Type] IN { "Store Sale", "Web Sale"},
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

### Measure Table.Transaction Number

```sql

VAR Txt = SELECTEDVALUE('Transactions (JumpMind)'[Transaction Key])
RETURN
IF(
    NOT ISBLANK(Txt),
    IFERROR(
        RIGHT(
            Txt,
            LEN(Txt) -
            SEARCH(
                "@",
                SUBSTITUTE(
                    Txt,
                    "-",
                    "@",
                    LEN(Txt) - LEN(SUBSTITUTE(Txt, "-", ""))
                )
            )
        ),
        Txt
    ),
    BLANK()
)
```

### Measure Table.Declared Settlement Amount

```sql

CALCULATE(
    SUM('Tender Settlement Lines (JumpMind)'[Pickup Amount]),
    UPPER('Transactions (JumpMind)'[Transaction Type]) = "CLOSE_STORE_BANK" 
)
```

### Measure Table.Reconciliation Variance

```sql

SUMX(
    VALUES('Tenders (JumpMind)'[Description]),
    VAR Declared = [Declared Settlement Amount]
    VAR System = [System Tender Total] 
    RETURN
        IF(
            ISBLANK(Declared) || Declared = 0, 
            BLANK(), 
            Declared - [System Tender Total]
        )
)
```

### Measure Table.System Tender Count

```sql

CALCULATE(
    COUNT('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]),
    'Transactions (JumpMind)'[Transaction Type] IN { "SALE", "RETURN" },
    'Transactions (JumpMind)'[Transaction Status] = "COMPLETED",
    'Tender Lines (JumpMind)'[Voided] = FALSE()
)
```

### Measure Table.System Tender Total

```sql

IF(
    ISINSCOPE('Tenders (JumpMind)'[Description]),
    CALCULATE(
        SUM('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]),
        'Transactions (JumpMind)'[Transaction Type] IN { "SALE", "RETURN" },
        'Transactions (JumpMind)'[Transaction Status] = "COMPLETED",
        'Tender Lines (JumpMind)'[Voided] = FALSE()
    ),
    BLANK()
)
```

### Measure Table.Cash (Deposit) _

```sql

CALCULATE(
    SUM('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]),
    'Tender Lines (JumpMind)'[Tender Type Code] = "Cash",
    'Transactions (JumpMind)'[Transaction Status] = "Completed",
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Type] IN {"SALE", "RETURN"},
    'Tender Lines (JumpMind)'[Voided] = FALSE()
)
```

### Measure Table.Cash Deposit Expected _

```sql

VAR _GLAmountExpected = 
CALCULATE(
    SUM('Tender Settlement Lines (JumpMind)'[Pickup Amount]),
    'Tender Settlement Lines (JumpMind)'[Repository Transfer Type] = "From Store Bank to External Bank",
    'Tender Settlement Lines (JumpMind)'[Tender Type Code] IN {"Cash", "Check"},
    'Transactions (JumpMind)'[Training Mode] = FALSE(),
    'Transactions (JumpMind)'[Transaction Status] = "Completed"
)

RETURN
CALCULATE(
    _GLAmountExpected 
)
```

### Measure Table.FBR (Over)/Short _

```sql

[Cash (Deposit) _] - [Cash Deposit Expected _]
```

### Measure Table.Bank (Deposit) _

```sql

VAR MainDeposit = 
    CALCULATE(
        SUM('Tender Settlement Lines (JumpMind)'[Pickup Amount]),
        'Tender Settlement Lines (JumpMind)'[Repository Transfer Type] = "From Store Bank to External Bank",
        'Transactions (JumpMind)'[Training Mode] = FALSE(),
        'Transactions (JumpMind)'[Transaction Status] = "Completed"
    )

VAR TenderControl = 
    CALCULATE(
        SUM('Tender Lines (JumpMind)'[Tender Amount (Native Currency)]),
        'Transactions (JumpMind)'[Transaction Type] IN {"CASH_UP", "CASH_DOWN"},
        'Transactions (JumpMind)'[Training Mode] = FALSE(),
        'Transactions (JumpMind)'[Transaction Status] = "Completed"
    )

RETURN
MainDeposit + TenderControl
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
    #"Changed Type" = Table.TransformColumnTypes(#"Reordered Columns",{{"Fiscal Month (Name)", type text}, {"Fiscal Year (Header)", type text}, {"Fiscal Quarter (Header)", type text}, {"Fiscal Month (Header)", type text}, {"Fiscal Week (Header)", type text}, {"Calendar Year (Header)", type text}, {"Calendar Quarter (Header)", type text}, {"Calendar Month (Header)", type text}, {"Calendar Week (Header)", type text}}),
    #"Filtered Rows" = Table.SelectRows(#"Changed Type", each [Actual Datetime] > #datetime(2024, 7, 31, 0, 0, 0))
in
    #"Filtered Rows"
```

### Business Units (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH oms_codes AS (#(lf)    SELECT#(lf)        NULLIF(CONVERT(varchar(64), dtt.MaxWarehouseCode), '') AS code,#(lf)        MIN(COALESCE(r.DateCreatedUTC, r.OrderDateUTC, r.OrderStatusChangeDateUTC, r.ExportCreatedUTC)) AS create_time,#(lf)        MAX(COALESCE(r.UpdateDate,     r.OrderStatusChangeDateUTC, r.OrderDateUTC,     r.ExportCreatedUTC)) AS last_update_time#(lf)    FROM [dbo].[mulesoft_dynamicstargettrans] AS dtt#(lf)    LEFT JOIN [dbo].[mulesoft_deckjsonraw_root] AS r#(lf)           ON r.OrderID = dtt.OrderId#(lf)    WHERE NULLIF(dtt.MaxWarehouseCode, '') IS NOT NULL#(lf)    GROUP BY NULLIF(CONVERT(varchar(64), dtt.MaxWarehouseCode), '')#(lf)),#(lf)oms_bu AS (#(lf)    SELECT#(lf)        CASE#(lf)          WHEN code = 'BAB'   THEN 1013#(lf)          WHEN code = 'BABUK' THEN 2013#(lf)          WHEN TRY_CONVERT(int, code) IS NOT NULL THEN TRY_CONVERT(int, code)#(lf)          ELSE 9999#(lf)        END                                                      AS business_unit_id,#(lf)        CASE#(lf)          WHEN code = 'BAB'   THEN '1013'#(lf)          WHEN code = 'BABUK' THEN '2013'#(lf)          WHEN TRY_CONVERT(int, code) IS NOT NULL THEN CONVERT(varchar(32), TRY_CONVERT(int, code))#(lf)          ELSE '9999'#(lf)        END                                                      AS geo_code,#(lf)        code                                                      AS business_unit_name,#(lf)        CAST(NULL AS varchar(64))                                 AS government_id,#(lf)        create_time,#(lf)        CAST('sp_bab_oms_merge_business_units' AS varchar(128))   AS create_by,#(lf)        last_update_time,#(lf)        CAST('sp_bab_oms_merge_business_units' AS varchar(128))   AS last_update_by#(lf)    FROM oms_codes#(lf))#(lf)#(lf)SELECT#(lf)    bu.business_unit_id,#(lf)    bu.geo_code,#(lf)    bu.business_unit_name,#(lf)    bu.government_id,#(lf)    bu.create_time,#(lf)    bu.create_by,#(lf)    bu.last_update_time,#(lf)    bu.last_update_by#(lf)FROM [dbo].[jumpmind_ctx_business_unit] AS bu#(lf)#(lf)UNION ALL#(lf)#(lf)SELECT#(lf)    o.business_unit_id,#(lf)    o.geo_code,#(lf)    o.business_unit_name,#(lf)    o.government_id,#(lf)    o.create_time,#(lf)    o.create_by,#(lf)    o.last_update_time,#(lf)    o.last_update_by#(lf)FROM oms_bu AS o#(lf)LEFT JOIN [dbo].[jumpmind_ctx_business_unit] AS bu#(lf)       ON bu.geo_code = o.geo_code   -- avoid duplicates where POS already defines this code#(lf)WHERE bu.geo_code IS NULL;", CreateNavigationProperties=false]),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"business_unit_id", "Business Unit Id"}, {"business_unit_name", "Business Unit Name"}}),
    #"Added Custom | Location Line" = Table.AddColumn(#"Renamed Columns", "Location Line", each Text.From([Business Unit Id]) & " | " & [Business Unit Name]),
    #"Changed Type" = Table.TransformColumnTypes(#"Added Custom | Location Line",{{"Location Line", type text}})
in
    #"Changed Type"
```

### Exchange rates (Dynamics)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_D365", [Query="/*#(lf)____________________________________________________________________________________________________#(lf)****************************************************************************************************#(lf)#(tab)#(tab)#(tab)#(tab)-----------------------#(tab)#(tab)#(tab)#(tab)#(lf)ENTITY#(tab)#(tab)|   (D365FO) Exchange rates#(lf)#(tab)#(tab)#(tab)#(tab)-----------------------#(lf)#(tab)#(tab)#(tab)#(tab)Datasource ID:#(tab)#(tab)#(tab)D365FO#(lf)#(tab)#(tab)#(tab)#(tab)Datasource name:#(tab)#(tab)Dynamics 365 Finance & Operations#(lf)#(tab)#(tab)#(tab)#(tab)Datasource publisher:#(tab)Microsoft#(lf)#(tab)#(tab)#(tab)#(tab)Schema last updated:#(tab)2025-MAY-01#(lf)#(tab)#(tab)#(tab)#(tab)Schema updated by:#(tab)#(tab)V King#(lf)#(lf)____________________________________________________________________________________________________#(lf)#(lf)TABLES#(tab)#(tab)|   Complete list of tables contained within this entity#(lf)#(lf)#(tab)#(tab)#(tab)#(tab)Primary table name:#(tab)#(tab)[ExchangeRate]#(lf)#(tab)#(tab)#(tab)#(tab)Table name:#(tab)#(tab)#(tab)#(tab)[ExchangeRateCurrencyPair]#(lf)#(tab)#(tab)#(tab)#(tab)Table name:#(tab)#(tab)#(tab)#(tab)[ExchangeRateType]#(lf)#(tab)#(tab)#(tab)#(tab)Table name:#(tab)#(tab)#(tab)#(tab)[GlobalOptionsetMetadata]#(lf)#(lf)#(tab)#(tab)#(tab)#(tab)#(lf)#(tab)#(tab)#(tab)#(tab)**See footnotes for references to datasource documentation#(lf)____________________________________________________________________________________________________#(lf)****************************************************************************************************#(lf)*/#(lf)#(lf)SELECT DISTINCT#(lf)#(tab)#(tab)#(tab)#(tab)#(lf)#(tab)#(tab)#(tab)#(tab)#(lf)#(tab)--------------------------------------------------------------------------------#(lf)#(tab)--#(tab)PRIMARY#(tab)TABLE#(tab)|#(tab)[ExchangeRate]#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab) #(lf)#(tab)-------------------------------------------------------------------------------- #(lf)#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)-- exchangerate.[Id] AS [exchangerate_Id]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[SinkCreatedOn] AS [exchangerate_SinkCreatedOn]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[SinkModifiedOn] AS [exchangerate_SinkModifiedOn]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[sysdatastatecode] AS [exchangerate_sysdatastatecode]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab) exchangerate.[exchangerate] AS [exchangerate_exchangerate]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[exchangeratecurrencypair] AS [exchangerate_exchangeratecurrencypair]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab),exchangerate.[validfrom] AS [exchangerate_validfrom]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab),exchangerate.[validto] AS [exchangerate_validto]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[modifieddatetime] AS [exchangerate_modifieddatetime]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[modifiedby] AS [exchangerate_modifiedby]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[modifiedtransactionid] AS [exchangerate_modifiedtransactionid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[createddatetime] AS [exchangerate_createddatetime]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[createdby] AS [exchangerate_createdby]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[createdtransactionid] AS [exchangerate_createdtransactionid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[dataareaid] AS [exchangerate_dataareaid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[recversion] AS [exchangerate_recversion]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[partition] AS [exchangerate_partition]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[sysrowversion] AS [exchangerate_sysrowversion]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[recid] AS [exchangerate_recid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[tableid] AS [exchangerate_tableid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[versionnumber] AS [exchangerate_versionnumber]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[createdon] AS [exchangerate_createdon]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[modifiedon] AS [exchangerate_modifiedon]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[IsDelete] AS [exchangerate_IsDelete]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[createdonpartition] AS [exchangerate_createdonpartition]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangerate.[PartitionId] AS [exchangerate_PartitionId]#(lf)#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(lf)#(tab)--------------------------------------------------------------------------------#(lf)#(tab)--#(tab)#(tab)#(tab)TABLE#(tab)|#(tab)[ExchangeRateCurrencyPair]#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab) #(lf)#(tab)-------------------------------------------------------------------------------- #(lf)#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[Id] AS [exchangeratecurrencypair_Id]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[SinkCreatedOn] AS [exchangeratecurrencypair_SinkCreatedOn]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[SinkModifiedOn] AS [exchangeratecurrencypair_SinkModifiedOn]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab),exchangeratecurrencypair.[exchangeratedisplayfactor] AS [exchangeratecurrencypair_exchangeratedisplayfactor]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[sysdatastatecode] AS [exchangeratecurrencypair_sysdatastatecode]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[exchangeratetype] AS [exchangeratecurrencypair_exchangeratetype]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab),exchangeratecurrencypair.[fromcurrencycode] AS [exchangeratecurrencypair_fromcurrencycode]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab),exchangeratecurrencypair.[tocurrencycode] AS [exchangeratecurrencypair_tocurrencycode]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[modifieddatetime] AS [exchangeratecurrencypair_modifieddatetime]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[modifiedby] AS [exchangeratecurrencypair_modifiedby]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[modifiedtransactionid] AS [exchangeratecurrencypair_modifiedtransactionid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[createddatetime] AS [exchangeratecurrencypair_createddatetime]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[createdby] AS [exchangeratecurrencypair_createdby]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[createdtransactionid] AS [exchangeratecurrencypair_createdtransactionid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[dataareaid] AS [exchangeratecurrencypair_dataareaid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[recversion] AS [exchangeratecurrencypair_recversion]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[partition] AS [exchangeratecurrencypair_partition]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[sysrowversion] AS [exchangeratecurrencypair_sysrowversion]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[recid] AS [exchangeratecurrencypair_recid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[tableid] AS [exchangeratecurrencypair_tableid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[versionnumber] AS [exchangeratecurrencypair_versionnumber]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[createdon] AS [exchangeratecurrencypair_createdon]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[modifiedon] AS [exchangeratecurrencypair_modifiedon]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[IsDelete] AS [exchangeratecurrencypair_IsDelete]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[createdonpartition] AS [exchangeratecurrencypair_createdonpartition]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratecurrencypair.[PartitionId] AS [exchangeratecurrencypair_PartitionId]#(lf)#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(lf)#(tab)--------------------------------------------------------------------------------#(lf)#(tab)--#(tab)#(tab)#(tab)TABLE#(tab)|#(tab)[ExchangeRateType]#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab) #(lf)#(tab)-------------------------------------------------------------------------------- #(lf)#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[Id] AS [exchangeratetype_Id]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[SinkCreatedOn] AS [exchangeratetype_SinkCreatedOn]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[SinkModifiedOn] AS [exchangeratetype_SinkModifiedOn]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[sysdatastatecode] AS [exchangeratetype_sysdatastatecode]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab),exchangeratetype.[description] AS [exchangeratetype_description]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab),exchangeratetype.[name] AS [exchangeratetype_name]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[calendarid] AS [exchangeratetype_calendarid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[modifieddatetime] AS [exchangeratetype_modifieddatetime]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[modifiedby] AS [exchangeratetype_modifiedby]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[modifiedtransactionid] AS [exchangeratetype_modifiedtransactionid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[createddatetime] AS [exchangeratetype_createddatetime]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[createdby] AS [exchangeratetype_createdby]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[createdtransactionid] AS [exchangeratetype_createdtransactionid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[dataareaid] AS [exchangeratetype_dataareaid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[recversion] AS [exchangeratetype_recversion]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[partition] AS [exchangeratetype_partition]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[sysrowversion] AS [exchangeratetype_sysrowversion]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[recid] AS [exchangeratetype_recid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[tableid] AS [exchangeratetype_tableid]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[versionnumber] AS [exchangeratetype_versionnumber]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[createdon] AS [exchangeratetype_createdon]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[modifiedon] AS [exchangeratetype_modifiedon]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[IsDelete] AS [exchangeratetype_IsDelete]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[createdonpartition] AS [exchangeratetype_createdonpartition]#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)--,exchangeratetype.[PartitionId] AS [exchangeratetype_PartitionId]#(lf)#(lf)#(lf)#(lf)  FROM#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)[exchangerate]#(lf)#(lf)  LEFT JOIN#(tab)#(tab)#(tab)#(tab)#(tab)[exchangeratecurrencypair]#(lf)  ON#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)exchangerate.[exchangeratecurrencypair]#(tab)#(tab)=#(tab)exchangeratecurrencypair.[recid]#(lf)#(lf)  LEFT JOIN#(tab)#(tab)#(tab)#(tab)#(tab)[exchangeratetype]#(lf)  ON#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)exchangeratecurrencypair.[exchangeratetype]#(tab)#(tab)=#(tab)exchangeratetype.[recid]#(lf)#(lf)#(lf)#(lf)#(tab)--------------------------------------------------------------------------------#(lf)#(tab)--#(tab)#(tab)#(tab)FILTER#(tab)|#(tab)Query optimization#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab) #(lf)#(tab)-------------------------------------------------------------------------------- #(lf)#(lf)  WHERE#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)exchangeratecurrencypair.[tocurrencycode]#(tab)#(tab)=#(tab)'USD'#(lf)  AND#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)exchangeratecurrencypair.[fromcurrencycode]#(tab)#(tab)IN#(tab)('CAD','GBP','EUR')#(lf)  AND#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)exchangeratetype.[description]#(tab)#(tab)#(tab)#(tab)#(tab)=#(tab)'Income Statement'#(lf)  AND#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)exchangerate.[validfrom]#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)>=#(tab)'2019-02-03'#(lf)#(lf)#(tab)--------------------------------------------------------------------------------#(lf)#(tab)--#(tab)#(tab)#(tab)FILTER#(tab)|#(tab)Remove deleted lines#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)  #(lf)#(tab)-------------------------------------------------------------------------------- #(lf)#(lf)  AND#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)(exchangerate.[IsDelete]#(tab)#(tab)#(tab)#(tab)IS NULL#(tab)OR#(tab)exchangerate.[IsDelete]#(tab)#(tab)#(tab)#(tab)= 0)#(lf)  AND#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)(exchangeratecurrencypair.[IsDelete]#(tab)IS NULL#(tab)OR#(tab)exchangeratecurrencypair.[IsDelete]#(tab)= 0)#(lf)  AND#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)(exchangeratetype.[IsDelete]#(tab)#(tab)#(tab)IS NULL#(tab)OR#(tab)exchangeratetype.[IsDelete]#(tab)#(tab)#(tab)= 0)#(lf)#(lf)#(lf)  ORDER BY#(tab)#(tab)#(tab)#(tab)#(tab)exchangerate.[validfrom]#(tab)#(tab)#(tab)#(tab)ASC#(lf)#(lf)#(lf)/*#(lf)____________________________________________________________________________________________________#(lf)****************************************************************************************************#(lf)#(lf)REFERENCES#(tab)|   Datasource documentation#(lf)#(lf)#(tab)#(tab)#(tab)#(tab)Entity name:#(tab)#(tab)#(tab)[ExchangeRateEntity]#(lf)#(tab)#(tab)#(tab)#(tab)Schema last updated:#(tab)2025-MAY-01#(lf)#(tab)#(tab)#(tab)#(tab)Schema updated by:#(tab)#(tab)V King#(lf)#(tab)#(tab)#(tab)#(tab)Microsoft schema:#(tab)#(tab)https://learn.microsoft.com/en-us/common-data-model/schema/core/operationscommon/entities/system/systemadministration/exchangerateentity#(lf)#(tab)#(tab)#(tab)#(tab)JSON definition:#(tab)#(tab)https://github.com/microsoft/CDM/blob/master/schemaDocuments/core/operationsCommon/Entities/System/SystemAdministration/ExchangeRateEntity.cdm.json#(lf)#(lf)#(tab)#(tab)#(tab)#(tab)Primary table name:#(tab)#(tab)[ExchangeRate]#(lf)#(tab)#(tab)#(tab)#(tab)Schema last updated:#(tab)2025-MAY-01#(lf)#(tab)#(tab)#(tab)#(tab)Schema updated by:#(tab)#(tab)V King#(lf)#(tab)#(tab)#(tab)#(tab)Microsoft schema:#(tab)#(tab)https://learn.microsoft.com/en-us/common-data-model/schema/core/operationscommon/tables/common/currency/reference/exchangerate#(lf)#(tab)#(tab)#(tab)#(tab)JSON definition:#(tab)#(tab)https://github.com/microsoft/CDM/blob/master/schemaDocuments/core/operationsCommon/Tables/Common/Currency/Reference/ExchangeRate.cdm.json#(lf)#(lf)#(tab)#(tab)#(tab)#(tab)Table name:#(tab)#(tab)#(tab)#(tab)[ExchangeRateCurrencyPair]#(lf)#(tab)#(tab)#(tab)#(tab)Schema last updated:#(tab)2025-MAY-01#(lf)#(tab)#(tab)#(tab)#(tab)Schema updated by:#(tab)#(tab)V King#(lf)#(tab)#(tab)#(tab)#(tab)Microsoft schema:#(tab)#(tab)https://learn.microsoft.com/en-us/common-data-model/schema/core/operationscommon/tables/common/currency/group/exchangeratecurrencypair#(lf)#(tab)#(tab)#(tab)#(tab)JSON definition:#(tab)#(tab)https://github.com/Microsoft/CDM/tree/master/schemaDocuments/core/operationsCommon/Tables/Common/Currency/Group/ExchangeRateCurrencyPair.cdm.json#(lf)#(lf)#(tab)#(tab)#(tab)#(tab)Table name:#(tab)#(tab)#(tab)#(tab)[ExchangeRateType]#(lf)#(tab)#(tab)#(tab)#(tab)Schema last updated:#(tab)2025-MAY-01#(lf)#(tab)#(tab)#(tab)#(tab)Schema updated by:#(tab)#(tab)V King#(lf)#(tab)#(tab)#(tab)#(tab)Microsoft schema:#(tab)#(tab)https://learn.microsoft.com/en-us/common-data-model/schema/core/operationscommon/tables/common/currency/group/exchangeratetype#(lf)#(tab)#(tab)#(tab)#(tab)JSON definition:#(tab)#(tab)https://github.com/Microsoft/CDM/tree/master/schemaDocuments/core/operationsCommon/Tables/Common/Currency/Group/ExchangeRateType.cdm.json#(lf)#(lf)#(tab)#(tab)#(tab)#(tab)Table name:#(tab)#(tab)#(tab)#(tab)[OptionSetMetadata]#(lf)#(tab)#(tab)#(tab)#(tab)Schema last updated:#(tab)2025-MAY-01#(lf)#(tab)#(tab)#(tab)#(tab)Schema updated by:#(tab)#(tab)V King#(lf)#(tab)#(tab)#(tab)#(tab)Microsoft schema:#(tab)#(tab)https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/optionsetmetadata?view=dataverse-latest#(lf)#(lf)____________________________________________________________________________________________________#(lf)****************************************************************************************************#(lf)*/", CreateNavigationProperties=false]),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"exchangeratecurrencypair_fromcurrencycode", "From Currency Code"}, {"exchangeratecurrencypair_tocurrencycode", "To Currency Code"}, {"exchangerate_validfrom", "Valid From"}, {"exchangerate_validto", "Valid To"}, {"exchangerate_exchangerate", "Exchange rate"}, {"exchangeratetype_name", "Exchange rate type"}, {"exchangeratetype_description", "Name"}, {"exchangeratecurrencypair_exchangeratedisplayfactor", "Conversion factor"} })
in
    #"Renamed Columns"
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

### Products (PLM)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Mart", [Query="SELECT DISTINCT#(lf)#(lf)       products.[product_key] AS [ProductKey]#(lf)      ,products.[BaseID] AS [BaseID]#(lf)      ,products.[style_code] AS [Style Code]#(lf)      ,products.[INLINE_CD] AS [Inline CD]#(lf)      ,products.[style_desc] AS [Style Description]#(lf)      ,products.[jurisdiction_code] AS [Jurisdiction Code]#(lf)      ,attributes.[ProductSellingGeography] AS [Product Selling Geography]#(lf)      ,products.[jurisdiction_id] AS [Jurisdiction Id]#(lf)      ,attributes.[ProductCountry] AS [Product Country]#(lf)      ,products.[original_retail] AS [Original Retail]#(lf)      ,products.[current_retail] AS [Current Retail]#(lf)      ,products.[current_selling_retail_home] AS [Current Selling Retail Home]#(lf)      ,products.[cdn_value] AS [CDN Value]#(lf)      ,products.[euro_value] AS [Euro Value]#(lf)      ,products.[price_with_vat] AS [Price with VAT]#(lf)      ,products.[priceline_code] AS [Priceline Code]#(lf)      ,products.[ScorecardCategory] AS [Scorecard Category]#(lf)      ,products.[department] AS [Department]#(lf)      ,products.[department_code] AS [Department Code]#(lf)      ,attributes.[DepartmentHierarchyGroupID] AS [Department Hierarchy Group ID]#(lf)      ,products.[class] AS [Class]#(lf)      ,products.[class_code] AS [Class Code]#(lf)      ,attributes.[ClassHierarchyGroupID] AS [Class Hierarchy Group ID]#(lf)      ,attributes.[ClassParentGroupID] AS [Class Parent Group ID]#(lf)      ,products.[subclass] AS [Subclass]#(lf)      ,products.[subclass_code] AS [Subclass Code]#(lf)      ,attributes.[SubClassHierarchyGroupID] AS [Subclass Hierarchy Group ID]#(lf)      ,attributes.[SubClassParentGroupID] AS [Subclass Parent Group ID]#(lf)      ,attributes.[StyleParentGroupID] AS [Style Parent Group ID]#(lf)      ,products.[division] AS [Division]#(lf)      ,attributes.[DivisionCode] AS [Division Code]#(lf)      ,attributes.[ConsumerGroup] AS [Consumer Group]#(lf)      ,products.[concept] AS [Concept]#(lf)      ,products.[chain] AS [Chain]#(lf)      ,attributes.[ChainCode] AS [Chain Code]#(lf)      ,attributes.[ItemType] AS [Item Type]#(lf)      ,attributes.[isBundleSKU] AS [Is Bundle SKU]#(lf)      ,attributes.[WebExclusive] AS [Web Exclusive]#(lf)      ,attributes.[Web] AS [Web]#(lf)      ,attributes.[KeyStory] AS [Key Story]#(lf)      ,attributes.[LICEN] AS [Licensed]#(lf)      ,attributes.[LicensedCollection] AS [Licensed Collection]#(lf)      ,attributes.[occasion] AS [Occasion]#(lf)      ,attributes.[OccasionCode] AS [Occasion Code]#(lf)      ,attributes.[Sound] AS [Sound]#(lf)      ,products.[color_code] AS [Color Code]#(lf)      ,products.[color_desc] AS [Color Description]#(lf)      ,products.[color_id] AS [Color Id]#(lf)      ,attributes.[sportsTeam] AS [Sports Team]#(lf)      ,products.[merch_status] AS [Merch Status]#(lf)      ,attributes.[SellingStatus] AS [Selling Status]#(lf)      ,attributes.[AvailB] AS [AvailB]#(lf)      ,products.[activation_date] AS [Activation Date]#(lf)      ,attributes.[MerchInDate] AS [Merch In Date]#(lf)      ,attributes.[merchOutDate] AS [Merch Out Date]#(lf)      ,attributes.[ODATE] AS [ODate]#(lf)      ,attributes.[ONOTE] AS [Out Date Note]#(lf)      ,attributes.[isOutOfStock] AS [Is Out Of Stock]#(lf)      ,products.[reorder_flag] AS [Reorder Flag]#(lf)      ,attributes.[OnOrderFlag] AS [On Order Flag]#(lf)      ,attributes.[isWebEligible] AS [Is Web Eligible]#(lf)      ,attributes.[WMSTAT] AS [WMSTAT]#(lf)      ,attributes.[OMSTAT] AS [OMSTAT]#(lf)      ,attributes.[OrderMultiple] AS [Order Multiple]#(lf)      ,attributes.[DistributionMultiple] AS [Distribution Multiple]#(lf)      ,attributes.[InnerCasePack] AS [Inner Case Pack]#(lf)      ,attributes.[ManufacturerCountry] AS [Manufacturer Country]#(lf)      ,products.[primary_vendor_name] AS [Primary Vendor Name]#(lf)      ,products.[primary_vendor_code] AS [Primary Vendor Code]#(lf)      ,products.[alt_primary_vendor_code] AS [Alt Primary Vendor Code]#(lf)      ,attributes.[InventoryBuffer] AS [Inventory Buffer]#(lf)      ,attributes.[CommodityCode] AS [Commodity Code]#(lf)      ,attributes.[QuantityRestriction] AS [Quantity Restriction]#(lf)      ,attributes.[AccessoryEligible] AS [Accessory Eligible]#(lf)      ,attributes.[AccessoryType] AS [Accessory Type]#(lf)      ,attributes.[AnimalSoldSeparately] AS [Animal Sold Separately]#(lf)      ,attributes.[AsthmaFriendly] AS [Asthma Friendly]#(lf)      ,attributes.[BirthCertificateRequired] AS [Birth Certificate Required]#(lf)      ,attributes.[BodyType] AS [Body Type]#(lf)      ,attributes.[Bottoms] AS [Bottoms]#(lf)      ,attributes.[Boy] AS [Boy]#(lf)      ,attributes.[BRF] AS [Back Room Fulfillment]#(lf)      ,attributes.[CompSetName] AS [Comp Set Name]#(lf)      ,products.[CORE_FASH_CD] AS [Core Fashion CD]#(lf)      ,attributes.[DisplayOnAmazon] AS [Display On Amazon]#(lf)      ,attributes.[EmbroideryProductList] AS [Embroidery Product List]#(lf)      ,attributes.[EyeColor] AS [Eye Color]#(lf)      ,attributes.[fourLeggedAnimal] AS [Four Legged Animal]#(lf)      ,attributes.[FriendHeight] AS [Friend Height]#(lf)      ,attributes.[FriendWeight] AS [Friend Weight]#(lf)      ,products.[GENDER] AS [Gender]#(lf)      ,attributes.[GiftBoxType] AS [Gift Box Type]#(lf)      ,attributes.[giftCardType] AS [Gift Card Type]#(lf)      ,attributes.[Girl] AS [Girl]#(lf)      ,attributes.[isCashierEnterQty] AS [Is Cashier Enters Quantity]#(lf)      ,attributes.[isCashierEntersPrice] AS [Is Cashier Enters Price]#(lf)      ,attributes.[isCouponEligible] AS [Is Coupon Eligible]#(lf)      ,attributes.[isEmployeeDiscountEligible] AS [Is Employee Discount Eligible]#(lf)      ,attributes.[isEndlessAisleEligible] AS [Is Endless Aisle Eligible]#(lf)      ,attributes.[isLoyaltyRewardsDiscountEligible] AS [Is Loyalty Rewards Discount Eligible]#(lf)      ,attributes.[isQtyRestricted] AS [Is Quantity Restricted]#(lf)      ,attributes.[isReturnEligible] AS [Is Return Eligible]#(lf)      ,attributes.[isTaxExempt] AS [Is Tax Exempt]#(lf)      ,attributes.[Mini] AS [Mini]#(lf)      ,attributes.[MLBTeams] AS [MLB Teams]#(lf)      ,attributes.[Music] AS [Music]#(lf)      ,attributes.[NBATeams] AS [NBA Teams]#(lf)      ,attributes.[Neutral] AS [Neutral]#(lf)      ,attributes.[NFLTeams] AS [NFL Teams]#(lf)      ,attributes.[NHLTeams] AS [NHL Teams]#(lf)      ,attributes.[NoInternationalShipping] AS [No International Shipping]#(lf)      ,attributes.[Outfits] AS [Outfits]#(lf)      ,attributes.[Outlet] AS [Outlet]#(lf)      ,attributes.[PackageOption] AS [Package Option]#(lf)      ,attributes.[ProductCanBeEmbroidered] AS [Product Can Be Embroidered]#(lf)      ,attributes.[ProductMustBeEmbroidered] AS [Product Must Be Embroidered]#(lf)      ,attributes.[Purses] AS [Purses]#(lf)      ,attributes.[RefundEligible] AS [Refund Eligible]#(lf)      ,attributes.[Seasonal] AS [Seasonal]#(lf)      ,attributes.[ShippingClass] AS [Shipping Class]#(lf)      ,attributes.[Shoes] AS [Shoes]#(lf)      ,attributes.[SkinType] AS [Skin Type]#(lf)      ,attributes.[SoundEligible] AS [Sound Eligible]#(lf)      ,attributes.[StoreFrontEligible] AS [Store Front Eligible]#(lf)      ,attributes.[Stuffable] AS [Stuffable]#(lf)      ,attributes.[SAC] AS [Stuffed-And-Closed]#(lf)      ,attributes.[SNC] AS [Stuffed-Not-Closed]#(lf)      ,attributes.[ThirdPartySiteEligible] AS [Third Party Site Eligible]#(lf)      ,attributes.[Tops] AS [Tops]#(lf)      ,attributes.[UKFootball] AS [UK Football]#(lf)      ,attributes.[UPC] AS [UPC]#(lf)      ,attributes.[WarningLabel] AS [Warning Label]#(lf)      ,products.[wss_reportable] AS [WSS Reportable]#(lf)      ,products.[UPDT_DT] AS [Last Update Datetime]#(lf)      ,products.[TotalFOB] AS [LastPOCost]#(lf)#(lf)#(lf)  FROM#(tab)#(tab)#(tab)[dbo].[product_dim] products#(lf)#(lf)  LEFT JOIN#(tab)#(tab)[dbo].[productcatalogmasterattributes] attributes#(lf)  ON#(tab)#(tab)#(tab)products.[jurisdiction_code] = attributes.[ProductSellingGeography]#(lf)  AND#(tab)#(tab)#(tab)products.[style_code] = attributes.[StyleCode]#(tab)#(lf)#(lf)  WHERE#(tab)#(tab)#(tab)products.[style_code] IS NOT NULL#(lf)  AND#(tab)#(tab)#(tab)products.[product_key] > 0#(lf)#(lf)  ORDER BY#(tab)#(tab)products.[style_code] ASC", CreateNavigationProperties=false]),
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
    #"Sorted Rows | Style Code ASC" = Table.Sort(#"Removed Duplicates | ItemKey",{{"Style Code", Order.Ascending}}),
    #"Renamed Columns1" = Table.RenameColumns(#"Sorted Rows | Style Code ASC",{{"LastPOCost", "Last PO Cost"}})
in
    #"Renamed Columns1"
```

### Retail Line Discounts (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH pos_tx_header AS (#(lf)#(tab)SELECT#(lf)#(tab)#(tab)#(tab)st.device_id,#(lf)#(tab)#(tab)#(tab)st.business_date,#(lf)#(tab)#(tab)#(tab)st.sequence_number#(lf)#(tab)FROM dbo.jumpmind_sls_retail_trans st#(lf)#(tab)WHERE st.business_date >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 2 MONTHS#(lf)),#(lf)pos_line_discounts AS (#(lf)#(tab)SELECT#(lf)#(tab)#(tab)#(tab)CONVERT(varchar(10), d.business_date, 120)        AS business_date,#(lf)#(tab)#(tab)#(tab)CASE#(lf)#(tab)#(tab)#(tab)#(tab)WHEN TRY_CONVERT(decimal(18,6), d.mod_by_percentage) IS NOT NULL#(lf)#(tab)#(tab)#(tab)#(tab)AND TRY_CONVERT(decimal(18,6), d.mod_by_percentage) <> 0#(lf)#(tab)#(tab)#(tab)#(tab)THEN 'PERCENT' ELSE 'AMOUNT'#(lf)#(tab)#(tab)#(tab)END                                               AS calc_method,#(lf)#(tab)#(tab)#(tab)d.device_id,#(lf)#(tab)#(tab)#(tab)d.entry_method_code,#(lf)#(tab)#(tab)#(tab)d.iso_currency_code,#(lf)#(tab)#(tab)#(tab)d.last_update_time,#(lf)#(tab)#(tab)#(tab)d.line_sequence_number,#(lf)#(tab)#(tab)#(tab)d.mod_line_sequence_number,#(lf)#(tab)#(tab)#(tab)d.override_user_id,#(lf)#(tab)#(tab)#(tab)d.price_mod_source_type_code,#(lf)#(tab)#(tab)#(tab)d.price_mod_type_code,#(lf)#(tab)#(tab)#(tab)d.reason_code,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS numeric(18,6))                       AS rounding_amount,#(lf)#(tab)#(tab)#(tab)d.sequence_number,#(lf)#(tab)#(tab)#(tab)d.username,#(lf)#(tab)#(tab)#(tab)ISNULL(d.voided, 0)                               AS voided,#(lf)#(tab)#(tab)#(tab)d.applied_coupon_item_ids,#(lf)#(tab)#(tab)#(tab)d.create_by,#(lf)#(tab)#(tab)#(tab)d.create_time,#(lf)#(tab)#(tab)#(tab)ISNULL(d.[description], '')                       AS [description],#(lf)#(tab)#(tab)#(tab)d.last_update_by,#(lf)#(tab)#(tab)#(tab)d.loyalty_promotion_id,#(lf)#(tab)#(tab)#(tab)d.mod_by_amount,#(lf)#(tab)#(tab)#(tab)d.mod_by_percentage,#(lf)#(tab)#(tab)#(tab)d.modification_total,                             -- existing#(lf)#(tab)#(tab)#(tab)d.modification_total AS GrossLineAmt,             -- new to match OMS GrossLineAmt#(lf)#(tab)#(tab)#(tab)d.modification_total AS CouponValue,              -- new to match OMS CouponValue#(lf)#(tab)#(tab)#(tab)d.price_mod_source_sub_type_code,#(lf)#(tab)#(tab)#(tab)ISNULL(d.promotion_id, '')                        AS promotion_id,#(lf)#(tab)#(tab)#(tab)d.promotion_reward_quantity,#(lf)#(tab)#(tab)#(tab)ISNULL(d.promotion_type, '')                      AS promotion_type,#(lf)#(tab)#(tab)#(tab)d.ref_line_sequence_number,#(lf)#(tab)#(tab)#(tab)d.promo_code_id#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)  AS promo_code_id,#(lf)#(tab)#(tab)#(tab)d.reward_base_price_type_code,#(lf)#(tab)#(tab)#(tab)ISNULL(d.vendor_funded_flag, 0)                   AS vendor_funded_flag,#(lf)#(tab)#(tab)#(tab)d.quantity_index,#(lf)#(tab)#(tab)#(tab)d.rtn_device_id,#(lf)#(tab)#(tab)#(tab)CONVERT(varchar(10), TRY_CONVERT(date, d.rtn_business_date), 120) AS rtn_business_date,#(lf)#(tab)#(tab)#(tab)d.rtn_sequence_number,#(lf)#(tab)#(tab)#(tab)ISNULL(d.returned_flag, 0)                        AS returned_flag,#(lf)#(tab)#(tab)#(tab)d.external_id,#(lf)#(tab)#(tab)#(tab)NULL                                              AS order_status_id,#(lf)#(tab)#(tab)#(tab)NULL                                              AS order_status_code,#(lf)#(tab)#(tab)#(tab)NULL                                              AS order_status#(lf)#(tab)FROM dbo.jumpmind_sls_retail_line_item_price_mod d#(lf)#(tab)WHERE d.business_date >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 2 MONTHS#(lf)),#(lf)hs AS (#(lf)#(tab)SELECT#(lf)#(tab)#(tab)#(tab)COALESCE(#(lf)#(tab)#(tab)#(tab)NULLIF(CONVERT(varchar(64), dtt.MaxWarehouseCode), ''),#(lf)#(tab)#(tab)#(tab)NULLIF(CONVERT(varchar(64), dtt.SiteWarehouseCode), ''),#(lf)#(tab)#(tab)#(tab)NULLIF(CONVERT(varchar(64), r.SiteCode), '')#(lf)#(tab)#(tab)#(tab))                                                AS InventLocationId,#(lf)#(tab)#(tab)#(tab)CAST(COALESCE(#(lf)#(tab)#(tab)#(tab)#(tab)r.OrderDateUTC,#(lf)#(tab)#(tab)#(tab)#(tab)r.DateCreatedUTC,#(lf)#(tab)#(tab)#(tab)#(tab)r.OrderStatusChangeDateUTC,#(lf)#(tab)#(tab)#(tab)#(tab)r.ExportCreatedUTC#(lf)#(tab)#(tab)#(tab)) AS date)                                       AS TransDate,#(lf)#(tab)#(tab)#(tab)CONVERT(varchar(64), r.OrderNumber)              AS Barcode,#(lf)#(tab)#(tab)#(tab)CONVERT(varchar(64), r.OrderID)                  AS OrderID,#(lf)#(tab)#(tab)#(tab)r.Custom3#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)AS EmployeeID,#(lf)#(tab)#(tab)#(tab)r._RowIndex,#(lf)#(tab)#(tab)#(tab)r.OrderStatus#(lf)#(tab)FROM dbo.mulesoft_deckjsonraw_root r#(lf)#(tab)LEFT JOIN dbo.mulesoft_dynamicstargettrans dtt#(lf)#(tab)ON CONVERT(varchar(64), dtt.OrderId) = CONVERT(varchar(64), r.OrderID)#(lf)#(tab)WHERE CAST(COALESCE(#(lf)#(tab)#(tab)r.OrderDateUTC,#(lf)#(tab)#(tab)r.DateCreatedUTC,#(lf)#(tab)#(tab)r.OrderStatusChangeDateUTC,#(lf)#(tab)#(tab)r.ExportCreatedUTC#(lf)#(tab)) AS date) >= DATEADD(month, -4, CAST(GETDATE() AS date))           -- 2 MONTHS#(lf)),#(lf)hs_norm AS (#(lf)SELECT#(lf)#(tab)#(tab)CASE#(lf)#(tab)#(tab)#(tab)WHEN hs.InventLocationId = 'BAB'   THEN '1013'#(lf)#(tab)#(tab)#(tab)WHEN hs.InventLocationId = 'BABUK' THEN '2013'#(lf)#(tab)#(tab)#(tab)WHEN NULLIF(hs.InventLocationId,'') IS NULL THEN '9999'#(lf)#(tab)#(tab)#(tab)ELSE '9999'#(lf)#(tab)#(tab)#(tab)END                                              AS InventLocationIdMapped,#(lf)#(tab)#(tab)#(tab)hs.*#(lf)#(tab)FROM hs#(lf)),#(lf)deck_adjustments AS (#(lf)#(tab)SELECT#(lf)#(tab)#(tab)#(tab)CONVERT(varchar(64), a._ParentKeyField)          AS OrderID_key,#(lf)#(tab)#(tab)#(tab)a.OrderTransactionIdentifier                    AS RootRowIndex,#(lf)#(tab)#(tab)#(tab)a.AdjustmentDate,#(lf)#(tab)#(tab)#(tab)a.AdjustmentTypeValue,#(lf)#(tab)#(tab)#(tab)a.CouponCode                                    AS CouponCode,#(lf)#(tab)#(tab)#(tab)a.GrossPrice                                    AS GrossPrice,      -- GrossLineAmt for OMS#(lf)#(tab)#(tab)#(tab)a.CampaignID AS campaign_id, #(lf)#(tab)#(tab)#(tab)a.NetPrice                                      AS NetPrice         -- CouponValue for OMS#(lf)#(tab)FROM dbo.mulesoft_deckjsonraw_orderadjustments a#(lf)#(tab)-- WHERE a.AdjustmentDate >= DATEADD(month, -2, CAST(GETDATE() AS date))  -- 2 MONTHS#(lf)#(tab)--REMOVED DATE CONSTRAINT BECAUSE ALL DATES IN THAT COLUMN ARE OUT OF RANGE (0000/00/00)#(lf))#(lf)#(lf)#(tab)SELECT#(lf)#(tab)#(tab)#(tab)'POS' AS SourceSystem,#(lf)#(tab)#(tab)#(tab)CONCAT(#(lf)#(tab)#(tab)#(tab)CAST(h.device_id AS varchar(64)), '-',#(lf)#(tab)#(tab)#(tab)CONVERT(varchar(10), h.business_date, 120), '-',#(lf)#(tab)#(tab)#(tab)CONVERT(varchar(50), h.sequence_number), '-',#(lf)#(tab)#(tab)#(tab)CONVERT(varchar(50), d.line_sequence_number)#(lf)#(tab)#(tab)#(tab)) AS TransactionKey,#(lf)#(tab)#(tab)#(tab)d.*#(lf)#(tab)FROM pos_line_discounts d#(lf)#(tab)#(tab)JOIN pos_tx_header h#(lf)#(tab)#(tab)#(tab)ON h.device_id       = d.device_id#(lf)#(tab)#(tab)#(tab)AND h.business_date   = CAST(d.business_date AS date)#(lf)#(tab)#(tab)#(tab)AND h.sequence_number = d.sequence_number#(lf)#(lf)#(tab)UNION ALL#(lf)#(lf)#(tab)SELECT#(lf)#(tab)#(tab)#(tab)'OMS' AS SourceSystem,#(lf)#(tab)#(tab)#(tab)CONCAT(#(lf)#(tab)#(tab)#(tab)hn.InventLocationIdMapped, '-', '052', '-', CONVERT(varchar, hn.TransDate, 112), '-', hn.Barcode#(lf)#(tab)#(tab)#(tab)) AS TransactionKey,#(lf)#(tab)#(tab)#(tab)CONVERT(varchar(10), hn.TransDate, 112)            AS business_date,#(lf)#(tab)#(tab)#(tab)'AMOUNT'                                          AS calc_method,#(lf)#(tab)#(tab)#(tab)CAST(COALESCE(hn.InventLocationIdMapped, '9999') + '-052' AS VARCHAR(8000)) AS device_id,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS varchar(64))                         AS entry_method_code,#(lf)#(tab)#(tab)#(tab)CASE WHEN hn.InventLocationIdMapped IN ('2013') THEN 'GBP' ELSE 'USD' END AS iso_currency_code,#(lf)#(tab)#(tab)#(tab)da.AdjustmentDate                                 AS last_update_time,#(lf)#(tab)#(tab)#(tab)CAST(hn._RowIndex AS VARCHAR(64))#(tab)#(tab)#(tab)#(tab)  AS line_sequence_number,#(lf)#(tab)#(tab)#(tab)CAST(1 AS int)                                    AS mod_line_sequence_number,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS varchar(64))                         AS override_user_id,#(lf)#(tab)#(tab)#(tab)CASE WHEN da.AdjustmentTypeValue LIKE '%Manual%' THEN 'MANUAL' ELSE NULL END AS price_mod_source_type_code,#(lf)#(tab)#(tab)#(tab)'TRANS'                                           AS price_mod_type_code,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS varchar(64))                         AS reason_code,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS numeric(18,6))                       AS rounding_amount,#(lf)#(tab)#(tab)#(tab)TRY_CONVERT(bigint, da.OrderID_key)               AS sequence_number,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS varchar(128))                        AS username,#(lf)#(tab)#(tab)#(tab)CAST(0 AS int)                                    AS voided,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS varchar(4000))                       AS applied_coupon_item_ids,#(lf)#(tab)#(tab)#(tab)'WEB'                                             AS create_by,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS datetime2(6))                        AS create_time,#(lf)#(tab)#(tab)#(tab)ISNULL(da.AdjustmentTypeValue, '')                AS [description],#(lf)#(tab)#(tab)#(tab)CAST(NULL AS varchar(128))                        AS last_update_by,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS varchar(64))                         AS loyalty_promotion_id,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS decimal(18,6))                       AS mod_by_amount,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS decimal(18,6))                       AS mod_by_percentage,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS decimal(18,6))                       AS modification_total,  -- existing#(lf)#(tab)#(tab)#(tab)da.GrossPrice                                     AS GrossLineAmt,         -- new#(lf)#(tab)#(tab)#(tab)da.NetPrice                                       AS CouponValue,          -- new#(lf)#(tab)#(tab)#(tab)CAST(NULL AS varchar(64))                         AS price_mod_source_sub_type_code,#(lf)#(tab)#(tab)#(tab)''                                                AS promotion_id,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS decimal(18,6))                       AS promotion_reward_quantity,#(lf)#(tab)#(tab)#(tab)CASE WHEN EmployeeID IS NOT NULL THEN 'Employee Discount' #(lf)#(tab)#(tab)#(tab)#(tab)ELSE 'Transaction' END                                    AS promotion_type,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS int)                                 AS ref_line_sequence_number,#(lf)#(tab)#(tab)#(tab)da.CouponCode                                     AS promo_code_id,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS varchar(64))                         AS reward_base_price_type_code,#(lf)#(tab)#(tab)#(tab)CAST(0 AS int)                                    AS vendor_funded_flag,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS int)                                 AS quantity_index,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS varchar(64))                         AS rtn_device_id,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS varchar(10))                         AS rtn_business_date,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS bigint)                              AS rtn_sequence_number,#(lf)#(tab)#(tab)#(tab)CAST(0 AS int)                                    AS returned_flag,#(lf)#(tab)#(tab)#(tab)CAST(NULL AS varchar(128))                        AS external_id,#(lf)#(tab)#(tab)#(tab) hn.OrderStatus                                   AS order_status_id,#(lf)#(tab)#(tab)#(tab)#(tab)CASE hn.OrderStatus #(lf)#(tab)#(tab)#(tab)#(tab)#(tab)WHEN 1 THEN 'CO'#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)WHEN 3 THEN 'AVS'#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)WHEN 4 THEN 'P'#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)WHEN 5 THEN 'PV'#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)WHEN 6 THEN 'Z'#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)WHEN 9 THEN 'MR'#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)WHEN 10 THEN 'PS'#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)WHEN 11 THEN 'DAP'#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)WHEN 12 THEN 'CF'#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)ELSE null#(lf)#(tab)#(tab)#(tab)#(tab)END                                            AS order_status_code,#(lf)#(tab)#(tab)#(tab)#(tab)CASE hn.OrderStatus #(lf)#(tab)#(tab)#(tab)#(tab)#(tab)WHEN 1 THEN 'New'#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)WHEN 3 THEN 'Review'#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)WHEN 4 THEN 'Pending'#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)WHEN 5 THEN 'Exception'#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)WHEN 6 THEN 'Completed'#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)WHEN 9 THEN 'Manual Review'#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)WHEN 10 THEN 'Pending Settlement'#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)WHEN 11 THEN 'Delayed Auto-Process'#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)WHEN 12 THEN 'Confirmed Fraud'#(lf)#(tab)#(tab)#(tab)#(tab)#(tab)ELSE null#(lf)#(tab)#(tab)#(tab)#(tab)END                                            AS order_status#(lf)FROM deck_adjustments da#(lf)#(tab)LEFT JOIN hs_norm hn#(lf)#(tab)#(tab)ON CONVERT(varchar(64), hn.OrderID) = CONVERT(varchar(64), da.OrderID_key)#(lf)#(tab)#(tab)AND hn._RowIndex = da.RootRowIndex#(lf)"]),
    #"Filtered Rows | Remove Voided Lines" = Table.SelectRows(Source, each [voided] = 0),
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

### Global Products (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH jumpmind_global_product_cte AS (#(lf)SELECT DISTINCT#(lf)       [item_id]#(tab)#(tab)#(tab)AS [Item ID]#(lf)      ,RIGHT([item_id],5)#(tab)AS [Core SKU]#(lf)      ,[item_description]#(tab)AS [Item Description]#(lf)      ,[iso_currency_code]#(tab)AS [Currency]#(lf)      ,[item_type]#(tab)#(tab)#(tab)AS [Item Type]#(lf)#(tab)  ,CASE#(lf)#(tab)#(tab)#(tab)WHEN#(tab)[iso_currency_code] =#(tab)'USD'#(lf)#(tab)#(tab)#(tab)THEN#(tab)[item_description]#(lf)#(tab)#(tab)#(tab)END AS#(tab)'Item Name (US)'#(lf)#(tab)  ,CASE#(lf)#(tab)#(tab)#(tab)WHEN#(tab)[iso_currency_code] =#(tab)'CAD'#(lf)#(tab)#(tab)#(tab)THEN#(tab)[item_description]#(lf)#(tab)#(tab)#(tab)END AS#(tab)'Item Name (CA)'#(lf)#(tab)  ,CASE#(lf)#(tab)#(tab)#(tab)WHEN#(tab)[iso_currency_code] =#(tab)'GBP'#(lf)#(tab)#(tab)#(tab)THEN#(tab)[item_description]#(lf)#(tab)#(tab)#(tab)END AS#(tab)'Item Name (UK)'#(lf)#(tab)  ,CASE#(lf)#(tab)#(tab)#(tab)WHEN#(tab)[iso_currency_code] =#(tab)'EUR'#(lf)#(tab)#(tab)#(tab)THEN#(tab)[item_description]#(lf)#(tab)#(tab)#(tab)END AS#(tab)'Item Name (IE)'#(lf)  FROM#(tab)#(tab)[dbo].[jumpmind_sls_retail_line_item]#(lf)  WHERE LEN(item_id)#(tab)#(tab)=#(tab)6#(lf)),#(lf)deck_global_products_cte AS (#(lf)SELECT DISTINCT#(lf)StyleNumber as [Item ID]#(lf), DeckSKU as [Core SKU]#(lf), oi.Custom1 as [Item Description]#(lf), case when r.SiteCode = 'BAB' #(lf)#(tab)#(tab)then 'USD'#(lf)#(tab)else 'GBP'#(lf)#(tab)end as [Currency]#(lf), CASE WHEN UPPER(oi.ItemTypeLocalizeName) = 'REGULAR ITEM' #(lf)#(tab)THEN 'STOCK' ELSE UPPER(oi.ItemTypeLocalizeName) END as [Item Type]#(lf)FROM LH_Source.dbo.mulesoft_deckjsonraw_orderitems oi#(lf)LEFT JOIN LH_Source.dbo.mulesoft_deckjsonraw_root r ON oi.OrderID = r.OrderID#(lf)LEFT JOIN LH_Source.dbo.mulesoft_deckjsonraw_orderpayments op on oi.PaymentID = op.ID#(lf)),#(lf)deck_global_products_ext AS (#(lf)#(tab)SELECT *#(lf)#(tab),CASE#(lf)#(tab)#(tab)WHEN#(tab)[Currency] =#(tab)'USD'#(lf)#(tab)#(tab)THEN#(tab)[Item Description]#(lf)#(tab)#(tab)END AS#(tab)'Item Name (US)'#(lf)#(tab),CASE#(lf)#(tab)#(tab)WHEN#(tab)[Currency] =#(tab)'CAD'#(lf)#(tab)#(tab)THEN#(tab)[Item Description]#(lf)#(tab)#(tab)END AS#(tab)'Item Name (CA)'#(lf)#(tab),CASE#(lf)#(tab)#(tab)WHEN#(tab)[Currency] =#(tab)'GBP'#(lf)#(tab)#(tab)THEN#(tab)[Item Description]#(lf)#(tab)#(tab)END AS#(tab)'Item Name (UK)'#(lf)#(tab),CASE#(lf)#(tab)#(tab)WHEN#(tab)[Currency] =#(tab)'EUR'#(lf)#(tab)#(tab)THEN#(tab)[Item Description]#(lf)#(tab)#(tab)END AS#(tab)'Item Name (IE)'#(lf)#(tab)FROM deck_global_products_cte#(lf))#(lf)SELECT *#(lf)FROM jumpmind_global_product_cte#(lf)UNION#(lf)SELECT *#(lf)FROM deck_global_products_ext", CreateNavigationProperties=false]),
    #"Removed Columns" = Table.RemoveColumns(Source,{"Item ID", "Item Description", "Currency"}),
    #"Grouped Rows" = Table.Group(#"Removed Columns", {"Core SKU", "Item Type"}, {{"Item Name (US)", each List.Max([#"Item Name (US)"]), type nullable text}, {"Item Name (CA)", each List.Max([#"Item Name (CA)"]), type nullable text}, {"Item Name (UK)", each List.Max([#"Item Name (UK)"]), type nullable text}, {"Item Name (IE)", each List.Max([#"Item Name (IE)"]), type nullable text}}),
    #"Added Conditional Column | Global Item Name" = Table.AddColumn(#"Grouped Rows", "Global Item Name", each if [#"Item Name (US)"] <> null then [#"Item Name (US)"] else if [#"Item Name (CA)"] <> null then [#"Item Name (CA)"] else if [#"Item Name (UK)"] <> null then [#"Item Name (UK)"] else if [#"Item Name (IE)"] <> null then [#"Item Name (IE)"] else null),
    #"Added Custom | Global Item Line" = Table.AddColumn(#"Added Conditional Column | Global Item Name", "Global Item Line", each [Core SKU] & " | " & [Global Item Name]),
    #"Changed Type" = Table.TransformColumnTypes(#"Added Custom | Global Item Line",{{"Global Item Name", type text}, {"Global Item Line", type text}}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Changed Type",{{"Item Type", Text.Proper, type text}})
in
    #"Capitalized Each Word"
```

### Retail Lines (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH pos_lines AS (#(lf)    SELECT#(lf)        CAST(j.device_id AS varchar(64)) AS device_id,#(lf)        CONVERT(varchar(8), TRY_CONVERT(date, j.business_date, 112), 112) AS business_date,#(lf)        CAST(j.sequence_number AS bigint) AS sequence_number,#(lf)        CAST(j.line_sequence_number AS int) AS line_sequence_number,#(lf)        CAST(j.pos_item_id AS varchar(8000)) AS pos_item_id,#(lf)        CAST(j.item_id AS varchar(8000)) AS item_id,#(lf)        CAST(j.item_description AS varchar(8000)) AS item_description,#(lf)        CAST(j.item_type AS varchar(8000)) AS item_type,#(lf)        CAST(j.regular_unit_price AS decimal(18,2)) AS regular_unit_price,#(lf)        CAST(j.actual_unit_price  AS decimal(18,2)) AS actual_unit_price,#(lf)        CAST(j.loyalty_unit_price AS decimal(18,2)) AS loyalty_unit_price,#(lf)        CAST(j.quantity AS decimal(18,2)) AS quantity,#(lf)        CAST(j.extended_amount AS decimal(18,2)) AS extended_amount,#(lf)        CAST(j.discount_amount AS decimal(18,2)) AS discount_amount,#(lf)        CAST(j.extended_discounted_amount AS decimal(18,2)) AS extended_discounted_amount,#(lf)        CAST(j.rtn_extended_discounted_amount AS decimal(18,2)) AS rtn_extended_discounted_amount,#(lf)        CAST(j.tax_amount AS decimal(18,2)) AS tax_amount,#(lf)        CAST(j.reason_code_group_id AS varchar(8000)) AS reason_code_group_id,#(lf)        CAST(j.reason_code AS varchar(8000)) AS reason_code,#(lf)        CAST(j.disposition_code AS varchar(8000)) AS disposition_code,#(lf)        CAST(j.gift_receipt AS int) AS gift_receipt,#(lf)        CAST(j.item_returnable AS int) AS item_returnable,#(lf)        CAST(j.item_taxable AS int) AS item_taxable,#(lf)        CAST(j.quantity_avail_for_return AS decimal(18,2)) AS quantity_avail_for_return,#(lf)        CAST(j.item_discountable AS int) AS item_discountable,#(lf)        CAST(j.employee_discount_allowed AS int) AS employee_discount_allowed,#(lf)        CAST(j.item_price_overridable AS int) AS item_price_overridable,#(lf)        CAST(j.discount_applied AS int) AS discount_applied,#(lf)        CAST(j.damage_discount_applied AS int) AS damage_discount_applied,#(lf)        CAST(j.tax_included_in_price AS int) AS tax_included_in_price,#(lf)        CAST(j.tax_group_id AS varchar(8000)) AS tax_group_id,#(lf)        CAST(j.orig_line_sequence_number AS int) AS orig_line_sequence_number,#(lf)        CAST(j.orig_sequence_number AS bigint) AS orig_sequence_number,#(lf)        CAST(j.orig_business_date AS varchar(8000)) AS orig_business_date,#(lf)        CAST(j.orig_device_id AS varchar(8000)) AS orig_device_id,#(lf)        CAST(j.orig_order_id AS varchar(8000)) AS orig_order_id,#(lf)        CAST(j.orig_username AS varchar(8000)) AS orig_username,#(lf)        CAST(j.orig_business_unit_id AS varchar(8000)) AS orig_business_unit_id,#(lf)        CAST(j.return_policy_id AS varchar(8000)) AS return_policy_id,#(lf)        CAST(j.item_returned AS int) AS item_returned,#(lf)        CAST(j.iso_currency_code AS varchar(8)) AS iso_currency_code,#(lf)        CAST(j.tare_weight AS decimal(18,2)) AS tare_weight,#(lf)        CAST(j.item_weight AS decimal(18,2)) AS item_weight,#(lf)        CAST(j.item_weight_plus_tare AS decimal(18,2)) AS item_weight_plus_tare,#(lf)        CAST(j.weight_unit_of_measure AS varchar(8000)) AS weight_unit_of_measure,#(lf)        CAST(j.weight_entry_method_code AS varchar(8000)) AS weight_entry_method_code,#(lf)        CAST(j.family_code AS varchar(8000)) AS family_code,#(lf)        CAST(j.item_length AS decimal(18,2)) AS item_length,#(lf)        CAST(j.length_unit_of_measure AS varchar(8000)) AS length_unit_of_measure,#(lf)        CAST(j.quantity_modifiable AS int) AS quantity_modifiable,#(lf)        CAST(j.save_value AS decimal(18,2)) AS save_value,#(lf)        CAST(j.save_value_type AS varchar(8000)) AS save_value_type,#(lf)        CAST(j.coupon_allowed AS int) AS coupon_allowed,#(lf)        CAST(j.eletronic_coupon_allowed AS int) AS eletronic_coupon_allowed,#(lf)        CAST(j.coupon_multiply_allowed AS int) AS coupon_multiply_allowed,#(lf)        CAST(j.username AS varchar(8000)) AS username,#(lf)        CAST(j.external_system_id AS varchar(8000)) AS external_system_id,#(lf)        CAST(j.product_id AS varchar(8000)) AS product_id,#(lf)        CAST(j.item_name AS varchar(8000)) AS item_name,#(lf)        CAST(j.item_long_description AS varchar(8000)) AS item_long_description,#(lf)        CAST(j.additional_classifiers AS varchar(8000)) AS additional_classifiers,#(lf)        CAST(j.order_line_number AS int) AS order_line_number,#(lf)        CAST(j.order_id AS varchar(8000)) AS order_id,#(lf)        CAST(j.line_item_type AS varchar(8000)) AS line_item_type,#(lf)        CAST(j.inquiry_method_code AS varchar(8000)) AS inquiry_method_code,#(lf)        CAST(j.voided AS int) AS voided,#(lf)        CAST(j.override_user_id AS varchar(8000)) AS override_user_id,#(lf)        CAST(j.entry_method_code AS varchar(8000)) AS entry_method_code,#(lf)        CAST(j.create_time AS datetime2) AS create_time,#(lf)        CAST(j.create_by AS varchar(8000)) AS create_by,#(lf)        CAST(j.last_update_time AS datetime2) AS last_update_time,#(lf)        CAST(j.last_update_by AS varchar(8000)) AS last_update_by,#(lf)        CAST(j.stuff_info AS varchar(8000)) AS stuff_info,#(lf)        CAST(j.find_a_bear_id AS varchar(8000)) AS find_a_bear_id,#(lf)        CAST(j.serialized_coupon_barcode AS varchar(8000)) AS serialized_coupon_barcode,#(lf)        CAST(j.classifier_class AS varchar(8000)) AS classifier_class,#(lf)        CAST(j.classifier_style AS varchar(8000)) AS classifier_style,#(lf)        CAST(j.classifier_brand AS varchar(8000)) AS classifier_brand,#(lf)        CAST(j.classifier_department AS varchar(8000)) AS classifier_department,#(lf)        CAST(j.price_type AS varchar(8000)) AS price_type,#(lf)        CAST(j.list_unit_price AS decimal(18,2)) AS list_unit_price,#(lf)        CAST(j.retail_unit_price AS decimal(18,2)) AS retail_unit_price,#(lf)        CAST(j.item_tax_group_id AS varchar(8000)) AS item_tax_group_id,#(lf)        CAST(j.tax_group_type AS varchar(8000)) AS tax_group_type,#(lf)        CAST(j.tax_exempted AS int) AS tax_exempted,#(lf)        CAST(j.tender_group AS varchar(8000)) AS tender_group,#(lf)        CAST(j.tender_auth_method_code AS varchar(8000)) AS tender_auth_method_code,#(lf)        CAST(j.serial_number AS varchar(8000)) AS serial_number,#(lf)        CAST(j.cart_line_item_uuid AS varchar(8000)) AS cart_line_item_uuid,#(lf)        CAST(j.related_line_sequence_number AS int) AS related_line_sequence_number,#(lf)        CAST(j.epc AS varchar(8000)) AS epc,#(lf)        CAST(j.tax_group_id_modification_type AS varchar(8000)) AS tax_group_id_modification_type,#(lf)        CAST(j.additional_attributes AS varchar(8000)) AS additional_attributes,#(lf)        CONCAT(#(lf)            CAST(j.device_id AS varchar(64)),#(lf)            '-',#(lf)            CONVERT(varchar(10), TRY_CONVERT(date, j.business_date, 112), 120),#(lf)            '-',#(lf)            CAST(j.sequence_number AS varchar(50))#(lf)        ) AS transaction_key,#(lf)        NULL                                                                       AS order_status_id,#(lf)        NULL                                                                       AS order_status_code,#(lf)        NULL                                                                       AS order_status,#(lf)        'POS' AS source#(lf)    FROM dbo.jumpmind_sls_retail_line_item j#(lf)    WHERE TRY_CONVERT(date, j.business_date, 112) >= DATEADD(MONTH, -4, CAST(GETDATE() AS date))#(lf)),#(lf)root AS (#(lf)    SELECT#(lf)        r.OrderID,#(lf)        r.OrderNumber,#(lf)        r.OrderStatus,#(lf)        r.SiteCode,#(lf)        CAST(COALESCE(r.OrderDateUTC, r.DateCreatedUTC) AS date) AS TransDate,#(lf)        r.OrderDateUTC,#(lf)        r.DateCreatedUTC,#(lf)        r.OrderStatusChangeDateUTC#(lf)    FROM dbo.mulesoft_deckjsonraw_root r#(lf)    WHERE CAST(COALESCE(r.OrderDateUTC, r.DateCreatedUTC) AS date) >= DATEADD(MONTH, -4, CAST(GETDATE() AS date))#(lf)),#(lf)site_wh AS (#(lf)    SELECT#(lf)        rt.OrderID,#(lf)        COALESCE(NULLIF(CONVERT(varchar(64), dtt.SiteWarehouseCode), ''),#(lf)                 NULLIF(CONVERT(varchar(64), rt.SiteCode), '')) AS InventLocationId,#(lf)        rt.TransDate,#(lf)        rt.OrderNumber,#(lf)        rt.OrderStatus,#(lf)        rt.SiteCode#(lf)    FROM root rt#(lf)    OUTER APPLY (#(lf)        SELECT TOP (1) dtt.SiteWarehouseCode#(lf)        FROM dbo.mulesoft_dynamicstargettrans dtt#(lf)        WHERE dtt.OrderId = rt.OrderID#(lf)        ORDER BY TRY_CONVERT(datetime2(7), dtt.ExportCreatedUTC) DESC#(lf)    ) dtt#(lf)),#(lf)site_wh_norm AS (#(lf)  SELECT#(lf)    CASE#(lf)      WHEN sw.InventLocationId = 'BAB'   THEN '1013'#(lf)      WHEN sw.InventLocationId = 'BABUK' THEN '2013'#(lf)      WHEN NULLIF(sw.InventLocationId,'') IS NULL THEN '9999'#(lf)      ELSE '9999'#(lf)    END AS InventLocationIdMapped,#(lf)    sw.*#(lf)  FROM site_wh sw#(lf)),#(lf)oms_base AS (#(lf)    SELECT#(lf)        oi.ID AS OI_ID,#(lf)        TRY_CONVERT(bigint, oi.OrderID) AS OI_OrderID,#(lf)        oi.ExternalItemID AS OI_ExternalItemID,#(lf)        oi.Custom1 AS OI_Custom1,#(lf)        oi.StyleNumber AS OI_StyleNumber,#(lf)        oi.ItemTypeID AS OI_ItemTypeID,#(lf)        CASE#(lf)    WHEN oi.ItemTypeID = 2 THEN 'GIFTCARD'#(lf)    WHEN oi.ItemTypeID = 3 THEN 'STOCK'#(lf)    WHEN oi.ItemTypeID = 4 THEN 'STOCK'#(lf)    WHEN oi.ItemTypeID = 5 THEN 'DONATION'#(lf)    WHEN oi.ItemTypeID = 24 THEN 'GIFTCARD'#(lf)    ELSE NULL END AS OI_ItemType,#(lf)        oi.ItemTypeLocalizeName AS OI_ItemTypeLocalizeName,#(lf)        oi.GrossPrice AS OI_GrossPrice,#(lf)        oi.NetPrice AS OI_NetPrice,#(lf)        oi.Returnable AS OI_Returnable,#(lf)        oi.InsertDate AS OI_InsertDate,#(lf)        oi.UpdateDate AS OI_UpdateDate#(lf)    FROM dbo.mulesoft_deckjsonraw_orderitems oi#(lf)),#(lf)oms_with_seq AS (#(lf)    SELECT#(lf)        ob.*,#(lf)        ROW_NUMBER() OVER (#(lf)            PARTITION BY ob.OI_OrderID#(lf)            ORDER BY COALESCE(ob.OI_UpdateDate, ob.OI_InsertDate) ASC, ob.OI_ID#(lf)        ) AS rn_line#(lf)    FROM oms_base ob#(lf)),#(lf)oms_lines AS (#(lf)    SELECT#(lf)        CAST(COALESCE(swn.InventLocationIdMapped, '9999') + '-052' AS varchar(8000)) AS device_id,#(lf)        CONVERT(varchar(8), rt.TransDate, 112) AS business_date,#(lf)        COALESCE(#(lf)            TRY_CONVERT(bigint, rt.OrderNumber),#(lf)            TRY_CONVERT(bigint, rt.OrderID),#(lf)            CAST(ABS(CHECKSUM(CAST(rt.OrderNumber AS nvarchar(4000)))) AS bigint)#(lf)        ) AS sequence_number,#(lf)        CAST(ow.rn_line AS int) AS line_sequence_number,#(lf)        CAST(ow.OI_ExternalItemID AS varchar(8000)) AS pos_item_id,#(lf)        CAST(ow.OI_StyleNumber AS varchar(8000)) AS item_id,#(lf)        CAST(ow.OI_Custom1 AS varchar(8000)) AS item_description,#(lf)#(lf)        CAST(ow.OI_ItemType AS VARCHAR(50)) AS item_type,#(lf)#(lf)        CAST(ow.OI_GrossPrice AS decimal(18,2)) AS regular_unit_price,#(lf)        CAST(ow.OI_NetPrice AS decimal(18,2)) AS actual_unit_price,#(lf)        CAST(NULL AS decimal(18,2)) AS loyalty_unit_price,#(lf)        CAST(1 AS decimal(18,2)) AS quantity,#(lf)        CAST(ow.OI_GrossPrice AS decimal(18,2)) AS extended_amount,#(lf)        CAST(NULLIF(ow.OI_GrossPrice - ow.OI_NetPrice, 0.0) AS decimal(18,2)) AS discount_amount,#(lf)        CAST(ow.OI_NetPrice AS decimal(18,2)) AS extended_discounted_amount,#(lf)        CAST(NULL AS decimal(18,2)) AS rtn_extended_discounted_amount,#(lf)        CAST(oit.Amount AS decimal(18,2)) AS tax_amount,#(lf)        CAST(NULL AS varchar(8000)) AS reason_code_group_id,#(lf)        CAST(NULL AS varchar(8000)) AS reason_code,#(lf)        CAST(NULL AS varchar(8000)) AS disposition_code,#(lf)        CAST(0 AS int) AS gift_receipt,#(lf)        CAST(ow.OI_Returnable AS int) AS item_returnable,#(lf)        CAST(1 AS int) AS item_taxable,#(lf)        CAST(NULL AS decimal(18,2)) AS quantity_avail_for_return,#(lf)        CAST(1 AS int) AS item_discountable,#(lf)        CAST(NULL AS int) AS employee_discount_allowed,#(lf)        CAST(NULL AS int) AS item_price_overridable,#(lf)        CASE WHEN NULLIF(ow.OI_GrossPrice - ow.OI_NetPrice, 0.0) IS NOT NULL THEN 1 ELSE 0 END AS discount_applied,#(lf)        CAST(0 AS int) AS damage_discount_applied,#(lf)        CAST(oit.IsVAT AS int) AS tax_included_in_price,#(lf)        CAST(NULL AS varchar(8000)) AS tax_group_id,#(lf)        CAST(NULL AS int) AS orig_line_sequence_number,#(lf)        CAST(NULL AS bigint) AS orig_sequence_number,#(lf)        CAST(NULL AS varchar(8000)) AS orig_business_date,#(lf)        CAST(NULL AS varchar(8000)) AS orig_device_id,#(lf)        CAST(NULL AS varchar(8000)) AS orig_order_id,#(lf)        CAST(NULL AS varchar(8000)) AS orig_username,#(lf)        CAST(NULL AS varchar(8000)) AS orig_business_unit_id,#(lf)        CAST(NULL AS varchar(8000)) AS return_policy_id,#(lf)        CAST(0 AS int) AS item_returned,#(lf)        CASE WHEN rt.SiteCode = 'BAB' THEN 'USD' ELSE 'GBP' END AS iso_currency_code,#(lf)        CAST(NULL AS decimal(18,2)) AS tare_weight,#(lf)        CAST(NULL AS decimal(18,2)) AS item_weight,#(lf)        CAST(NULL AS decimal(18,2)) AS item_weight_plus_tare,#(lf)        CAST(NULL AS varchar(8000)) AS weight_unit_of_measure,#(lf)        CAST(NULL AS varchar(8000)) AS weight_entry_method_code,#(lf)        CAST(NULL AS varchar(8000)) AS family_code,#(lf)        CAST(NULL AS decimal(18,2)) AS item_length,#(lf)        CAST(NULL AS varchar(8000)) AS length_unit_of_measure,#(lf)        CAST(NULL AS int) AS quantity_modifiable,#(lf)        CAST(NULL AS decimal(18,2)) AS save_value,#(lf)        CAST(NULL AS varchar(8000)) AS save_value_type,#(lf)        CAST(1 AS int) AS coupon_allowed,#(lf)        CAST(NULL AS int) AS eletronic_coupon_allowed,#(lf)        CAST(NULL AS int) AS coupon_multiply_allowed,#(lf)        CAST(NULL AS varchar(8000)) AS username,#(lf)        CAST(NULL AS varchar(8000)) AS external_system_id,#(lf)        CAST(ow.OI_ExternalItemID AS varchar(8000)) AS product_id,#(lf)        CAST(NULL AS varchar(8000)) AS item_name,#(lf)        CAST(NULL AS varchar(8000)) AS item_long_description,#(lf)        CAST(NULL AS varchar(8000)) AS additional_classifiers,#(lf)        CAST(ow.rn_line AS int) AS order_line_number,#(lf)        CAST(ow.OI_OrderID AS varchar(8000)) AS order_id,#(lf)        CAST('Web Sale' AS varchar(8000)) AS line_item_type,#(lf)        CAST(NULL AS varchar(8000)) AS inquiry_method_code,#(lf)        CAST(0 AS int) AS voided,#(lf)        CAST(NULL AS varchar(8000)) AS override_user_id,#(lf)        CAST('WEB' AS varchar(8000)) AS entry_method_code,#(lf)        CAST(rt.DateCreatedUTC AS datetime2) AS create_time,#(lf)        CAST('deckjsonraw' AS varchar(8000)) AS create_by,#(lf)        CAST(rt.OrderStatusChangeDateUTC AS datetime2) AS last_update_time,#(lf)        CAST('deckjsonraw' AS varchar(8000)) AS last_update_by,#(lf)        CAST(NULL AS varchar(8000)) AS stuff_info,#(lf)        CAST(NULL AS varchar(8000)) AS find_a_bear_id,#(lf)        CAST(NULL AS varchar(8000)) AS serialized_coupon_barcode,#(lf)        CAST(NULL AS varchar(8000)) AS classifier_class,#(lf)        CAST(NULL AS varchar(8000)) AS classifier_style,#(lf)        CAST(NULL AS varchar(8000)) AS classifier_brand,#(lf)        CAST(NULL AS varchar(8000)) AS classifier_department,#(lf)        CAST('P' AS varchar(8000)) AS price_type,#(lf)        CAST(NULL AS decimal(18,2)) AS list_unit_price,#(lf)        CAST(NULL AS decimal(18,2)) AS retail_unit_price,#(lf)        CAST(NULL AS varchar(8000)) AS item_tax_group_id,#(lf)        CAST(NULL AS varchar(8000)) AS tax_group_type,#(lf)        CAST(0 AS int) AS tax_exempted,#(lf)        CAST('WEB' AS varchar(8000)) AS tender_group,#(lf)        CAST(NULL AS varchar(8000)) AS tender_auth_method_code,#(lf)        CAST(NULL AS varchar(8000)) AS serial_number,#(lf)        CAST(NULL AS varchar(8000)) AS cart_line_item_uuid,#(lf)        CAST(NULL AS int) AS related_line_sequence_number,#(lf)        CAST(NULL AS varchar(8000)) AS epc,#(lf)        CAST(NULL AS varchar(8000)) AS tax_group_id_modification_type,#(lf)        CAST(NULL AS varchar(8000)) AS additional_attributes,#(lf)        CONCAT(#(lf)            COALESCE(swn.InventLocationIdMapped, '9999'),#(lf)            '-052-',#(lf)            CONVERT(varchar(8), rt.TransDate, 112),#(lf)            '-',#(lf)            CONVERT(varchar(64), rt.OrderNumber)#(lf)        ) AS transaction_key,#(lf)        swn.OrderStatus                                                              AS order_status_id,#(lf)        CASE swn.OrderStatus #(lf)            WHEN 1 THEN 'CO'#(lf)            WHEN 3 THEN 'AVS'#(lf)            WHEN 4 THEN 'P'#(lf)            WHEN 5 THEN 'PV'#(lf)            WHEN 6 THEN 'Z'#(lf)            WHEN 9 THEN 'MR'#(lf)            WHEN 10 THEN 'PS'#(lf)            WHEN 11 THEN 'DAP'#(lf)            WHEN 12 THEN 'CF'#(lf)            ELSE null#(lf)        END                                                                        AS order_status_code,#(lf)        CASE swn.OrderStatus #(lf)            WHEN 1 THEN 'New'#(lf)            WHEN 3 THEN 'Review'#(lf)            WHEN 4 THEN 'Pending'#(lf)            WHEN 5 THEN 'Exception'#(lf)            WHEN 6 THEN 'Completed'#(lf)            WHEN 9 THEN 'Manual Review'#(lf)            WHEN 10 THEN 'Pending Settlement'#(lf)            WHEN 11 THEN 'Delayed Auto-Process'#(lf)            WHEN 12 THEN 'Confirmed Fraud'#(lf)            ELSE null#(lf)        END                                                                        AS order_status,#(lf)        'OMS' AS source#(lf)    FROM oms_with_seq ow#(lf)    JOIN root rt#(lf)      ON ow.OI_OrderID = TRY_CONVERT(bigint, rt.OrderID)#(lf)    JOIN site_wh_norm swn#(lf)      ON swn.OrderID = rt.OrderID#(lf)    LEFT JOIN dbo.mulesoft_deckjsonraw_orderitemtaxes oit#(lf)      ON TRY_CONVERT(bigint, ow.OI_ID) = TRY_CONVERT(bigint, oit._ParentKeyField)#(lf))#(lf)SELECT *#(lf)FROM pos_lines#(lf)UNION ALL#(lf)SELECT *#(lf)FROM oms_lines"]),
    #"Replaced Value" = Table.ReplaceValue(Source,null,0,Replacer.ReplaceValue,{"tax_amount"}),
    #"Filtered Rows | Remove Voided Lines" = Table.SelectRows(#"Replaced Value", each ([voided] = 0)),
    #"Renamed Columns" = Table.RenameColumns(#"Filtered Rows | Remove Voided Lines",{{"actual_unit_price", "Actual Unit Price (Native Currency)"}, {"additional_classifiers", "Additional Classifiers"}, {"business_date", "Business Date"}, {"classifier_brand", "Brand"}, {"classifier_class", "JM Class"}, {"classifier_department", "JM Department"}, {"classifier_style", "Style"}, {"coupon_allowed", "Coupon Allowed"}, {"coupon_multiply_allowed", "Coupon Multiply Allowed"}, {"create_by", "Created By"}, {"create_time", "Created Datetime"}, {"damage_discount_applied", "Damage Discount Applied"}, {"device_id", "Device Id"}, {"discount_amount", "Discount Amount (Native Currency)"}, {"discount_applied", "Discount Applied"}, {"disposition_code", "Disposition Code"}, {"eletronic_coupon_allowed", "Electronic Coupon Allowed"}, {"employee_discount_allowed", "Employee Discount Allowed"}, {"extended_amount", "Regular Sales Amount (Native Currency)"}, {"entry_method_code", "Entry Method Code"}, {"extended_discounted_amount", "Actual Sales Amount (Native Currency)"}, {"external_system_id", "External System Id"}, {"family_code", "Family Code"}, {"find_a_bear_id", "Find A Bear Id"}, {"gift_receipt", "Gift Receipt"}, {"inquiry_method_code", "Inquiry Method Code"}, {"iso_currency_code", "ISO Currency Code"}, {"item_description", "Item Description"}, {"item_discountable", "Item Discountable"}, {"item_id", "Item Id"}, {"item_length", "Item Length"}, {"item_long_description", "Item Long Description"}, {"item_name", "Item Name"}, {"item_price_overridable", "Item Price Overridable"}, {"item_returnable", "Item Returnable"}, {"item_returned", "Item Returned"}, {"item_taxable", "Item Taxable"}, {"item_type", "Item Type"}, {"item_weight", "Item Weight"}, {"item_weight_plus_tare", "Item Weight Plus Tare"}, {"last_update_by", "Last Updated By"}, {"last_update_time", "Last Updated Datetime"}, {"length_unit_of_measure", "Length Unit of Measure"}, {"line_item_type", "Line Item Type"}, {"line_sequence_number", "Line Sequence Number"}, {"loyalty_unit_price", "Loyalty Unit Price (Native Currency)"}, {"order_id", "Order Id"}, {"order_line_number", "Order Line Number"}, {"orig_business_date", "Orig_Business Date"}, {"orig_business_unit_id", "Orig_Business Unit Id"}, {"orig_device_id", "Orig_Device Id"}, {"orig_line_sequence_number", "Orig_Line Sequence Number"}, {"orig_order_id", "Orig_Order Id"}, {"orig_sequence_number", "Orig_Sequence Number"}, {"orig_username", "Orig_Username"}, {"override_user_id", "Override User Id"}, {"pos_item_id", "POS Item Id"}, {"product_id", "Product Id"}, {"quantity", "Quantity"}, {"quantity_avail_for_return", "Quantity Available for Return"}, {"quantity_modifiable", "Quantity Modifiable"}, {"reason_code", "Reason Code"}, {"reason_code_group_id", "Reason Code Group Id"}, {"regular_unit_price", "Regular Unit Price (Native Currency)"}, {"return_policy_id", "Return Policy Id"}, {"rtn_extended_discounted_amount", "Return Value Amount (Native Currency)"}, {"save_value", "Save Value"}, {"save_value_type", "Save Value Type"}, {"sequence_number", "Sequence Number"}, {"serialized_coupon_barcode", "Serialized Coupon Barcode"}, {"stuff_info", "Stuff Info"}, {"tare_weight", "Tare Weight"}, {"tax_amount", "Tax Amount (Native Currency)"}, {"tax_group_id", "Tax Group Id"}, {"tax_included_in_price", "Tax Included in Price"}, {"username", "Username"}, {"voided", "Voided"}, {"weight_entry_method_code", "Weight Entry Method Code"}, {"weight_unit_of_measure", "Weight Unit of Measure"}}),
    #"Removed Columns | Redundant Columns" = Table.RemoveColumns(#"Renamed Columns",{"tender_auth_method_code", "Created By", "Created Datetime", "Last Updated By"}),
    #"Removed Columns | Empty Columns" = Table.RemoveColumns(#"Removed Columns | Redundant Columns",{"Additional Classifiers", "Brand", "Family Code", "External System Id", "Loyalty Unit Price (Native Currency)", "Style", "JM Class", "JM Department", "Item Length", "Length Unit of Measure", "Item Weight", "Weight Entry Method Code", "Weight Unit of Measure", "Tare Weight", "Save Value Type", "Save Value", "Disposition Code"}),
    #"Merged Columns | Transaction Key" = Table.CombineColumns(Table.TransformColumnTypes(#"Removed Columns | Empty Columns", {{"Sequence Number", type text}}, "en-US"),{"Device Id", "Business Date", "Sequence Number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Transaction Key"),
    #"Added Custom | Transaction Line Key" = Table.AddColumn(#"Merged Columns | Transaction Key", "Transaction Line Key", each [Transaction Key] & "-" & Text.From([Line Sequence Number])),
    #"Added Conditional Column | Endless Aisle" = Table.AddColumn(#"Added Custom | Transaction Line Key", "Endless Aisle", each if [Line Item Type] = "STORE_SALE" then false else if [Line Item Type] = "ORDER_IN_STORE" then true else null),
    #"Added Custom | Item Key" = Table.AddColumn(#"Added Conditional Column | Endless Aisle", "Item Key", each [ISO Currency Code] & [Item Id]),
    #"Added Custom | Item Line" = Table.AddColumn(#"Added Custom | Item Key", "Item Line", each [Item Id] & " - " & [Item Description]),
    #"Added Custom | Actual Sales Amount TE" = Table.AddColumn(#"Added Custom | Item Line", "Actual Sales Amount TE (Native Currency)", each if [#"ISO Currency Code"] = "GBP" or [#"ISO Currency Code"] = "EUR" then (Number.Abs([#"Actual Sales Amount (Native Currency)"]) - Number.Abs([#"Tax Amount (Native Currency)"])) * Number.Sign([#"Quantity"]) else [#"Actual Sales Amount (Native Currency)"]),
    #"Added Custom | Tax Percentage" = Table.AddColumn(#"Added Custom | Actual Sales Amount TE", "Tax Percentage", each if [#"Actual Sales Amount TE (Native Currency)"] <> 0
then ([#"Tax Amount (Native Currency)"] / [#"Actual Sales Amount TE (Native Currency)"])
else 0),
    #"Added Custom | Discount Amount TE" = Table.AddColumn(#"Added Custom | Tax Percentage", "Discount Amount TE (Native Currency)", each if [#"ISO Currency Code"] = "GBP" or [#"ISO Currency Code"] = "EUR" then (Number.Abs([#"Discount Amount (Native Currency)"]) - (Number.Abs([#"Discount Amount (Native Currency)"])*[Tax Percentage])) * Number.Sign([#"Quantity"]) else [#"Discount Amount (Native Currency)"]),
    #"Replace nulls With 0 | Discount Amount TE" = Table.ReplaceValue(#"Added Custom | Discount Amount TE",null,0,Replacer.ReplaceValue,{"Discount Amount TE (Native Currency)"}),
    #"Added Custom | Regular Sales Amount TE" = Table.AddColumn(#"Replace nulls With 0 | Discount Amount TE", "Regular Sales Amount TE (Native Currency)", each if [ISO Currency Code] = "GBP" or [ISO Currency Code] = "EUR" then (Number.Abs([#"Actual Sales Amount (Native Currency)"]) - Number.Abs([#"Tax Amount (Native Currency)"]) + Number.Abs([#"Discount Amount TE (Native Currency)"])) * Number.Sign([#"Quantity"]) else [#"Regular Sales Amount (Native Currency)"]),
    #"Added Custom | Actual Unit Price TE" = Table.AddColumn(#"Added Custom | Regular Sales Amount TE", "Actual Unit Price TE (Native Currency)", each [#"Actual Sales Amount TE (Native Currency)"] / [Quantity]),
    #"Added Custom | Regular Unit Price TE" = Table.AddColumn(#"Added Custom | Actual Unit Price TE", "Regular Unit Price TE (Native Currency)", each [#"Regular Sales Amount TE (Native Currency)"] / [Quantity]),
    #"Added Custom | Discount Amount Per Unit TE" = Table.AddColumn(#"Added Custom | Regular Unit Price TE", "Discount Amount Per Unit TE (Native Currency)", each [#"Discount Amount TE (Native Currency)"] / [Quantity] * Number.Sign([#"Quantity"])),
    #"Added Custom | Item Line (SKU5)" = Table.AddColumn(#"Added Custom | Discount Amount Per Unit TE", "Item Line (SKU5)", each Text.End([Item Id],5) & " - " & [Item Description]),
    #"Added Custom | Total Tender Amount (Native Currency)" = Table.AddColumn(#"Added Custom | Item Line (SKU5)", "Total Tender Amount (Native Currency)", each if [tax_exempted] = 1 
        then [#"Actual Sales Amount TE (Native Currency)"]
        else [#"Actual Sales Amount TE (Native Currency)"] + [#"Tax Amount (Native Currency)"]),
    #"Changed Type" = Table.TransformColumnTypes(#"Added Custom | Total Tender Amount (Native Currency)",{{"Coupon Multiply Allowed", type logical}, {"Electronic Coupon Allowed", type logical}, {"Coupon Allowed", type logical}, {"Quantity Modifiable", type logical}, {"Item Returned", type logical}, {"Item Price Overridable", type logical}, {"Discount Applied", type logical}, {"Damage Discount Applied", type logical}, {"Tax Included in Price", type logical}, {"Item Returnable", type logical}, {"Item Taxable", type logical}, {"Item Discountable", type logical}, {"Employee Discount Allowed", type logical}, {"Gift Receipt", type logical}, {"Endless Aisle", type logical}, {"Actual Unit Price TE (Native Currency)", type number}, {"Actual Sales Amount TE (Native Currency)", type number}, {"Quantity", Int64.Type}, {"Voided", type logical}, {"Transaction Line Key", type text}, {"Item Line", type text}, {"Regular Unit Price TE (Native Currency)", type number}, {"Regular Sales Amount TE (Native Currency)", type number}, {"Discount Amount Per Unit TE (Native Currency)", type number}, {"Item Line (SKU5)", type text}, {"Item Key", type text}, {"Tax Percentage", Percentage.Type}, {"Discount Amount TE (Native Currency)", type number}, {"Total Tender Amount (Native Currency)", type number}}),
    #"Replaced Errors" = Table.ReplaceErrorValues(#"Changed Type", {{"Tax Percentage", null}}),
    #"Replaced Value | _ with SPACE" = Table.ReplaceValue(#"Replaced Errors","_"," ",Replacer.ReplaceText,{"Item Type", "Line Item Type", "Inquiry Method Code", "Entry Method Code"}),
    #"Replaced Value | GIFTCARD with GIFT CARD" = Table.ReplaceValue(#"Replaced Value | _ with SPACE","GIFTCARD","GIFT CARD",Replacer.ReplaceText,{"Item Type"}),
    #"Replaced Value | loyalty with loyaltySPACE" = Table.ReplaceValue(#"Replaced Value | GIFTCARD with GIFT CARD","loyalty","loyalty ",Replacer.ReplaceText,{"Return Policy Id"}),
    #"Replaced Value | nonreceipted with non-Receipted" = Table.ReplaceValue(#"Replaced Value | loyalty with loyaltySPACE","nonreceipted","non-Receipted",Replacer.ReplaceText,{"Return Policy Id"}),
    #"Replaced Value | returns with returnsSPACE" = Table.ReplaceValue(#"Replaced Value | nonreceipted with non-Receipted","returns","returns ",Replacer.ReplaceText,{"Return Policy Id"}),
    #"Replaced Value | orders with ordersSPACE" = Table.ReplaceValue(#"Replaced Value | returns with returnsSPACE","orders","orders ",Replacer.ReplaceText,{"Return Policy Id"}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Replaced Value | orders with ordersSPACE",{{"Item Type", Text.Proper, type text}, {"Line Item Type", Text.Proper, type text}, {"Return Policy Id", Text.Proper, type text}, {"Inquiry Method Code", Text.Proper, type text}, {"Entry Method Code", Text.Proper, type text}}),
    #"Reordered Columns" = Table.ReorderColumns(#"Capitalized Each Word",{"Transaction Key", "Transaction Line Key", "Line Item Type", "Item Type", "Voided", "POS Item Id", "Item Id", "Item Description", "Item Long Description", "Item Name", "Item Line", "ISO Currency Code", "Quantity", "Regular Unit Price (Native Currency)", "Regular Unit Price TE (Native Currency)", "Regular Sales Amount (Native Currency)", "Regular Sales Amount TE (Native Currency)", "Discount Amount (Native Currency)", "Discount Amount TE (Native Currency)", "Discount Amount Per Unit TE (Native Currency)", "Tax Amount (Native Currency)", "Tax Percentage", "Actual Unit Price (Native Currency)", "Actual Unit Price TE (Native Currency)", "Actual Sales Amount (Native Currency)", "Actual Sales Amount TE (Native Currency)", "Item Taxable", "Tax Group Id", "Tax Included in Price", "Endless Aisle", "Order Id", "Order Line Number", "Item Price Overridable", "Coupon Allowed", "Coupon Multiply Allowed", "Electronic Coupon Allowed", "Serialized Coupon Barcode", "Item Discountable", "Item Weight Plus Tare", "Damage Discount Applied", "Discount Applied", "Employee Discount Allowed", "Find A Bear Id", "Gift Receipt", "Product Id", "Stuff Info", "Quantity Modifiable", "Item Returnable", "Item Returned", "Quantity Available for Return", "Return Policy Id", "Return Value Amount (Native Currency)", "Reason Code Group Id", "Reason Code", "Inquiry Method Code", "Entry Method Code", "Orig_Business Date", "price_type", "list_unit_price", "retail_unit_price", "item_tax_group_id", "tax_group_type", "tax_exempted", "tender_group", "serial_number", "cart_line_item_uuid", "related_line_sequence_number", "Orig_Business Unit Id", "Orig_Device Id", "Orig_Line Sequence Number", "Orig_Order Id", "Orig_Sequence Number", "Orig_Username", "Line Sequence Number", "Username", "Override User Id", "Item Key", "Item Line (SKU5)"}),
    #"Removed Duplicates" = Table.Distinct(#"Reordered Columns", {"Transaction Line Key"})
in
    #"Removed Duplicates"
```

### Retail Return Lines (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH pos_ret_raw AS (#(lf)  SELECT#(lf)      j.device_id,#(lf)      TRY_CONVERT(date, j.business_date, 112)      AS j_bd,#(lf)      j.sequence_number,#(lf)      j.line_sequence_number,#(lf)      j.rtn_event_type_code,#(lf)      j.rtn_rejection_code,#(lf)      j.pos_item_id,#(lf)      j.item_id,#(lf)      j.entry_mode_code,#(lf)      j.orig_line_sequence_number,#(lf)      j.orig_sequence_number,#(lf)      TRY_CONVERT(date, j.orig_business_date, 112) AS j_orig_bd,#(lf)      j.orig_device_id,#(lf)      j.orig_order_id,#(lf)      j.rtn_policy_id,#(lf)      j.voided,#(lf)      j.override_user_id,#(lf)      j.entry_method_code,#(lf)      j.create_time#(lf)  FROM dbo.jumpmind_sls_rtn_event_line_item j#(lf)),#(lf)st_parsed AS (#(lf)  SELECT#(lf)      st.device_id,#(lf)      TRY_CONVERT(date, st.business_date, 112) AS st_bd,#(lf)      st.sequence_number,#(lf)      st.training_mode,#(lf)      st.trans_status#(lf)  FROM dbo.jumpmind_sls_trans st#(lf)),#(lf)pos_ret AS (#(lf)  SELECT#(lf)      CAST(r.device_id AS varchar(64))                               AS device_id,#(lf)      CONVERT(varchar(8), r.j_bd, 112)                               AS business_date,#(lf)      CAST(r.sequence_number AS bigint)                              AS sequence_number,#(lf)      CAST(r.line_sequence_number AS int)                            AS line_sequence_number,#(lf)      CAST(r.rtn_event_type_code AS varchar(64))                     AS rtn_event_type_code,#(lf)      CAST(r.rtn_rejection_code AS varchar(256))                     AS rtn_rejection_code,#(lf)      CAST(r.pos_item_id AS varchar(64))                             AS pos_item_id,#(lf)      CAST(r.item_id AS varchar(64))                                 AS item_id,#(lf)      CAST(r.entry_mode_code AS varchar(32))                         AS entry_mode_code,#(lf)      CAST(r.orig_line_sequence_number AS int)                       AS orig_line_sequence_number,#(lf)      CAST(r.orig_sequence_number AS bigint)                         AS orig_sequence_number,#(lf)      CASE WHEN r.j_orig_bd IS NULL THEN NULL#(lf)           ELSE CONVERT(varchar(8), r.j_orig_bd, 112) END            AS orig_business_date,#(lf)      CAST(r.orig_device_id AS varchar(64))                          AS orig_device_id,#(lf)      CAST(r.orig_order_id AS varchar(64))                           AS orig_order_id,#(lf)      CAST(r.rtn_policy_id AS varchar(64))                           AS rtn_policy_id,#(lf)      CAST(r.voided AS bit)                                          AS voided,#(lf)      CAST(r.override_user_id AS varchar(64))                        AS override_user_id,#(lf)      CAST(r.entry_method_code AS varchar(32))                       AS entry_method_code,#(lf)      CAST(r.create_time AS datetime2)                               AS create_time,#(lf)      CAST('openpos-sls' AS varchar(64))                             AS create_by,#(lf)      CAST(NULL AS datetime2)                                        AS last_update_time,#(lf)      CAST(NULL AS varchar(64))                                      AS last_update_by,#(lf)      NULL                                                           AS order_status_id,#(lf)      NULL                                                           AS order_status_code,#(lf)      NULL                                                           AS order_status,#(lf)      CAST('POS' AS varchar(8))                                      AS source#(lf)  FROM pos_ret_raw r#(lf)  JOIN st_parsed s#(lf)    ON s.device_id = r.device_id#(lf)   AND s.sequence_number = r.sequence_number#(lf)   AND s.st_bd = r.j_bd#(lf)  WHERE s.training_mode = 0#(lf)    AND s.trans_status = 'COMPLETED'#(lf)    AND s.st_bd >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 4 MONTHS, using parsed date#(lf)    AND r.j_bd IS NOT NULL#(lf)),#(lf)oms_items AS (#(lf)  SELECT#(lf)      TRY_CONVERT(int, oi._ParentKeyField) AS ParentOrderID,#(lf)      CAST(oi.ID AS varchar(64))           AS OI_ID,#(lf)      CAST(oi._RowIndex AS int)            AS RowIndex,#(lf)      oi.ReturnTypeID, oi.ReturnReasonID,#(lf)      CAST(oi.ReturnReasonText AS varchar(256)) AS ReturnReasonText,#(lf)      CAST(oi.ItemStatusName AS varchar(128))   AS ItemStatusName,#(lf)      CAST(oi.ItemStatusCode AS varchar(64))    AS ItemStatusCode,#(lf)      TRY_CONVERT(bigint, oi.ExternalItemID)    AS ExternalItemID_bigint,#(lf)      TRY_CONVERT(bigint, oi.OrderID)           AS OrderID_bigint,#(lf)      CAST(oi.DeckSKU AS varchar(64))           AS DeckSKU,#(lf)      CAST(oi.GTIN AS varchar(64))              AS GTIN,#(lf)      CAST(oi.WarehouseCode AS varchar(64))     AS WarehouseCode,#(lf)      oi.InsertDate, oi.UpdateDate#(lf)  FROM dbo.mulesoft_deckjsonraw_orderitems oi#(lf)  WHERE TRY_CONVERT(int, oi._ParentKeyField) IS NOT NULL#(lf)),#(lf)oms_join AS (#(lf)  SELECT#(lf)      r.OrderID, r.OrderNumber, r.OrderStatus, r.SiteCode,#(lf)      CAST(COALESCE(r.OrderDateUTC, r.DateCreatedUTC) AS date) AS TransDate,#(lf)      COALESCE(i.UpdateDate, r.UpdateDate, r.OrderDateUTC, r.DateCreatedUTC, i.InsertDate) AS LastUpd,#(lf)      i.RowIndex, i.ReturnTypeID, i.ReturnReasonID, i.ReturnReasonText,#(lf)      i.ItemStatusName, i.ItemStatusCode, i.ExternalItemID_bigint, i.OrderID_bigint, i.DeckSKU, i.GTIN, i.WarehouseCode#(lf)  FROM oms_items i#(lf)  JOIN dbo.mulesoft_deckjsonraw_root r#(lf)    ON r.OrderID = i.ParentOrderID#(lf)  WHERE CAST(COALESCE(r.OrderDateUTC, r.DateCreatedUTC) AS date)#(lf)        >= DATEADD(month, -4, CAST(GETDATE() AS date))   -- 2 MONTHS#(lf)),#(lf)oms_ret AS (#(lf)  SELECT#(lf)      CAST(COALESCE(#(lf)              CASE WHEN swh.SiteWarehouseCode = 'BAB'   THEN '1013'#(lf)                   WHEN swh.SiteWarehouseCode = 'BABUK' THEN '2013'#(lf)              END,#(lf)              CASE WHEN j.SiteCode = 'BAB'   THEN '1013'#(lf)                   WHEN j.SiteCode = 'BABUK' THEN '2013'#(lf)              END,#(lf)              '9999') + '-052' AS varchar(64))          AS device_id,#(lf)      CONVERT(varchar(8), j.TransDate, 112)             AS business_date,#(lf)      CAST(j.OrderID AS bigint)                         AS sequence_number,#(lf)      CAST(COALESCE(j.RowIndex, 1) AS int)              AS line_sequence_number,#(lf)      CAST(CASE#(lf)            WHEN j.ReturnTypeID IS NOT NULL THEN 'RETURN'#(lf)            WHEN j.ItemStatusName IN ('Returned','Refund','Return Authorized') THEN 'RETURN'#(lf)            WHEN j.ItemStatusCode IN ('RET','RFND','RAUTH') THEN 'RETURN'#(lf)            ELSE 'ORDER_ITEM'#(lf)          END AS varchar(64))                           AS rtn_event_type_code,#(lf)      CAST(j.ReturnReasonText AS varchar(256))          AS rtn_rejection_code,#(lf)      CAST(NULL AS varchar(64))                         AS pos_item_id,#(lf)      CONVERT(varchar(64), j.ExternalItemID_bigint)     AS item_id,#(lf)      CAST(NULL AS varchar(32))                         AS entry_mode_code,#(lf)      CAST(NULL AS int)                                 AS orig_line_sequence_number,#(lf)      CAST(NULL AS bigint)                              AS orig_sequence_number,#(lf)      CAST(NULL AS varchar(8))                          AS orig_business_date,#(lf)      CAST(NULL AS varchar(64))                         AS orig_device_id,#(lf)      CAST(NULL AS varchar(64))                         AS orig_order_id,#(lf)      CAST(NULL AS varchar(64))                         AS rtn_policy_id,#(lf)      CAST(0 AS bit)                                    AS voided,#(lf)      CAST(NULL AS varchar(64))                         AS override_user_id,#(lf)      CAST(NULL AS varchar(32))                         AS entry_method_code,#(lf)      CAST(j.LastUpd AS datetime2)                      AS create_time,#(lf)      CAST('openpos-sls' AS varchar(64))                AS create_by,#(lf)      CAST(NULL AS datetime2)                           AS last_update_time,#(lf)      CAST(NULL AS varchar(64))                         AS last_update_by,#(lf)      j.OrderStatus                                                              AS order_status_id,#(lf)        CASE j.OrderStatus #(lf)            WHEN 1 THEN 'CO'#(lf)            WHEN 3 THEN 'AVS'#(lf)            WHEN 4 THEN 'P'#(lf)            WHEN 5 THEN 'PV'#(lf)            WHEN 6 THEN 'Z'#(lf)            WHEN 9 THEN 'MR'#(lf)            WHEN 10 THEN 'PS'#(lf)            WHEN 11 THEN 'DAP'#(lf)            WHEN 12 THEN 'CF'#(lf)            ELSE null#(lf)        END                                                                        AS order_status_code,#(lf)        CASE j.OrderStatus #(lf)            WHEN 1 THEN 'New'#(lf)            WHEN 3 THEN 'Review'#(lf)            WHEN 4 THEN 'Pending'#(lf)            WHEN 5 THEN 'Exception'#(lf)            WHEN 6 THEN 'Completed'#(lf)            WHEN 9 THEN 'Manual Review'#(lf)            WHEN 10 THEN 'Pending Settlement'#(lf)            WHEN 11 THEN 'Delayed Auto-Process'#(lf)            WHEN 12 THEN 'Confirmed Fraud'#(lf)            ELSE null#(lf)        END                                                                        AS order_status,#(lf)      CAST('OMS' AS varchar(8))                         AS source#(lf)  FROM oms_join j#(lf)  OUTER APPLY (#(lf)    SELECT TOP (1) dtt.SiteWarehouseCode#(lf)    FROM dbo.mulesoft_dynamicstargettrans dtt#(lf)    WHERE dtt.OrderId = j.OrderID#(lf)    ORDER BY TRY_CONVERT(datetime2(7), dtt.ExportCreatedUTC) DESC#(lf)  ) swh#(lf))#(lf)SELECT * FROM pos_ret#(lf)UNION ALL#(lf)SELECT * FROM oms_ret;"]),
    #"Changed Type" = Table.TransformColumnTypes(Source,{{"voided", type logical}}),
    #"Renamed Columns" = Table.RenameColumns(#"Changed Type",{{"business_date", "Business Date"}, {"create_by", "Created By"}, {"create_time", "Created Datetime"}, {"device_id", "Device Id"}, {"entry_method_code", "Entry Method Code"}, {"entry_mode_code", "Entry Mode Code"}, {"item_id", "Item Id"}, {"last_update_by", "Last Updated By"}, {"last_update_time", "Last Updated Datetime"}, {"line_sequence_number", "Line Sequence Number"}, {"orig_business_date", "Original Business Date"}, {"orig_device_id", "Original Device Id"}, {"orig_line_sequence_number", "Original Line Sequence Number"}, {"orig_order_id", "Original Order Id"}, {"orig_sequence_number", "Original Sequence Number"}, {"override_user_id", "Override User Id"}, {"pos_item_id", "POS Item Id"}, {"rtn_event_type_code", "Return Event Type Code"}, {"rtn_policy_id", "Return Policy Id"}, {"rtn_rejection_code", "Return Rejection Code"}, {"sequence_number", "Sequence Number"}, {"voided", "Voided"}}),
    #"Removed Columns | Redundant Columns" = Table.RemoveColumns(#"Renamed Columns",{"Created Datetime", "Created By", "Last Updated By"}),
    #"Merged Columns | Transaction Key" = Table.CombineColumns(Table.TransformColumnTypes(#"Removed Columns | Redundant Columns", {{"Sequence Number", type text}}, "en-US"),{"Device Id", "Business Date", "Sequence Number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Transaction Key"),
    #"Replaced Value | receipted with SPACEreceipted" = Table.ReplaceValue(#"Merged Columns | Transaction Key","receipted"," receipted",Replacer.ReplaceText,{"Return Policy Id"}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Replaced Value | receipted with SPACEreceipted",{{"Return Policy Id", Text.Proper, type text}, {"Entry Method Code", Text.Proper, type text}}),
    #"Replaced Value | nonSPACE with SPACENon-" = Table.ReplaceValue(#"Capitalized Each Word","non "," Non-",Replacer.ReplaceText,{"Return Policy Id"})
in
    #"Replaced Value | nonSPACE with SPACENon-"
```

### Retail Transaction Discounts (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH jumpmind_retail_transaction_discounts AS (#(lf)    SELECT#(lf)        CAST(j.device_id AS varchar(64))                                         AS device_id,#(lf)        CONVERT(varchar(8), TRY_CONVERT(date, j.business_date, 112), 112)        AS business_date,#(lf)        CAST(j.sequence_number AS bigint)                                        AS sequence_number,#(lf)        CAST(j.line_sequence_number AS int)                                      AS line_sequence_number,#(lf)        CAST(j.mod_line_sequence_number AS int)                                  AS mod_line_sequence_number,#(lf)        CAST(j.username AS varchar(128))                                         AS username,#(lf)        CAST(j.reason_code AS varchar(64))                                       AS reason_code,#(lf)        CAST(NULL AS numeric(18,2))                                              AS mod_by_percentage,#(lf)        CAST(NULL AS numeric(18,2))                                              AS mod_by_amount,#(lf)        CAST(j.rounding_amount AS numeric(18,2))                                 AS rounding_amount,#(lf)        CAST(j.calc_method AS varchar(32))                                       AS calc_method,#(lf)        CAST(j.iso_currency_code AS varchar(8))                                  AS iso_currency_code,#(lf)        CAST(j.price_mod_type_code AS varchar(16))                               AS price_mod_type_code,#(lf)        CAST(j.price_mod_source_type_code AS varchar(16))                        AS price_mod_source_type_code,#(lf)        CAST(j.voided AS bit)                                                    AS voided,#(lf)        CAST(j.override_user_id AS varchar(64))                                  AS override_user_id,#(lf)        CAST(j.entry_method_code AS varchar(64))                                 AS entry_method_code,#(lf)        CAST(j.last_update_time AS datetime2)                                    AS create_time,#(lf)        CAST('openpos-sls' AS varchar(64))                                       AS create_by,#(lf)        CAST(j.last_update_time AS datetime2)                                    AS last_update_time,#(lf)        CAST('openpos-sls' AS varchar(64))                                       AS last_update_by,#(lf)        NULL                                                                     AS order_status_id,#(lf)        NULL                                                                     AS order_status_code,#(lf)        NULL                                                                     AS order_status#(lf)    FROM dbo.jumpmind_sls_retail_trans_price_mod j#(lf)    WHERE TRY_CONVERT(date, j.business_date, 112) >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 4 months#(lf)),#(lf)hs AS (#(lf)    SELECT#(lf)        COALESCE(#(lf)          NULLIF(CONVERT(varchar(64), dtt.MaxWarehouseCode), ''),#(lf)          NULLIF(CONVERT(varchar(64), dtt.SiteWarehouseCode), ''),#(lf)          NULLIF(CONVERT(varchar(64), r.SiteCode), '')#(lf)        )                                    AS InventLocationId,#(lf)        CAST(COALESCE(r.OrderDateUTC, r.DateCreatedUTC, r.OrderStatusChangeDateUTC, r.ExportCreatedUTC) AS date)#(lf)                                              AS TransDate,#(lf)        CONVERT(varchar(64), r.OrderNumber)  AS Barcode,#(lf)        r.OrderID,#(lf)        r._RowIndex,#(lf)        r.OrderStatus#(lf)    FROM dbo.mulesoft_deckjsonraw_root r#(lf)    LEFT JOIN dbo.mulesoft_dynamicstargettrans dtt#(lf)      ON CONVERT(varchar(64), dtt.OrderId) = CONVERT(varchar(64), r.OrderID)#(lf)    WHERE CAST(COALESCE(r.OrderDateUTC, r.DateCreatedUTC, r.OrderStatusChangeDateUTC, r.ExportCreatedUTC) AS date)#(lf)          >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 2 months#(lf)),#(lf)deck_adjustments AS (#(lf)    SELECT#(lf)        a._ParentKeyField                              AS OrderID_key,#(lf)        a.OrderTransactionIdentifier                   AS RootRowIndex,#(lf)        a.AdjustmentDate,#(lf)        a.AdjustmentTypeValue#(lf)    FROM dbo.mulesoft_deckjsonraw_orderadjustments a#(lf)    WHERE a.AdjustmentDate >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 2 months#(lf))#(lf)SELECT#(lf)    device_id,#(lf)    business_date,#(lf)    sequence_number,#(lf)    line_sequence_number,#(lf)    mod_line_sequence_number,#(lf)    username,#(lf)    reason_code,#(lf)    mod_by_percentage,#(lf)    mod_by_amount,#(lf)    rounding_amount,#(lf)    calc_method,#(lf)    iso_currency_code,#(lf)    price_mod_type_code,#(lf)    price_mod_source_type_code,#(lf)    voided,#(lf)    override_user_id,#(lf)    entry_method_code,#(lf)    create_time,#(lf)    create_by,#(lf)    last_update_time,#(lf)    last_update_by,#(lf)    order_status_id,#(lf)    order_status_code,#(lf)    order_status#(lf)FROM jumpmind_retail_transaction_discounts#(lf)#(lf)UNION ALL#(lf)#(lf)SELECT#(lf)    CAST('WEB' AS varchar(64))                                                                AS device_id,#(lf)    CONVERT(varchar(8), hs.TransDate, 112)                                                    AS business_date,#(lf)    TRY_CONVERT(bigint, da.OrderID_key)                                                       AS sequence_number,#(lf)    CAST(0 AS int)                                                                            AS line_sequence_number,#(lf)    CAST(1 AS int)                                                                            AS mod_line_sequence_number,#(lf)    CAST(NULL AS varchar(128))                                                                AS username,#(lf)    CAST(NULL AS varchar(64))                                                                 AS reason_code,#(lf)    CAST(NULL AS numeric(18,2))                                                               AS mod_by_percentage,#(lf)    CAST(NULL AS numeric(18,2))                                                               AS mod_by_amount,#(lf)    CAST(NULL AS numeric(18,2))                                                               AS rounding_amount,#(lf)    CAST('AMOUNT' AS varchar(32))                                                             AS calc_method,#(lf)    CASE#(lf)        WHEN hs.InventLocationId LIKE 'BAB%' THEN 'USD'#(lf)        WHEN hs.InventLocationId LIKE 'UK%'  THEN 'GBP'#(lf)        ELSE NULL#(lf)    END                                                                                       AS iso_currency_code,#(lf)    CAST('TRANS' AS varchar(16))                                                              AS price_mod_type_code,#(lf)    CAST(CASE WHEN da.AdjustmentTypeValue LIKE '%Manual%' THEN 'MANUAL' END AS varchar(16))  AS price_mod_source_type_code,#(lf)    CAST(0 AS bit)                                                                            AS voided,#(lf)    CAST(NULL AS varchar(64))                                                                 AS override_user_id,#(lf)    CAST(NULL AS varchar(64))                                                                 AS entry_method_code,#(lf)    CAST(da.AdjustmentDate AS datetime2)                                                      AS create_time,#(lf)    CAST('deckjsonraw' AS varchar(64))                                                        AS create_by,#(lf)    CAST(da.AdjustmentDate AS datetime2)                                                      AS last_update_time,#(lf)    CAST('deckjsonraw' AS varchar(64))                                                        AS last_update_by,#(lf)    hs.OrderStatus                                                                            AS order_status_id,#(lf)        CASE hs.OrderStatus #(lf)            WHEN 1 THEN 'CO'#(lf)            WHEN 3 THEN 'AVS'#(lf)            WHEN 4 THEN 'P'#(lf)            WHEN 5 THEN 'PV'#(lf)            WHEN 6 THEN 'Z'#(lf)            WHEN 9 THEN 'MR'#(lf)            WHEN 10 THEN 'PS'#(lf)            WHEN 11 THEN 'DAP'#(lf)            WHEN 12 THEN 'CF'#(lf)            ELSE null#(lf)        END                                                                                    AS order_status_code,#(lf)        CASE hs.OrderStatus #(lf)            WHEN 1 THEN 'New'#(lf)            WHEN 3 THEN 'Review'#(lf)            WHEN 4 THEN 'Pending'#(lf)            WHEN 5 THEN 'Exception'#(lf)            WHEN 6 THEN 'Completed'#(lf)            WHEN 9 THEN 'Manual Review'#(lf)            WHEN 10 THEN 'Pending Settlement'#(lf)            WHEN 11 THEN 'Delayed Auto-Process'#(lf)            WHEN 12 THEN 'Confirmed Fraud'#(lf)            ELSE null#(lf)        END                                                                                     AS order_status#(lf)FROM deck_adjustments da#(lf)JOIN hs#(lf)  ON CONVERT(varchar(64), hs.OrderID) = CONVERT(varchar(64), da.OrderID_key)#(lf) AND hs._RowIndex = da.RootRowIndex;"]),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"business_date", "Business Date"}, {"calc_method", "Calculation Method"}, {"create_by", "Created By"}, {"create_time", "Created Datetime"}, {"device_id", "Device Id"}, {"entry_method_code", "Entry Method Code"}, {"iso_currency_code", "ISO Currency Code"}, {"last_update_by", "Last Updated By"}, {"last_update_time", "Last Updated Datetime"}, {"line_sequence_number", "Line Sequence Number"}, {"mod_by_amount", "Modification by Amount (Native Currency)"}, {"mod_by_percentage", "Modification by Percentage"}, {"mod_line_sequence_number", "Mod Line Sequence Number"}, {"override_user_id", "Override User Id"}, {"price_mod_source_type_code", "Price Mod Source Type Code"}, {"price_mod_type_code", "Price Mod Type Code"}, {"reason_code", "Reason Code"}, {"rounding_amount", "Rounding Amount (Native Currency)"}, {"sequence_number", "Sequence Number"}, {"username", "Username"}, {"voided", "Voided"}}),
    #"Merged Columns | Transaction Key" = Table.CombineColumns(Table.TransformColumnTypes(#"Renamed Columns", {{"Sequence Number", type text}}, "en-US"),{"Device Id", "Business Date", "Sequence Number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Transaction Key"),
    #"Changed Type" = Table.TransformColumnTypes(#"Merged Columns | Transaction Key",{{"Modification by Percentage", Percentage.Type}, {"Voided", type logical}}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Changed Type",{{"Calculation Method", Text.Proper, type text}, {"Price Mod Type Code", Text.Proper, type text}, {"Price Mod Source Type Code", Text.Proper, type text}}),
    #"Removed Columns | Redundant Columns" = Table.RemoveColumns(#"Capitalized Each Word",{"Created Datetime", "Created By", "Last Updated By"}),
    #"Removed Duplicates" = Table.Distinct(#"Removed Columns | Redundant Columns", {"Transaction Key"})
in
    #"Removed Duplicates"
```

### Retail Transactions (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH #(lf)emp_dict AS (        #(lf)    SELECT #(lf)        CONCAT(FirstName, ' ') AS FirstName, #(lf)        LastName, #(lf)        CustomerID,#(lf)        CustomerNumber#(lf)    FROM [LH_Mart].[dbo].[crmcustomerdim]#(lf)    WHERE MembershipType = 'EMP'#(lf)),#(lf)#(lf)pos_tx AS (#(lf)    SELECT#(lf)        CONVERT(varchar(128),#(lf)            CONCAT(#(lf)                st.device_id, '-',#(lf)                st.business_date, '-',#(lf)                CONVERT(varchar(50), st.sequence_number)#(lf)            )#(lf)        ) AS TransactionKey,#(lf)        st.device_id,#(lf)        CAST(st.business_date AS date) AS business_date,#(lf)        st.sequence_number,#(lf)        st.total,#(lf)        st.pre_tender_balance_due,#(lf)        st.subtotal,#(lf)        st.tax_total,#(lf)        st.tax_total_for_display,#(lf)        st.discount_total,#(lf)        st.discount_total AS discount_emp,#(lf)        st.customer_id,#(lf)        st.selling_channel_code,#(lf)        st.loyalty_card_number,#(lf)        st.tax_exempt_customer_id,#(lf)        st.tax_exempt_certificate,#(lf)        st.tax_exempt_code,#(lf)        st.employee_id_for_discount,#(lf)        st.iso_currency_code,#(lf)        st.line_item_count,#(lf)        st.age_restricted_date_of_birth,#(lf)        st.item_count,#(lf)        st.customer_name,#(lf)        st.tender_type_codes,#(lf)        st.voidable_flag,#(lf)        st.tax_geo_code_origin,#(lf)        st.rcpt_rtn_total,#(lf)        st.non_rcpt_rtn_total,#(lf)        st.customer_entry_method_code,#(lf)        st.cust_other_id,#(lf)        st.rcpt_rtn_count,#(lf)        st.non_rcpt_rtn_count,#(lf)        st.ring_elapsed_time_in_secs,#(lf)        st.tender_elapsed_time_in_secs,#(lf)        st.idle_elapsed_time_in_secs,#(lf)        st.lock_elapsed_time_in_secs,#(lf)        st.entry_mode_code,#(lf)        st.suspended_reason_code,#(lf)        st.suspended_note,#(lf)        st.order_id,#(lf)        st.loyalty_points_earned,#(lf)        st.customer_callout,#(lf)        st.fiscal_control_number,#(lf)        st.gift_receipt_print_type,#(lf)        st.fiscal_processor_code,#(lf)        st.create_time,#(lf)        CAST(st.create_time AS date) AS [Date Created],#(lf)        st.create_by,#(lf)        st.last_update_time,#(lf)        st.last_update_by,#(lf)        st.party_id,#(lf)        st.employee_name_for_discount,#(lf)        CONCAT(emp_dict.FirstName, emp_dict.LastName) AS employee_name_for_discount_LH_Mart,#(lf)        st.event_id,#(lf)        st.event_invoice,#(lf)        st.extended_subtotal,#(lf)        st.parent_order_id,#(lf)        st.additional_attributes,#(lf)        NULL AS OrderDateUTC,#(lf)        NULL AS DateCreatedUTC,#(lf)        NULL AS OrderStatusChangeDateUTC,#(lf)        NULL AS UpdateDate,#(lf)        NULL AS [Update Date (orderpayments)],#(lf)        NULL AS [AuthorizedAmount (orderpayments)],#(lf)        NULL AS [CapturedAmount (orderpayments)],#(lf)        NULL AS [EarlyCaptureAmount (orderpayments)],#(lf)        NULL AS [EarlyUsedAmount (orderpayments)],#(lf)        NULL AS [EarlyCreditAmount (orderpayments)],#(lf)        NULL AS [CreditedAmount (orderpayments)],#(lf)        NULL AS [AmountAvailableForCapture (orderpayments)],#(lf)        NULL AS [AmountAvailableForCredit (orderpayments)],#(lf)        NULL AS [TenderCode (orderpayments)],#(lf)        NULL AS [TenderTypeCode (orderpayments)],#(lf)        NULL AS order_status_id,#(lf)        NULL AS order_status_code,#(lf)        NULL AS order_status,#(lf)        ts.total AS [Tender Total],#(lf)        NULL AS emp_disc_flag,#(lf)        'POS' AS Source,#(lf)        NULL AS DiscountText#(lf)    FROM LH_Source.dbo.jumpmind_sls_retail_trans AS st#(lf)    LEFT JOIN emp_dict#(lf)        ON emp_dict.CustomerNumber = st.loyalty_card_number#(lf)    LEFT JOIN (#(lf)        SELECT #(lf)            total,#(lf)            business_date,#(lf)            device_id,#(lf)            sequence_number#(lf)        FROM [LH_Source].[dbo].[jumpmind_sls_trans_summary] s#(lf)        WHERE employee_id_for_discount IS NOT NULL#(lf)          AND TRY_CAST(business_date AS date) >= DATEADD(month, -4, CAST(GETDATE() AS date))#(lf)    ) ts#(lf)        ON  ts.business_date   = st.business_date#(lf)        AND ts.device_id       = st.device_id#(lf)        AND ts.sequence_number = st.sequence_number#(lf)    WHERE st.business_date >= DATEADD(month, -4, CAST(GETDATE() AS date))#(lf)),#(lf)#(lf)pos_tx_addrs AS (#(lf)    SELECT#(lf)        pt.*,#(lf)        c.address_1 AS Guest_Address1, #(lf)        c.address_2 AS Guest_Address2, #(lf)        c.address_3 AS Guest_City, #(lf)        c.address_4 AS Guest_State, #(lf)        c.post_code AS Guest_PostalCode#(lf)    FROM pos_tx pt #(lf)    LEFT JOIN [dbo].[inboundloyalty_customermasterde] c#(lf)        ON pt.loyalty_card_number = c.customerNumber#(lf)),#(lf)#(lf)hs AS (#(lf)    SELECT#(lf)        COALESCE(#(lf)            NULLIF(CONVERT(varchar(64), dtt.MaxWarehouseCode), ''),#(lf)            NULLIF(CONVERT(varchar(64), dtt.SiteWarehouseCode), ''),#(lf)            NULLIF(CONVERT(varchar(64), r.SiteCode), '')#(lf)        ) AS InventLocationId,#(lf)        COALESCE(r.OrderDateUTC, r.DateCreatedUTC, r.OrderStatusChangeDateUTC, r.ExportCreatedUTC) AS TransDateDT,#(lf)        CONVERT(varchar(64), r.OrderNumber) AS OrderNumber,#(lf)        CONVERT(varchar(64), r.OrderID)     AS [OrderID],#(lf)        CONCAT(r.FirstName1, ' ', r.LastName1) AS customer_name,#(lf)        r.Custom3 AS LoyaltyNumber,#(lf)        r.Custom3 AS EmployeeID,#(lf)        TRY_CONVERT(decimal(17,2), r.Discount) AS Discount,#(lf)        TRY_CONVERT(decimal(17,2), r.SubTotal) AS SubTotal_Dec,#(lf)        TRY_CONVERT(decimal(17,2), r.Tax)      AS Tax_Dec,#(lf)        TRY_CONVERT(decimal(17,2), r.Total)    AS Total_Dec,#(lf)        CONVERT(varchar(8000), r.OrderSource)  AS OrderSource,#(lf)        COALESCE(r.UpdateDate, r.OrderDateUTC, r.DateCreatedUTC) AS LastUpdateTime,#(lf)        r.ExportCreatedUTC AS ExportCreatedUTC,#(lf)        r.OrderDateUTC AS OrderDateUTC,#(lf)        r.DateCreatedUTC AS DateCreatedUTC,#(lf)        r.OrderStatusChangeDateUTC AS OrderStatusChangeDateUTC,#(lf)        r.UpdateDate AS UpdatedDate,#(lf)        r.OrderStatus,#(lf)        r.Address1 AS Guest_Address1, #(lf)        r.Address2 AS Guest_Address2,#(lf)        r.City     AS Guest_City,#(lf)        r.Province AS Guest_State,#(lf)        r.PostalCode AS Guest_PostalCode#(lf)    FROM LH_Source.dbo.mulesoft_deckjsonraw_root r#(lf)    LEFT JOIN LH_Source.dbo.mulesoft_dynamicstargettrans dtt#(lf)        ON CONVERT(varchar(64), dtt.OrderId) = CONVERT(varchar(64), r.OrderID)#(lf)    WHERE CAST(COALESCE(r.OrderDateUTC, r.DateCreatedUTC, r.OrderStatusChangeDateUTC, r.ExportCreatedUTC) AS date)#(lf)          >= DATEADD(month, -4, CAST(GETDATE() AS date))#(lf)),#(lf)#(lf)paymenttrans AS (#(lf)    SELECT #(lf)        Amount AS [Tender Total],#(lf)        _ParentKeyField AS OrderID#(lf)    FROM [LH_Source].[dbo].[mulesoft_deckjsonraw_paymenttransactions]#(lf)    WHERE PaymentTransactionTypeId = 10#(lf)),#(lf)#(lf)adjustments AS (#(lf)    SELECT #(lf)        r.OrderID,#(lf)        SUM(o.NetPrice) AS tender_total,#(lf)        o.DiscountText#(lf)    FROM [LH_Source].[dbo].[mulesoft_deckjsonraw_orderitemadjustments] o#(lf)    INNER JOIN [LH_Source].[dbo].[mulesoft_deckjsonraw_root] r#(lf)        ON o._ParentKeyField = r.OrderID#(lf)    WHERE (o.PromotionID LIKE '%Emp%' OR o.DiscountText LIKE '%Associate%' OR o.CampaignID LIKE '%EmployeeDisc%')#(lf)      AND r.OrderNumber NOT LIKE 'B%'#(lf)    GROUP BY r.OrderID, o.DiscountText#(lf)),#(lf)#(lf)orderpayments AS (#(lf)    SELECT #(lf)        _ParentKeyField, #(lf)        CAST(MAX(DateCreated) AS date) AS DateCreated, #(lf)        CAST(MAX(UpdateDate) AS date)  AS UpdateDate, #(lf)        TRY_CONVERT(decimal(17,2), SUM(AuthorizedAmount))        AS AuthorizedAmount, #(lf)        TRY_CONVERT(decimal(17,2), SUM(CapturedAmount))          AS CapturedAmount,#(lf)        TRY_CONVERT(decimal(17,2), SUM(EarlyCaptureAmount))      AS EarlyCaptureAmount,#(lf)        TRY_CONVERT(decimal(17,2), SUM(EarlyUsedAmount))         AS EarlyUsedAmount,#(lf)        TRY_CONVERT(decimal(17,2), SUM(EarlyCreditAmount))       AS EarlyCreditAmount,#(lf)        TRY_CONVERT(decimal(17,2), SUM(CreditedAmount))          AS CreditedAmount,#(lf)        TRY_CONVERT(decimal(17,2), SUM(AmountAvailableForCapture)) AS AmountAvailableForCapture,#(lf)        TRY_CONVERT(decimal(17,2), SUM(AmountAvaialbleForCredit))  AS AmountAvailableForCredit,#(lf)        CAST(p.Generic1 AS varchar(30))        AS OP_TenderCode,#(lf)        CAST(p.PaymentProcessor AS varchar(30)) AS OP_TenderTypeCode#(lf)    FROM LH_Source.[dbo].[mulesoft_deckjsonraw_orderpayments] p#(lf)    WHERE DateCreated >= DATEADD(month, -4, CAST(GETDATE() AS date))#(lf)    GROUP BY _ParentKeyField, Generic1, PaymentProcessor#(lf)),#(lf)#(lf)hs_norm AS (#(lf)    SELECT#(lf)        CASE#(lf)            WHEN hs.InventLocationId = 'BAB'   THEN '1013'#(lf)            WHEN hs.InventLocationId = 'BABUK' THEN '2013'#(lf)            WHEN NULLIF(hs.InventLocationId,'') IS NULL THEN '9999'#(lf)            ELSE '9999'#(lf)        END AS InventLocationIdMapped,#(lf)        hs.*,#(lf)        p.*#(lf)    FROM hs#(lf)    LEFT JOIN orderpayments p#(lf)        ON hs.OrderID = p._ParentKeyField#(lf)),#(lf)#(lf)oms_tx AS (#(lf)    SELECT#(lf)        CONVERT(varchar(128),#(lf)            CONCAT(#(lf)                hn.InventLocationIdMapped, '-','052','-',#(lf)                CONVERT(varchar(8), CAST(hn.TransDateDT AS date), 112),#(lf)                '-',#(lf)                COALESCE(#(lf)                    CONVERT(varchar(50), TRY_CONVERT(bigint, hn.OrderID)),#(lf)                    CONVERT(varchar(64), hn.OrderID)#(lf)                )#(lf)            )#(lf)        ) AS TransactionKey,#(lf)        CONVERT(varchar(100), CONCAT(hn.InventLocationIdMapped, '-', '052')) AS device_id,#(lf)        CONVERT(varchar(10), CAST(hn.TransDateDT AS date), 120) AS business_date,#(lf)        TRY_CONVERT(bigint, hn.OrderID) AS sequence_number,#(lf)        hn.Total_Dec AS total,#(lf)        CAST(NULL AS decimal(17,2)) AS pre_tender_balance_due,#(lf)        hn.SubTotal_Dec AS subtotal,#(lf)        hn.Tax_Dec AS tax_total,#(lf)        hn.Tax_Dec AS tax_total_for_display,#(lf)        CAST(hn.Discount AS decimal(17,2)) AS discount_total,#(lf)        adjustments.tender_total AS discount_emp,#(lf)        CAST(NULL AS varchar(100)) AS customer_id,#(lf)        hn.OrderSource AS selling_channel_code,#(lf)        CAST(hn.LoyaltyNumber AS varchar(100)) AS loyalty_card_number,#(lf)        CAST(NULL AS varchar(100)) AS tax_exempt_customer_id,#(lf)        CAST(NULL AS varchar(100)) AS tax_exempt_certificate,#(lf)        CAST(NULL AS varchar(100)) AS tax_exempt_code,#(lf)        CAST(emp_dict.CustomerID AS varchar(100)) AS employee_id_for_discount,#(lf)        CAST(NULL AS varchar(100)) AS iso_currency_code,#(lf)        CAST(NULL AS int) AS line_item_count,#(lf)        CAST(NULL AS datetime2(6)) AS age_restricted_date_of_birth,#(lf)        CAST(NULL AS int) AS item_count,#(lf)        CAST(hn.customer_name AS varchar(100)) AS customer_name,#(lf)        CAST(NULL AS varchar(100)) AS tender_type_codes,#(lf)        CAST(0 AS int) AS voidable_flag,#(lf)        CAST(NULL AS varchar(100)) AS tax_geo_code_origin,#(lf)        CAST(NULL AS decimal(17,2)) AS rcpt_rtn_total,#(lf)        CAST(NULL AS decimal(17,2)) AS non_rcpt_rtn_total,#(lf)        CAST(NULL AS varchar(100)) AS customer_entry_method_code,#(lf)        CAST(NULL AS varchar(100)) AS cust_other_id,#(lf)        CAST(NULL AS int) AS rcpt_rtn_count,#(lf)        CAST(NULL AS int) AS non_rcpt_rtn_count,#(lf)        CAST(NULL AS int) AS ring_elapsed_time_in_secs,#(lf)        CAST(NULL AS int) AS tender_elapsed_time_in_secs,#(lf)        CAST(NULL AS int) AS idle_elapsed_time_in_secs,#(lf)        CAST(NULL AS int) AS lock_elapsed_time_in_secs,#(lf)        CAST(NULL AS varchar(100)) AS entry_mode_code,#(lf)        CAST(NULL AS varchar(100)) AS suspended_reason_code,#(lf)        CAST(NULL AS varchar(100)) AS suspended_note,#(lf)        CONVERT(varchar(100), hn.OrderID) AS order_id,#(lf)        CAST(NULL AS decimal(17,2)) AS loyalty_points_earned,#(lf)        CAST(NULL AS varchar(100)) AS customer_callout,#(lf)        CAST(NULL AS varchar(100)) AS fiscal_control_number,#(lf)        CAST(NULL AS varchar(100)) AS gift_receipt_print_type,#(lf)        CAST(NULL AS varchar(100)) AS fiscal_processor_code,#(lf)        CAST(hn.ExportCreatedUTC AS datetime2(6)) AS create_time,#(lf)        CAST(hn.DateCreated AS date) AS [Date Created],#(lf)        CAST('WEB' AS varchar(100)) AS create_by,#(lf)        CAST(hn.LastUpdateTime AS datetime2(6)) AS last_update_time,#(lf)        CAST(NULL AS varchar(100)) AS last_update_by,#(lf)        CAST(NULL AS varchar(100)) AS party_id,#(lf)        CAST(hn.customer_name AS varchar(100)) AS employee_name_for_discount,#(lf)        CONCAT(emp_dict.FirstName, emp_dict.LastName) AS employee_name_for_discount_LH_Mart,#(lf)        CAST(NULL AS varchar(100)) AS event_id,#(lf)        CAST(NULL AS varchar(100)) AS event_invoice,#(lf)        CAST(NULL AS decimal(17,2)) AS extended_subtotal,#(lf)        CAST(NULL AS varchar(100)) AS parent_order_id,#(lf)        CAST(NULL AS varchar(100)) AS additional_attributes,#(lf)        hn.OrderDateUTC AS OrderDateUTC,#(lf)        hn.DateCreatedUTC AS DateCreatedUTC,#(lf)        hn.OrderStatusChangeDateUTC AS OrderStatusChangeDateUTC,#(lf)        hn.UpdatedDate AS UpdateDate,#(lf)        hn.UpdateDate AS [Update Date (orderpayments)],#(lf)        hn.AuthorizedAmount AS [AuthorizedAmount (orderpayments)],#(lf)        hn.CapturedAmount AS [CapturedAmount (orderpayments)],#(lf)        hn.EarlyCaptureAmount AS [EarlyCaptureAmount (orderpayments)],#(lf)        hn.EarlyUsedAmount AS [EarlyUsedAmount (orderpayments)],#(lf)        hn.EarlyCreditAmount AS [EarlyCreditAmount (orderpayments)],#(lf)        hn.CreditedAmount AS [CreditedAmount (orderpayments)],#(lf)        hn.AmountAvailableForCapture AS [AmountAvailableForCapture (orderpayments)],#(lf)        hn.AmountAvailableForCredit AS [AmountAvailableForCredit (orderpayments)],#(lf)        hn.OP_TenderCode AS [TenderCode (orderpayments)],#(lf)        hn.OP_TenderTypeCode AS [TenderTypeCode (orderpayments)],#(lf)        hn.OrderStatus AS order_status_id,#(lf)        CASE hn.OrderStatus #(lf)            WHEN 1 THEN 'CO'#(lf)            WHEN 3 THEN 'AVS'#(lf)            WHEN 4 THEN 'P'#(lf)            WHEN 5 THEN 'PV'#(lf)            WHEN 6 THEN 'Z'#(lf)            WHEN 9 THEN 'MR'#(lf)            WHEN 10 THEN 'PS'#(lf)            WHEN 11 THEN 'DAP'#(lf)            WHEN 12 THEN 'CF'#(lf)            ELSE NULL#(lf)        END AS order_status_code,#(lf)        CASE hn.OrderStatus #(lf)            WHEN 1 THEN 'New'#(lf)            WHEN 3 THEN 'Review'#(lf)            WHEN 4 THEN 'Pending'#(lf)            WHEN 5 THEN 'Exception'#(lf)            WHEN 6 THEN 'Completed'#(lf)            WHEN 9 THEN 'Manual Review'#(lf)            WHEN 10 THEN 'Pending Settlement'#(lf)            WHEN 11 THEN 'Delayed Auto-Process'#(lf)            WHEN 12 THEN 'Confirmed Fraud'#(lf)            ELSE NULL#(lf)        END AS order_status,#(lf)        paymenttrans.[Tender Total] AS [Tender Total],#(lf)        IIF(adjustments.OrderID IS NOT NULL, 1, NULL) AS emp_disc_flag,#(lf)        'OMS' AS Source,#(lf)        hn.Guest_Address1,#(lf)        hn.Guest_Address2,#(lf)        hn.Guest_City,#(lf)        hn.Guest_State,#(lf)        hn.Guest_PostalCode,#(lf)        adjustments.DiscountText AS DiscountText#(lf)    FROM hs_norm hn#(lf)    LEFT JOIN emp_dict#(lf)        ON emp_dict.CustomerNumber = hn.LoyaltyNumber#(lf)    LEFT JOIN adjustments#(lf)        ON adjustments.OrderID = hn.OrderID#(lf)    LEFT JOIN paymenttrans#(lf)        ON hn.OrderID = paymenttrans.OrderID#(lf))#(lf)#(lf)-- IMPORTANT: explicit column lists so UNION matches by POSITION safely#(lf)SELECT#(lf)    TransactionKey,#(lf)    device_id,#(lf)    business_date,#(lf)    sequence_number,#(lf)    total,#(lf)    pre_tender_balance_due,#(lf)    subtotal,#(lf)    tax_total,#(lf)    tax_total_for_display,#(lf)    discount_total,#(lf)    discount_emp,#(lf)    customer_id,#(lf)    selling_channel_code,#(lf)    loyalty_card_number,#(lf)    tax_exempt_customer_id,#(lf)    tax_exempt_certificate,#(lf)    tax_exempt_code,#(lf)    employee_id_for_discount,#(lf)    iso_currency_code,#(lf)    line_item_count,#(lf)    age_restricted_date_of_birth,#(lf)    item_count,#(lf)    customer_name,#(lf)    tender_type_codes,#(lf)    voidable_flag,#(lf)    tax_geo_code_origin,#(lf)    rcpt_rtn_total,#(lf)    non_rcpt_rtn_total,#(lf)    customer_entry_method_code,#(lf)    cust_other_id,#(lf)    rcpt_rtn_count,#(lf)    non_rcpt_rtn_count,#(lf)    ring_elapsed_time_in_secs,#(lf)    tender_elapsed_time_in_secs,#(lf)    idle_elapsed_time_in_secs,#(lf)    lock_elapsed_time_in_secs,#(lf)    entry_mode_code,#(lf)    suspended_reason_code,#(lf)    suspended_note,#(lf)    order_id,#(lf)    loyalty_points_earned,#(lf)    customer_callout,#(lf)    fiscal_control_number,#(lf)    gift_receipt_print_type,#(lf)    fiscal_processor_code,#(lf)    create_time,#(lf)    [Date Created],#(lf)    create_by,#(lf)    last_update_time,#(lf)    last_update_by,#(lf)    party_id,#(lf)    employee_name_for_discount,#(lf)    employee_name_for_discount_LH_Mart,#(lf)    event_id,#(lf)    event_invoice,#(lf)    extended_subtotal,#(lf)    parent_order_id,#(lf)    additional_attributes,#(lf)    OrderDateUTC,#(lf)    DateCreatedUTC,#(lf)    OrderStatusChangeDateUTC,#(lf)    UpdateDate,#(lf)    [Update Date (orderpayments)],#(lf)    [AuthorizedAmount (orderpayments)],#(lf)    [CapturedAmount (orderpayments)],#(lf)    [EarlyCaptureAmount (orderpayments)],#(lf)    [EarlyUsedAmount (orderpayments)],#(lf)    [EarlyCreditAmount (orderpayments)],#(lf)    [CreditedAmount (orderpayments)],#(lf)    [AmountAvailableForCapture (orderpayments)],#(lf)    [AmountAvailableForCredit (orderpayments)],#(lf)    [TenderCode (orderpayments)],#(lf)    [TenderTypeCode (orderpayments)],#(lf)    order_status_id,#(lf)    order_status_code,#(lf)    order_status,#(lf)    [Tender Total],#(lf)    emp_disc_flag,#(lf)    Source,#(lf)    Guest_Address1,#(lf)    Guest_Address2,#(lf)    Guest_City,#(lf)    Guest_State,#(lf)    Guest_PostalCode,#(lf)    DiscountText#(lf)FROM pos_tx_addrs#(lf)#(lf)UNION ALL#(lf)#(lf)SELECT#(lf)    TransactionKey,#(lf)    device_id,#(lf)    business_date,#(lf)    sequence_number,#(lf)    total,#(lf)    pre_tender_balance_due,#(lf)    subtotal,#(lf)    tax_total,#(lf)    tax_total_for_display,#(lf)    discount_total,#(lf)    discount_emp,#(lf)    customer_id,#(lf)    selling_channel_code,#(lf)    loyalty_card_number,#(lf)    tax_exempt_customer_id,#(lf)    tax_exempt_certificate,#(lf)    tax_exempt_code,#(lf)    employee_id_for_discount,#(lf)    iso_currency_code,#(lf)    line_item_count,#(lf)    age_restricted_date_of_birth,#(lf)    item_count,#(lf)    customer_name,#(lf)    tender_type_codes,#(lf)    voidable_flag,#(lf)    tax_geo_code_origin,#(lf)    rcpt_rtn_total,#(lf)    non_rcpt_rtn_total,#(lf)    customer_entry_method_code,#(lf)    cust_other_id,#(lf)    rcpt_rtn_count,#(lf)    non_rcpt_rtn_count,#(lf)    ring_elapsed_time_in_secs,#(lf)    tender_elapsed_time_in_secs,#(lf)    idle_elapsed_time_in_secs,#(lf)    lock_elapsed_time_in_secs,#(lf)    entry_mode_code,#(lf)    suspended_reason_code,#(lf)    suspended_note,#(lf)    order_id,#(lf)    loyalty_points_earned,#(lf)    customer_callout,#(lf)    fiscal_control_number,#(lf)    gift_receipt_print_type,#(lf)    fiscal_processor_code,#(lf)    create_time,#(lf)    [Date Created],#(lf)    create_by,#(lf)    last_update_time,#(lf)    last_update_by,#(lf)    party_id,#(lf)    employee_name_for_discount,#(lf)    employee_name_for_discount_LH_Mart,#(lf)    event_id,#(lf)    event_invoice,#(lf)    extended_subtotal,#(lf)    parent_order_id,#(lf)    additional_attributes,#(lf)    OrderDateUTC,#(lf)    DateCreatedUTC,#(lf)    OrderStatusChangeDateUTC,#(lf)    UpdateDate,#(lf)    [Update Date (orderpayments)],#(lf)    [AuthorizedAmount (orderpayments)],#(lf)    [CapturedAmount (orderpayments)],#(lf)    [EarlyCaptureAmount (orderpayments)],#(lf)    [EarlyUsedAmount (orderpayments)],#(lf)    [EarlyCreditAmount (orderpayments)],#(lf)    [CreditedAmount (orderpayments)],#(lf)    [AmountAvailableForCapture (orderpayments)],#(lf)    [AmountAvailableForCredit (orderpayments)],#(lf)    [TenderCode (orderpayments)],#(lf)    [TenderTypeCode (orderpayments)],#(lf)    order_status_id,#(lf)    order_status_code,#(lf)    order_status,#(lf)    [Tender Total],#(lf)    emp_disc_flag,#(lf)    Source,#(lf)    Guest_Address1,#(lf)    Guest_Address2,#(lf)    Guest_City,#(lf)    Guest_State,#(lf)    Guest_PostalCode,#(lf)    DiscountText#(lf)FROM oms_tx;#(lf)", CreateNavigationProperties=false]),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"business_date", "Business Date"}, {"age_restricted_date_of_birth", "Age Restricted Date of Birth"}, {"create_by", "Created By"}, {"create_time", "Created Datetime"}, {"customer_callout", "Customer Callout"}, {"customer_id", "Customer Id"}, {"customer_name", "Customer Name"}, {"device_id", "Device Id"}, {"customer_entry_method_code", "Customer Entry Method Code"}, {"cust_other_id", "Customer Id (Other)"}, {"discount_total", "Discount Total"}, {"employee_id_for_discount", "Employee Id for Discount"}, {"employee_name_for_discount", "Employee Name for Discount"}, {"entry_mode_code", "Entry Mode Code"}, {"event_id", "Event Id"}, {"event_invoice", "Event Invoice"}, {"fiscal_control_number", "Fiscal Control Number"}, {"fiscal_processor_code", "Fiscal Processor Code"}, {"gift_receipt_print_type", "Gift Receipt Print Type"}, {"iso_currency_code", "ISO Currency Code"}, {"idle_elapsed_time_in_secs", "Idle Elapsed Time (in Seconds)"}, {"item_count", "Item Count"}, {"last_update_by", "Last Updated By"}, {"last_update_time", "Last Updated Datetime"}, {"line_item_count", "Line Item Count"}, {"lock_elapsed_time_in_secs", "Lock Elapsed Time (in Seconds)"}, {"loyalty_card_number", "Loyalty Card Number"}, {"loyalty_points_earned", "Loyalty Points Earned"}, {"non_rcpt_rtn_count", "Non-Receipt Return Count"}, {"non_rcpt_rtn_total", "Non-Receipt Return Total"}, {"order_id", "Order Id"}, {"party_id", "Party Id"}, {"pre_tender_balance_due", "Pre-Tender Balance Due"}, {"rcpt_rtn_count", "Receipt Return Count"}, {"rcpt_rtn_total", "Receipt Return Total"}, {"ring_elapsed_time_in_secs", "Ring Elapsed Time (in Seconds)"}, {"selling_channel_code", "Selling Channel Code"}, {"sequence_number", "Sequence Number"}, {"subtotal", "Subtotal"}, {"suspended_note", "Suspended Note"}, {"suspended_reason_code", "Suspended Reason Code"}, {"tax_exempt_certificate", "Tax Exempt Certificate"}, {"tax_exempt_code", "Tax Exempt Code"}, {"tax_exempt_customer_id", "Tax Exempt Customer Id"}, {"tax_geo_code_origin", "Tax Geo Code Origin"}, {"tax_total", "Tax Total"}, {"tax_total_for_display", "Tax Total for Display"}, {"tender_elapsed_time_in_secs", "Tender Elapsed Time (in Seconds)"}, {"tender_type_codes", "Tender Type Codes"}, {"total", "Total"}, {"voidable_flag", "Voidable Flag"}}),
    #"Added Custom | Tender Type Count" = Table.AddColumn(#"Renamed Columns", "Tender Type Count", each List.Count(Text.Split([Tender Type Codes]," "))),
    #"Replaced Errors | Tender Type Count NULL" = Table.ReplaceErrorValues(#"Added Custom | Tender Type Count", {{"Tender Type Count", null}}),
    #"Cleaned Text" = Table.TransformColumns(#"Replaced Errors | Tender Type Count NULL",{{"Customer Name", Text.Clean, type text}}),
    #"Trimmed Text" = Table.TransformColumns(#"Cleaned Text",{{"Customer Name", Text.Trim, type text}}),
    #"Replaced Value | blank with NULL" = Table.ReplaceValue(#"Trimmed Text","",null,Replacer.ReplaceValue,{"Customer Name"}),
    #"Replaced Value | _ with SPACE" = Table.ReplaceValue(#"Replaced Value | blank with NULL","_"," ",Replacer.ReplaceText,{"Gift Receipt Print Type"}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Replaced Value | _ with SPACE",{{"Customer Name", Text.Proper, type text}, {"Gift Receipt Print Type", Text.Proper, type text}, {"Customer Entry Method Code", Text.Proper, type text}, {"Selling Channel Code", Text.Proper, type text}, {"Employee Name for Discount", Text.Proper, type text}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Capitalized Each Word",{{"Voidable Flag", type logical}, {"Tender Type Count", Int64.Type}}),
    #"Removed Columns | Redundant Columns" = Table.RemoveColumns(#"Changed Type",{"Created Datetime", "Created By", "Last Updated By"}),
    #"Removed Columns | Empty Columns" = Table.RemoveColumns(#"Removed Columns | Redundant Columns",{"Age Restricted Date of Birth", "Suspended Note", "Fiscal Control Number", "Fiscal Processor Code"}),
    #"Added Custom | City State" = Table.AddColumn(#"Capitalized Each Word", "City, State", each [Guest_City] & ", " & [Guest_State]),
    #"Removed Duplicates" = Table.Distinct(#"Added Custom | City State", {"TransactionKey"})
in
    #"Removed Duplicates"
```

### Tax Authorities (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH pos_auth AS (#(lf)  SELECT DISTINCT#(lf)      CAST(ja.id AS varchar(64))                 AS id,#(lf)      CAST(ja.auth_name AS varchar(256))         AS auth_name,#(lf)      CAST(ja.rounding_code AS int)              AS rounding_code,#(lf)      CAST(ja.rounding_digits_quantity AS int)   AS rounding_digits_quantity,#(lf)      CAST(ja.auth_type_name AS varchar(256))    AS auth_type_name,#(lf)      CAST('POS' AS varchar(8))                  AS source#(lf)  FROM dbo.jumpmind_tax_authority ja#(lf)),#(lf)root_site AS (#(lf)  SELECT _RowIndex, SiteCode#(lf)  FROM dbo.mulesoft_deckjsonraw_root#(lf)),#(lf)oms_src AS (#(lf)  SELECT DISTINCT#(lf)      it._ParentKeyField AS RootRowKey,#(lf)      UPPER(COALESCE(#(lf)        NULLIF(LTRIM(RTRIM(CAST(it.Description AS varchar(256)))), ''),#(lf)        CASE WHEN TRY_CONVERT(int, it.IsVAT) = 1 THEN 'VAT'#(lf)             ELSE CONCAT('TAXTYPE_', CONVERT(varchar(32), it.TaxType))#(lf)        END#(lf)      ))                                    AS auth_name,#(lf)      TRY_CONVERT(decimal(18,6), it.Rate)   AS rate_val,#(lf)      TRY_CONVERT(int, it.IsVAT)            AS is_vat#(lf)  FROM dbo.mulesoft_deckjsonraw_orderitemtaxes it#(lf)  WHERE COALESCE(TRY_CONVERT(decimal(18,6), it.Amount), 0) <> 0#(lf)),#(lf)oms_norm AS (#(lf)  SELECT DISTINCT#(lf)      CONVERT(varchar(64),#(lf)              -ABS(CHECKSUM(CONCAT(rs.SiteCode, ':', os.auth_name, ':',#(lf)                                   COALESCE(CONVERT(varchar(64), os.rate_val), '0'), ':',#(lf)                                   COALESCE(CONVERT(varchar(8),  os.is_vat),   '0'))))#(lf)      )                                       AS id,#(lf)      os.auth_name                             AS auth_name,#(lf)      CAST(4  AS int)                          AS rounding_code,#(lf)      CAST(10 AS int)                          AS rounding_digits_quantity,#(lf)      CAST(NULL AS varchar(256))               AS auth_type_name,#(lf)      CAST('OMS' AS varchar(8))                AS source#(lf)  FROM oms_src os#(lf)  LEFT JOIN root_site rs#(lf)    ON rs._RowIndex = os.RootRowKey#(lf)),#(lf)unioned AS (#(lf)  SELECT id, auth_name, rounding_code, rounding_digits_quantity, auth_type_name, source FROM pos_auth#(lf)  UNION ALL#(lf)  SELECT id, auth_name, rounding_code, rounding_digits_quantity, auth_type_name, source FROM oms_norm#(lf))#(lf)SELECT#(lf)  id,#(lf)  auth_name,#(lf)  rounding_code,#(lf)  rounding_digits_quantity,#(lf)  auth_type_name,#(lf)  source#(lf)FROM unioned#(lf)ORDER BY#(lf)  CASE WHEN TRY_CONVERT(int, id) IS NOT NULL THEN 0 ELSE 1 END,#(lf)  TRY_CONVERT(int, id),#(lf)  id,#(lf)  auth_name;", CreateNavigationProperties=false]),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"auth_name", "Authorization Name"}, {"id", "Id"}, 
{"rounding_code", "Rounding Code"}, {"rounding_digits_quantity", "Rounding Digits Quantity"}, {"auth_type_name", "Authorization Type Name"}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Renamed Columns",{{"Rounding Code", Int64.Type}})
in
    #"Changed Type"
```

### Tax Groups (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH pos_groups AS (#(lf)  SELECT DISTINCT#(lf)    CAST(id            AS varchar(64))   AS [Id],#(lf)    CAST(group_name    AS varchar(256))  AS [Group Name],#(lf)    CAST([description] AS varchar(256))  AS [Description],#(lf)    CAST('POS'         AS varchar(8))    AS [source]#(lf)  FROM dbo.jumpmind_tax_group#(lf)),#(lf)root_site AS (#(lf)  SELECT _RowIndex, SiteCode#(lf)  FROM dbo.mulesoft_deckjsonraw_root#(lf)),#(lf)oms_item AS (#(lf)  SELECT DISTINCT#(lf)      it._ParentKeyField                         AS RootRowKey,#(lf)      TRY_CONVERT(int, it.IsVAT)                 AS IsVAT,#(lf)      TRY_CONVERT(decimal(18,6), it.Rate)        AS Rate#(lf)  FROM dbo.mulesoft_deckjsonraw_orderitemtaxes it#(lf)  WHERE COALESCE(TRY_CONVERT(decimal(18,6), it.Amount), 0) <> 0#(lf)),#(lf)oms_ship AS (#(lf)  SELECT DISTINCT#(lf)      ot._ParentKeyField                         AS RootRowKey,#(lf)      UPPER(NULLIF(LTRIM(RTRIM(CAST(ot.Description AS varchar(256)))), '')) AS DescText#(lf)  FROM dbo.mulesoft_deckjsonraw_ordertaxes ot#(lf)  WHERE COALESCE(TRY_CONVERT(decimal(18,6), ot.Amount), 0) <> 0#(lf)),#(lf)oms_sales_tax AS (#(lf)  SELECT DISTINCT#(lf)      td1._ParentKeyField                        AS RootRowKey#(lf)  FROM dbo.mulesoft_deckjsonraw_taxdetails td1#(lf)  WHERE UPPER(NULLIF(LTRIM(RTRIM(CAST(td1.TaxType AS varchar(64)))), '')) = 'TAX'#(lf)),#(lf)oms_item_site AS (#(lf)  SELECT i.RootRowKey, i.IsVAT, i.Rate, rs.SiteCode#(lf)  FROM oms_item i#(lf)  LEFT JOIN root_site rs ON rs._RowIndex = i.RootRowKey#(lf)),#(lf)oms_ship_site AS (#(lf)  SELECT s.RootRowKey, s.DescText, rs.SiteCode#(lf)  FROM oms_ship s#(lf)  LEFT JOIN root_site rs ON rs._RowIndex = s.RootRowKey#(lf)),#(lf)oms_sales_tax_site AS (#(lf)  SELECT t.RootRowKey, rs.SiteCode#(lf)  FROM oms_sales_tax t#(lf)  LEFT JOIN root_site rs ON rs._RowIndex = t.RootRowKey#(lf)),#(lf)oms_groups AS (#(lf)  SELECT DISTINCT#(lf)      CONCAT('OMS-', COALESCE(SiteCode,'WEB'), '-S') AS [Id],#(lf)      'S'                                            AS [Group Name],#(lf)      'Taxable'                                      AS [Description],#(lf)      'OMS'                                          AS [source]#(lf)  FROM oms_item_site#(lf)  WHERE IsVAT = 1 AND COALESCE(Rate,0) > 0#(lf)  UNION ALL#(lf)  SELECT DISTINCT#(lf)      CONCAT('OMS-', COALESCE(SiteCode,'WEB'), '-Z') AS [Id],#(lf)      'Z'                                            AS [Group Name],#(lf)      'Zero Rated'                                   AS [Description],#(lf)      'OMS'                                          AS [source]#(lf)  FROM oms_item_site#(lf)  WHERE IsVAT = 1 AND COALESCE(Rate,0) = 0#(lf)  UNION ALL#(lf)  SELECT DISTINCT#(lf)      CONCAT('OMS-', COALESCE(SiteCode,'WEB'), '-S_SHIP') AS [Id],#(lf)      'S_SHIP'                                           AS [Group Name],#(lf)      'VAT Shipping'                                     AS [Description],#(lf)      'OMS'                                              AS [source]#(lf)  FROM oms_ship_site#(lf)  WHERE DescText LIKE '%VAT%' AND DescText LIKE '%SHIP%'#(lf)  UNION ALL#(lf)  SELECT DISTINCT#(lf)      CONCAT('OMS-', COALESCE(SiteCode,'WEB'), '-TAX') AS [Id],#(lf)      'TAX'                                            AS [Group Name],#(lf)      'Sales Tax'                                      AS [Description],#(lf)      'OMS'                                            AS [source]#(lf)  FROM oms_sales_tax_site#(lf))#(lf)SELECT [Id], [Group Name], [Description], [source]#(lf)FROM pos_groups#(lf)UNION ALL#(lf)SELECT [Id], [Group Name], [Description], [source]#(lf)FROM oms_groups#(lf)ORDER BY [source], [Id], [Group Name];", CreateNavigationProperties=false]),
    #"Replaced Value | """" with NULL" = Table.ReplaceValue(Source,"",null,Replacer.ReplaceValue,{"Group Name"})
in
    #"Replaced Value | """" with NULL"
```

### Tax Lines (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH jm_base AS (#(lf)  SELECT#(lf)      device_id,#(lf)      business_date,#(lf)      sequence_number,#(lf)      line_sequence_number,#(lf)      tax_line_sequence_number,#(lf)      authority_id,#(lf)      authority_type,#(lf)      group_id,#(lf)      rule_name,#(lf)      tax_type,#(lf)      tax_holiday_indicator,#(lf)      rate_rule_sequence_number,#(lf)      override_applied,#(lf)      tax_exempt_id,#(lf)      tax_exempt,#(lf)      tax_exempt_amount,#(lf)      override_percent,#(lf)      override_amount,#(lf)      override_reason_code,#(lf)      tax_percentage,#(lf)      tax_amount,#(lf)      money_tax_amount,#(lf)      taxable_amount,#(lf)      iso_currency_code,#(lf)      calculation_source,#(lf)      tax_included_in_price,#(lf)      voided,#(lf)      override_user_id,#(lf)      entry_method_code,#(lf)      create_time,#(lf)      create_by,#(lf)      last_update_time,#(lf)      last_update_by,#(lf)      rule_description,#(lf)      CAST(NULL AS varchar(100)) AS calculation_method#(lf)  FROM dbo.jumpmind_sls_tax_retail_line_item#(lf)  WHERE create_by = 'openpos-sls'#(lf)    AND voided = 0#(lf)    AND TRY_CONVERT(date, business_date, 112) >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 4 MONTHS#(lf)),#(lf)jm_cur AS (#(lf)  SELECT#(lf)      device_id,#(lf)      TRY_CONVERT(date, business_date, 112) AS business_date,   -- safe parse#(lf)      sequence_number,#(lf)      line_sequence_number,#(lf)      tax_line_sequence_number,#(lf)      CAST(authority_id AS varchar(100)) AS authority_id,#(lf)      CAST(authority_type AS varchar(100)) AS authority_type,#(lf)      CAST(group_id AS varchar(100)) AS group_id,#(lf)      CAST(rule_name AS varchar(256)) AS rule_name,#(lf)      CAST(tax_type AS varchar(100)) AS tax_type,#(lf)      CAST(tax_holiday_indicator AS bit) AS tax_holiday_indicator,#(lf)      rate_rule_sequence_number,#(lf)      CAST(override_applied AS bit) AS override_applied,#(lf)      CAST(tax_exempt_id AS varchar(100)) AS tax_exempt_id,#(lf)      CAST(tax_exempt AS bit) AS tax_exempt,#(lf)      CAST(tax_exempt_amount AS decimal(18,6)) AS tax_exempt_amount,#(lf)      CASE WHEN override_percent IS NULL THEN NULL#(lf)           ELSE TRY_CONVERT(decimal(18,6), override_percent) / 100.0 END AS override_percent,#(lf)      CAST(override_amount AS decimal(18,6)) AS override_amount,#(lf)      CAST(override_reason_code AS varchar(100)) AS override_reason_code,#(lf)      CASE WHEN tax_percentage IS NULL THEN NULL#(lf)           ELSE TRY_CONVERT(decimal(18,6), tax_percentage) / 100.0 END AS tax_percentage,#(lf)      CAST(tax_amount AS decimal(18,6)) AS tax_amount,#(lf)      CAST(money_tax_amount AS decimal(18,6)) AS money_tax_amount,#(lf)      CAST(taxable_amount AS decimal(18,6)) AS taxable_amount,#(lf)      CAST(iso_currency_code AS varchar(8)) AS iso_currency_code,#(lf)      CAST(calculation_source AS varchar(64)) AS calculation_source,#(lf)      CAST(tax_included_in_price AS bit) AS tax_included_in_price,#(lf)      CAST(voided AS bit) AS voided,#(lf)      CAST(override_user_id AS varchar(100)) AS override_user_id,#(lf)      CAST(entry_method_code AS varchar(64)) AS entry_method_code,#(lf)      create_time,#(lf)      create_by,#(lf)      last_update_time,#(lf)      last_update_by,#(lf)      CAST(rule_description AS varchar(512)) AS rule_description,#(lf)      CAST(calculation_method AS varchar(100)) AS calculation_method,#(lf)      NULL                                                                       AS order_status_id,#(lf)      NULL                                                                       AS order_status_code,#(lf)      NULL                                                                       AS order_status,#(lf)      CAST('POS' AS varchar(8)) AS source#(lf)  FROM jm_base#(lf)),#(lf)oms_td1 AS (#(lf)  SELECT#(lf)      TRY_CONVERT(int, td1._ParentKeyField)       AS ParentOrderID,#(lf)      CAST(td1._RowIndex AS int)                  AS RowIndex,#(lf)      CAST(td1.TaxType AS varchar(100))           AS TaxType,#(lf)      TRY_CONVERT(decimal(18,6), td1.TotalAmount) AS TotalAmount,#(lf)      td1.InsertDate,#(lf)      td1.UpdateDate#(lf)  FROM dbo.mulesoft_deckjsonraw_taxdetails td1#(lf)  WHERE TRY_CONVERT(int, td1._ParentKeyField) IS NOT NULL#(lf)),#(lf)oms_base AS (#(lf)  SELECT#(lf)      r.OrderID,#(lf)      r.OrderNumber,#(lf)      r.OrderStatus,#(lf)      r.SiteCode,#(lf)      COALESCE(t.UpdateDate, t.InsertDate) AS TransDate,#(lf)      COALESCE(t.UpdateDate, t.InsertDate) AS LastUpd,#(lf)      t.RowIndex,#(lf)      t.TaxType,#(lf)      t.TotalAmount,#(lf)      dtt.SiteWarehouseCode#(lf)  FROM oms_td1 t#(lf)  JOIN dbo.mulesoft_deckjsonraw_root r#(lf)    ON r.OrderID = t.ParentOrderID#(lf)  OUTER APPLY (#(lf)    SELECT TOP (1) d.SiteWarehouseCode#(lf)    FROM dbo.mulesoft_dynamicstargettrans d#(lf)    WHERE d.OrderId = r.OrderID#(lf)    ORDER BY TRY_CONVERT(datetime2(7), d.ExportCreatedUTC) DESC#(lf)  ) dtt#(lf)  WHERE TRY_CONVERT(date, COALESCE(t.UpdateDate, t.InsertDate)) >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 2 MONTHS#(lf)),#(lf)ms_cur AS (#(lf)  SELECT#(lf)      CAST(#(lf)        COALESCE(#(lf)          NULLIF(LTRIM(RTRIM(SiteWarehouseCode)), ''),#(lf)          NULLIF(LTRIM(RTRIM(SiteCode)), ''),#(lf)          'WEB'#(lf)        ) + '-052'#(lf)      AS varchar(64)) AS device_id,#(lf)      CAST(CAST(TransDate AS date) AS date) AS business_date,#(lf)      CAST(r.OrderID AS bigint) AS sequence_number,#(lf)      CAST(RowIndex AS int) AS line_sequence_number,#(lf)      CAST(ROW_NUMBER() OVER (PARTITION BY OrderID, RowIndex ORDER BY TaxType, LastUpd) AS bigint) AS tax_line_sequence_number,#(lf)      CAST(NULL AS varchar(100)) AS authority_id,#(lf)      CAST(NULL AS varchar(100)) AS authority_type,#(lf)      CAST(NULL AS varchar(100)) AS group_id,#(lf)      CAST(TaxType AS varchar(256)) AS rule_name,#(lf)      CAST(TaxType AS varchar(100)) AS tax_type,#(lf)      CAST(0 AS bit) AS tax_holiday_indicator,#(lf)      CAST(NULL AS int) AS rate_rule_sequence_number,#(lf)      CAST(0 AS bit) AS override_applied,#(lf)      CAST(NULL AS varchar(100)) AS tax_exempt_id,#(lf)      CAST(0 AS bit) AS tax_exempt,#(lf)      CAST(NULL AS decimal(18,6)) AS tax_exempt_amount,#(lf)      CAST(NULL AS decimal(18,6)) AS override_percent,#(lf)      CAST(NULL AS decimal(18,6)) AS override_amount,#(lf)      CAST(NULL AS varchar(100)) AS override_reason_code,#(lf)      CAST(NULL AS decimal(18,6)) AS tax_percentage,#(lf)      CAST(TotalAmount AS decimal(18,6)) AS tax_amount,#(lf)      CAST(TotalAmount AS decimal(18,6)) AS money_tax_amount,#(lf)      CAST(NULL AS decimal(18,6)) AS taxable_amount,#(lf)      CASE WHEN SiteCode = 'BABUK' THEN 'GBP'#(lf)           WHEN SiteCode = 'BAB'   THEN 'USD'#(lf)           ELSE NULL END AS iso_currency_code,#(lf)      CAST('Ecommerce' AS varchar(64)) AS calculation_source,#(lf)      CAST(0 AS bit) AS tax_included_in_price,#(lf)      CAST(0 AS bit) AS voided,#(lf)      CAST(NULL AS varchar(100)) AS override_user_id,#(lf)      CAST(NULL AS varchar(64)) AS entry_method_code,#(lf)      CAST(TransDate AS datetime2) AS create_time,#(lf)      CAST('sp_bab_pos_merge_webreturns' AS varchar(128)) AS create_by,#(lf)      CAST(LastUpd AS datetime2) AS last_update_time,#(lf)      CAST('sp_bab_pos_merge_webreturns' AS varchar(128)) AS last_update_by,#(lf)      CAST(TaxType AS varchar(512)) AS rule_description,#(lf)      CAST(NULL AS varchar(100)) AS calculation_method,#(lf)      r.OrderStatus                                                              AS order_status_id,#(lf)        CASE r.OrderStatus #(lf)            WHEN 1 THEN 'CO'#(lf)            WHEN 3 THEN 'AVS'#(lf)            WHEN 4 THEN 'P'#(lf)            WHEN 5 THEN 'PV'#(lf)            WHEN 6 THEN 'Z'#(lf)            WHEN 9 THEN 'MR'#(lf)            WHEN 10 THEN 'PS'#(lf)            WHEN 11 THEN 'DAP'#(lf)            WHEN 12 THEN 'CF'#(lf)            ELSE null#(lf)        END                                                                        AS order_status_code,#(lf)        CASE r.OrderStatus #(lf)            WHEN 1 THEN 'New'#(lf)            WHEN 3 THEN 'Review'#(lf)            WHEN 4 THEN 'Pending'#(lf)            WHEN 5 THEN 'Exception'#(lf)            WHEN 6 THEN 'Completed'#(lf)            WHEN 9 THEN 'Manual Review'#(lf)            WHEN 10 THEN 'Pending Settlement'#(lf)            WHEN 11 THEN 'Delayed Auto-Process'#(lf)            WHEN 12 THEN 'Confirmed Fraud'#(lf)            ELSE null#(lf)        END                                                                        AS order_status,#(lf)      CAST('OMS' AS varchar(8)) AS source#(lf)  FROM oms_base r#(lf))#(lf)SELECT#(lf)  device_id,#(lf)  business_date,#(lf)  sequence_number,#(lf)  line_sequence_number,#(lf)  tax_line_sequence_number,#(lf)  authority_id,#(lf)  authority_type,#(lf)  group_id,#(lf)  rule_name,#(lf)  tax_type,#(lf)  tax_holiday_indicator,#(lf)  rate_rule_sequence_number,#(lf)  override_applied,#(lf)  tax_exempt_id,#(lf)  tax_exempt,#(lf)  tax_exempt_amount,#(lf)  override_percent,#(lf)  override_amount,#(lf)  override_reason_code,#(lf)  tax_percentage,#(lf)  tax_amount,#(lf)  money_tax_amount,#(lf)  taxable_amount,#(lf)  iso_currency_code,#(lf)  calculation_source,#(lf)  tax_included_in_price,#(lf)  voided,#(lf)  override_user_id,#(lf)  entry_method_code,#(lf)  create_time,#(lf)  create_by,#(lf)  last_update_time,#(lf)  last_update_by,#(lf)  rule_description,#(lf)  calculation_method,#(lf)  order_status_id,#(lf)  order_status_code,#(lf)  order_status,#(lf)  source#(lf)FROM jm_cur#(lf)UNION ALL#(lf)SELECT#(lf)  device_id,#(lf)  business_date,#(lf)  sequence_number,#(lf)  line_sequence_number,#(lf)  tax_line_sequence_number,#(lf)  authority_id,#(lf)  authority_type,#(lf)  group_id,#(lf)  rule_name,#(lf)  tax_type,#(lf)  tax_holiday_indicator,#(lf)  rate_rule_sequence_number,#(lf)  override_applied,#(lf)  tax_exempt_id,#(lf)  tax_exempt,#(lf)  tax_exempt_amount,#(lf)  override_percent,#(lf)  override_amount,#(lf)  override_reason_code,#(lf)  tax_percentage,#(lf)  tax_amount,#(lf)  money_tax_amount,#(lf)  taxable_amount,#(lf)  iso_currency_code,#(lf)  calculation_source,#(lf)  tax_included_in_price,#(lf)  voided,#(lf)  override_user_id,#(lf)  entry_method_code,#(lf)  create_time,#(lf)  create_by,#(lf)  last_update_time,#(lf)  last_update_by,#(lf)  rule_description,#(lf)  calculation_method,#(lf)  order_status_id,#(lf)  order_status_code,#(lf)  order_status,#(lf)  source#(lf)FROM ms_cur;", CommandTimeout=#duration(0, 0, 30, 0)]),
    #"Filtered Rows | Remove Voided Lines" = Table.SelectRows(Source, each [voided] = false),
    #"Renamed Columns" = Table.RenameColumns(#"Filtered Rows | Remove Voided Lines",{{"authority_id", "Authority Id"}, {"authority_type", "Authority Type"}, {"business_date", "Business Date"}, {"calculation_source", "Calculation Source"}, {"create_by", "Created By"}, {"create_time", "Created Datetime"}, {"device_id", "Device Id"}, {"entry_method_code", "Entry Method Code"}, {"group_id", "Group Id"}, {"iso_currency_code", "ISO Currency Code"}, {"last_update_by", "Last Updated By"}, {"last_update_time", "Last Updated Datetime"}, {"line_sequence_number", "Line Sequence Number"}, {"money_tax_amount", "Money Tax Amount (Native Currency)"}, {"override_amount", "Override Amount (Native Currency)"}, {"override_applied", "Override Applied"}, {"override_percent", "Override Percent"}, {"override_reason_code", "Override Reason Code"}, {"override_user_id", "Override User Id"}, {"rate_rule_sequence_number", "Rate Rule Sequence Number"}, {"rule_name", "Rule Name"}, {"sequence_number", "Sequence Number"}, {"tax_amount", "Tax Amount (Native Currency)"}, {"tax_exempt", "Tax Exempt"}, {"tax_exempt_amount", "Tax Exempt Amount (Native Currency)"}, {"tax_exempt_id", "Tax Exempt Id"}, {"tax_holiday_indicator", "Tax Holiday Indicator"}, {"tax_included_in_price", "Tax Included in Price"}, {"tax_line_sequence_number", "Tax Line Sequence Number"}, {"tax_percentage", "Tax Percentage"}, {"tax_type", "Tax Type"}, {"taxable_amount", "Taxable Amount (Native Currency)"}, {"voided", "Voided"}, {"rule_description", "Rule Description"}}),
    #"Removed Columns | Empty Columns" = Table.RemoveColumns(#"Renamed Columns",{"Entry Method Code"}),
    #"Merged Columns | Transaction Line Key" =
    Table.CombineColumns(
        Table.TransformColumns(
            Table.TransformColumnTypes(
                #"Removed Columns | Empty Columns",
                {{"Sequence Number", type text}, {"Line Sequence Number", type text}, {"Device Id", type text}},
                "en-US"
            ),
            {{"Business Date", each Date.ToText(Date.From(_), "yyyyMMdd"), type text}}
        ),
        {"Device Id", "Business Date", "Sequence Number", "Line Sequence Number"},
        Combiner.CombineTextByDelimiter("-", QuoteStyle.None),
        "Transaction Line Key"
    ),
    #"Divided Column | Percentages by 100" = Table.TransformColumns(#"Merged Columns | Transaction Line Key", {{"Override Percent", each _ / 100, type number}, {"Tax Percentage", each _ / 100, type number}}),
    #"Added Conditional Column | Tax Category" = Table.AddColumn(#"Divided Column | Percentages by 100", "Tax Category", each if [Tax Type] = "Fee" then "Fee" else if [Tax Type] = "Surcharge" then "Fee" else "Merchandise"),
    #"Replaced Value | IndigenousTaxExemption" = Table.ReplaceValue(#"Added Conditional Column | Tax Category","IndigenousTaxExemption","Indigenous Tax Exemption",Replacer.ReplaceText,{"Rule Name"}),
    #"Changed Type" = Table.TransformColumnTypes(#"Replaced Value | IndigenousTaxExemption",{{"Voided", type logical}, {"Tax Holiday Indicator", type logical}, {"Override Applied", type logical}, {"Tax Exempt", type logical}, {"Tax Included in Price", type logical}, {"Override Percent", Percentage.Type}, {"Tax Percentage", Percentage.Type}, {"Tax Category", type text}})
in
    #"Changed Type"
```

### Tender Card Lines (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH #(lf)pos_shaped AS (#(lf)  SELECT#(lf)      device_id AS device_id,#(lf)      CONVERT(varchar(8), TRY_CONVERT(date, business_date, 112), 112) AS business_date,#(lf)      sequence_number AS sequence_number,#(lf)      line_sequence_number AS line_sequence_number,#(lf)      CAST(brand AS varchar(200)) AS brand,#(lf)      CAST(card_name AS varchar(200)) AS card_name,#(lf)      CAST(code AS varchar(200)) AS code,#(lf)      CAST(type_code AS varchar(200)) AS type_code,#(lf)      CAST(payment_provider_code AS varchar(200)) AS payment_provider_code,#(lf)      CAST(masked_card_number AS varchar(64)) AS masked_card_number,#(lf)      CAST(entry_mode AS varchar(64)) AS entry_mode,#(lf)      CAST(service_code AS varchar(64)) AS service_code,#(lf)      CAST(expiration_date AS varchar(10)) AS expiration_date,#(lf)      ref_line_sequence_number AS ref_line_sequence_number,#(lf)      CAST(card_number AS varchar(64)) AS card_number,#(lf)      create_time AS create_time,#(lf)      create_by AS create_by,#(lf)      last_update_time AS last_update_time,#(lf)      last_update_by AS last_update_by,#(lf)      CAST(gift_card_action_code AS varchar(64)) AS gift_card_action_code,#(lf)      NULL                                                                       AS order_status_id,#(lf)      NULL                                                                       AS order_status_code,#(lf)      NULL                                                                       AS order_status,#(lf)      'POS' AS source#(lf)  FROM dbo.jumpmind_sls_card_line_item#(lf)  WHERE TRY_CONVERT(date, business_date, 112) >= DATEADD(month, -4, CAST(GETDATE() AS date))#(lf)),#(lf)op AS (#(lf)  SELECT#(lf)      TRY_CONVERT(int, op._ParentKeyField) AS ParentOrderID,#(lf)      CAST(op.ID AS bigint) AS OP_ID,#(lf)      op.InsertDate AS OP_InsertDate,#(lf)      op.UpdateDate AS OP_UpdateDate,#(lf)      CAST(op.PaymentProcessor AS varchar(200)) AS OP_PaymentProcessor,#(lf)      CAST(op.PaymentSubType  AS varchar(200)) AS OP_PaymentSubType,#(lf)      CAST(op.Generic1 AS varchar(200)) AS OP_TenderCode,#(lf)      CAST(op.Generic2 AS varchar(64)) AS OP_MaskedCardNumber,#(lf)      TRY_CONVERT(int, op.ExpirationMonth) AS OP_ExpMonth,#(lf)      TRY_CONVERT(int, op.ExpirationYear) AS OP_ExpYear#(lf)  FROM dbo.mulesoft_deckjsonraw_orderpayments op#(lf)  WHERE TRY_CONVERT(int, op._ParentKeyField) IS NOT NULL#(lf)    AND TRY_CONVERT(date, COALESCE(op.UpdateDate, op.InsertDate)) >= DATEADD(month, -4, CAST(GETDATE() AS date))#(lf)),#(lf)pt AS (#(lf)  SELECT#(lf)      CAST(pt.OrderPaymentId AS bigint) AS PT_OrderPaymentId,#(lf)      CAST(pt.PaymentTransactionTypeId AS int) AS PT_TypeId,#(lf)      Generic1 AS PT_CardNumber,#(lf)      CAST(pt.Amount AS decimal(18,6)) AS PT_Amount,#(lf)      CAST(pt.IsDecline AS bit) AS PT_IsDecline,#(lf)      pt.TransactionDateUTC AS PT_TransUTC,#(lf)      pt.InsertDate AS PT_InsertDate,#(lf)      pt.UpdateDate AS PT_UpdateDate#(lf)  FROM dbo.mulesoft_deckjsonraw_paymenttransactions pt#(lf)  WHERE TRY_CONVERT(date, COALESCE(pt.UpdateDate, pt.InsertDate, pt.TransactionDateUTC)) >= DATEADD(month, -4, CAST(GETDATE() AS date))#(lf)),#(lf)root AS (#(lf)  SELECT#(lf)      r.OrderID,#(lf)      r.OrderNumber,#(lf)      r.SiteCode,#(lf)      r.OrderStatus#(lf)  FROM dbo.mulesoft_deckjsonraw_root r#(lf)),#(lf)op_ranked AS (#(lf)  SELECT#(lf)      o.*,#(lf)      ROW_NUMBER() OVER (#(lf)        PARTITION BY o.ParentOrderID#(lf)        ORDER BY COALESCE(p.PT_UpdateDate, p.PT_InsertDate, o.OP_UpdateDate, o.OP_InsertDate) ASC, o.OP_ID#(lf)      ) AS rn#(lf)  FROM op o#(lf)  LEFT JOIN pt p#(lf)    ON p.PT_OrderPaymentId = o.OP_ID#(lf)),#(lf)oms_enriched AS (#(lf)  SELECT#(lf)      CAST((#(lf)        CASE #(lf)          WHEN rt.SiteCode = 'BAB' THEN '1013'#(lf)          WHEN rt.SiteCode = 'BABUK' THEN '2013'#(lf)          ELSE CAST(rt.SiteCode AS varchar(64))#(lf)        END#(lf)      ) + '-052' AS varchar(64)) AS device_id,#(lf)      CONVERT(varchar(8), CAST(p.PT_TransUTC AS date), 112) AS business_date, --I'M FORCING THE UTC DATE FOR BUSINESS DATE HERE#(lf)      CAST(rt.OrderID AS bigint) AS sequence_number,#(lf)      CAST(orx.rn AS int) AS line_sequence_number,#(lf)      CAST(o.OP_TenderCode AS varchar(200)) AS brand,#(lf)      CAST(NULL AS varchar(200)) AS card_name,#(lf)      CAST(o.OP_TenderCode AS varchar(200)) AS code,#(lf)      CASE#(lf)        WHEN UPPER(ISNULL(o.OP_PaymentSubType,'')) IN ('CASH','GIFTCARD') THEN o.OP_PaymentSubType#(lf)        ELSE 'Credit'#(lf)      END AS type_code,#(lf)      CAST(NULL AS varchar(200)) AS payment_provider_code,#(lf)      CAST(o.OP_MaskedCardNumber AS varchar(64)) AS masked_card_number,#(lf)      CAST(NULL AS varchar(64)) AS entry_mode,#(lf)      CAST(NULL AS varchar(64)) AS service_code,#(lf)      CASE#(lf)        WHEN ISNULL(o.OP_ExpMonth,0) BETWEEN 1 AND 12 AND ISNULL(o.OP_ExpYear,0) > 0#(lf)          THEN RIGHT('00'+CAST(o.OP_ExpMonth AS varchar(2)),2) + RIGHT(RIGHT('0000'+CAST(o.OP_ExpYear AS varchar(4)),4),2)#(lf)      END AS expiration_date,#(lf)      CAST(orx.rn AS int) AS ref_line_sequence_number,#(lf)      CAST(p.PT_CardNumber AS varchar(64)) AS card_number,          #(lf)      COALESCE(p.PT_InsertDate, o.OP_InsertDate) AS create_time,#(lf)      'sp_bab_pos_merge_webreturns' AS create_by,#(lf)      COALESCE(p.PT_UpdateDate, p.PT_InsertDate, o.OP_UpdateDate, o.OP_InsertDate) AS last_update_time,#(lf)      'sp_bab_pos_merge_webreturns' AS last_update_by,#(lf)      CAST(NULL AS varchar(64)) AS gift_card_action_code,#(lf)      rt.OrderStatus                                                              AS order_status_id,#(lf)        CASE rt.OrderStatus #(lf)            WHEN 1 THEN 'CO'#(lf)            WHEN 3 THEN 'AVS'#(lf)            WHEN 4 THEN 'P'#(lf)            WHEN 5 THEN 'PV'#(lf)            WHEN 6 THEN 'Z'#(lf)            WHEN 9 THEN 'MR'#(lf)            WHEN 10 THEN 'PS'#(lf)            WHEN 11 THEN 'DAP'#(lf)            WHEN 12 THEN 'CF'#(lf)            ELSE null#(lf)        END                                                                        AS order_status_code,#(lf)        CASE rt.OrderStatus #(lf)            WHEN 1 THEN 'New'#(lf)            WHEN 3 THEN 'Review'#(lf)            WHEN 4 THEN 'Pending'#(lf)            WHEN 5 THEN 'Exception'#(lf)            WHEN 6 THEN 'Completed'#(lf)            WHEN 9 THEN 'Manual Review'#(lf)            WHEN 10 THEN 'Pending Settlement'#(lf)            WHEN 11 THEN 'Delayed Auto-Process'#(lf)            WHEN 12 THEN 'Confirmed Fraud'#(lf)            ELSE null#(lf)        END                                                                        AS order_status,#(lf)      'OMS' AS source#(lf)  FROM op_ranked orx#(lf)  JOIN op o#(lf)    ON o.OP_ID = orx.OP_ID#(lf)  LEFT JOIN pt p#(lf)    ON p.PT_OrderPaymentId = o.OP_ID#(lf)  JOIN root rt#(lf)    ON rt.OrderID = orx.ParentOrderID#(lf)  WHERE TRY_CONVERT(date, COALESCE(p.PT_UpdateDate, p.PT_InsertDate, o.OP_UpdateDate, o.OP_InsertDate)) >= DATEADD(month, -4, CAST(GETDATE() AS date))#(lf))#(lf)SELECT *#(lf)FROM pos_shaped#(lf)UNION ALL#(lf)SELECT *#(lf)FROM oms_enriched#(lf);"]),
    #"Merged Columns | Transaction Line Key" = Table.CombineColumns(Table.TransformColumnTypes(Source, {{"sequence_number", type text}, {"ref_line_sequence_number", type text}}, "en-US"),{"device_id", "business_date", "sequence_number", "ref_line_sequence_number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Transaction Line Key"),
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

### Tender Lines (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="  WITH #(lf)pos_base AS (#(lf)  SELECT#(lf)      CAST(tli.device_id AS varchar(64))                                   AS device_id,#(lf)      CONVERT(varchar(8), TRY_CONVERT(date, tli.business_date, 112), 112)  AS business_date,#(lf)      CAST(tli.sequence_number AS bigint)                                   AS sequence_number,#(lf)      CAST(tli.line_sequence_number AS int)                                 AS line_sequence_number,#(lf)      -1                                                              as PaymentTransactionTypeId,#(lf)      NULL                                                              AS warehouse_code,#(lf)      CAST(tli.tender_code AS varchar(200))                                 AS tender_code,#(lf)      CAST(tli.tender_type_code AS varchar(200))                            AS tender_type_code,#(lf)      NULL                                                              AS payment_sub_type,#(lf)      CAST(tli.change_flag AS bit)                                          AS change_flag,#(lf)      CAST(tli.customer_account_number AS varchar(128))                     AS customer_account_number,#(lf)      CAST(tli.tender_account_number AS varchar(64))                        AS tender_account_number,#(lf)      CAST(tli.iso_currency_code AS varchar(10))                            AS iso_currency_code,#(lf)      NULL                                                              AS early_capture_amount,#(lf)      CAST(tli.tender_amount AS decimal(18,6))                              AS tender_amount,#(lf)      CAST(tli.cash_back_amount AS decimal(18,6))                           AS cash_back_amount,#(lf)      CAST(tli.iso_foreign_currency_code AS varchar(10))                    AS iso_foreign_currency_code,#(lf)      CAST(tli.foreign_currency_amount AS decimal(18,6))                    AS foreign_currency_amount,#(lf)      CAST(tli.exchange_rate AS decimal(18,6))                              AS exchange_rate,#(lf)      CAST(tli.overtendered AS bit)                                         AS overtendered,#(lf)      CAST(tli.partially_approved AS bit)                                   AS partially_approved,#(lf)      CAST(tli.tender_finance_id AS varchar(64))                            AS tender_finance_id,#(lf)      CAST(tli.certificate_number AS varchar(128))                          AS certificate_number,#(lf)      CAST(tli.post_void AS bit)                                            AS post_void,#(lf)      CAST(tli.voided AS bit)                                               AS voided,#(lf)      CAST(tli.override_user_id AS varchar(64))                             AS override_user_id,#(lf)      CAST(tli.entry_method_code AS varchar(64))                            AS entry_method_code,#(lf)      CAST(tli.create_time AS datetime2)                                    AS create_time,#(lf)      CAST(tli.create_by AS varchar(128))                                   AS create_by,#(lf)      CAST(tli.last_update_time AS datetime2)                               AS last_update_time,#(lf)      CAST(tli.last_update_by AS varchar(128))                              AS last_update_by,#(lf)      CAST(tli.tender_auth_method_code AS varchar(64))                      AS tender_auth_method_code,#(lf)      CAST(tli.tender_group AS varchar(64))                                 AS tender_group,#(lf)      CAST(tli.tender_id AS varchar(64))                                    AS tender_id,#(lf)      CAST(tli.voucher_id AS varchar(64))                                   AS voucher_id,#(lf)      NULL                                                              AS order_status_id,#(lf)      NULL                                                              AS order_status_code,#(lf)      NULL                                                              AS order_status,#(lf)      CAST('POS' AS varchar(8))                                         AS source,#(lf)      CAST('NONE' AS varchar(20))                                       AS reference_no,#(lf)      CAST(ts.tender1_auth_code AS varchar(64)) AS tender1_auth_code#(lf)  FROM dbo.jumpmind_sls_tender_line_item tli#(lf)      left join dbo.jumpmind_sls_trans_summary ts on #(lf)            TRY_CONVERT(date, ts.business_date) >= DATEADD(MONTH, -4, CAST(GETDATE() AS date))#(lf)            and tli.device_id = ts.device_id #(lf)            and tli.sequence_number = ts.sequence_number#(lf)            and tli.business_date = ts.business_date#(lf)  WHERE tli.create_by = 'openpos-sls'#(lf)    AND ISNULL(tli.voided,0) = 0#(lf)    AND TRY_CONVERT(date, tli.business_date, 112) >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 4 MONTHS#(lf)),#(lf)#(lf)root AS (#(lf)  SELECT#(lf)      r.OrderID,#(lf)      r.OrderNumber,#(lf)      r.OrderStatus,#(lf)      r._RowIndex as rootRowIndex,#(lf)      r.SiteCode,#(lf)      oi.WarehouseCode,#(lf)      CAST(COALESCE(r.OrderDateUTC, r.DateCreatedUTC, r.OrderStatusChangeDateUTC, r.ExportCreatedUTC) AS date) AS TransDate,#(lf)      r.OrderDateUTC,#(lf)      r.DateCreatedUTC,#(lf)      r.OrderStatusChangeDateUTC,#(lf)      r.ExportCreatedUTC#(lf)  FROM dbo.mulesoft_deckjsonraw_root r#(lf)  LEFT JOIN dbo.mulesoft_deckjsonraw_orderitems oi#(lf)    ON r.OrderID = oi._ParentKeyField#(lf)   AND oi._RowIndex = r._RowIndex#(lf)  WHERE CAST(COALESCE(r.OrderDateUTC, r.DateCreatedUTC, r.OrderStatusChangeDateUTC, r.ExportCreatedUTC) AS date)#(lf)        >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 2 MONTHS#(lf)),#(lf)hs AS (#(lf)  SELECT#(lf)      COALESCE(#(lf)        NULLIF(CONVERT(varchar(64), dtt.MaxWarehouseCode), ''),#(lf)        NULLIF(CONVERT(varchar(64), dtt.SiteWarehouseCode), ''),#(lf)        NULLIF(CONVERT(varchar(64), r.SiteCode), '')#(lf)      ) AS InventLocationId,#(lf)      r.*#(lf)  FROM root r#(lf)  LEFT JOIN dbo.mulesoft_dynamicstargettrans dtt#(lf)    ON CONVERT(varchar(64), dtt.OrderId) = CONVERT(varchar(64), r.OrderID)#(lf)),#(lf)hs_norm AS (#(lf)  SELECT#(lf)    CASE#(lf)      WHEN hs.InventLocationId = 'BAB'   THEN '1013'#(lf)      WHEN hs.InventLocationId = 'BABUK' THEN '2013'#(lf)      WHEN NULLIF(hs.InventLocationId,'') IS NULL THEN '9999'#(lf)      ELSE '9999'#(lf)    END AS InventLocationIdMapped,#(lf)    hs.*#(lf)  FROM hs#(lf)),#(lf)op AS (#(lf)  SELECT#(lf)      TRY_CONVERT(int, op._ParentKeyField)           AS ParentOrderID,#(lf)      CONVERT(varchar(64), op.ID)                    AS OrderPaymentId,#(lf)      CAST(op._RowIndex AS int)                      AS OP_RowIndex,#(lf)      CAST(op.PaymentProcessor AS varchar(200))      AS PaymentProcessor,#(lf)      CAST(op.PaymentSubType  AS varchar(200))       AS PaymentSubType,#(lf)      CAST(op.CardType        AS varchar(200))       AS CardType,#(lf)      CAST(op.AuthorizedAmount AS decimal(18,6))     AS AuthorizedAmount,#(lf)      CAST(op.EarlyCaptureAmount AS decimal(18,6))   AS EarlyCaptureAmount,#(lf)      CAST(op.CapturedAmount AS decimal(18,6))       AS CapturedAmount,#(lf)      CAST(op.CreditedAmount AS decimal(18,6))       AS CreditedAmount,#(lf)      op.InsertDate                                  AS OP_InsertDate,#(lf)      op.UpdateDate                                  AS OP_UpdateDate#(lf)  FROM dbo.mulesoft_deckjsonraw_orderpayments op#(lf)  WHERE TRY_CONVERT(int, op._ParentKeyField) IS NOT NULL#(lf)),#(lf)pt AS (#(lf)  SELECT Distinct ----YA (01/07/26): added distinct trying to remove duplicated rows#(lf)      CONVERT(varchar(64), pt.OrderPaymentId)        AS OrderPaymentId,#(lf)      pt._ParentKeyField                            AS OrderID,#(lf)      pt._RowIndex                                  AS PT_RowIndex,#(lf)      CAST(pt.PaymentTransactionTypeId AS int)       AS PaymentTransactionTypeId,#(lf)      CAST(pt.Amount AS decimal(18,6))               AS Amount,#(lf)      max(CAST(pt.TransactionDateUTC AS Date))                         AS TransactionDateUTC,#(lf)      max(CAST(pt.InsertDate AS Date)  )                                 AS PT_InsertDate,#(lf)      max(CAST(pt.UpdateDate    AS Date) )                              AS PT_UpdateDate,#(lf)      pt.Generic1                                    AS Generic1#(lf)  FROM dbo.mulesoft_deckjsonraw_paymenttransactions pt --YA (01/07/26): added this trying to remove duplicated rows because we use just these for define amounts below#(lf)  --where PaymentTransactionTypeId in (1,2,3,4,14)#(lf)  group by OrderPaymentId, _ParentKeyField, _RowIndex, PaymentTransactionTypeId, Amount, Generic1 --YA (01/07/26): added this & MAX functions trying to remove duplicated rows #(lf)),#(lf)#(lf)oms_base AS (#(lf)  SELECT#(lf)      CAST(COALESCE(hn.InventLocationIdMapped, '9999') + '-052' AS varchar(64)) AS device_id,#(lf)      CONVERT(varchar(8), hn.TransDate, 112)                  AS business_date,#(lf)      CAST(hn.OrderID AS bigint)                              AS sequence_number,#(lf)      ROW_NUMBER() OVER (#(lf)        PARTITION BY hn.OrderID#(lf)        ORDER BY COALESCE(pt.TransactionDateUTC, op.OP_UpdateDate, op.OP_InsertDate)#(lf)      )                                                      AS line_sequence_number,#(lf)      COALESCE(pt.PaymentTransactionTypeId, -1)                           AS PaymentTransactionTypeId,#(lf)      hn.WarehouseCode                                       AS warehouse_code,#(lf)      COALESCE(op.CardType, op.PaymentSubType, op.PaymentProcessor) AS tender_code,#(lf)      COALESCE(op.PaymentSubType, op.PaymentProcessor, op.CardType) AS tender_type_code,#(lf)      op.PaymentSubType                                      AS payment_sub_type,#(lf)      CAST(0 AS bit)                                         AS change_flag,#(lf)      CAST(NULL AS varchar(128))                             AS customer_account_number,#(lf)      CAST(NULL AS varchar(64))                              AS tender_account_number,#(lf)      CASE WHEN hn.InventLocationIdMapped = '2013' THEN 'GBP' ELSE 'USD' END AS iso_currency_code,#(lf)      op.EarlyCaptureAmount                                  AS early_capture_amount,#(lf)#(lf)      /* PT first; OP as fallback; final default 0 so never NULL */#(lf)      COALESCE(#(lf)        /* Prefer PT.Amount when present and non-zero */#(lf)        CASE#(lf)          WHEN pt.Amount IS NULL OR pt.Amount = 0 THEN NULL#(lf)          WHEN pt.PaymentTransactionTypeId IN (3,4,11) THEN -ABS(pt.Amount)#(lf)          WHEN pt.PaymentTransactionTypeId IN (1,2,10,14) THEN  ABS(pt.Amount)#(lf)          ELSE pt.Amount#(lf)        END,#(lf)        /* Fallbacks from OP */#(lf)        NULLIF(op.CapturedAmount, 0),#(lf)        NULLIF(op.AuthorizedAmount, 0),#(lf)        -1 * NULLIF(op.CreditedAmount, 0),#(lf)        /* Final default */#(lf)        0#(lf)      )                                                      AS tender_amount,#(lf)#(lf)      CAST(NULL AS decimal(18,6))                             AS cash_back_amount,#(lf)      CAST(NULL AS varchar(10))                               AS iso_foreign_currency_code,#(lf)      CAST(NULL AS decimal(18,6))                             AS foreign_currency_amount,#(lf)      CAST(NULL AS decimal(18,6))                             AS exchange_rate,#(lf)      CAST(0 AS bit)                                          AS overtendered,#(lf)      CAST(0 AS bit)                                          AS partially_approved,#(lf)      CAST(NULL AS varchar(64))                               AS tender_finance_id,#(lf)      CAST(NULL AS varchar(128))                              AS certificate_number,#(lf)      CAST(0 AS bit)                                          AS post_void,#(lf)      CAST(0 AS bit)                                          AS voided,#(lf)      CAST(NULL AS varchar(64))                               AS override_user_id,#(lf)      CAST(NULL AS varchar(64))                               AS entry_method_code,#(lf)      COALESCE(hn.OrderDateUTC, hn.DateCreatedUTC)            AS create_time,#(lf)      'sp_bab_pos_merge_webreturns'                           AS create_by,#(lf)      COALESCE(pt.PT_UpdateDate, pt.PT_InsertDate, hn.OrderStatusChangeDateUTC, hn.OrderDateUTC, hn.DateCreatedUTC) AS last_update_time,#(lf)      'sp_bab_pos_merge_webreturns'                           AS last_update_by,#(lf)      CAST(NULL AS varchar(64))                               AS tender_auth_method_code,#(lf)      'WEB'                                                   AS tender_group,#(lf)      CAST(NULL AS varchar(64))                               AS tender_id,#(lf)      CAST(NULL AS varchar(64))                               AS voucher_id,#(lf)      hn.OrderStatus                                          AS order_status_id,#(lf)        CASE hn.OrderStatus #(lf)            WHEN 1 THEN 'CO'#(lf)            WHEN 3 THEN 'AVS'#(lf)            WHEN 4 THEN 'P'#(lf)            WHEN 5 THEN 'PV'#(lf)            WHEN 6 THEN 'Z'#(lf)            WHEN 9 THEN 'MR'#(lf)            WHEN 10 THEN 'PS'#(lf)            WHEN 11 THEN 'DAP'#(lf)            WHEN 12 THEN 'CF'#(lf)            ELSE null#(lf)        END                                                    AS order_status_code,#(lf)        CASE hn.OrderStatus #(lf)            WHEN 1 THEN 'New'#(lf)            WHEN 3 THEN 'Review'#(lf)            WHEN 4 THEN 'Pending'#(lf)            WHEN 5 THEN 'Exception'#(lf)            WHEN 6 THEN 'Completed'#(lf)            WHEN 9 THEN 'Manual Review'#(lf)            WHEN 10 THEN 'Pending Settlement'#(lf)            WHEN 11 THEN 'Delayed Auto-Process'#(lf)            WHEN 12 THEN 'Confirmed Fraud'#(lf)            ELSE null#(lf)        END                                                    AS order_status,#(lf)#(lf)      'OMS'                                                   AS source,#(lf)      CAST(COALESCE(NULLIF(pt.Generic1, ''), 'NONE') AS varchar(20)) AS reference_no,#(lf)      CAST(COALESCE(NULLIF(pt.Generic1, ''), 'NONE') AS varchar(20)) AS tender1_auth_code#(lf)  FROM op op#(lf)  #(lf)  JOIN hs_norm hn#(lf)    ON hn.OrderID = op.ParentOrderID#(lf)   AND hn.rootRowIndex = op.OP_RowIndex#(lf)#(lf)  LEFT JOIN pt pt#(lf)    ON pt.OrderPaymentId = op.OrderPaymentId #(lf))#(lf)#(lf)SELECT *#(lf)FROM pos_base#(lf)UNION ALL#(lf)SELECT *#(lf)FROM oms_base#(lf);#(lf)#(lf)"]),
    #"Filtered Rows | Remove Voided Lines" = Table.SelectRows(Source, each [voided] = false),
    #"Renamed Columns" = Table.RenameColumns(#"Filtered Rows | Remove Voided Lines",{{"business_date", "Business Date"}, {"cash_back_amount", "Cash Back Amount (Native Currency)"}, {"certificate_number", "Certificate Number"}, {"change_flag", "Change Flag"}, {"create_by", "Created By"}, {"create_time", "Created Datetime"}, {"customer_account_number", "Customer Account Number"}, {"device_id", "Device Id"},{"early_capture_amount", "Early Capture Amount"}, {"entry_method_code", "Entry Method Code"}, {"exchange_rate", "Exchange Rate"}, {"foreign_currency_amount", "Foreign Currency Amount"}, {"iso_currency_code", "ISO Currency Code"}, {"iso_foreign_currency_code", "ISO Foreign Currency Code"}, {"last_update_by", "Last Updated By"}, {"last_update_time", "Last Updated Datetime"}, {"line_sequence_number", "Line Sequence Number"}, {"override_user_id", "Override User Id"}, {"overtendered", "Overtendered"}, {"partially_approved", "Partially Approved"}, {"payment_sub_type", "Payment Sub-Type"}, {"post_void", "Post Void"}, {"reference_no", "Reference No"}, {"sequence_number", "Sequence Number"}, {"tender_account_number", "Tender Account Number"}, {"tender_amount", "Tender Amount (Native Currency)"}, {"tender_code", "Tender Code"}, {"tender_finance_id", "Tender Finance Id"}, {"tender_type_code", "Tender Type Code"}, {"voided", "Voided"}, {"warehouse_code", "Warehouse Code"}}),
    #"Removed Columns | Empty Columns" = Table.RemoveColumns(#"Renamed Columns",{"Entry Method Code", "Tender Finance Id", "Certificate Number", "ISO Foreign Currency Code", "Foreign Currency Amount", "Customer Account Number", "Tender Account Number"}),
    #"Duplicated Column" = Table.DuplicateColumn(#"Removed Columns | Empty Columns", "Business Date", "Business Date - Copy"),
    #"Merged Columns | Transaction Key" = Table.CombineColumns(Table.TransformColumnTypes(#"Duplicated Column", {{"Sequence Number", type text}}, "en-US"),{"Device Id", "Business Date", "Sequence Number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Transaction Key"),
    #"Added Custom | Transaction Line Key" = Table.AddColumn(#"Merged Columns | Transaction Key", "Transaction Line Key", each [Transaction Key] & "-" & Text.From([Line Sequence Number])),
    #"Replaced Value | _ with SPACE" = Table.ReplaceValue(#"Added Custom | Transaction Line Key","_"," ",Replacer.ReplaceText,{"Tender Code", "Tender Type Code"}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Replaced Value | _ with SPACE",{{"Tender Code", Text.Proper, type text}, {"Tender Type Code", Text.Proper, type text}}),
    #"Replaced Value | Usd with USD" = Table.ReplaceValue(#"Capitalized Each Word","Usd","USD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Cad with CAD" = Table.ReplaceValue(#"Replaced Value | Usd with USD","Cad","CAD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Eur with EUR" = Table.ReplaceValue(#"Replaced Value | Cad with CAD","Eur","EUR",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Gbp with GBP" = Table.ReplaceValue(#"Replaced Value | Eur with EUR","Gbp","GBP",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Amex with American Express" = Table.ReplaceValue(#"Replaced Value | Gbp with GBP","Amex","American Express",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Giftcard with Gift Card" = Table.ReplaceValue(#"Replaced Value | Amex with American Express","Giftcard","Gift Card",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Adyen_GiftCard with Gift Card" = Table.ReplaceValue(#"Replaced Value | Giftcard with Gift Card","Adyen Giftcard","Gift Card",Replacer.ReplaceValue,{"Tender Type Code"}),
    #"Replaced Value | Mastercard with MasterCard" = Table.ReplaceValue(#"Replaced Value | Adyen_GiftCard with Gift Card","Mastercard","MasterCard",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | E Wallet with E-Wallet" = Table.ReplaceValue(#"Replaced Value | Mastercard with MasterCard","E Wallet","E-Wallet",Replacer.ReplaceText,{"Tender Type Code"}),
    #"Added Conditional Column | Charge Type" = Table.AddColumn(#"Replaced Value | E Wallet with E-Wallet", "Charge Type", each if [#"Tender Amount (Native Currency)"] < 0 then "Credit" else if [#"Tender Amount (Native Currency)"] >= 0 then "Debit" else null),
    #"Added Custom | Tender Object-Action" = Table.AddColumn(#"Added Conditional Column | Charge Type", "Tender Object-Action", each if [Charge Type] = "Debit" then [Tender Code] & " charged" else [Tender Code] & " credited"),
    #"Changed Type" = Table.TransformColumnTypes(#"Added Custom | Tender Object-Action",{{"Change Flag", type logical}, {"Voided", type logical}, {"Overtendered", type logical}, {"Partially Approved", type logical}, {"Post Void", type logical}, {"Charge Type", type text}, {"Tender Object-Action", type text}}),
    #"Renamed Columns | Business Date" = Table.RenameColumns(#"Changed Type",{{"Business Date - Copy", "Business Date"}}),
    #"Changed Type | Business Date" = Table.TransformColumnTypes(#"Renamed Columns | Business Date",{{"Business Date", type date}})
in
    #"Changed Type | Business Date"
```

### Tender Settlement Lines (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH pos_settlements AS (#(lf)  SELECT#(lf)      tsl.device_id,#(lf)      TRY_CONVERT(date, tsl.business_date, 112)         AS business_date,           -- safe parse#(lf)      CAST(tsl.sequence_number AS varchar(64))          AS sequence_number,#(lf)      tsl.line_sequence_number                          AS line_sequence_number,#(lf)      tsl.session_id,#(lf)      tsl.till_id,#(lf)      tsl.store_bank_id,#(lf)      tsl.tender_type_code,#(lf)      tsl.tender_code,#(lf)      tsl.iso_currency_code,#(lf)      tsl.open_session_amount,#(lf)      tsl.close_session_amount,#(lf)      tsl.counted_session_amount,#(lf)      tsl.over_under_session_amount,#(lf)      tsl.open_media_quantity,#(lf)      tsl.close_media_quantity,#(lf)      tsl.counted_media_quantity,#(lf)      tsl.over_under_media_quantity,#(lf)      tsl.from_repository,#(lf)      tsl.to_repository,#(lf)      tsl.pickup_amount,#(lf)      tsl.reason_code,#(lf)      tsl.difference_reason,#(lf)      CAST(ISNULL(tsl.voided,0) AS bit)                 AS voided,#(lf)      tsl.override_user_id,#(lf)      tsl.entry_method_code,#(lf)      tsl.create_time,#(lf)      tsl.create_by,#(lf)      tsl.last_update_time,#(lf)      tsl.last_update_by,#(lf)      tsl.expected_pickup_amount,#(lf)      tsl.bank_bag_number,#(lf)      'POS'                                             AS source#(lf)  FROM dbo.jumpmind_sls_tender_settlement_line_itm tsl#(lf)  WHERE TRY_CONVERT(date, tsl.business_date, 112) >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 4 MONTHS#(lf)),#(lf)oms_map AS (#(lf)  SELECT#(lf)      COALESCE(NULLIF(CONVERT(varchar(64), t.InventLocationId), ''), '') AS inventloc,#(lf)      CAST(t.TransDate AS date)                                          AS business_date,#(lf)      CONVERT(varchar(64), t.Barcode)                                    AS order_number,#(lf)      TRY_CONVERT(numeric(18,2), t.AmountCur)                            AS pickup_amount,#(lf)      CONVERT(varchar(128), t.NativePaymentMethod)                       AS tender_code,#(lf)      CONVERT(varchar(8), t.CurrencyCode)                                AS iso_currency_code,#(lf)      TRY_CONVERT(int, t.LineNum)                                        AS line_sequence_number,#(lf)      t.CreateTime                                                       AS create_time#(lf)  FROM dbo.mulesoft_dynamicstenderlineoms t#(lf)  WHERE CAST(t.TransDate AS date) >= DATEADD(month, -4, CAST(GETDATE() AS date))                    -- 4 MONTHS#(lf)),#(lf)oms_settlements AS (#(lf)  SELECT#(lf)      CONCAT(#(lf)        CASE#(lf)          WHEN om.inventloc = 'BAB'   THEN '1013'#(lf)          WHEN om.inventloc = 'BABUK' THEN '2013'#(lf)          WHEN NULLIF(om.inventloc,'') IS NULL THEN '9999'#(lf)          ELSE '9999'#(lf)        END,#(lf)        '-052'#(lf)      )                                                                  AS device_id,#(lf)      om.business_date                                                   AS business_date,#(lf)      om.order_number                                                    AS sequence_number,#(lf)      om.line_sequence_number                                            AS line_sequence_number,#(lf)      CAST(NULL AS varchar(64))                                          AS session_id,#(lf)      CAST(NULL AS varchar(64))                                          AS till_id,#(lf)      CAST(NULL AS varchar(64))                                          AS store_bank_id,#(lf)      CAST(NULL AS varchar(200))                                         AS tender_type_code,#(lf)      om.tender_code                                                     AS tender_code,#(lf)      om.iso_currency_code                                               AS iso_currency_code,#(lf)      CAST(NULL AS decimal(18,2))                                        AS open_session_amount,#(lf)      CAST(NULL AS decimal(18,2))                                        AS close_session_amount,#(lf)      CAST(NULL AS decimal(18,2))                                        AS counted_session_amount,#(lf)      CAST(NULL AS decimal(18,2))                                        AS over_under_session_amount,#(lf)      CAST(NULL AS int)                                                  AS open_media_quantity,#(lf)      CAST(NULL AS int)                                                  AS close_media_quantity,#(lf)      CAST(NULL AS int)                                                  AS counted_media_quantity,#(lf)      CAST(NULL AS int)                                                  AS over_under_media_quantity,#(lf)      CAST('' AS varchar(64))                                            AS from_repository,#(lf)      CAST('' AS varchar(64))                                            AS to_repository,#(lf)      om.pickup_amount                                                   AS pickup_amount,#(lf)      CAST(NULL AS varchar(200))                                         AS reason_code,#(lf)      CAST(NULL AS varchar(200))                                         AS difference_reason,#(lf)      CAST(0 AS bit)                                                     AS voided,#(lf)      CAST(NULL AS varchar(64))                                          AS override_user_id,#(lf)      CAST(NULL AS varchar(64))                                          AS entry_method_code,#(lf)      om.create_time                                                     AS create_time,#(lf)      CAST('deck-merge' AS varchar(128))                                 AS create_by,#(lf)      om.create_time                                                     AS last_update_time,#(lf)      CAST(NULL AS varchar(128))                                         AS last_update_by,#(lf)      om.pickup_amount                                                   AS expected_pickup_amount,#(lf)      CAST(NULL AS varchar(64))                                          AS bank_bag_number,#(lf)      'OMS'                                                              AS source#(lf)  FROM oms_map om#(lf))#(lf)SELECT * FROM pos_settlements#(lf)UNION ALL#(lf)SELECT * FROM oms_settlements;#(lf)"]),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"business_date", "Business Date"}, {"close_media_quantity", "Close Media Quantity"}, {"close_session_amount", "Close Session Amount"}, {"counted_media_quantity", "Counted Media Quantity"}, {"counted_session_amount", "Counted Session Amount"}, {"create_by", "Created By"}, {"create_time", "Created Datetime"}, {"device_id", "Device Id"}, {"difference_reason", "Difference Reason"}, {"entry_method_code", "Entry Method Code"}, {"from_repository", "From Repository"}, {"iso_currency_code", "ISO Currency Code"}, {"last_update_by", "Last Updated By"}, {"last_update_time", "Last Updated Datetime"}, {"line_sequence_number", "Line Sequence Number"}, {"open_media_quantity", "Open Media Quantity"}, {"open_session_amount", "Open Session Amount"}, {"over_under_media_quantity", "Over Under Media Quantity"}, {"over_under_session_amount", "Over Under Session Amount"}, {"override_user_id", "Override User Id"}, {"pickup_amount", "Pickup Amount"}, {"reason_code", "Reason Code"}, {"sequence_number", "Sequence Number"}, {"session_id", "Session Id"}, {"store_bank_id", "Store Bank Id"}, {"tender_code", "Tender Code"}, {"tender_type_code", "Tender Type Code"}, {"till_id", "Till Id"}, {"to_repository", "To Repository"}, {"voided", "Voided"}}),
    #"Removed Columns | Redundant Columns" = Table.RemoveColumns(#"Renamed Columns",{"Created Datetime", "Created By", "Last Updated By"}),
    #"Removed Columns | Empty Columns" = Table.RemoveColumns(#"Removed Columns | Redundant Columns",{"Entry Method Code"}),
    #"Filtered Rows | Remove Voided Lines" = Table.SelectRows(#"Removed Columns | Empty Columns", each [Voided] = false),
    #"Merged Columns | Transaction Key" =
        Table.CombineColumns(
            Table.TransformColumns(
                #"Filtered Rows | Remove Voided Lines",
                {
                    {"Device Id", each Text.From(_, "en-US"), type text},
                    {"Business Date",
                        each if Value.Is(_, type date)
                             then Date.ToText(_, "yyyyMMdd")
                             else DateTime.ToText(_, "yyyyMMdd"),
                     type text},
                    {"Sequence Number", each Text.From(_, "en-US"), type text}
                }
            ),
            {"Device Id", "Business Date", "Sequence Number"},
            Combiner.CombineTextByDelimiter("-", QuoteStyle.None),
            "Transaction Key"
        ),
    #"Replaced Value | _ with SPACE" = Table.ReplaceValue(#"Merged Columns | Transaction Key","_"," ",Replacer.ReplaceText,{"Tender Type Code", "Tender Code", "From Repository", "To Repository", "Reason Code"}),
    #"Uppercased Reason Code" = Table.TransformColumns(#"Replaced Value | _ with SPACE", {{"Reason Code", Text.Upper, type text}}),
    #"Reason Code | Insert Token Spaces 1" = Table.ReplaceValue(#"Uppercased Reason Code","OPEN","OPEN ",Replacer.ReplaceText,{"Reason Code"}),
    #"Reason Code | Insert Token Spaces 2" = Table.ReplaceValue(#"Reason Code | Insert Token Spaces 1","CLOSE","CLOSE ",Replacer.ReplaceText,{"Reason Code"}),
    #"Reason Code | Insert Token Spaces 3" = Table.ReplaceValue(#"Reason Code | Insert Token Spaces 2","STORE","STORE ",Replacer.ReplaceText,{"Reason Code"}),
    #"Reason Code | Insert Token Spaces 4" = Table.ReplaceValue(#"Reason Code | Insert Token Spaces 3","NONCOUNTED","NON-COUNTED ",Replacer.ReplaceText,{"Reason Code"}),
    #"Reason Code | Insert Token Spaces 5" = Table.ReplaceValue(#"Reason Code | Insert Token Spaces 4","TENDERUNITCOUNT"," TENDER UNIT COUNT",Replacer.ReplaceText,{"Reason Code"}),
    #"Replaced Value | E WALLET with E-Wallet" = Table.ReplaceValue(#"Reason Code | Insert Token Spaces 5","E WALLET","E-Wallet",Replacer.ReplaceText,{"Reason Code"}),
    #"Capitalized Each Word | Reason Code" = Table.TransformColumns(#"Replaced Value | E WALLET with E-Wallet",{{"Reason Code", Text.Proper, type text}}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Capitalized Each Word | Reason Code",{{"Tender Type Code", Text.Proper, type text}, {"From Repository", Text.Proper, type text}, {"To Repository", Text.Proper, type text}}),
    #"Added Prefix | FromSPACE" = Table.TransformColumns(#"Capitalized Each Word", {{"From Repository", each "From " & _, type text}}),
    #"Added Prefix | toSPACE" = Table.TransformColumns(#"Added Prefix | FromSPACE", {{"To Repository", each "to " & _, type text}}),
    #"Merged Columns | Repository Transfer Type" = Table.CombineColumns(#"Added Prefix | toSPACE",{"From Repository", "To Repository"},Combiner.CombineTextByDelimiter(" ", QuoteStyle.None),"Repository Transfer Type"),
    #"Changed Type" = Table.TransformColumnTypes(#"Merged Columns | Repository Transfer Type",{{"Voided", type logical}}),
    #"Reordered Columns" = Table.ReorderColumns(#"Changed Type",{"Transaction Key", "Line Sequence Number", "Session Id", "Till Id", "Store Bank Id", "Tender Type Code", "Tender Code", "ISO Currency Code", "Repository Transfer Type", "Reason Code", "Open Session Amount", "Close Session Amount", "Counted Session Amount", "Over Under Session Amount", "Pickup Amount", "Difference Reason", "Open Media Quantity", "Close Media Quantity", "Counted Media Quantity", "Over Under Media Quantity", "Voided", "Override User Id"}),
    #"Replaced Value | E Wallet with E-Wallet" = Table.ReplaceValue(#"Reordered Columns","E Wallet","E-Wallet",Replacer.ReplaceText,{"Tender Code"}),
    #"Capitalized Each Word2" = Table.TransformColumns(#"Replaced Value | E Wallet with E-Wallet",{{"Tender Code", Text.Proper, type text}}),
    #"Replaced Value | Usd with USD" = Table.ReplaceValue(#"Capitalized Each Word2","Usd","USD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Cad with CAD" = Table.ReplaceValue(#"Replaced Value | Usd with USD","Cad","CAD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Eur with EUR" = Table.ReplaceValue(#"Replaced Value | Cad with CAD","Eur","EUR",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Gbp with GBP" = Table.ReplaceValue(#"Replaced Value | Eur with EUR","Gbp","GBP",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Hkd with HKD" = Table.ReplaceValue(#"Replaced Value | Gbp with GBP","Hkd","HKD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Mxn with MXN" = Table.ReplaceValue(#"Replaced Value | Hkd with HKD","Mxn","MXN",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Amex with American Express" = Table.ReplaceValue(#"Replaced Value | Mxn with MXN","Amex","American Express",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Mastercard with MasterCard" = Table.ReplaceValue(#"Replaced Value | Amex with American Express","Mastercard","MasterCard",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Globale with Global-e" = Table.ReplaceValue(#"Replaced Value | Mastercard with MasterCard","Globale","Global-e",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Applepay with Apple Pay" = Table.ReplaceValue(#"Replaced Value | Globale with Global-e","Applepay","Apple Pay",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Giftcard with Gift Card" = Table.ReplaceValue(#"Replaced Value | Applepay with Apple Pay","Giftcard","Gift Card",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Paypal with PayPal" = Table.ReplaceValue(#"Replaced Value | Giftcard with Gift Card","Paypal","PayPal",Replacer.ReplaceText,{"Tender Code"})
in
    #"Replaced Value | Paypal with PayPal"
```

### Tenders (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH pos_norm AS (#(lf)  SELECT DISTINCT#(lf)      CAST(tender_code                AS varchar(200))  AS tender_code,#(lf)      CAST(tender_type_code           AS varchar(200))  AS tender_type_code,#(lf)      CAST(COALESCE(iso_currency_code,'*') AS varchar(16)) AS iso_currency_code,#(lf)      CAST([description]              AS varchar(400))  AS [description],#(lf)      CAST(cash_drawer_open_required  AS bit)           AS cash_drawer_open_required,#(lf)      CAST(till_unit_count_required   AS bit)           AS till_unit_count_required,#(lf)      CAST(till_amount_count_required AS bit)           AS till_amount_count_required,#(lf)      CAST(return_tender_type_code    AS varchar(200))  AS return_tender_type_code,#(lf)      CAST('POS' AS varchar(8))                         AS source,#(lf)      1                                                 AS source_rank#(lf)  FROM dbo.jumpmind_sls_tender#(lf)),#(lf)oms_raw AS (#(lf)  SELECT DISTINCT#(lf)      UPPER(NULLIF(LTRIM(RTRIM(op.PaymentProcessor)) ,'')) AS pproc,#(lf)      UPPER(NULLIF(LTRIM(RTRIM(op.PaymentSubType))  ,''))  AS psub,#(lf)      UPPER(NULLIF(LTRIM(RTRIM(op.CardType))        ,''))  AS ctype#(lf)  FROM dbo.mulesoft_deckjsonraw_orderpayments op#(lf)  WHERE op._ParentKeyField IS NOT NULL#(lf)),#(lf)oms_norm AS (#(lf)  SELECT DISTINCT#(lf)      CASE#(lf)        WHEN psub LIKE '%APPLEPAY%'  OR pproc LIKE 'ADYEN_APPLEPAY%'  THEN 'Apple Pay'#(lf)        WHEN psub LIKE '%GOOGLEPAY%' OR pproc LIKE 'ADYEN_GOOGLEPAY%' THEN 'Google Pay'#(lf)        WHEN psub LIKE '%PAYPAL%'    OR pproc LIKE 'ADYEN_PAYPAL%'    THEN 'PayPal'#(lf)        WHEN psub LIKE '%GIFTCARD%'  OR pproc LIKE 'ADYEN_GIFTCARD%'  THEN 'Giftcard'#(lf)        WHEN psub LIKE '%KLARNA%'    OR pproc LIKE 'ADYEN_KLARNA%'    THEN 'Klarna'#(lf)        WHEN psub LIKE '%AFTERPAY%'  OR pproc LIKE 'ADYEN_AFTERPAY%'  THEN 'Afterpay'#(lf)        WHEN ctype IN ('VISA','VISA CREDIT','VISA DEBIT')             THEN 'Visa'#(lf)        WHEN ctype IN ('MASTERCARD','MC','MASTERCARD CREDIT','MASTERCARD DEBIT') THEN 'Mastercard'#(lf)        WHEN ctype IN ('DISCOVER','DISCOVER CREDIT','DISCOVER DEBIT') THEN 'Discover'#(lf)        WHEN ctype IN ('AMEX','AMERICAN EXPRESS','AMERICANEXPRESS')   THEN 'American Express'#(lf)        WHEN pproc LIKE 'GLOBAL%E' OR pproc='GLOBALE'                 THEN 'Global-E'#(lf)        WHEN pproc = 'CASH'                                           THEN 'Cash'#(lf)        WHEN pproc <> ''                                              THEN pproc#(lf)        ELSE 'Other'#(lf)      END AS tender_code,#(lf)      CASE#(lf)        WHEN psub LIKE '%APPLEPAY%'  OR pproc LIKE 'ADYEN_APPLEPAY%'  THEN 'E-Wallet'#(lf)        WHEN psub LIKE '%GOOGLEPAY%' OR pproc LIKE 'ADYEN_GOOGLEPAY%' THEN 'E-Wallet'#(lf)        WHEN psub LIKE '%PAYPAL%'    OR pproc LIKE 'ADYEN_PAYPAL%'    THEN 'E-Wallet'#(lf)        WHEN psub LIKE '%GIFTCARD%'  OR pproc LIKE 'ADYEN_GIFTCARD%'  THEN 'E-Wallet'#(lf)        WHEN psub LIKE '%KLARNA%'    OR pproc LIKE 'ADYEN_KLARNA%'    THEN 'E-Wallet'#(lf)        WHEN psub LIKE '%AFTERPAY%'  OR pproc LIKE 'ADYEN_AFTERPAY%'  THEN 'E-Wallet'#(lf)        WHEN pproc LIKE 'GLOBAL%E'   OR pproc='GLOBALE'               THEN 'Globale'#(lf)        WHEN pproc = 'CASH'                                           THEN 'Cash'#(lf)        WHEN pproc = 'CYBERSOURCE'                                    THEN 'Cybersource'#(lf)        WHEN pproc LIKE 'ADYEN%'                                      THEN 'E-Wallet'#(lf)        WHEN ctype IN ('VISA','MASTERCARD','MC','DISCOVER','AMEX','AMERICAN EXPRESS','AMERICANEXPRESS') THEN 'Credit Card'#(lf)        ELSE COALESCE(NULLIF(pproc,''),'Other')#(lf)      END AS tender_type_code,#(lf)      CAST('*' AS varchar(16)) AS iso_currency_code,#(lf)      CASE#(lf)        WHEN psub LIKE '%APPLEPAY%'  OR pproc LIKE 'ADYEN_APPLEPAY%'  THEN 'ADYEN_APPLEPAY'#(lf)        WHEN psub LIKE '%GOOGLEPAY%' OR pproc LIKE 'ADYEN_GOOGLEPAY%' THEN 'ADYEN_GOOGLEPAY'#(lf)        WHEN psub LIKE '%PAYPAL%'    OR pproc LIKE 'ADYEN_PAYPAL%'    THEN 'ADYEN_PAYPAL'#(lf)        WHEN psub LIKE '%GIFTCARD%'  OR pproc LIKE 'ADYEN_GIFTCARD%'  THEN 'ADYEN_GIFTCARD'#(lf)        WHEN psub LIKE '%KLARNA%'    OR pproc LIKE 'ADYEN_KLARNA%'    THEN 'ADYEN_KLARNA'#(lf)        WHEN psub LIKE '%AFTERPAY%'  OR pproc LIKE 'ADYEN_AFTERPAY%'  THEN 'ADYEN_AFTERPAY'#(lf)        WHEN pproc LIKE 'GLOBAL%E'   OR pproc='GLOBALE'               THEN 'GLOBAL_E'#(lf)        WHEN pproc = 'CASH'                                           THEN 'CASH'#(lf)        WHEN pproc = 'CYBERSOURCE'                                    THEN 'CYBERSOURCE'#(lf)        WHEN ctype IN ('VISA','MASTERCARD','MC','DISCOVER','AMEX','AMERICAN EXPRESS','AMERICANEXPRESS') THEN COALESCE(ctype,'CREDIT')#(lf)        ELSE COALESCE(NULLIF(pproc,''),'OTHER')#(lf)      END AS [description],#(lf)      CAST(0 AS bit) AS cash_drawer_open_required,#(lf)      CAST(0 AS bit) AS till_unit_count_required,#(lf)      CAST(0 AS bit) AS till_amount_count_required,#(lf)      CASE#(lf)        WHEN psub LIKE '%APPLEPAY%'  OR pproc LIKE 'ADYEN_APPLEPAY%'  THEN 'E-Wallet'#(lf)        WHEN psub LIKE '%GOOGLEPAY%' OR pproc LIKE 'ADYEN_GOOGLEPAY%' THEN 'E-Wallet'#(lf)        WHEN psub LIKE '%PAYPAL%'    OR pproc LIKE 'ADYEN_PAYPAL%'    THEN 'E-Wallet'#(lf)        WHEN psub LIKE '%GIFTCARD%'  OR pproc LIKE 'ADYEN_GIFTCARD%'  THEN 'E-Wallet'#(lf)        WHEN psub LIKE '%KLARNA%'    OR pproc LIKE 'ADYEN_KLARNA%'    THEN 'E-Wallet'#(lf)        WHEN psub LIKE '%AFTERPAY%'  OR pproc LIKE 'ADYEN_AFTERPAY%'  THEN 'E-Wallet'#(lf)        WHEN pproc LIKE 'GLOBAL%E'   OR pproc='GLOBALE'               THEN 'Globale'#(lf)        WHEN pproc = 'CASH'                                           THEN 'Cash'#(lf)        WHEN pproc = 'CYBERSOURCE'                                    THEN 'Cybersource'#(lf)        WHEN pproc LIKE 'ADYEN%'                                      THEN 'E-Wallet'#(lf)        WHEN ctype IN ('VISA','MASTERCARD','MC','DISCOVER','AMEX','AMERICAN EXPRESS','AMERICANEXPRESS') THEN 'Credit Card'#(lf)        ELSE COALESCE(NULLIF(pproc,''),'Other')#(lf)      END AS return_tender_type_code,#(lf)      CAST('OMS' AS varchar(8)) AS source,#(lf)      2 AS source_rank#(lf)  FROM oms_raw#(lf)  WHERE COALESCE(pproc, ctype, psub) IS NOT NULL#(lf)),#(lf)unioned AS (#(lf)  SELECT * FROM pos_norm#(lf)  UNION ALL#(lf)  SELECT * FROM oms_norm#(lf)),#(lf)dedup AS (#(lf)  SELECT *#(lf)  FROM (#(lf)    SELECT u.*,#(lf)           ROW_NUMBER() OVER (PARTITION BY tender_code#(lf)                              ORDER BY source_rank, tender_type_code) AS rn#(lf)    FROM unioned u#(lf)  ) d#(lf)  WHERE rn = 1#(lf))#(lf)SELECT#(lf)  tender_code,#(lf)  tender_type_code,#(lf)  iso_currency_code,#(lf)  [description],#(lf)  cash_drawer_open_required,#(lf)  till_unit_count_required,#(lf)  till_amount_count_required,#(lf)  return_tender_type_code,#(lf)  source#(lf)FROM dedup#(lf)ORDER BY tender_code;", CreateNavigationProperties=false]),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"cash_drawer_open_required", "Cash Drawer Open Required"}, {"description", "Description"}, {"iso_currency_code", "ISO Currency Code"}, {"return_tender_type_code", "Return Tender Type Code"}, {"tender_code", "Tender Code"}, {"tender_type_code", "Tender Type Code"}, {"till_amount_count_required", "Till Amount Count Required"}, {"till_unit_count_required", "Till Unit Count Required"}}),
    #"Sorted Rows" = Table.Sort(#"Renamed Columns",{{"Tender Code", Order.Ascending}}),
    #"Replaced Value | _ with SPACE" = Table.ReplaceValue(#"Sorted Rows","_"," ",Replacer.ReplaceText,{"Tender Code", "Tender Type Code", "Return Tender Type Code"}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Replaced Value | _ with SPACE",{{"Tender Code", Text.Proper, type text}, {"Return Tender Type Code", Text.Proper, type text}, {"Tender Type Code", Text.Proper, type text}}),
    #"Replaced Value | Cad with CAD" = Table.ReplaceValue(#"Capitalized Each Word","Cad","CAD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Eur with EUR" = Table.ReplaceValue(#"Replaced Value | Cad with CAD","Eur","EUR",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Gbp with GBP" = Table.ReplaceValue(#"Replaced Value | Eur with EUR","Gbp","GBP",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Hkd with HKD" = Table.ReplaceValue(#"Replaced Value | Gbp with GBP","Hkd","HKD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Mxn with MXN" = Table.ReplaceValue(#"Replaced Value | Hkd with HKD","Mxn","MXN",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Usd with USD" = Table.ReplaceValue(#"Replaced Value | Mxn with MXN","Usd","USD",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Amex with American Express" = Table.ReplaceValue(#"Replaced Value | Usd with USD","Amex","American Express",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | Applepay with Apple Pay" = Table.ReplaceValue(#"Replaced Value | Amex with American Express","Applepay","Apple Pay",Replacer.ReplaceText,{"Tender Code", "Description"}),
    #"Replaced Value | Paypal with PayPal" = Table.ReplaceValue(#"Replaced Value | Applepay with Apple Pay","Paypal","PayPal",Replacer.ReplaceText,{"Tender Code"}),
    #"Replaced Value | E Wallet with E-Wallet" = Table.ReplaceValue(#"Replaced Value | Paypal with PayPal","E Wallet","E-Wallet",Replacer.ReplaceText,{"Tender Type Code", "Return Tender Type Code"}),
    #"Replaced Value | Apply pay with Apple Pay" = Table.ReplaceValue(#"Replaced Value | E Wallet with E-Wallet","Apply pay","Apple Pay",Replacer.ReplaceText,{"Description"}),
    #"Changed Type" = Table.TransformColumnTypes(#"Replaced Value | Apply pay with Apple Pay",{{"Cash Drawer Open Required", type logical}, {"Till Unit Count Required", type logical}, {"Till Amount Count Required", type logical}}),
    #"Removed Duplicates" = Table.Distinct(#"Changed Type", {"Tender Code"})
in
    #"Removed Duplicates"
```

### Transaction Summaries (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH pos_base AS (#(lf)#(lf)  SELECT#(lf)#(lf)      CAST(device_id AS varchar(64)) AS device_id,#(lf)#(lf)      CAST(business_date AS varchar(16)) AS business_date,#(lf)#(lf)      CAST(sequence_number AS varchar(50)) AS sequence_number,#(lf)#(lf)      CAST(barcode AS varchar(100)) AS barcode,#(lf)#(lf)      CAST(begin_time AS datetime2) AS begin_time,#(lf)#(lf)      CAST(business_unit_id AS varchar(32)) AS business_unit_id,#(lf)#(lf)      CAST(client_offset AS varchar(32)) AS client_offset,#(lf)#(lf)      CAST(create_by AS varchar(128)) AS create_by,#(lf)#(lf)      CAST(create_time AS datetime2) AS create_time,#(lf)#(lf)      CAST(customer_id AS varchar(64)) AS customer_id,#(lf)#(lf)      CAST(customer_name AS varchar(256)) AS customer_name,#(lf)#(lf)      CAST(device_type AS varchar(64)) AS device_type,#(lf)#(lf)      CAST(discount_total AS decimal(18,6)) AS discount_total,#(lf)#(lf)      CAST(employee_id_for_discount AS varchar(64)) AS employee_id_for_discount,#(lf)#(lf)      CAST(end_time AS datetime2) AS end_time,#(lf)#(lf)      CAST(iso_currency_code AS varchar(16)) AS iso_currency_code,#(lf)#(lf)      CAST(item_count AS int) AS item_count,#(lf)#(lf)      CAST(last_update_by AS varchar(128)) AS last_update_by,#(lf)#(lf)      CAST(last_update_time AS datetime2) AS last_update_time,#(lf)#(lf)      CAST(local_offset AS varchar(32)) AS local_offset,#(lf)#(lf)      CAST(loyalty_card_number AS varchar(64)) AS loyalty_card_number,#(lf)#(lf)      CAST(loyalty_rewards_count AS int) AS loyalty_rewards_count,#(lf)#(lf)      CAST(loyalty_rewards_total AS decimal(18,6)) AS loyalty_rewards_total,#(lf)#(lf)      CAST(mfr_coupons_count AS int) AS mfr_coupons_count,#(lf)#(lf)      CAST(mfr_coupons_non_taxable_count AS int) AS mfr_coupons_non_taxable_count,#(lf)#(lf)      CAST(mfr_coupons_non_taxable_total AS decimal(18,6)) AS mfr_coupons_non_taxable_total,#(lf)#(lf)      CAST(mfr_coupons_taxable_count AS int) AS mfr_coupons_taxable_count,#(lf)#(lf)      CAST(mfr_coupons_taxable_total AS decimal(18,6)) AS mfr_coupons_taxable_total,#(lf)#(lf)      CAST(mfr_coupons_total AS decimal(18,6)) AS mfr_coupons_total,#(lf)#(lf)      CAST(non_rcpt_rtn_count AS int) AS non_rcpt_rtn_count,#(lf)#(lf)      CAST(paid_to AS varchar(64)) AS paid_to,#(lf)#(lf)      CAST(pre_tender_balance_due AS decimal(18,6)) AS pre_tender_balance_due,#(lf)#(lf)      CAST(rcpt_rtn_count AS int) AS rcpt_rtn_count,#(lf)#(lf)      CAST(resumed_device_id AS varchar(64)) AS resumed_device_id,#(lf)#(lf)      CAST(resumed_sequence_number AS varchar(50)) AS resumed_sequence_number,#(lf)#(lf)      CAST(session_id AS varchar(64)) AS session_id,#(lf)#(lf)      CAST(store_bank_id AS varchar(64)) AS store_bank_id,#(lf)#(lf)      CAST(store_electronic_promos_count AS int) AS store_electronic_promos_count,#(lf)#(lf)      CAST(store_electronic_promos_total AS decimal(18,6)) AS store_electronic_promos_total,#(lf)#(lf)      CAST(store_physical_coupons_count AS int) AS store_physical_coupons_count,#(lf)#(lf)      CAST(store_physical_coupons_total AS decimal(18,6)) AS store_physical_coupons_total,#(lf)#(lf)      CAST(store_promos_count AS int) AS store_promos_count,#(lf)#(lf)      CAST(store_promos_non_taxable_count AS int) AS store_promos_non_taxable_count,#(lf)#(lf)      CAST(store_promos_non_taxable_total AS decimal(18,6)) AS store_promos_non_taxable_total,#(lf)#(lf)      CAST(store_promos_taxable_count AS int) AS store_promos_taxable_count,#(lf)#(lf)      CAST(store_promos_taxable_total AS decimal(18,6)) AS store_promos_taxable_total,#(lf)#(lf)      CAST(store_promos_total AS decimal(18,6)) AS store_promos_total,#(lf)#(lf)      CAST(suspended_device_id AS varchar(64)) AS suspended_device_id,#(lf)#(lf)      CAST(suspended_sequence_number AS varchar(50)) AS suspended_sequence_number,#(lf)#(lf)      CAST(tax_total AS decimal(18,6)) AS tax_total,#(lf)#(lf)      CAST(tender_type_codes AS varchar(200)) AS tender_type_codes,#(lf)#(lf)      CAST(tender1_amount AS decimal(18,6)) AS tender1_amount,#(lf)#(lf)      CAST(tender1_auth_code AS varchar(64)) AS tender1_auth_code,#(lf)#(lf)      CAST(tender1_card_type_code AS varchar(64)) AS tender1_card_type_code,#(lf)#(lf)      CAST(tender1_masked_card_number AS varchar(64)) AS tender1_masked_card_number,#(lf)#(lf)      CAST(tender1_type_code AS varchar(64)) AS tender1_type_code,#(lf)#(lf)      CAST(tender2_amount AS decimal(18,6)) AS tender2_amount,#(lf)#(lf)      CAST(tender2_auth_code AS varchar(64)) AS tender2_auth_code,#(lf)#(lf)      CAST(tender2_card_type_code AS varchar(64)) AS tender2_card_type_code,#(lf)#(lf)      CAST(tender2_masked_card_number AS varchar(64)) AS tender2_masked_card_number,#(lf)#(lf)      CAST(tender2_type_code AS varchar(64)) AS tender2_type_code,#(lf)#(lf)      CAST(tender3_amount AS decimal(18,6)) AS tender3_amount,#(lf)#(lf)      CAST(tender3_auth_code AS varchar(64)) AS tender3_auth_code,#(lf)#(lf)      CAST(tender3_card_type_code AS varchar(64)) AS tender3_card_type_code,#(lf)#(lf)      CAST(tender3_masked_card_number AS varchar(64)) AS tender3_masked_card_number,#(lf)#(lf)      CAST(tender3_type_code AS varchar(64)) AS tender3_type_code,#(lf)#(lf)      CAST(tender4_amount AS decimal(18,6)) AS tender4_amount,#(lf)#(lf)      CAST(tender4_auth_code AS varchar(64)) AS tender4_auth_code,#(lf)#(lf)      CAST(tender4_card_type_code AS varchar(64)) AS tender4_card_type_code,#(lf)#(lf)      CAST(tender4_masked_card_number AS varchar(64)) AS tender4_masked_card_number,#(lf)#(lf)      CAST(tender4_type_code AS varchar(64)) AS tender4_type_code,#(lf)#(lf)      CAST(tender5_amount AS decimal(18,6)) AS tender5_amount,#(lf)#(lf)      CAST(tender5_auth_code AS varchar(64)) AS tender5_auth_code,#(lf)#(lf)      CAST(tender5_card_type_code AS varchar(64)) AS tender5_card_type_code,#(lf)#(lf)      CAST(tender5_masked_card_number AS varchar(64)) AS tender5_masked_card_number,#(lf)#(lf)      CAST(tender5_type_code AS varchar(64)) AS tender5_type_code,#(lf)#(lf)      CAST(till_id AS varchar(64)) AS till_id,#(lf)#(lf)      CAST(total AS decimal(18,6)) AS total,#(lf)#(lf)      CAST(total_physical_coupons_count AS int) AS total_physical_coupons_count,#(lf)#(lf)      CAST(training_mode AS bit) AS training_mode,#(lf)#(lf)      CAST(trans_status_code AS varchar(64)) AS trans_status_code,#(lf)#(lf)      CAST(transaction_duration_in_sec AS int) AS transaction_duration_in_sec,#(lf)#(lf)      CAST(username AS varchar(64)) AS username,#(lf)#(lf)      CAST(voidable_flag AS bit) AS voidable_flag,#(lf)#(lf)      CAST(voided_sequence_number AS varchar(50)) AS voided_sequence_number,#(lf)#(lf)      CAST(trans_type_code AS varchar(64)) AS trans_type_code,#(lf)#(lf)      CAST(reason_code AS varchar(64)) AS reason_code,#(lf)      NULL                                                                       AS order_status_id,#(lf)      NULL                                                                       AS order_status_code,#(lf)      NULL                                                                       AS order_status,#(lf)#(lf)      CAST('POS' AS varchar(8)) AS source#(lf)#(lf)  FROM dbo.jumpmind_sls_trans_summary s#(lf)#(lf)  WHERE TRY_CONVERT(date, s.business_date) >= DATEADD(MONTH, -4, CAST(GETDATE() AS date))#(lf)#(lf)),#(lf)#(lf)oms_root AS (#(lf)#(lf)  SELECT#(lf)#(lf)      r.OrderID,#(lf)#(lf)      r.OrderNumber,#(lf)      r.OrderStatus,#(lf)#(lf)      r.SiteCode,#(lf)#(lf)      COALESCE(#(lf)#(lf)        TRY_CONVERT(datetime2(7), r.OrderDateUTC),#(lf)#(lf)        TRY_CONVERT(datetime2(7), r.DateCreatedUTC),#(lf)#(lf)        TRY_CONVERT(datetime2(7), r.UpdateDate)#(lf)#(lf)      ) AS biz_dt_raw,#(lf)#(lf)      COALESCE(#(lf)#(lf)        TRY_CONVERT(datetime2(7), r.UpdateDate),#(lf)#(lf)        TRY_CONVERT(datetime2(7), r.LastUpdateUTC),#(lf)#(lf)        TRY_CONVERT(datetime2(7), r.OrderDateUTC),#(lf)#(lf)        TRY_CONVERT(datetime2(7), r.DateCreatedUTC)#(lf)#(lf)      ) AS last_upd_raw#(lf)#(lf)  FROM dbo.mulesoft_deckjsonraw_root r#(lf)#(lf)  WHERE TRY_CONVERT(date, COALESCE(r.OrderDateUTC, r.DateCreatedUTC, r.UpdateDate)) >= DATEADD(MONTH, -4, CAST(GETDATE() AS date))#(lf)#(lf)),#(lf)#(lf)oms_header AS (#(lf)#(lf)  SELECT#(lf)#(lf)      rf.OrderID,#(lf)#(lf)      rf.OrderNumber,#(lf)      rf.OrderStatus, #(lf)#(lf)      rf.SiteCode,#(lf)#(lf)      CAST(CAST(rf.biz_dt_raw AS date) AS date) AS business_date,#(lf)#(lf)      (#(lf)#(lf)        CASE #(lf)#(lf)          WHEN rf.SiteCode = 'BAB'   THEN '1013'#(lf)#(lf)          WHEN rf.SiteCode = 'BABUK' THEN '2013'#(lf)#(lf)          ELSE CAST(rf.SiteCode AS varchar(64))#(lf)#(lf)        END#(lf)#(lf)      ) + '-052' AS device_id,#(lf)#(lf)      CASE WHEN rf.SiteCode = 'BABUK' THEN 'GBP'#(lf)#(lf)           WHEN rf.SiteCode = 'BAB'   THEN 'USD'#(lf)#(lf)           ELSE '*' END AS iso_currency_code,#(lf)#(lf)      rf.last_upd_raw AS last_update_time#(lf)#(lf)  FROM oms_root rf#(lf)#(lf)),#(lf)#(lf)oms_payments AS (#(lf)#(lf)  SELECT#(lf)#(lf)      TRY_CONVERT(int, pt._ParentKeyField) AS OrderID,#(lf)#(lf)      pt.Amount AS tender1_amount,#(lf)#(lf)      pt.Generic1 AS tender1_auth_code,#(lf)#(lf)      pt.PaymentTransactionTypeId AS tender1_type_code,#(lf)#(lf)      CASE WHEN NULLIF(pt.Generic1, '') IS NOT NULL THEN '****' + RIGHT(pt.Generic1, 4) END AS tender1_masked_card_number#(lf)#(lf)  FROM dbo.mulesoft_deckjsonraw_paymenttransactions pt#(lf)#(lf)  WHERE TRY_CONVERT(date, pt.TransactionDateUTC) >= DATEADD(MONTH, -4, CAST(GETDATE() AS date))#(lf)#(lf)    AND TRY_CONVERT(int, pt._ParentKeyField) IS NOT NULL#(lf)#(lf)    --AND pt.PaymentTransactionTypeId = 10   -- <= added filter so we only pull tender1_auth_code for paymenttransactiontypeid = 10#(lf)#(lf)),#(lf)#(lf)oms_base AS (#(lf)#(lf)  SELECT#(lf)#(lf)      CAST(oh.device_id AS varchar(64)) AS device_id,#(lf)#(lf)      CAST(FORMAT(oh.business_date, 'yyyyMMdd') AS varchar(16)) AS business_date,#(lf)#(lf)      CAST(oh.OrderID AS varchar(50)) AS sequence_number,#(lf)#(lf)      CAST(NULL AS varchar(100)) AS barcode,#(lf)#(lf)      CAST(NULL AS datetime2) AS begin_time,#(lf)#(lf)      CAST(NULL AS varchar(32)) AS business_unit_id,#(lf)#(lf)      CAST(NULL AS varchar(32)) AS client_offset,#(lf)#(lf)      CAST(NULL AS varchar(128)) AS create_by,#(lf)#(lf)      CAST(NULL AS datetime2) AS create_time,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS customer_id,#(lf)#(lf)      CAST(NULL AS varchar(256)) AS customer_name,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS device_type,#(lf)#(lf)      CAST(NULL AS decimal(18,6)) AS discount_total,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS employee_id_for_discount,#(lf)#(lf)      CAST(NULL AS datetime2) AS end_time,#(lf)#(lf)      CAST(oh.iso_currency_code AS varchar(16)) AS iso_currency_code,#(lf)#(lf)      CAST(NULL AS int) AS item_count,#(lf)#(lf)      CAST(NULL AS varchar(128)) AS last_update_by,#(lf)#(lf)      CAST(oh.last_update_time AS datetime2) AS last_update_time,#(lf)#(lf)      CAST(NULL AS varchar(32)) AS local_offset,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS loyalty_card_number,#(lf)#(lf)      CAST(NULL AS int) AS loyalty_rewards_count,#(lf)#(lf)      CAST(NULL AS decimal(18,6)) AS loyalty_rewards_total,#(lf)#(lf)      CAST(NULL AS int) AS mfr_coupons_count,#(lf)#(lf)      CAST(NULL AS int) AS mfr_coupons_non_taxable_count,#(lf)#(lf)      CAST(NULL AS decimal(18,6)) AS mfr_coupons_non_taxable_total,#(lf)#(lf)      CAST(NULL AS int) AS mfr_coupons_taxable_count,#(lf)#(lf)      CAST(NULL AS decimal(18,6)) AS mfr_coupons_taxable_total,#(lf)#(lf)      CAST(NULL AS decimal(18,6)) AS mfr_coupons_total,#(lf)#(lf)      CAST(NULL AS int) AS non_rcpt_rtn_count,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS paid_to,#(lf)#(lf)      CAST(NULL AS decimal(18,6)) AS pre_tender_balance_due,#(lf)#(lf)      CAST(NULL AS int) AS rcpt_rtn_count,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS resumed_device_id,#(lf)#(lf)      CAST(NULL AS varchar(50)) AS resumed_sequence_number,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS session_id,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS store_bank_id,#(lf)#(lf)      CAST(NULL AS int) AS store_electronic_promos_count,#(lf)#(lf)      CAST(NULL AS decimal(18,6)) AS store_electronic_promos_total,#(lf)#(lf)      CAST(NULL AS int) AS store_physical_coupons_count,#(lf)#(lf)      CAST(NULL AS decimal(18,6)) AS store_physical_coupons_total,#(lf)#(lf)      CAST(NULL AS int) AS store_promos_count,#(lf)#(lf)      CAST(NULL AS int) AS store_promos_non_taxable_count,#(lf)#(lf)      CAST(NULL AS decimal(18,6)) AS store_promos_non_taxable_total,#(lf)#(lf)      CAST(NULL AS int) AS store_promos_taxable_count,#(lf)#(lf)      CAST(NULL AS decimal(18,6)) AS store_promos_taxable_total,#(lf)#(lf)      CAST(NULL AS decimal(18,6)) AS store_promos_total,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS suspended_device_id,#(lf)#(lf)      CAST(NULL AS varchar(50)) AS suspended_sequence_number,#(lf)#(lf)      CAST(NULL AS decimal(18,6)) AS tax_total,#(lf)#(lf)      CAST(NULL AS varchar(200)) AS tender_type_codes,#(lf)#(lf)      CAST(pt.tender1_amount AS decimal(18,6)) AS tender1_amount,#(lf)#(lf)      CAST(pt.tender1_auth_code AS varchar(64)) AS tender1_auth_code,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS tender1_card_type_code,#(lf)#(lf)      CAST(pt.tender1_masked_card_number AS varchar(64)) AS tender1_masked_card_number,#(lf)#(lf)      CAST(pt.tender1_type_code AS varchar(64)) AS tender1_type_code,#(lf)#(lf)      CAST(NULL AS decimal(18,6)) AS tender2_amount,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS tender2_auth_code,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS tender2_card_type_code,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS tender2_masked_card_number,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS tender2_type_code,#(lf)#(lf)      CAST(NULL AS decimal(18,6)) AS tender3_amount,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS tender3_auth_code,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS tender3_card_type_code,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS tender3_masked_card_number,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS tender3_type_code,#(lf)#(lf)      CAST(NULL AS decimal(18,6)) AS tender4_amount,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS tender4_auth_code,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS tender4_card_type_code,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS tender4_masked_card_number,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS tender4_type_code,#(lf)#(lf)      CAST(NULL AS decimal(18,6)) AS tender5_amount,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS tender5_auth_code,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS tender5_card_type_code,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS tender5_masked_card_number,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS tender5_type_code,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS till_id,#(lf)#(lf)      CAST(NULL AS decimal(18,6)) AS total,#(lf)#(lf)      CAST(NULL AS int) AS total_physical_coupons_count,#(lf)#(lf)      CAST(NULL AS bit) AS training_mode,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS trans_status_code,#(lf)#(lf)      CAST(NULL AS int) AS transaction_duration_in_sec,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS username,#(lf)#(lf)      CAST(NULL AS bit) AS voidable_flag,#(lf)#(lf)      CAST(NULL AS varchar(50)) AS voided_sequence_number,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS trans_type_code,#(lf)#(lf)      CAST(NULL AS varchar(64)) AS reason_code,#(lf)      OrderStatus                                                              AS order_status_id,#(lf)        CASE OrderStatus #(lf)            WHEN 1 THEN 'CO'#(lf)            WHEN 3 THEN 'AVS'#(lf)            WHEN 4 THEN 'P'#(lf)            WHEN 5 THEN 'PV'#(lf)            WHEN 6 THEN 'Z'#(lf)            WHEN 9 THEN 'MR'#(lf)            WHEN 10 THEN 'PS'#(lf)            WHEN 11 THEN 'DAP'#(lf)            WHEN 12 THEN 'CF'#(lf)            ELSE null#(lf)        END                                                                        AS order_status_code,#(lf)        CASE OrderStatus #(lf)            WHEN 1 THEN 'New'#(lf)            WHEN 3 THEN 'Review'#(lf)            WHEN 4 THEN 'Pending'#(lf)            WHEN 5 THEN 'Exception'#(lf)            WHEN 6 THEN 'Completed'#(lf)            WHEN 9 THEN 'Manual Review'#(lf)            WHEN 10 THEN 'Pending Settlement'#(lf)            WHEN 11 THEN 'Delayed Auto-Process'#(lf)            WHEN 12 THEN 'Confirmed Fraud'#(lf)            ELSE null#(lf)        END                                                                        AS order_status,#(lf)#(lf)      CAST('OMS' AS varchar(8)) AS source#(lf)#(lf)  FROM oms_header oh#(lf)#(lf)  LEFT JOIN oms_payments pt ON pt.OrderID = oh.OrderID#(lf)#(lf))#(lf)#(lf)SELECT * FROM pos_base#(lf)#(lf)UNION ALL#(lf)#(lf)SELECT * FROM oms_base"]),
#"Merged Columns | Transaction Key" =
    Table.CombineColumns(
        Table.TransformColumns(
            Source,
            {
                {"device_id", each Text.From(_), type text},
                {"business_date",
                    each if Value.Is(_, type date) then Date.ToText(_, "yyyy-MM-dd")
                    else if Value.Is(_, type datetime) then Date.ToText(DateTime.Date(_), "yyyy-MM-dd")
                    else if Value.Is(_, type datetimezone) then Date.ToText(DateTime.Date(DateTimeZone.RemoveZone(_)), "yyyy-MM-dd")
                    else Text.From(_),
                    type text
                },
                {"sequence_number", each Text.From(_), type text}
            }
        ),
        {"device_id","business_date","sequence_number"},
        Combiner.CombineTextByDelimiter("-", QuoteStyle.None),
        "Transaction Key"
    ),
    #"Renamed Columns" = Table.RenameColumns(#"Merged Columns | Transaction Key",{{"barcode", "Barcode"}, {"begin_time", "Begin Time"},  {"business_unit_id", "Business Unit Id"}, {"client_offset", "Client Offset"}, {"create_by", "Created By"}, {"create_time", "Created Datetime"}, {"customer_id", "Customer Id"}, {"customer_name", "Customer Name"}, {"device_type", "Device Type"}, {"discount_total", "Discount Total"}, {"employee_id_for_discount", "Employee Id for Discount"}, {"end_time", "End Time"}, {"iso_currency_code", "ISO Currency Code"}, {"item_count", "Item Count"}, {"last_update_by", "Last Updated By"}, {"last_update_time", "Last Updated Datetime"}, {"local_offset", "Local Offset"}, {"loyalty_card_number", "Loyalty Card Number"}, {"loyalty_rewards_count", "Loyalty Rewards Count"}, {"loyalty_rewards_total", "Loyalty Rewards Total"}, {"mfr_coupons_count", "Manufacturer Coupons Count"}, {"mfr_coupons_non_taxable_count", "Manufacturer Coupons Non-taxable Count"}, {"mfr_coupons_non_taxable_total", "Manufacturer Coupons Non-taxable Total"}, {"mfr_coupons_taxable_count", "Manufacturer Coupons Taxable Count"}, {"mfr_coupons_taxable_total", "Manufacturer Coupons Taxable Total"}, {"mfr_coupons_total", "Manufacturer Coupons Total"}, {"non_rcpt_rtn_count", "Non-Receipt Return Count"}, {"paid_to", "Paid To"}, {"pre_tender_balance_due", "Pre-tender Balance Due"}, {"rcpt_rtn_count", "Receipt Return Count"}, {"resumed_device_id", "Resumed Device Id"}, {"resumed_sequence_number", "Resumed Sequence Number"}, {"session_id", "Session Id"}, {"store_bank_id", "Store Bank Id"}, {"store_electronic_promos_count", "Store Electronic Promos Count"}, {"store_electronic_promos_total", "Store Electronic Promos Total"}, {"store_physical_coupons_count", "Store Physical Coupons Count"}, {"store_physical_coupons_total", "Store Physical Coupons Total"}, {"store_promos_count", "Store Promos Count"}, {"store_promos_non_taxable_count", "Store Promos Non-taxable Count"}, {"store_promos_non_taxable_total", "Store Promos Non-taxable Total"}, {"store_promos_taxable_count", "Store Promos Taxable Count"}, {"store_promos_taxable_total", "Store Promos Taxable Total"}, {"store_promos_total", "Store Promos Total"}, {"suspended_device_id", "Suspended Device Id"}, {"suspended_sequence_number", "Suspended Sequence Number"}, {"tax_total", "Tax Total"}, {"tender_type_codes", "Tender Type Codes"}, {"tender1_amount", "Tender1 Amount"}, {"tender1_auth_code", "Tender1 Authorization Code"}, {"tender1_card_type_code", "Tender1 Card Type Code"}, {"tender1_masked_card_number", "Tender1 Masked Card Number"}, {"tender1_type_code", "Tender1 Type Code"}, {"tender2_amount", "Tender2 Amount"}, {"tender2_auth_code", "Tender2 Authorization Code"}, {"tender2_card_type_code", "Tender2 Card Type Code"}, {"tender2_masked_card_number", "Tender2 Masked Card Number"}, {"tender2_type_code", "Tender2 Type Code"}, {"tender3_amount", "Tender3 Amount"}, {"tender3_auth_code", "Tender3 Authorization Code"}, {"tender3_card_type_code", "Tender3 Card Type Code"}, {"tender3_masked_card_number", "Tender3 Masked Card Number"}, {"tender3_type_code", "Tender3 Type Code"}, {"tender4_amount", "Tender4 Amount"}, {"tender4_auth_code", "Tender4 Authorization Code"}, {"tender4_card_type_code", "Tender4 Card Type Code"}, {"tender4_masked_card_number", "Tender4 Masked Card Number"}, {"tender4_type_code", "Tender4 Type Code"}, {"tender5_amount", "Tender5 Amount"}, {"tender5_auth_code", "Tender5 Authorization Code"}, {"tender5_card_type_code", "Tender5 Card Type Code"}, {"tender5_masked_card_number", "Tender5 Masked Card Number"}, {"tender5_type_code", "Tender5 Type Code"}, {"till_id", "Till Id"}, {"total", "Total"}, {"total_physical_coupons_count", "Total Physical Coupons Count"}, {"training_mode", "Training Mode"}, {"trans_status_code", "Transaction Status Code"}, {"transaction_duration_in_sec", "Transaction Duration (in Seconds)"}, {"username", "Username"}, {"voidable_flag", "Voidable Flag"}, {"voided_sequence_number", "Voided Sequence Number"}, {"trans_type_code", "Transaction Type Code"}, {"reason_code", "Reason Code"}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Renamed Columns",{{"Training Mode", type logical}, {"Voidable Flag", type logical}}),
    #"Removed Columns | Redundant Columns" = Table.RemoveColumns(#"Changed Type",{"Business Unit Id", "Username", "Begin Time", "End Time", "Local Offset", "Training Mode", "Barcode", "Session Id", "Till Id", "Customer Id", "Loyalty Card Number", "Customer Name", "Employee Id for Discount", "Voidable Flag", "Item Count", "Receipt Return Count", "Non-Receipt Return Count", "Total", "Pre-tender Balance Due", "Tax Total", "Discount Total", "Tender Type Codes", "Created Datetime", "Created By", "Last Updated By", "Transaction Type Code", "Transaction Status Code"}),
    #"Removed Columns | Empty Columns" = Table.RemoveColumns(#"Removed Columns | Redundant Columns",{"Device Type"}),
    #"Removed Duplicates" = Table.Distinct(#"Removed Columns | Empty Columns", {"Transaction Key"})
in
    #"Removed Duplicates"
```

### Users (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH deck_base AS (#(lf)  SELECT#(lf)      LOWER(LTRIM(RTRIM(#(lf)        COALESCE(NULLIF(CONVERT(varchar(256), r.LockedByName), ''),#(lf)                 NULLIF(CONVERT(varchar(256), r.SourceAgent), ''))#(lf)      )))                               AS username_norm,#(lf)      NULLIF(CONVERT(varchar(256), r.LockedByName), '') AS locked_by_name,#(lf)      NULLIF(CONVERT(varchar(256), r.SourceAgent),  '') AS source_agent,#(lf)      NULLIF(CONVERT(varchar(128), r.MembershipID), '') AS membership_id,#(lf)      r.SiteCode,#(lf)      COALESCE(r.OrderDateUTC, r.DateCreatedUTC, r.LastUpdateUTC) AS activity_dt#(lf)  FROM dbo.mulesoft_deckjsonraw_root r#(lf)  WHERE (NULLIF(CONVERT(varchar(256), r.LockedByName), '') IS NOT NULL#(lf)      OR NULLIF(CONVERT(varchar(256), r.SourceAgent),  '') IS NOT NULL)#(lf)),#(lf)agent_site_rank AS (#(lf)  SELECT#(lf)      username_norm,#(lf)      SiteCode,#(lf)      ROW_NUMBER() OVER (#(lf)        PARTITION BY username_norm#(lf)        ORDER BY COUNT(*) DESC, MAX(activity_dt) DESC#(lf)      ) AS rn#(lf)  FROM deck_base#(lf)  GROUP BY username_norm, SiteCode#(lf)),#(lf)agent_top_site AS (#(lf)  SELECT username_norm, SiteCode#(lf)  FROM agent_site_rank#(lf)  WHERE rn = 1#(lf)),#(lf)deck_agents AS (#(lf)  SELECT#(lf)      b.username_norm AS username,#(lf)      MAX(b.membership_id)              AS alternate_id,#(lf)      MAX(b.activity_dt)                AS last_login,#(lf)      ts.SiteCode                       AS site_code#(lf)  FROM deck_base b#(lf)  LEFT JOIN agent_top_site ts#(lf)    ON ts.username_norm = b.username_norm#(lf)  GROUP BY b.username_norm, ts.SiteCode#(lf))#(lf)#(lf)SELECT#(lf)    business_unit_id,#(lf)    username,#(lf)    last_name,#(lf)    first_name,#(lf)    last_login,#(lf)    locked_out_flag,#(lf)    alternate_id,#(lf)    workgroup_id,#(lf)    user_active_flag,#(lf)    'POS' AS source#(lf)FROM dbo.jumpmind_bab_active_user#(lf)#(lf)UNION ALL#(lf)#(lf)SELECT#(lf)    CASE#(lf)      WHEN da.site_code = 'BAB'   THEN 1013#(lf)      WHEN da.site_code = 'BABUK' THEN 2013#(lf)      ELSE NULL#(lf)    END                           AS business_unit_id,#(lf)    da.username                   AS username,#(lf)    CAST(NULL AS varchar(200))    AS last_name,#(lf)    CAST(NULL AS varchar(200))    AS first_name,#(lf)    da.last_login                 AS last_login,#(lf)    CAST(NULL AS bit)             AS locked_out_flag,#(lf)    da.alternate_id               AS alternate_id,#(lf)    CAST(NULL AS varchar(64))     AS workgroup_id,#(lf)    CAST(1 AS bit)                AS user_active_flag,#(lf)    'OMS'                         AS source#(lf)FROM deck_agents da;", CreateNavigationProperties=false]),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"alternate_id", "Alternate Id"}, {"business_unit_id", "Business Unit Id"},  {"first_name", "First Name"}, {"last_login", "Last Login"}, {"last_name", "Last Name"},  {"locked_out_flag", "Locked Out Flag"}, {"user_active_flag", "User Active Flag"}, {"username", "Username Id"}, {"workgroup_id", "Workgroup Id"}}),
    #"Added Custom | Username Key" = 
    Table.AddColumn(
        #"Renamed Columns",
        "Username Key",
        each Text.From([Business Unit Id], "en-US") & "-" & Text.From([Username Id], "en-US"),
        type text
    ),
    #"Removed Duplicates | Username Key" = Table.Distinct(#"Added Custom | Username Key", {"Username Key"}),
    #"Inserted Merged Column | Username" = Table.AddColumn(#"Removed Duplicates | Username Key", "Username", each Text.Combine({[First Name], [Last Name]}, " "), type text),
    #"Added Conditional Column | Work Group" = Table.AddColumn(#"Inserted Merged Column | Username", "Work Group", each if Text.Contains([Workgroup Id], "BB") then "Bear Builder" else if Text.Contains([Workgroup Id], "SL") then "Sales Lead" else if Text.Contains([Workgroup Id], "AWM") then "Assistant Workshop Manager" else if Text.Contains([Workgroup Id], "CWM") then "Chief Workshop Manager" else if Text.Contains([Workgroup Id], "Bear Builder") then "Bear Builder" else if Text.Contains([Workgroup Id], "Sales Lead") then "Sales Lead" else if Text.Contains([Workgroup Id], "Assistant Workshop Manager") then "Assistant Workshop Manager" else if Text.Contains([Workgroup Id], "Chief Workshop Manager") then "Chief Workshop Manager" else if Text.Contains([Workgroup Id], "WM") then "Workshop Manager (Other)" else if Text.Contains([Workgroup Id], "DM") then "District Manager" else if Text.Contains([Workgroup Id], "SRVDSK") then "Service Desk" else if [Workgroup Id] = null then null else "Other"),
    #"Replaced Errors" = Table.ReplaceErrorValues(#"Added Conditional Column | Work Group", {{"Work Group", null}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Replaced Errors",{{"Locked Out Flag", type logical}, {"User Active Flag", type logical}, {"Username Key", type text}, {"Work Group", type text}})
in
    #"Changed Type"
```

### Transactions (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH pos AS (#(lf)  SELECT#(lf)      null                                                                  AS OrderNumber,  #(lf)      CAST(device_id AS varchar(64))                                        AS device_id,#(lf)      CAST(business_date AS varchar(8))                                     AS business_date,#(lf)#(tab)    TRY_CONVERT(datetime2(6), last_update_time) #(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)            AS Capture_Date,#(lf)      CAST(#(lf)            TRY_CONVERT(datetime2(6), last_update_time) #(lf)            AT TIME ZONE 'UTC' #(lf)            AT TIME ZONE 'Central Standard Time' #(lf)            AS datetime2(6))                                                AS Capture_Date_CST,#(lf)      CAST(sequence_number AS varchar(50))                                  AS sequence_number,#(lf)      CAST(trans_type AS varchar(64))                                       AS trans_type,#(lf)      CAST(trans_status AS varchar(64))                                     AS trans_status,#(lf)      TRY_CONVERT(int, business_unit_id)                                    AS business_unit_id,#(lf)      TRY_CONVERT(int, business_unit_id)                                    AS invent_location_id_mapped,#(lf)      null                                                                  AS register,#(lf)      dh.eCommOrderType                                                     AS eCommOrderType,#(lf)      CAST(username AS varchar(64))                                         AS username,#(lf)      TRY_CONVERT(datetime2(6), begin_time)                                 AS begin_time,#(lf)      TRY_CONVERT(datetime2(6), end_time)                                   AS end_time,#(lf)      TRY_CONVERT(int, local_offset)                                        AS local_offset,#(lf)      TRY_CONVERT(int, client_offset)                                       AS client_offset,#(lf)      TRY_CONVERT(bit, keyed_offline)                                       AS keyed_offline,#(lf)      CAST(override_user_id AS varchar(64))                                 AS override_user_id,#(lf)      CAST(barcode AS varchar(64))                                          AS barcode,#(lf)      TRY_CONVERT(bit, training_mode)                                       AS training_mode,#(lf)      CAST(session_id AS varchar(64))                                       AS session_id,#(lf)      CAST(trans_pin AS varchar(64))                                        AS trans_pin,#(lf)      CAST(till_id AS varchar(64))                                          AS till_id,#(lf)      CAST(app_id AS varchar(64))                                           AS app_id,#(lf)      CAST(app_version AS varchar(64))                                      AS app_version,#(lf)      TRY_CONVERT(datetime2(6), create_time)                                AS create_time,#(lf)      CAST(create_by AS varchar(128))                                       AS create_by,#(lf)      TRY_CONVERT(datetime2(6), last_update_time)                           AS last_update_time,#(lf)      CAST(last_update_by AS varchar(128))                                  AS last_update_by,#(lf)      CAST(suspended_trans_data AS varchar(max))                            AS suspended_trans_data,#(lf)      CAST(bank_bag_number AS varchar(64))                                  AS bank_bag_number,#(lf)      CAST(RetailTransactionId AS varchar(64))                              AS retail_transaction_id,#(lf)      null                                                                  AS gross_line_amount,#(lf)      null                                                                  AS tender_total,#(lf)      NULL                                                                  AS order_status_id,#(lf)      NULL                                                                  AS order_status_code,#(lf)      NULL                                                                  AS order_status,#(lf)      'POS'                                                                 AS source,#(lf)      CAST('NONE' AS varchar(20))                                           AS reference_no,#(lf)      NULL                                                                  AS WarehouseCode,#(lf)      NULL AS Tender_Total_Transaction_Level,  #(lf)      NULL AS PaymentTransactionTypeId#(lf)  FROM dbo.jumpmind_sls_trans t#(lf)  LEFT JOIN dbo.mulesoft_dynamicsheader dh ON dh.TransactionKey = concat(t.device_id, '-', t.business_date, '-', t.sequence_number)#(lf)  WHERE create_by = 'openpos-sls'#(lf)    AND TRY_CONVERT(date, business_date, 112) >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 4 months#(lf)),#(lf)pt AS (#(lf)   SELECT Distinct #(lf)      CONVERT(varchar(64), pt.OrderPaymentId)       AS OrderPaymentId,#(lf)      pt._ParentKeyField                            AS OrderID,#(lf)#(tab)  TRY_CONVERT(datetime2(6), TransactionDateUTC) AS Capture_Date,#(lf)      pt.Generic1                                   AS Generic1,#(lf)      Amount                                        AS Tender_Total_Transaction_Level,#(lf)      PaymentTransactionTypeId#(lf)  FROM dbo.mulesoft_deckjsonraw_paymenttransactions pt #(lf)  WHERE CAST(pt.TransactionDateUTC AS date)#(lf)        >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 4 MONTHS#(lf) ),#(lf)root_warehouse AS (#(lf)  SELECT#(lf)      r.OrderID,#(lf)      oi.WarehouseCode#(lf)  FROM dbo.mulesoft_deckjsonraw_root r#(lf)  LEFT JOIN dbo.mulesoft_deckjsonraw_orderitems oi#(lf)    ON r.OrderID = oi._ParentKeyField#(lf)   AND oi._RowIndex = r._RowIndex#(lf)  WHERE CAST(COALESCE(r.OrderDateUTC, r.DateCreatedUTC, r.OrderStatusChangeDateUTC, r.ExportCreatedUTC) AS date)#(lf)        >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 4 MONTHS#(lf)),#(lf)#(lf)oms_root AS (#(lf)  SELECT#(lf)      r.OrderID,#(lf)      r.OrderNumber,#(lf)      r.OrderStatus,#(lf)      r.UserID,#(lf)      r.SiteCode,#(lf)      r.OrderDateUTC,#(lf)#(tab)  pt.Capture_Date,#(lf)      r.DateCreatedUTC,#(lf)      r.DeliveryDate,#(lf)      r.InsertDate,#(lf)      r.UpdateDate,#(lf)      dtt.SiteWarehouseCode,#(lf)      r.ItemChangeType,#(lf)      r.TotalGrossTotal AS 'tender_total',#(lf)      op.EarlyCaptureAmount AS 'gross_line_amount',#(lf)      CAST(COALESCE(NULLIF(pt.Generic1, ''), 'NONE') AS varchar(20)) AS reference_no,#(lf)      WarehouseCode,#(lf)      Tender_Total_Transaction_Level,#(lf)      PaymentTransactionTypeId#(lf)  FROM dbo.mulesoft_deckjsonraw_root r#(lf)    left join root_warehouse rw ON CONVERT(varchar(64), rw.OrderID) = CONVERT(varchar(64), r.OrderID)#(lf)    left join [dbo].[mulesoft_deckjsonraw_orderpayments] op on op._ParentKeyField = r.OrderID#(lf)    left join pt  on CONVERT(varchar(64), op.ID) = pt.OrderPaymentId#(lf)  OUTER APPLY (#(lf)    SELECT TOP (1) dtt.SiteWarehouseCode#(lf)    FROM dbo.mulesoft_dynamicstargettrans dtt#(lf)    WHERE dtt.OrderId = r.OrderID#(lf)    ORDER BY TRY_CONVERT(datetime2(7), dtt.ExportCreatedUTC) DESC#(lf)  ) dtt#(lf)  WHERE TRY_CONVERT(date, COALESCE(r.OrderDateUTC, r.DateCreatedUTC, r.InsertDate))#(lf)        >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 4 months#(lf)),#(lf)oms_norm AS (#(lf)  SELECT#(lf)    CASE#(lf)      WHEN COALESCE(NULLIF(CAST(orm.SiteWarehouseCode AS varchar(64)),''), NULLIF(CAST(orm.SiteCode AS varchar(64)),'')) = 'BAB'   THEN '1013'#(lf)      WHEN COALESCE(NULLIF(CAST(orm.SiteWarehouseCode AS varchar(64)),''), NULLIF(CAST(orm.SiteCode AS varchar(64)),'')) = 'BABUK' THEN '2013'#(lf)      WHEN COALESCE(NULLIF(CAST(orm.SiteWarehouseCode AS varchar(64)),''), NULLIF(CAST(orm.SiteCode AS varchar(64)),'')) IS NULL THEN '9999'#(lf)      ELSE '9999'#(lf)    END AS InventLocationIdMapped,#(lf)    orm.*#(lf)  FROM oms_root orm#(lf)),#(lf)oms AS (#(lf)  SELECT#(lf)  COALESCE(CAST(TRY_CONVERT(BIGINT, orm.OrderNumber) AS VARCHAR(50)), orm.OrderNumber) AS OrderNumber,#(lf)      CONCAT(InventLocationIdMapped,'-052')                                   AS device_id,#(lf)      CONVERT(varchar(8), TRY_CONVERT(date, COALESCE(orm.OrderDateUTC, orm.DateCreatedUTC, orm.InsertDate)), 112)#(lf)                                                                              AS business_date,#(lf)#(tab)  orm.Capture_Date,#(lf)    CAST(#(lf)            TRY_CONVERT(datetime2(6), orm.Capture_Date) #(lf)            AT TIME ZONE 'UTC' #(lf)            AT TIME ZONE 'Central Standard Time' #(lf)            AS datetime2(6))                                                AS Capture_Date_CST,#(lf)      COALESCE(#(lf)  TRY_CONVERT(bigint, orm.OrderNumber),#(lf)  TRY_CONVERT(bigint, orm.OrderID),#(lf)  CAST(ABS(CHECKSUM(CAST(orm.OrderNumber AS nvarchar(4000)))) AS bigint)#(lf)) AS sequence_number,#(lf)      CAST(ItemChangeType AS varchar(64))                                              AS trans_type,#(lf)      CAST('COMPLETED' AS varchar(64))                                       AS trans_status,#(lf)      TRY_CONVERT(int, InventLocationIdMapped)                               AS business_unit_id,  -- align type with POS#(lf)      coalesce(TRY_CONVERT(int,dsl.InventLocationId), TRY_CONVERT(int, InventLocationIdMapped))                                AS invent_location_id_mapped,#(lf)      iif(coalesce(TRY_CONVERT(int,dsl.InventLocationId), TRY_CONVERT(int, InventLocationIdMapped)) = 1013 OR#(lf)        coalesce(TRY_CONVERT(int,dsl.InventLocationId), TRY_CONVERT(int, InventLocationIdMapped)) = 2013, 3,#(lf)            iif(dh.eCommOrderType = 'BOSFS' OR  dh.eCommOrderType = 'BOPIS', 52, null)#(lf)            )                                                                AS register,#(lf)      iif(coalesce(TRY_CONVERT(int,dsl.InventLocationId), TRY_CONVERT(int, InventLocationIdMapped)) = 1013 OR#(lf)        coalesce(TRY_CONVERT(int,dsl.InventLocationId), TRY_CONVERT(int, InventLocationIdMapped)) = 2013, null,#(lf)        dh.eCommOrderType)                                                   AS eCommOrderType,#(lf)      CAST(UserID AS varchar(64))                                            AS username,#(lf)      TRY_CONVERT(datetime2(6), COALESCE(orm.OrderDateUTC, orm.DateCreatedUTC, orm.InsertDate))#(lf)                                                                             AS begin_time,#(lf)      TRY_CONVERT(datetime2(6), COALESCE(orm.DeliveryDate, orm.UpdateDate, orm.OrderDateUTC, orm.DateCreatedUTC))#(lf)                                                                             AS end_time,#(lf)      CAST(0 AS int)                                                         AS local_offset,#(lf)      CAST(0 AS int)                                                         AS client_offset,#(lf)      CAST(0 AS bit)                                                         AS keyed_offline,#(lf)      CAST(NULL AS varchar(64))                                              AS override_user_id,#(lf)      CAST(dh.Barcode AS varchar(64))                                        AS barcode,#(lf)      CAST(0 AS bit)                                                         AS training_mode,#(lf)      CAST(NULL AS varchar(64))                                              AS session_id,#(lf)      CAST(NULL AS varchar(64))                                              AS trans_pin,#(lf)      CAST('052' AS varchar(64))                                             AS till_id,#(lf)      CAST(NULL AS varchar(64))                                              AS app_id,#(lf)      CAST(NULL AS varchar(64))                                              AS app_version,#(lf)      TRY_CONVERT(datetime2(6), COALESCE(orm.DateCreatedUTC, orm.InsertDate)) AS create_time,#(lf)      CAST(orm.SiteCode AS varchar(128))                                     AS create_by,#(lf)      COALESCE(orm.OrderDateUTC, orm.DateCreatedUTC, orm.InsertDate)#(lf)                                                                             AS last_update_time,#(lf)      CAST(NULL AS varchar(128))                                             AS last_update_by,#(lf)      CAST(NULL AS varchar(max))                                             AS suspended_trans_data,#(lf)      CAST(NULL AS varchar(64))                                              AS bank_bag_number,#(lf)      CAST(dh.RetailTransactionId AS varchar(64))                            AS retail_transaction_id,#(lf)      orm.gross_line_amount,#(lf)      orm.tender_total,#(lf)      orm.OrderStatus                                                              AS order_status_id,#(lf)        CASE orm.OrderStatus #(lf)            WHEN 1 THEN 'CO'#(lf)            WHEN 3 THEN 'AVS'#(lf)            WHEN 4 THEN 'P'#(lf)            WHEN 5 THEN 'PV'#(lf)            WHEN 6 THEN 'Z'#(lf)            WHEN 9 THEN 'MR'#(lf)            WHEN 10 THEN 'PS'#(lf)            WHEN 11 THEN 'DAP'#(lf)            WHEN 12 THEN 'CF'#(lf)            ELSE null#(lf)        END                                                                        AS order_status_code,#(lf)        CASE orm.OrderStatus #(lf)            WHEN 1 THEN 'New'#(lf)            WHEN 3 THEN 'Review'#(lf)            WHEN 4 THEN 'Pending'#(lf)            WHEN 5 THEN 'Exception'#(lf)            WHEN 6 THEN 'Completed'#(lf)            WHEN 9 THEN 'Manual Review'#(lf)            WHEN 10 THEN 'Pending Settlement'#(lf)            WHEN 11 THEN 'Delayed Auto-Process'#(lf)            WHEN 12 THEN 'Confirmed Fraud'#(lf)            ELSE null#(lf)        END                                                                        AS order_status,#(lf)      'OMS'                                                                  AS source,#(lf)      reference_no,#(lf)      WarehouseCode,#(lf)      Tender_Total_Transaction_Level,#(lf)      PaymentTransactionTypeId#(lf)  FROM oms_norm orm#(lf)    left join dbo.mulesoft_dynamicsheaderoms dh on#(lf)#(tab)orm.OrderNumber = dh.RetailReceiptId#(lf)#(tab)left join (select distinct RetailReceiptId, InventLocationId from [LH_Source].[dbo].[mulesoft_dynamicssaleslineoms]) dsl on#(lf)#(tab)orm.OrderNumber = dsl.RetailReceiptId#(lf))#(lf)#(lf)SELECT *#(lf)FROM pos#(lf)UNION ALL#(lf)SELECT *#(lf)FROM oms"]),
    #"Inserted Text After Delimiter | Till Id" = Table.AddColumn(Source, "Till Id", each Text.AfterDelimiter([device_id], "-"), type text),
    #"Duplicated Column | Sequence Number" = Table.DuplicateColumn(#"Inserted Text After Delimiter | Till Id", "sequence_number", "sequence_number - Copy"),
    #"Duplicated Column | Business Date" = Table.DuplicateColumn(#"Duplicated Column | Sequence Number", "business_date", "business_date - Copy"),
    #"Merged Columns | Transaction Key" =
  Table.CombineColumns(
    Table.TransformColumnTypes(#"Duplicated Column | Business Date", {{"sequence_number", type text}}, "en-US"),
    {"device_id","business_date","sequence_number"},
    Combiner.CombineTextByDelimiter("-", QuoteStyle.None),
    "Transaction Key"
),
    #"Changed Type1" = Table.TransformColumnTypes(#"Merged Columns | Transaction Key",{{"business_date - Copy", type date}}),
    #"Renamed Columns" = Table.RenameColumns(#"Changed Type1",{{"trans_type", "Transaction Type"}, {"business_date - Copy", "Business Date"}, {"trans_status", "Transaction Status"}, {"business_unit_id", "Business Unit Id"}, {"username", "Username Id"}, {"begin_time", "Begin Datetime"}, {"end_time", "End Datetime"}, {"local_offset", "Local Offset"}, {"client_offset", "Client Offset"}, {"keyed_offline", "Keyed Offline"}, {"override_user_id", "Override User Id"}, {"barcode", "Barcode"}, {"training_mode", "Training Mode"}, {"session_id", "Session Id"}, {"trans_pin", "Transaction PIN"}, {"till_id", "BusinessUnitTillId"}, {"app_id", "App Id"}, {"app_version", "App Version"}, {"create_time", "Created Datetime"}, {"create_by", "Created By"}, {"last_update_time", "Last Updated Datetime"}, {"sequence_number - Copy", "Sequence Number"}, {"last_update_by", "Last Updated By"},{"Capture_Date_CST", "Capture Date CST"}}),
    #"Added Custom | Username Key" =
  Table.AddColumn(#"Renamed Columns", "Username Key",
    each Text.From([Business Unit Id]) & "-" & [Username Id], type text),
    #"Replaced Value | _ with SPACE" = Table.ReplaceValue(#"Added Custom | Username Key","_"," ",Replacer.ReplaceText,{"Transaction Type", "Transaction Status"}),
    #"Added Custom | Override Username Key" =
  Table.AddColumn(#"Added Custom | Username Key", "Override Username Key",
    each Text.From([Business Unit Id]) & "-" & [Override User Id], type text),
    #"Inserted Date | Transaction Date" = Table.AddColumn(#"Added Custom | Override Username Key", "Transaction Date", each Date.From([Last Updated Datetime]), type date),
    #"Inserted Date | Transaction Date CST" = Table.AddColumn(#"Inserted Date | Transaction Date", "Transaction Date CST", each Date.From([Capture Date CST]), type date),
    #"Inserted Time | Begin Time" = Table.AddColumn(#"Inserted Date | Transaction Date CST", "Begin Time", each Time.From([Begin Datetime]), type time),
    #"Inserted Time | End Time (Transaction Time)" = Table.AddColumn(#"Inserted Time | Begin Time", "Transaction Time", each Time.From([End Datetime]), type time),
    #"Capitalized Each Word" = Table.TransformColumns(#"Inserted Time | End Time (Transaction Time)",{{"Transaction Type", Text.Proper, type text}, {"Transaction Status", Text.Proper, type text}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Capitalized Each Word",{{"Keyed Offline", type logical}, {"Training Mode", type logical}, {"Username Key", type text}, {"Override Username Key", type text}}),
    #"Reordered Columns" = Table.ReorderColumns(#"Changed Type",{"Transaction Status", "Transaction Key", "Transaction Type", "Barcode", "Business Unit Id", "Till Id", "Training Mode", "Begin Datetime", "End Datetime", "Local Offset", "Client Offset", "Username Id", "Username Key", "Override User Id", "Override Username Key", "Keyed Offline", "Session Id", "Transaction PIN", "BusinessUnitTillId", "App Id", "App Version", "Created Datetime", "Created By", "Last Updated Datetime", "Last Updated By"}),
    #"Merged Queries | Users" = Table.NestedJoin(#"Reordered Columns", {"Username Key"}, #"Users (JumpMind)", {"Username Key"}, "Users (JumpMind)", JoinKind.LeftOuter),
    #"Expanded Users (JumpMind)" = Table.ExpandTableColumn(#"Merged Queries | Users", "Users (JumpMind)", {"Username", "Work Group"}, {"Username", "Work Group"}),
    #"Merged Queries | Users (Override)" = Table.NestedJoin(#"Expanded Users (JumpMind)", {"Override Username Key"}, #"Users (JumpMind)", {"Username Key"}, "Users (JumpMind)", JoinKind.LeftOuter),
    #"Expanded Users (JumpMind) | Override Users" = Table.ExpandTableColumn(#"Merged Queries | Users (Override)", "Users (JumpMind)", {"Username", "Work Group"}, {"Users (JumpMind).Username", "Users (JumpMind).Work Group"}),
    #"Renamed Columns | Users" = Table.RenameColumns(#"Expanded Users (JumpMind) | Override Users",{{"Users (JumpMind).Username", "Override Associate Name"}, {"Users (JumpMind).Work Group", "Override Associate Work Group"}, {"Username", "Associate Name"}, {"Work Group", "Associate Work Group"}}),
    #"Removed Duplicates" = Table.Distinct(#"Renamed Columns | Users", {"Transaction Key"}),
    #"Replaced Value" = Table.ReplaceValue(#"Removed Duplicates",null,"InStore",Replacer.ReplaceValue,{"eCommOrderType"})
in
    #"Replaced Value"
```

### Activated Gift Cards (JumpMind)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH pos_giftcards AS (#(lf)    SELECT#(lf)        CONVERT(varchar(32),  j.device_id)                                         AS device_id,#(lf)        CONVERT(varchar(8),   j.business_date)                                     AS business_date,#(lf)        CONVERT(varchar(50),  j.sequence_number)                                   AS sequence_number,#(lf)        CONVERT(varchar(50),  j.line_sequence_number)                              AS line_sequence_number,#(lf)        CONVERT(varchar(200), j.brand)                                             AS brand,#(lf)        CONVERT(varchar(200), j.card_name)                                         AS card_name,#(lf)        CONVERT(varchar(200), j.code)                                              AS code,#(lf)        CONVERT(varchar(200), j.type_code)                                         AS type_code,#(lf)        CONVERT(varchar(200), j.payment_provider_code)                             AS payment_provider_code,#(lf)        CONVERT(varchar(64),  j.masked_card_number)                                AS masked_card_number,#(lf)        CONVERT(varchar(64),  j.entry_mode)                                        AS entry_mode,#(lf)        CONVERT(varchar(64),  j.service_code)                                      AS service_code,#(lf)        CONVERT(varchar(16),  j.expiration_date)                                   AS expiration_date,#(lf)        CONVERT(varchar(50),  j.ref_line_sequence_number)                          AS ref_line_sequence_number,#(lf)        CONVERT(varchar(64),  j.card_number)                                       AS card_number,#(lf)        CONVERT(varchar(64),  j.gift_card_action_code)                             AS gift_card_action_code,#(lf)        CAST(j.last_update_time AS datetime2(6))                                   AS last_update_time,#(lf)        NULL                                                                       AS order_status_id,#(lf)        NULL                                                                       AS order_status_code,#(lf)        NULL                                                                       AS order_status,#(lf)        'POS'                                                                      AS source#(lf)    FROM dbo.jumpmind_sls_card_line_item AS j#(lf)    WHERE j.type_code = 'GIFTCARD'#(lf)      AND TRY_CONVERT(date, j.business_date, 112) >= DATEADD(month, -4, CAST(GETDATE() AS date))#(lf)),#(lf)hs AS (#(lf)    SELECT#(lf)        NULLIF(CONVERT(varchar(64), r.SiteCode), '')                               AS InventLocationId,#(lf)        CAST(COALESCE(r.OrderDateUTC, r.DateCreatedUTC, r.OrderStatusChangeDateUTC, r.ExportCreatedUTC) AS date) AS TransDate,#(lf)        CONVERT(varchar(64), r.OrderNumber)  AS OrderNumber,#(lf)        r.OrderID,#(lf)        r._RowIndex,#(lf)        r.OrderStatus #(lf)    FROM dbo.mulesoft_deckjsonraw_root r#(lf)    WHERE CAST(COALESCE(r.OrderDateUTC, r.DateCreatedUTC, r.OrderStatusChangeDateUTC, r.ExportCreatedUTC) AS date)#(lf)          >= DATEADD(month, -4, CAST(GETDATE() AS date))#(lf)),#(lf)hs_norm AS (#(lf)  SELECT#(lf)    CASE#(lf)      WHEN hs.InventLocationId = 'BAB'   THEN '1013'#(lf)      WHEN hs.InventLocationId = 'BABUK' THEN '2013'#(lf)      WHEN NULLIF(hs.InventLocationId,'') IS NULL THEN '9999'#(lf)      ELSE hs.InventLocationId#(lf)    END AS InventLocationIdMapped,#(lf)    hs.*#(lf)  FROM hs#(lf)),#(lf)oms_giftcards AS (#(lf)    SELECT#(lf)        CONCAT(COALESCE(hn.InventLocationIdMapped,'9999'), '-052')                  AS device_id,#(lf)        CONVERT(varchar(8), hn.TransDate, 112)                                      AS business_date,#(lf)        CONVERT(varchar(50),#(lf)            COALESCE(#(lf)                TRY_CONVERT(bigint, hn.OrderNumber),#(lf)                TRY_CONVERT(bigint, hn.OrderID),#(lf)                ABS(CHECKSUM(CAST(hn.OrderNumber AS nvarchar(4000))))#(lf)            )#(lf)        )                                                                           AS sequence_number,#(lf)        CONVERT(varchar(50), hn._RowIndex)                                         AS line_sequence_number,   -- always use OrderItemID#(lf)        CAST('Build-A-Bear' AS varchar(200))                                        AS brand,#(lf)        CAST('Gift Card' AS varchar(200))                                           AS card_name,#(lf)        'GIFTCARD'                                                                  AS code,#(lf)        'GIFTCARD'                                                                  AS type_code,#(lf)        CAST(NULL AS varchar(200))                                                  AS payment_provider_code,#(lf)        CASE#(lf)          WHEN g.GiftCardNumber IS NOT NULL#(lf)            THEN REPLICATE('*', 12) + RIGHT(CONVERT(varchar(32), TRY_CONVERT(bigint, g.GiftCardNumber)), 4)#(lf)          ELSE NULL#(lf)        END                                                                         AS masked_card_number,#(lf)        CAST(NULL AS varchar(64))                                                   AS entry_mode,#(lf)        CAST(NULL AS varchar(64))                                                   AS service_code,#(lf)        CAST(NULL AS varchar(16))                                                   AS expiration_date,#(lf)        CONVERT(varchar(50), hn._RowIndex)                                          AS ref_line_sequence_number,#(lf)        CONVERT(varchar(64), TRY_CONVERT(bigint, g.GiftCardNumber))                 AS card_number,#(lf)        CASE WHEN TRY_CONVERT(int, g.Processed) = 1 THEN 'Issue' ELSE NULL END      AS gift_card_action_code,#(lf)        CAST(COALESCE(TRY_CONVERT(datetime2(6), g.UpdateDate),#(lf)                      TRY_CONVERT(datetime2(6), g.InsertDate)) AS datetime2(6))     AS last_update_time,#(lf)        hn.OrderStatus                                                              AS order_status_id,#(lf)        CASE hn.OrderStatus #(lf)            WHEN 1 THEN 'CO'#(lf)            WHEN 3 THEN 'AVS'#(lf)            WHEN 4 THEN 'P'#(lf)            WHEN 5 THEN 'PV'#(lf)            WHEN 6 THEN 'Z'#(lf)            WHEN 9 THEN 'MR'#(lf)            WHEN 10 THEN 'PS'#(lf)            WHEN 11 THEN 'DAP'#(lf)            WHEN 12 THEN 'CF'#(lf)            ELSE null#(lf)        END                                                                        AS order_status_code,#(lf)        CASE hn.OrderStatus #(lf)            WHEN 1 THEN 'New'#(lf)            WHEN 3 THEN 'Review'#(lf)            WHEN 4 THEN 'Pending'#(lf)            WHEN 5 THEN 'Exception'#(lf)            WHEN 6 THEN 'Completed'#(lf)            WHEN 9 THEN 'Manual Review'#(lf)            WHEN 10 THEN 'Pending Settlement'#(lf)            WHEN 11 THEN 'Delayed Auto-Process'#(lf)            WHEN 12 THEN 'Confirmed Fraud'#(lf)            ELSE null#(lf)        END                                                                        AS order_status,#(lf)        'OMS'                                                                      AS source#(lf)    FROM dbo.mulesoft_deckjsonraw_giftcards g#(lf)    JOIN dbo.mulesoft_deckjsonraw_orderitems oi #(lf)        ON g.OrderItemID = oi.ID#(lf)    JOIN hs_norm hn#(lf)        ON oi.OrderID = hn.OrderID#(lf)            AND oi._RowIndex = hn._RowIndex#(lf))#(lf)SELECT * FROM pos_giftcards#(lf)UNION ALL#(lf)SELECT * FROM oms_giftcards;", CreateNavigationProperties=false]),
    #"Filtered Rows | Type Code = GIFTCARD" = Table.SelectRows(Source, each ([type_code] = "GIFTCARD")),
    #"Merged Columns | Transaction Line Key" = Table.CombineColumns(Table.TransformColumnTypes(#"Filtered Rows | Type Code = GIFTCARD", {{"sequence_number", type text}, {"ref_line_sequence_number", type text}}, "en-US"),{"device_id", "business_date", "sequence_number", "ref_line_sequence_number"},Combiner.CombineTextByDelimiter("-", QuoteStyle.None),"Transaction Line Key"),
    #"Reordered Columns" = Table.ReorderColumns(#"Merged Columns | Transaction Line Key",{"Transaction Line Key", "line_sequence_number", "brand", "card_name", "code", "type_code", "payment_provider_code", "masked_card_number", "entry_mode", "service_code", "expiration_date", "card_number", "last_update_time"}),
    #"Renamed Columns" = Table.RenameColumns(#"Reordered Columns",{{"brand", "Brand"}, {"card_name", "Card Name"}, {"card_number", "Card Number"}, {"code", "Code"}, {"entry_mode", "Entry Mode"}, {"expiration_date", "Expiration Date"},  {"last_update_time", "Last Updated Datetime"}, {"masked_card_number", "Masked Card Number"}, {"payment_provider_code", "Payment Provider Code"}, {"line_sequence_number", "Line Sequence Number"}, {"service_code", "Service Code"}, {"type_code", "Type Code"}, {"gift_card_action_code", "Gift Card Action Code"}}),
    #"Replaced Value | GIFTCARD with Gift Card" = Table.ReplaceValue(#"Renamed Columns","GIFTCARD","Gift Card",Replacer.ReplaceText,{"Brand", "Code", "Type Code"}),
    #"Removed Duplicates | Transaction Line Key" = Table.Distinct(#"Replaced Value | GIFTCARD with Gift Card", {"Transaction Line Key"}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Removed Duplicates | Transaction Line Key",{{"Card Name", Text.Proper, type text}, {"Entry Mode", Text.Proper, type text}})
in
    #"Capitalized Each Word"
```

### Measure Table

```sql
Row("Column", BLANK())
```

### vwJumpMindEventReportingSummary

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com", "LH_Source"),
    dbo_vwJumpMindEventReportingSummary = Source{[Schema="dbo",Item="vwJumpMindEventReportingSummary"]}[Data]
in
    dbo_vwJumpMindEventReportingSummary
```

### Gift Cards Details

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Mart", [Query="SELECT#(lf)    gd.account_number,#(lf)    gd.[consortium_code],#(lf)    CASE gd.[consortium_code]#(lf)        WHEN 192 THEN 'Build a Bear Intl'#(lf)        WHEN 5901 THEN 'BAB Walgreens'#(lf)        WHEN 8410 THEN 'Build a Bear Denmark'#(lf)        WHEN 8478 THEN 'Build A Bear Incomm'#(lf)        WHEN 8615 THEN 'BAB Blackhawk Cross'#(lf)        WHEN 8760 THEN 'Build A Bear Blackhawk Canada'#(lf)        WHEN 9342 THEN 'Build a Bear Ireland'#(lf)        ELSE 'Unknown Consortium' #(lf)    END AS consortium_name,#(lf)    gd.[promotion_code],#(lf)    gd.[merchant_id],#(lf)    gd.balance,#(lf)    gd.terminal_local_timestamp,#(lf)    gd.[transaction_amount],#(lf)    gd.[base_amount],#(lf)    gd.[reporting_amount],#(lf)    CAST(gd.terminal_local_timestamp AS Date) as card_detail_date,#(lf)    gd.[alternate_merchant_number],#(lf)    gd.terminal_transaction_number#(lf)FROM#(lf)    [LH_Mart].[dbo].[giftcard_detail] gd#(lf)WHERE TRY_CONVERT(date, terminal_local_timestamp, 112) >= DATEADD(month, -4, CAST(GETDATE() AS date))", CreateNavigationProperties=false])
in
    Source
```

### Dict Payment Transaction Type

```sql
let
    Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("XY/NCgIhFIVfRVxPMM7fPqJ9tBUXkndKMA1Hg3r6vDo0Frg4er57zpVz2tKGHqS9gDGgkm6paDhlSe1juDmv3zJoZ9OdZafL/CNED0l1+a1P6gxztBjQlwDMPYFV2l7JxrM1nlXud5KVBoZxR+nNqx5cY4etnsze3UkGERgKMCLgQenw54/Fn6rmnx+mPZ7gF2kQnjK8wzXxCPEB", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [PaymentTransactionTypeId = _t, PaymentTransactionType = _t, #"Payment Transaction Type ID" = _t]),
    #"Changed Type" = Table.TransformColumnTypes(Source,{{"PaymentTransactionTypeId", Int64.Type}, {"PaymentTransactionType", type text}})
in
    #"Changed Type"
```

### Transactions Extra Values

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH pos AS (#(lf)  SELECT#(lf)      null                                                                  AS OrderNumber,  #(lf)      CAST(device_id AS varchar(64))                                        AS device_id,#(lf)      CAST(business_date AS varchar(8))                                     AS business_date,#(lf)#(tab)    TRY_CONVERT(datetime2(6), last_update_time) #(tab)#(tab)#(tab)#(tab)#(tab)#(tab)#(tab)            AS Capture_Date,#(lf)      CAST(#(lf)            TRY_CONVERT(datetime2(6), last_update_time) #(lf)            AT TIME ZONE 'UTC' #(lf)            AT TIME ZONE 'Central Standard Time' #(lf)            AS datetime2(6))                                                AS Capture_Date_CST,#(lf)      CAST(sequence_number AS varchar(50))                                  AS sequence_number,#(lf)      CAST(trans_type AS varchar(64))                                       AS trans_type,#(lf)      CAST(trans_status AS varchar(64))                                     AS trans_status,#(lf)      TRY_CONVERT(int, business_unit_id)                                    AS business_unit_id,#(lf)      TRY_CONVERT(int, business_unit_id)                                    AS invent_location_id_mapped,#(lf)      null                                                                  AS register,#(lf)      dh.eCommOrderType                                                     AS eCommOrderType,#(lf)      CAST(username AS varchar(64))                                         AS username,#(lf)      TRY_CONVERT(datetime2(6), begin_time)                                 AS begin_time,#(lf)      TRY_CONVERT(datetime2(6), end_time)                                   AS end_time,#(lf)      TRY_CONVERT(int, local_offset)                                        AS local_offset,#(lf)      TRY_CONVERT(int, client_offset)                                       AS client_offset,#(lf)      TRY_CONVERT(bit, keyed_offline)                                       AS keyed_offline,#(lf)      CAST(override_user_id AS varchar(64))                                 AS override_user_id,#(lf)      CAST(barcode AS varchar(64))                                          AS barcode,#(lf)      TRY_CONVERT(bit, training_mode)                                       AS training_mode,#(lf)      CAST(session_id AS varchar(64))                                       AS session_id,#(lf)      CAST(trans_pin AS varchar(64))                                        AS trans_pin,#(lf)      CAST(till_id AS varchar(64))                                          AS till_id,#(lf)      CAST(app_id AS varchar(64))                                           AS app_id,#(lf)      CAST(app_version AS varchar(64))                                      AS app_version,#(lf)      TRY_CONVERT(datetime2(6), create_time)                                AS create_time,#(lf)      CAST(create_by AS varchar(128))                                       AS create_by,#(lf)      TRY_CONVERT(datetime2(6), last_update_time)                           AS last_update_time,#(lf)      CAST(last_update_by AS varchar(128))                                  AS last_update_by,#(lf)      CAST(suspended_trans_data AS varchar(max))                            AS suspended_trans_data,#(lf)      CAST(bank_bag_number AS varchar(64))                                  AS bank_bag_number,#(lf)      CAST(RetailTransactionId AS varchar(64))                              AS retail_transaction_id,#(lf)      null                                                                  AS gross_line_amount,#(lf)      null                                                                  AS tender_total,#(lf)      NULL                                                                  AS order_status_id,#(lf)      NULL                                                                  AS order_status_code,#(lf)      NULL                                                                  AS order_status,#(lf)      'POS'                                                                 AS source,#(lf)      CAST('NONE' AS varchar(20))                                           AS reference_no,#(lf)      NULL                                                                  AS WarehouseCode,#(lf)      NULL AS Tender_Total_Transaction_Level,  #(lf)      NULL AS PaymentTransactionTypeId#(lf)  FROM dbo.jumpmind_sls_trans t#(lf)  LEFT JOIN dbo.mulesoft_dynamicsheader dh ON dh.TransactionKey = concat(t.device_id, '-', t.business_date, '-', t.sequence_number)#(lf)  WHERE create_by = 'openpos-sls'#(lf)    AND TRY_CONVERT(date, business_date, 112) >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 4 months#(lf)),#(lf)pt AS (#(lf)   SELECT Distinct #(lf)      CONVERT(varchar(64), pt.OrderPaymentId)       AS OrderPaymentId,#(lf)      pt._ParentKeyField                            AS OrderID,#(lf)#(tab)  TRY_CONVERT(datetime2(6), TransactionDateUTC) AS Capture_Date,#(lf)      pt.Generic1                                   AS Generic1,#(lf)      Amount                                        AS Tender_Total_Transaction_Level,#(lf)      PaymentTransactionTypeId#(lf)  FROM dbo.mulesoft_deckjsonraw_paymenttransactions pt #(lf)  WHERE CAST(pt.TransactionDateUTC AS date)#(lf)        >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 4 MONTHS#(lf) ),#(lf)root_warehouse AS (#(lf)  SELECT#(lf)      r.OrderID,#(lf)      oi.WarehouseCode#(lf)  FROM dbo.mulesoft_deckjsonraw_root r#(lf)  LEFT JOIN dbo.mulesoft_deckjsonraw_orderitems oi#(lf)    ON r.OrderID = oi._ParentKeyField#(lf)   AND oi._RowIndex = r._RowIndex#(lf)  WHERE CAST(COALESCE(r.OrderDateUTC, r.DateCreatedUTC, r.OrderStatusChangeDateUTC, r.ExportCreatedUTC) AS date)#(lf)        >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 4 MONTHS#(lf)),#(lf)#(lf)oms_root AS (#(lf)  SELECT#(lf)      r.OrderID,#(lf)      r.OrderNumber,#(lf)      r.OrderStatus,#(lf)      r.UserID,#(lf)      r.SiteCode,#(lf)      r.OrderDateUTC,#(lf)#(tab)  pt.Capture_Date,#(lf)      r.DateCreatedUTC,#(lf)      r.DeliveryDate,#(lf)      r.InsertDate,#(lf)      r.UpdateDate,#(lf)      dtt.SiteWarehouseCode,#(lf)      r.ItemChangeType,#(lf)      r.TotalGrossTotal AS 'tender_total',#(lf)      op.EarlyCaptureAmount AS 'gross_line_amount',#(lf)      CAST(COALESCE(NULLIF(pt.Generic1, ''), 'NONE') AS varchar(20)) AS reference_no,#(lf)      WarehouseCode,#(lf)      Tender_Total_Transaction_Level,#(lf)      PaymentTransactionTypeId#(lf)  FROM dbo.mulesoft_deckjsonraw_root r#(lf)    left join root_warehouse rw ON CONVERT(varchar(64), rw.OrderID) = CONVERT(varchar(64), r.OrderID)#(lf)    left join [dbo].[mulesoft_deckjsonraw_orderpayments] op on op._ParentKeyField = r.OrderID#(lf)    left join pt  on CONVERT(varchar(64), op.ID) = pt.OrderPaymentId#(lf)  OUTER APPLY (#(lf)    SELECT TOP (1) dtt.SiteWarehouseCode#(lf)    FROM dbo.mulesoft_dynamicstargettrans dtt#(lf)    WHERE dtt.OrderId = r.OrderID#(lf)    ORDER BY TRY_CONVERT(datetime2(7), dtt.ExportCreatedUTC) DESC#(lf)  ) dtt#(lf)  WHERE TRY_CONVERT(date, COALESCE(r.OrderDateUTC, r.DateCreatedUTC, r.InsertDate))#(lf)        >= DATEADD(month, -4, CAST(GETDATE() AS date))  -- 4 months#(lf)),#(lf)oms_norm AS (#(lf)  SELECT#(lf)    CASE#(lf)      WHEN COALESCE(NULLIF(CAST(orm.SiteWarehouseCode AS varchar(64)),''), NULLIF(CAST(orm.SiteCode AS varchar(64)),'')) = 'BAB'   THEN '1013'#(lf)      WHEN COALESCE(NULLIF(CAST(orm.SiteWarehouseCode AS varchar(64)),''), NULLIF(CAST(orm.SiteCode AS varchar(64)),'')) = 'BABUK' THEN '2013'#(lf)      WHEN COALESCE(NULLIF(CAST(orm.SiteWarehouseCode AS varchar(64)),''), NULLIF(CAST(orm.SiteCode AS varchar(64)),'')) IS NULL THEN '9999'#(lf)      ELSE '9999'#(lf)    END AS InventLocationIdMapped,#(lf)    orm.*#(lf)  FROM oms_root orm#(lf)),#(lf)oms AS (#(lf)  SELECT#(lf)  COALESCE(CAST(TRY_CONVERT(BIGINT, orm.OrderNumber) AS VARCHAR(50)), orm.OrderNumber) AS OrderNumber,#(lf)      CONCAT(InventLocationIdMapped,'-052')                                   AS device_id,#(lf)      CONVERT(varchar(8), TRY_CONVERT(date, COALESCE(orm.OrderDateUTC, orm.DateCreatedUTC, orm.InsertDate)), 112)#(lf)                                                                              AS business_date,#(lf)#(tab)  orm.Capture_Date,#(lf)    CAST(#(lf)            TRY_CONVERT(datetime2(6), orm.Capture_Date) #(lf)            AT TIME ZONE 'UTC' #(lf)            AT TIME ZONE 'Central Standard Time' #(lf)            AS datetime2(6))                                                AS Capture_Date_CST,#(lf)      COALESCE(#(lf)  TRY_CONVERT(bigint, orm.OrderNumber),#(lf)  TRY_CONVERT(bigint, orm.OrderID),#(lf)  CAST(ABS(CHECKSUM(CAST(orm.OrderNumber AS nvarchar(4000)))) AS bigint)#(lf)) AS sequence_number,#(lf)      CAST(ItemChangeType AS varchar(64))                                              AS trans_type,#(lf)      CAST('COMPLETED' AS varchar(64))                                       AS trans_status,#(lf)      TRY_CONVERT(int, InventLocationIdMapped)                               AS business_unit_id,  -- align type with POS#(lf)      coalesce(TRY_CONVERT(int,dsl.InventLocationId), TRY_CONVERT(int, InventLocationIdMapped))                                AS invent_location_id_mapped,#(lf)      iif(coalesce(TRY_CONVERT(int,dsl.InventLocationId), TRY_CONVERT(int, InventLocationIdMapped)) = 1013 OR#(lf)        coalesce(TRY_CONVERT(int,dsl.InventLocationId), TRY_CONVERT(int, InventLocationIdMapped)) = 2013, 3,#(lf)            iif(dh.eCommOrderType = 'BOSFS' OR  dh.eCommOrderType = 'BOPIS', 52, null)#(lf)            )                                                                AS register,#(lf)      iif(coalesce(TRY_CONVERT(int,dsl.InventLocationId), TRY_CONVERT(int, InventLocationIdMapped)) = 1013 OR#(lf)        coalesce(TRY_CONVERT(int,dsl.InventLocationId), TRY_CONVERT(int, InventLocationIdMapped)) = 2013, null,#(lf)        dh.eCommOrderType)                                                   AS eCommOrderType,#(lf)      CAST(UserID AS varchar(64))                                            AS username,#(lf)      TRY_CONVERT(datetime2(6), COALESCE(orm.OrderDateUTC, orm.DateCreatedUTC, orm.InsertDate))#(lf)                                                                             AS begin_time,#(lf)      TRY_CONVERT(datetime2(6), COALESCE(orm.DeliveryDate, orm.UpdateDate, orm.OrderDateUTC, orm.DateCreatedUTC))#(lf)                                                                             AS end_time,#(lf)      CAST(0 AS int)                                                         AS local_offset,#(lf)      CAST(0 AS int)                                                         AS client_offset,#(lf)      CAST(0 AS bit)                                                         AS keyed_offline,#(lf)      CAST(NULL AS varchar(64))                                              AS override_user_id,#(lf)      CAST(dh.Barcode AS varchar(64))                                        AS barcode,#(lf)      CAST(0 AS bit)                                                         AS training_mode,#(lf)      CAST(NULL AS varchar(64))                                              AS session_id,#(lf)      CAST(NULL AS varchar(64))                                              AS trans_pin,#(lf)      CAST('052' AS varchar(64))                                             AS till_id,#(lf)      CAST(NULL AS varchar(64))                                              AS app_id,#(lf)      CAST(NULL AS varchar(64))                                              AS app_version,#(lf)      TRY_CONVERT(datetime2(6), COALESCE(orm.DateCreatedUTC, orm.InsertDate)) AS create_time,#(lf)      CAST(orm.SiteCode AS varchar(128))                                     AS create_by,#(lf)      COALESCE(orm.OrderDateUTC, orm.DateCreatedUTC, orm.InsertDate)#(lf)                                                                             AS last_update_time,#(lf)      CAST(NULL AS varchar(128))                                             AS last_update_by,#(lf)      CAST(NULL AS varchar(max))                                             AS suspended_trans_data,#(lf)      CAST(NULL AS varchar(64))                                              AS bank_bag_number,#(lf)      CAST(dh.RetailTransactionId AS varchar(64))                            AS retail_transaction_id,#(lf)      orm.gross_line_amount,#(lf)      orm.tender_total,#(lf)      orm.OrderStatus                                                              AS order_status_id,#(lf)        CASE orm.OrderStatus #(lf)            WHEN 1 THEN 'CO'#(lf)            WHEN 3 THEN 'AVS'#(lf)            WHEN 4 THEN 'P'#(lf)            WHEN 5 THEN 'PV'#(lf)            WHEN 6 THEN 'Z'#(lf)            WHEN 9 THEN 'MR'#(lf)            WHEN 10 THEN 'PS'#(lf)            WHEN 11 THEN 'DAP'#(lf)            WHEN 12 THEN 'CF'#(lf)            ELSE null#(lf)        END                                                                        AS order_status_code,#(lf)        CASE orm.OrderStatus #(lf)            WHEN 1 THEN 'New'#(lf)            WHEN 3 THEN 'Review'#(lf)            WHEN 4 THEN 'Pending'#(lf)            WHEN 5 THEN 'Exception'#(lf)            WHEN 6 THEN 'Completed'#(lf)            WHEN 9 THEN 'Manual Review'#(lf)            WHEN 10 THEN 'Pending Settlement'#(lf)            WHEN 11 THEN 'Delayed Auto-Process'#(lf)            WHEN 12 THEN 'Confirmed Fraud'#(lf)            ELSE null#(lf)        END                                                                        AS order_status,#(lf)      'OMS'                                                                  AS source,#(lf)      reference_no,#(lf)      WarehouseCode,#(lf)      Tender_Total_Transaction_Level,#(lf)      PaymentTransactionTypeId#(lf)  FROM oms_norm orm#(lf)    left join dbo.mulesoft_dynamicsheaderoms dh on#(lf)#(tab)orm.OrderNumber = dh.RetailReceiptId#(lf)#(tab)left join (select distinct RetailReceiptId, InventLocationId from [LH_Source].[dbo].[mulesoft_dynamicssaleslineoms]) dsl on#(lf)#(tab)orm.OrderNumber = dsl.RetailReceiptId#(lf))#(lf)#(lf)SELECT *#(lf)FROM pos#(lf)UNION ALL#(lf)SELECT *#(lf)FROM oms"]),
    #"Inserted Text After Delimiter | Till Id" = Table.AddColumn(Source, "Till Id", each Text.AfterDelimiter([device_id], "-"), type text),
    #"Duplicated Column | Sequence Number" = Table.DuplicateColumn(#"Inserted Text After Delimiter | Till Id", "sequence_number", "sequence_number - Copy"),
    #"Duplicated Column | Business Date" = Table.DuplicateColumn(#"Duplicated Column | Sequence Number", "business_date", "business_date - Copy"),
    #"Merged Columns | Transaction Key" =
  Table.CombineColumns(
    Table.TransformColumnTypes(#"Duplicated Column | Business Date", {{"sequence_number", type text}}, "en-US"),
    {"device_id","business_date","sequence_number"},
    Combiner.CombineTextByDelimiter("-", QuoteStyle.None),
    "Transaction Key"
),
    #"Changed Type1" = Table.TransformColumnTypes(#"Merged Columns | Transaction Key",{{"business_date - Copy", type date}}),
    #"Renamed Columns" = Table.RenameColumns(#"Changed Type1",{{"trans_type", "Transaction Type"}, {"business_date - Copy", "Business Date"}, {"trans_status", "Transaction Status"}, {"business_unit_id", "Business Unit Id"}, {"username", "Username Id"}, {"begin_time", "Begin Datetime"}, {"end_time", "End Datetime"}, {"local_offset", "Local Offset"}, {"client_offset", "Client Offset"}, {"keyed_offline", "Keyed Offline"}, {"override_user_id", "Override User Id"}, {"barcode", "Barcode"}, {"training_mode", "Training Mode"}, {"session_id", "Session Id"}, {"trans_pin", "Transaction PIN"}, {"till_id", "BusinessUnitTillId"}, {"app_id", "App Id"}, {"app_version", "App Version"}, {"create_time", "Created Datetime"}, {"create_by", "Created By"}, {"last_update_time", "Last Updated Datetime"}, {"sequence_number - Copy", "Sequence Number"}, {"last_update_by", "Last Updated By"},{"Capture_Date_CST", "Capture Date CST"}}),
    #"Added Custom | Username Key" =
  Table.AddColumn(#"Renamed Columns", "Username Key",
    each Text.From([Business Unit Id]) & "-" & [Username Id], type text),
    #"Replaced Value | _ with SPACE" = Table.ReplaceValue(#"Added Custom | Username Key","_"," ",Replacer.ReplaceText,{"Transaction Type", "Transaction Status"}),
    #"Added Custom | Override Username Key" =
  Table.AddColumn(#"Added Custom | Username Key", "Override Username Key",
    each Text.From([Business Unit Id]) & "-" & [Override User Id], type text),
    #"Inserted Date | Transaction Date" = Table.AddColumn(#"Added Custom | Override Username Key", "Transaction Date", each Date.From([Last Updated Datetime]), type date),
    #"Inserted Date | Transaction Date CST" = Table.AddColumn(#"Inserted Date | Transaction Date", "Transaction Date CST", each Date.From([Capture Date CST]), type date),
    #"Inserted Time | Begin Time" = Table.AddColumn(#"Inserted Date | Transaction Date CST", "Begin Time", each Time.From([Begin Datetime]), type time),
    #"Inserted Time | End Time (Transaction Time)" = Table.AddColumn(#"Inserted Time | Begin Time", "Transaction Time", each Time.From([End Datetime]), type time),
    #"Capitalized Each Word" = Table.TransformColumns(#"Inserted Time | End Time (Transaction Time)",{{"Transaction Type", Text.Proper, type text}, {"Transaction Status", Text.Proper, type text}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Capitalized Each Word",{{"Keyed Offline", type logical}, {"Training Mode", type logical}, {"Username Key", type text}, {"Override Username Key", type text}}),
    #"Reordered Columns" = Table.ReorderColumns(#"Changed Type",{"Transaction Status", "Transaction Key", "Transaction Type", "Barcode", "Business Unit Id", "Till Id", "Training Mode", "Begin Datetime", "End Datetime", "Local Offset", "Client Offset", "Username Id", "Username Key", "Override User Id", "Override Username Key", "Keyed Offline", "Session Id", "Transaction PIN", "BusinessUnitTillId", "App Id", "App Version", "Created Datetime", "Created By", "Last Updated Datetime", "Last Updated By"}),
    #"Merged Queries | Users" = Table.NestedJoin(#"Reordered Columns", {"Username Key"}, #"Users (JumpMind)", {"Username Key"}, "Users (JumpMind)", JoinKind.LeftOuter),
    #"Expanded Users (JumpMind)" = Table.ExpandTableColumn(#"Merged Queries | Users", "Users (JumpMind)", {"Username", "Work Group"}, {"Username", "Work Group"}),
    #"Merged Queries | Users (Override)" = Table.NestedJoin(#"Expanded Users (JumpMind)", {"Override Username Key"}, #"Users (JumpMind)", {"Username Key"}, "Users (JumpMind)", JoinKind.LeftOuter),
    #"Expanded Users (JumpMind) | Override Users" = Table.ExpandTableColumn(#"Merged Queries | Users (Override)", "Users (JumpMind)", {"Username", "Work Group"}, {"Users (JumpMind).Username", "Users (JumpMind).Work Group"}),
    #"Renamed Columns | Users" = Table.RenameColumns(#"Expanded Users (JumpMind) | Override Users",{{"Users (JumpMind).Username", "Override Associate Name"}, {"Users (JumpMind).Work Group", "Override Associate Work Group"}, {"Username", "Associate Name"}, {"Work Group", "Associate Work Group"}}),
    #"Removed Duplicates" = Table.Distinct(#"Renamed Columns | Users", {"Transaction Key", "PaymentTransactionTypeId"}),
    #"Replaced Value" = Table.ReplaceValue(#"Removed Duplicates",null,"InStore",Replacer.ReplaceValue,{"eCommOrderType"})
in
    #"Replaced Value"
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

### Errors in Tender Lines (JumpMind) (0)

```sql
let
Source = #"Tender Lines (JumpMind)",
  #"Detected Type Mismatches" = let
    tableWithOnlyPrimitiveTypes = Table.SelectColumns(Source, Table.ColumnsOfType(Source, {type nullable number, type nullable text, type nullable logical, type nullable date, type nullable datetime, type nullable datetimezone, type nullable time, type nullable duration})),
    recordTypeFields = Type.RecordFields(Type.TableRow(Value.Type(tableWithOnlyPrimitiveTypes))),
    fieldNames = Record.FieldNames(recordTypeFields),
    fieldTypes = List.Transform(Record.ToList(recordTypeFields), each [Type]),
    pairs = List.Transform(List.Positions(fieldNames), (i) => {fieldNames{i}, (v) => if v = null or Value.Is(v, fieldTypes{i}) then v else error [Message = "The type of the value does not match the type of the column.", Detail = v], fieldTypes{i}})
in
    Table.TransformColumns(Source, pairs),
  #"Added Index" = Table.AddIndexColumn(#"Detected Type Mismatches", "Row Number" ,1),
  #"Kept Errors" = Table.SelectRowsWithErrors(#"Added Index", {"Transaction Key", "Line Sequence Number", "Warehouse Code", "Tender Code", "Tender Type Code", "Payment Sub-Type", "Change Flag", "ISO Currency Code", "Early Capture Amount", "Tender Amount (Native Currency)", "Cash Back Amount (Native Currency)", "Exchange Rate", "Overtendered", "Partially Approved", "Post Void", "Voided", "Override User Id", "Created Datetime", "Created By", "Last Updated Datetime", "Last Updated By", "tender_auth_method_code", "tender_group", "tender_id", "voucher_id", "source", "Reference No", "Transaction Line Key", "Charge Type", "Tender Object-Action"}),
  #"Reordered Columns" = Table.ReorderColumns(#"Kept Errors", {"Row Number", "Transaction Key", "Line Sequence Number", "Warehouse Code", "Tender Code", "Tender Type Code", "Payment Sub-Type", "Change Flag", "ISO Currency Code", "Early Capture Amount", "Tender Amount (Native Currency)", "Cash Back Amount (Native Currency)", "Exchange Rate", "Overtendered", "Partially Approved", "Post Void", "Voided", "Override User Id", "Created Datetime", "Created By", "Last Updated Datetime", "Last Updated By", "tender_auth_method_code", "tender_group", "tender_id", "voucher_id", "source", "Reference No", "Transaction Line Key", "Charge Type", "Tender Object-Action"}),
    #"Tender Object-Action" = #"Reordered Columns"{0}[#"Tender Object-Action"]
in
    #"Tender Object-Action"
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com | LH_Mart | [4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/LH_Mart](../../../4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/DataDictionary/LH_Mart/) |
| 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com | LH_Source | [4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/LH_Source](../../../4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/DataDictionary/LH_Source/) |
| 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com | LH_D365 | [4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/LH_D365](../../../4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/DataDictionary/LH_D365/) |
| 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com | LH_Source | [4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com/LH_Source](../../../4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com/DataDictionary/LH_Source/) |
