# dbo.sfs_rfm_score_dim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sfs_rfm_key | int | 4 | 0 | YES |  | Internal Key |
| rfm_score | varchar | 10 | 1 |  |  | Brierly RFM Score |
| rfm_group | varchar | 50 | 1 |  |  | Group that this RFM_Score belongs to. |
| priority | int | 4 | 1 |  |  | Relative priority of this rfm_Score |
| r_score | varchar | 10 | 1 |  |  |  |
| f_score | varchar | 10 | 1 |  |  |  |
| m_score | varchar | 10 | 1 |  |  |  |
