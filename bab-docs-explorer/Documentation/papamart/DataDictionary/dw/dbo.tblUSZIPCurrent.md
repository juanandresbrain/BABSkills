# dbo.tblUSZIPCurrent

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ZIP | char | 5 | 0 |  |  |  |
| Enc_ZIP | char | 5 | 1 |  |  |  |
| St | char | 2 | 1 |  |  |  |
| St_FIPS | char | 2 | 1 |  |  |  |
| Name | varchar | 50 | 1 |  |  |  |
| Multiple_Name | bit | 1 | 1 |  |  |  |
| Cty1Fips | char | 3 | 1 |  |  |  |
| Cty2Fips | char | 3 | 1 |  |  |  |
| Cty3Fips | char | 3 | 1 |  |  |  |
| Area_mi | float | 8 | 1 |  |  |  |
| RPO_Flag | char | 1 | 1 |  |  |  |
| ZipType | char | 1 | 1 |  |  |  |
| Pt_loc | char | 1 | 1 |  |  |  |
| Lat | decimal | 5 | 1 |  |  |  |
| Lon | decimal | 9 | 1 |  |  |  |
| iNearestStore | int | 4 | 1 |  |  |  |
| fDistanceToNearestStore | float | 8 | 1 |  |  |  |
