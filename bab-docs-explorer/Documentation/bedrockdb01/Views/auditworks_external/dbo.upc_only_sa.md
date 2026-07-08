# dbo.upc_only_sa

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.upc_only_sa"]
    user_upc(["user_upc"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| user_upc |

## View Code

```sql
create view dbo.upc_only_sa AS
SELECT u.upc_lookup_division, u.upc_no, u.style_reference_id
FROM user_upc u
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

dbo,employee_comms_auto_adj_a_c_vw,--Assignment Definition grid-style retrieval
CREATE VIEW employee_comms_auto_adj_a_c_vw
AS
SELECT a.auto_commission_adj_id, a.auto_adjustment_description, 
       t.assignment_type,
       CASE WHEN t.assignment_type = '50_home_store' THEN NULL ELSE COUNT(aa.auto_commission_adj_id) END assignment_cnt
  FROM employee_comms_auto_adj a
       INNER JOIN (SELECT '10_employee_no' assignment_type UNION SELECT '20_employee_commission_code'UNION SELECT '30_primary_selling_area_no' UNION SELECT '40_primary_position' UNION SELECT '50_home_store' UNION SELECT '60_home_store_no' UNION SELECT '70_home_store_commission_code') t
         ON 1=1
       LEFT OUTER JOIN employee_comms_auto_adj_assign aa
          ON a.auto_commission_adj_id = aa.auto_commission_adj_id
         AND CASE WHEN employee_no <> -1
            THEN '10_employee_no'
            ELSE CASE WHEN employee_commission_code <> '-1' 
                      THEN '20_employee_commission_code'
                      ELSE CASE WHEN primary_selling_area_no <> -1
                                THEN '30_primary_selling_area_no'
                                ELSE CASE WHEN primary_position <> '-1'
                                          THEN '40_primary_position'
                                          ELSE CASE WHEN home_store_no <> -1
                                                    THEN '60_home_store_no'
                                                    ELSE CASE WHEN home_store_commission_code <> '-1'
                                                             THEN '70_home_store_commission_code'
                                                              ELSE '20_employee_commission_code'
                                                         END
                                               END
                                     END
                           END
                  END
       END = t.assignment_type
GROUP BY a.auto_commission_adj_id, a.auto_adjustment_description, t.assignment_type
--ORDER BY a.auto_commission_adj_id, t.assignment_type
```

