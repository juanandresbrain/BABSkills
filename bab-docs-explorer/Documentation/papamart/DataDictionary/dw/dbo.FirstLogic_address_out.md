# dbo.FirstLogic_address_out

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| I_tblKey | int | 4 | 0 |  |  |  |
| I_Address | char | 60 | 1 |  |  |  |
| I_City | char | 60 | 1 |  |  |  |
| I_State | char | 60 | 1 |  |  |  |
| I_Country | char | 60 | 1 |  |  |  |
| I_Zip | char | 60 | 1 |  |  |  |
| O_Address | char | 100 | 1 |  |  |  |
| O_City | char | 60 | 1 |  |  |  |
| O_State | char | 60 | 1 |  |  |  |
| O_Zip | char | 20 | 1 |  |  |  |
| O_Zip4 | char | 4 | 1 |  |  |  |
| O_Fault_Code | char | 6 | 1 |  |  |  |
| O_Latitude | char | 10 | 1 |  |  |  |
| O_Longitude | char | 11 | 1 |  |  |  |
| O_Block | char | 7 | 1 |  |  |  |
| O_AGeo_City | char | 3 | 1 |  |  |  |
| O_AGeo_State | char | 2 | 1 |  |  |  |
| O_County_Name | char | 100 | 1 |  |  |  |
| O_Country | char | 60 | 1 |  |  |  |
| O_Unit_Num | char | 8 | 1 |  |  |  |
| O_Unit_Desc | char | 10 | 1 |  |  |  |
| O_Local_Alt | char | 79 | 1 |  |  |  |
| O_Geo_Match | char | 1 | 1 |  |  |  |
| O_Prim_Range | varchar | 100 | 1 |  |  |  |
| O_Prim_Name | varchar | 100 | 1 |  |  |  |
| O_Prim_Addr | varchar | 100 | 1 |  |  |  |
| O_Sec_Addr | varchar | 100 | 1 |  |  |  |
| O_Ctry_Alph2 | varchar | 100 | 1 |  |  |  |
| O_Cgeo_CBSA | varchar | 100 | 1 |  |  |  |
| O_Cgeo_MSA | varchar | 100 | 1 |  |  |  |
| O_Sort_Route | varchar | 100 | 1 |  |  |  |
| O_Addr_Type | char | 2 | 1 |  |  |  |
| O_Stat_Code | varchar | 10 | 1 |  |  |  |
| O_Eng_Used | varchar | 10 | 1 |  |  |  |
| O_Locality2 | varchar | 100 | 1 |  |  |  |
| O_Locality3 | varchar | 100 | 1 |  |  |  |
| O_Locality4 | varchar | 100 | 1 |  |  |  |
