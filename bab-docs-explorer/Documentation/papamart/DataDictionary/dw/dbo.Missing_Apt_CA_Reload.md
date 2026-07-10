# dbo.Missing_Apt_CA_Reload

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| qas_rtrn_cd | varchar | 30 | 1 |  |  |  |
| problem | varchar | 52 | 1 |  |  |  |
| clnsd_addr_id | int | 4 | 0 |  |  |  |
| inp_addr_ln_1_txt | varchar | 100 | 1 |  |  |  |
| inp_addr_ln_2_txt | varchar | 60 | 1 |  |  |  |
| inp_apt_unit_nbr | varchar | 50 | 1 |  |  |  |
| inp_cty_nm | varchar | 50 | 1 |  |  |  |
| inp_st_prvnc_txt | varchar | 50 | 1 |  |  |  |
| inp_pstl_cd | varchar | 30 | 1 |  |  |  |
| inp_country | varchar | 3 | 0 |  |  |  |
| cur_addr_ln_1_txt | varchar | 60 | 1 |  |  |  |
| cur_cty_nm | varchar | 60 | 1 |  |  |  |
| cur_pstl_cd | varchar | 10 | 1 |  |  |  |
| clnsd_addr_ln_1_txt | varchar | 60 | 1 |  |  |  |
| clnsd_addr_ln_2_txt | varchar | 60 | 1 |  |  |  |
| clnsd_apt_unit_nbr | varchar | 60 | 1 |  |  |  |
| clnsd_cty_nm | varchar | 60 | 1 |  |  |  |
| clnsd_st_prvnc_abbrv | varchar | 5 | 1 |  |  |  |
| clnsd_pstl_cd | varchar | 10 | 1 |  |  |  |
| clnsd_cntry_abbrv | varchar | 5 | 1 |  |  |  |
| done_datetime | datetime | 8 | 1 |  |  |  |
