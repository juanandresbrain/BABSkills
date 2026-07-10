# dbo.vwProduct_Dim2

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwProduct_Dim2"]
    product_dim(["product_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| product_dim |

## View Code

```sql
CREATE view [dbo].[vwProduct_Dim2]
as
select 
CASE WHEN right(department_code,2)='05' or department = 'Accessories' THEN 'ACCESSORIES'
	 WHEN right(department_code,2)='06' THEN 'FURNITURE'
	 WHEN right(department_code,2)='07' or department = 'Pets' THEN 'PETS'
	 WHEN right(department_code,2)='10' or department = 'Clothes' THEN 'CLOTHING'
	 WHEN right(department_code,2) in ('12','33','38') THEN 'LICENSING'
	 WHEN right(department_code,2)='15' THEN 'FOOTWEAR'
	 WHEN right(department_code,2)='20' THEN 'SOUNDS'
	 WHEN right(department_code,2)='25' THEN 'UNSTUFFED'
	 WHEN right(subclass_code,2)='25' THEN 'UNSTUFFED'
	 WHEN right(department_code,2)='30' THEN 'PRESTUFFED'
	 WHEN right(department_code,2)='35' or department = 'Human' THEN 'HUMAN'
	 WHEN right(department_code,2) in ('40','48') THEN 'PARTIES'
	 WHEN right(department_code,2)='45' THEN 'BEARBUCKS/COUPONS'
	 WHEN right(department_code,2)='46' THEN 'DONATION/DISCOUNTS'
	 WHEN right(department_code,2)='47' or department = 'Transaction Flags' THEN 'TRANSACTION FLAGS'
	 WHEN right(department_code,2)='50' THEN 'WEB'
	 WHEN right(department_code,2)='51' THEN 'KITS'
	 WHEN right(department_code,2)='55' THEN 'CORPORATE'
	 WHEN right(department_code,2)='60' or department = 'Supplies' THEN 'SUPPLIES'
	 WHEN right(department_code,2)='65' THEN 'EMBROIDERY'
	 WHEN right(department_code,2)='70' THEN 'FORMER BUSINESSES'
	 WHEN right(department_code,2)='75' THEN 'PROMOTIONS'
	 WHEN right(department_code,2)='80' THEN 'GIFT CARDS'
	 WHEN right(department_code,2)='85' THEN 'BLANKS'
	 WHEN right(department_code,2)='99' THEN 'TEST'
ELSE department_code
END as PRODUCT_GROUP,
 
CASE WHEN right(department_code,2)='25' THEN 'BEAR'
	 WHEN right(subclass_code,2)='25' THEN 'BEAR'
     WHEN right(department_code,2) IN (10,15,20,05,30,35,12) and right(subclass_code,2) <> 25 THEN 'PLUS'
ELSE 'OTHER'
END as TRAN_TYPE_GROUP,

CASE WHEN right(department_code,2)='25' THEN 1
	 WHEN right(subclass_code,2)='25' THEN 1
	 WHEN right(department_code,2)='20' THEN 0
     WHEN right(department_code,2) IN (10,15,05,30,35,12) and right(subclass_code,2) <> 25 THEN 2
ELSE 4
END as TRAN_TYPE_NUM,
*
from product_dim
```

