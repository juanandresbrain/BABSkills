# dbo.dim_transaction_series

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dim_transaction_series"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE   VIEW dbo.dim_transaction_series AS SELECT * FROM (VALUES     /* series, description,                                              sequential, sequential_by, ownership, is_active, min_trans_no, max_trans_no */     ('A',     'Auditor transaction series',                              0, NULL,             'System', 1, 1, 9999999),     ('B',     'POS 6.2 System Transactions',                             1, 'Workstation loop', 'User', 1, 1, 999999),     ('C',     'Customer Liability Maintenance',                          0, NULL,             'System', 1, 1, 999999),     ('D',     'House Card/PLCC Account Management',                      0, NULL,             'System', 1, 0, 999999),     ('E',     'Transaction Excerpt',                                     0, NULL,             'System', 1, 1, 999999),     ('F',     'Build-A-Dino',                                            0, NULL,             'User',   1, 1, 999999),     ('G',     'Gift Card - Value Link Inventory txn series',             0, NULL,             'User',   1, 1, 999999),     ('I',     'Stock control',                                           1, 'Workstation loop', 'System', 1, 1, 999999),     ('K',     'EOM Order Management',                                    0, NULL,             'System', 1, 1, 2147483647),     ('L',     'POS Order Management',                                    1, 'Workstation loop', 'System', 1, NULL, NULL),     ('M',     'Media Reconciliation',                                    0, NULL,             'System', 1, 1, 999999),     ('N',     'Non-sequential',                                          0, NULL,             'System', 1, 1, 999999),     ('O',     'Cash office',                                             0, NULL,             'System', 1, 1, 999999),     ('P',     'POS',                                                     0, NULL,             'User',   1, 1, 999999),     ('R',     'Externally Reported Error / Message',                     0, NULL,             'System', 1, 0, 999999),     ('S',     'Security',                                                0, NULL,             'User',   1, 1, 999999),     ('T',     'Time clock',                                              1, 'Workstation loop', 'System', 1, 1, 999999),     ('W',     'Web Sales',                                               0, NULL,             'User',   1, 1, 999999),     ('X',     'Archive Transaction Modification',                        0, NULL,             'System', 1, 0, 999999),     ('Z',     'Media transactions',                                      0, NULL,             'User',   1, 1, 999999) ) AS s(series_code, description, is_sequential, sequential_by, ownership, is_active, min_transaction_no, max_transaction_no);
```

