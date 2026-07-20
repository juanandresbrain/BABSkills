# dbo.tbluszipcurrent

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ZIP | varchar | 8000 | 1 |  |  |  |
| Enc_ZIP | varchar | 8000 | 1 |  |  |  |
| St | varchar | 8000 | 1 |  |  |  |
| St_FIPS | varchar | 8000 | 1 |  |  |  |
| Name | varchar | 8000 | 1 |  |  |  |
| Multiple_Name | bit | 1 | 1 |  |  |  |
| Cty1Fips | varchar | 8000 | 1 |  |  |  |
| Cty2Fips | varchar | 8000 | 1 |  |  |  |
| Cty3Fips | varchar | 8000 | 1 |  |  |  |
| Area_mi | float | 8 | 1 |  |  |  |
| RPO_Flag | varchar | 8000 | 1 |  |  |  |
| ZipType | varchar | 8000 | 1 |  |  |  |
| Pt_loc | varchar | 8000 | 1 |  |  |  |
| Lat | decimal | 5 | 1 |  |  |  |
| Lon | decimal | 9 | 1 |  |  |  |
| iNearestStore | int | 4 | 1 |  |  |  |
| fDistanceToNearestStore | float | 8 | 1 |  |  |  |
