# dbo.sv_employee_master

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sv_employee_master"]
    EMPLY(["EMPLY"]) --> VIEW
    EMPLY_ORG_CHN_PSTN_A(["EMPLY_ORG_CHN_PSTN_A"]) --> VIEW
    EMPLY_ORG_CHN_PSTN_A_HSTRY(["EMPLY_ORG_CHN_PSTN_A_HSTRY"]) --> VIEW
    EMPLY_STS_HSTRY(["EMPLY_STS_HSTRY"]) --> VIEW
    ORG_CHN_PSTN(["ORG_CHN_PSTN"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| EMPLY |
| EMPLY_ORG_CHN_PSTN_A |
| EMPLY_ORG_CHN_PSTN_A_HSTRY |
| EMPLY_STS_HSTRY |
| ORG_CHN_PSTN |

## View Code

```sql
create view dbo.sv_employee_master as
SELECT employee_no = E.EMPLY_NUM,
    employee_first_name = E.FRST_NAME,
    employee_last_name = E.LAST_NAME,
    home_store = E.PRMY_ORG_CHN_NUM,
    primary_position_code = E.TTL_PSTN_CODE,
    house_account_no = E.HS_ACNT_NUM,
    date_of_hire =  convert(varchar(10),MIN(ESH.EFCTV_DATE),101)  + ' ' + convert(varchar(8),MIN(ESH.EFCTV_DATE),114),
    date_of_termination = null,
    employee_dept_no = ISNULL(EOCPA.PRMRY_LOC_ID,EOCPAH.PRMRY_LOC_ID ),
    employee_dept_desc = NULL,
    primary_position_descr = OCP1.PSTN_DESC,
    active_flag = E.ACTV
FROM EMPLY E
JOIN EMPLY_STS_HSTRY ESH 
    ON E.EMPLY_NUM = ESH.EMPLY_NUM
    AND ESH.EMPLY_STS_CODE = 'HIRE'
    AND  E.EMPLY_STS_CODE NOT IN ('TERM','SUSP','RESN','RETD')
JOIN  ORG_CHN_PSTN OCP1
    ON  E.TTL_PSTN_CODE = OCP1.PSTN_CODE  
LEFT OUTER JOIN EMPLY_ORG_CHN_PSTN_A EOCPA
    ON (E.EMPLY_NUM = EOCPA.EMPLY_NUM
    AND E.PRMY_ORG_CHN_NUM = EOCPA.ORG_CHN_NUM
    AND E.TTL_PSTN_CODE =EOCPA.PSTN_CODE  
    AND EOCPA.EFCTV_DATE <= getdate() 
    AND EOCPA.EXPRTN_DATE IS NULL)
LEFT OUTER JOIN  EMPLY_ORG_CHN_PSTN_A_HSTRY EOCPAH
    ON (E.EMPLY_NUM = EOCPAH.EMPLY_NUM
    AND E.PRMY_ORG_CHN_NUM = EOCPAH.ORG_CHN_NUM
    AND E.TTL_PSTN_CODE =EOCPAH.PSTN_CODE  
    AND EOCPAH.EFCTV_DATE <= getdate() 
    AND EOCPAH.EXPRTN_DATE > getdate()) 
GROUP BY E.EMPLY_NUM,E.FRST_NAME,E.LAST_NAME,E.PRMY_ORG_CHN_NUM, 
        E.TTL_PSTN_CODE,E.HS_ACNT_NUM,	
       ISNULL(EOCPA.PRMRY_LOC_ID,EOCPAH.PRMRY_LOC_ID ),OCP1.PSTN_DESC,E.ACTV
UNION 
SELECT employee_no = E.EMPLY_NUM,
    employee_first_name = E.FRST_NAME,
    employee_last_name = E.LAST_NAME,
    home_store_no = E.PRMY_ORG_CHN_NUM,
    primary_position_code = E.TTL_PSTN_CODE,
    house_account_no = E.HS_ACNT_NUM,
    date_of_hire =  convert(varchar(10),MIN(ESH.EFCTV_DATE),101)  + ' ' + convert(varchar(8),MIN(ESH.EFCTV_DATE),114),--MIN(ESH.EFCTV_DATE),
    date_of_termination = convert(varchar(10),ESH1.EFCTV_DATE,101)  + ' ' + convert(varchar(8),ESH1.EFCTV_DATE,114),--ESH1.EFCTV_DATE,
    employee_dept_no = ISNULL(EOCPA.PRMRY_LOC_ID,EOCPAH.PRMRY_LOC_ID ),  
    employee_dept_desc = NULL,
    primary_position_descr = OCP1.PSTN_DESC,
    active_flag = E.ACTV
FROM EMPLY E
JOIN EMPLY_STS_HSTRY ESH 
    ON E.EMPLY_NUM = ESH.EMPLY_NUM
    AND ESH.EMPLY_STS_CODE = 'HIRE'
    AND  E.EMPLY_STS_CODE IN ('TERM','SUSP','RESN','RETD')
JOIN  ORG_CHN_PSTN OCP1
    ON  E.TTL_PSTN_CODE = OCP1.PSTN_CODE      
JOIN  EMPLY_STS_HSTRY ESH1       
    ON E.EMPLY_NUM = ESH1.EMPLY_NUM
    AND ESH1.EMPLY_STS_CODE = E.EMPLY_STS_CODE
LEFT OUTER JOIN EMPLY_ORG_CHN_PSTN_A EOCPA 
    ON (E.EMPLY_NUM = EOCPA.EMPLY_NUM
    AND E.PRMY_ORG_CHN_NUM = EOCPA.ORG_CHN_NUM
    AND EOCPA.EFCTV_DATE <= getdate() 
    AND E.TTL_PSTN_CODE =EOCPA.PSTN_CODE  
    AND EOCPA.EXPRTN_DATE IS NULL)
LEFT OUTER JOIN  EMPLY_ORG_CHN_PSTN_A_HSTRY EOCPAH 
    ON (E.EMPLY_NUM = EOCPAH.EMPLY_NUM
    AND E.PRMY_ORG_CHN_NUM = EOCPAH.ORG_CHN_NUM
    AND E.TTL_PSTN_CODE =EOCPAH.PSTN_CODE  
    AND EOCPAH.EFCTV_DATE <= getdate() 
 AND EOCPAH.EXPRTN_DATE > getdate())      
GROUP BY E.EMPLY_NUM,E.FRST_NAME,E.LAST_NAME,E.PRMY_ORG_CHN_NUM, 
        E.TTL_PSTN_CODE,E.HS_ACNT_NUM, ESH1.EFCTV_DATE,
        ISNULL(EOCPA.PRMRY_LOC_ID,EOCPAH.PRMRY_LOC_ID ) ,OCP1.PSTN_DESC,E.ACTV
```

