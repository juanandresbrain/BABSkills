# WEB.UKWebstoreProductBalanceStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BEG | varchar | 50 | 1 |  |  |  |
| Location | varchar | 50 | 1 |  |  |  |
| Company | varchar | 50 | 1 |  |  |  |
| Date | varchar | 50 | 1 |  |  |  |
| Batch | varchar | 50 | 1 |  |  |  |
| StyleCode | varchar | 50 | 1 |  |  |  |
| Available | varchar | 50 | 1 |  |  |  |
| ARR | varchar | 50 | 1 |  |  |  |
| ARRQuantity | int | 4 | 1 |  |  |  |
| ArrUOM | varchar | 50 | 1 |  |  |  |
| AVL | varchar | 50 | 1 |  |  |  |
| AVLQuantity | bigint | 8 | 1 |  |  |  |
| AvlUOM | varchar | 50 | 1 |  |  |  |
| TRA | varchar | 50 | 1 |  |  |  |
| TRAQuantity | int | 4 | 1 |  |  |  |
| TraUOM | varchar | 50 | 1 |  |  |  |
| Ord | varchar | 50 | 1 |  |  |  |
| ORDQuantity | int | 4 | 1 |  |  |  |
| OrdUOM | varchar | 50 | 1 |  |  |  |
| PCK | varchar | 50 | 1 |  |  |  |
| PCKQuantity | int | 4 | 1 |  |  |  |
| PckUOM | varchar | 50 | 1 |  |  |  |
| AWP | varchar | 50 | 1 |  |  |  |
| AWPQuantity | int | 4 | 1 |  |  |  |
| AwpUOM | varchar | 50 | 1 |  |  |  |
| ALL | varchar | 50 | 1 |  |  |  |
| ALLQuantity | int | 4 | 1 |  |  |  |
| AllUOM | varchar | 50 | 1 |  |  |  |
| ADV | varchar | 50 | 1 |  |  |  |
| ADVQuantity | int | 4 | 1 |  |  |  |
| AdvUOM | varchar | 50 | 1 |  |  |  |
| HLD | varchar | 50 | 1 |  |  |  |
| HLDQuantity | int | 4 | 1 |  |  |  |
| HldUOM | varchar | 50 | 1 |  |  |  |
| DetailRowNumber | varchar | 50 | 1 |  |  |  |
| FileName | varchar | 50 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WEB.spMergeUKWebProductBalance](../../StoredProcedures/IntegrationStaging/WEB.spMergeUKWebProductBalance.md)
- [IntegrationStaging: WEB.spMergeUKWebProductBalance_BAK20230822](../../StoredProcedures/IntegrationStaging/WEB.spMergeUKWebProductBalance_BAK20230822.md)

