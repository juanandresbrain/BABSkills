# dbo.avalara_tax_trans_vw

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.avalara_tax_trans_vw"]
    avalara_tax_trans(["avalara_tax_trans"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| avalara_tax_trans |

## View Code

```sql
create view dbo.avalara_tax_trans_vw  AS
 SELECT N'ProcessCode' ProcessCode,
       N'DocCode' DocCode,
       N'DocType' DocType,
       N'DocDate' DocDate,
       N'CompanyCode' CompanyCode,
       N'CustomerCode' CustomerCode,
       N'EntityUseCode' EntityUseCode,
       N'LineNo' LineNum,
       N'TaxCode' TaxCode,
       N'TaxDate' TaxDate,
       N'ItemCode' ItemCode,
       N'Description' Description,
       N'Qty' Qty,
       N'Amount' Amount,
       N'Taxable' Taxable,
       N'Discount' Discount,
       N'TotalTax' TotalTax,
       N'CountryTax' CountryTax, 
       N'StateTax' StateTax,
       N'CountyTax' CountyTax,
       N'CityTax' CityTax,
       N'Other1Tax' Other1Tax,
       N'Other2Tax' Other2Tax,
       N'Ref1' Ref1,
       N'Ref2' Ref2,
       N'ExemptionNo' ExemptionNo,
       N'RevAcct' RevAcct, 
       N'TaxType' TaxType,
       N'DestAddress' DestAddress,
       N'DestCity' DestCity,
       N'DestRegion' DestRegion,
       N'DestPostalCode' DestPostalCode,
       N'DestCountry' DestCountry,
       N'OrigAddress' OrigAddress,
       N'OrigCity' OrigCity,
       N'OrigRegion' OrigRegion,
       N'OrigPostalCode' OrigPostalCode,
       N'OrigCountry' OrigCountry,
       N'LocationCode' LocationCode,
       N'SalesPersonCode' SalesPersonCode,
       N'PurchaseOrderNo' PurchaseOrderNo,
       N'CurrencyCode' CurrencyCode,
       N'ExchangeRate' ExchangeRate,
       N'ExchangeRateEffDate' ExchangeRateEffDate,
       N'PaymentDate' PaymentDate,
       N'TaxIncluded' TaxIncluded,
       N'DestTaxRegion' DestTaxRegion,
       N'OrigTaxRegion' OrigTaxRegion
WHERE EXISTS (SELECT 1 FROM avalara_tax_trans)
UNION ALL     
 SELECT convert(nvarchar, ProcessCode), 
	DocCode, 
	convert(nvarchar, DocType), 
	convert(nvarchar, DocDate, 101), 
	CompanyCode, 
	CustomerCode, 
	EntityUseCode, 
	convert(nvarchar, LineNum), 
	TaxCode, 
	convert(nvarchar, TaxDate, 101), 
	ItemCode, 
	Description, 
	convert(nvarchar, Qty), 
	convert(nvarchar, Amount), 
	convert(nvarchar, Taxable), 
	convert(nvarchar, Discount), 
	convert(nvarchar, TotalTax), 
	convert(nvarchar, CountryTax), 
	convert(nvarchar, StateTax), 
	convert(nvarchar, CountyTax), 
	convert(nvarchar, CityTax), 
	convert(nvarchar, Other1Tax), 
	convert(nvarchar, Other2Tax), 
	Ref1, 
	Ref2, 
	ExemptionNo, 
	RevAcct, 
	TaxType, 
	DestAddress, 
	DestCity, 
	DestRegion, 
	DestPostalCode, 
	DestCountry, 
	OrigAddress, 
	OrigCity, 
	OrigRegion, 
	OrigPostalCode, 
	OrigCountry , 
	LocationCode, 
	SalesPersonCode, 
	PurchaseOrderNo, 
	CurrencyCode, 
	convert(nvarchar, ExchangeRate), 
	convert(nvarchar, ExchangeRateEffDate, 101), 
	convert(nvarchar, PaymentDate, 101), 
	convert(nvarchar, TaxIncluded), 
	DestTaxRegion, 
	OrigTaxRegion
  FROM avalara_tax_trans
```

