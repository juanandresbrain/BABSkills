# Merchandise Transactional Report Model

**Workspace:** Enterprise Analytics QA  
**Dataset ID:** ebc963bd-12f4-4959-8d69-477e4a8f7ad9  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| vendtable | 218 | 0 |  |
| DateTableTemplate_bd621608-5813-48a2-9dfc-9f7f8eb0b93c | 8 | 0 | Yes |
| LocalDateTable_7c867e80-b28a-4699-b7fc-ce7100991356 | 8 | 0 | Yes |
| LocalDateTable_13c791e0-4f8d-4396-887f-36d72abadf53 | 8 | 0 | Yes |
| LocalDateTable_bd1a434b-1d8d-4a51-b62b-d4ab91130244 | 8 | 0 | Yes |
| LocalDateTable_6950c822-9189-45dc-838d-46116058dec1 | 8 | 0 | Yes |
| LocalDateTable_2a0a8ba9-927b-4e8b-8329-733acca3ef48 | 8 | 0 | Yes |
| LocalDateTable_e7b67ea3-d4ce-447c-a824-17416d42ed09 | 8 | 0 | Yes |
| LocalDateTable_d9b68a08-be40-4820-bad9-bef4f888decf | 8 | 0 | Yes |
| LocalDateTable_eec567c3-09a1-4003-8763-1e7208a09dd7 | 8 | 0 | Yes |
| LocalDateTable_5fabdb19-41d2-49b3-a8be-74759e793f03 | 8 | 0 | Yes |
| vendpackingslipjour | 67 | 0 |  |
| LocalDateTable_8a48ef1e-66cb-457f-a9cc-1f2c2e5765c2 | 8 | 0 | Yes |
| LocalDateTable_f37f73d0-97fb-489d-97ad-732aa97771ff | 8 | 0 | Yes |
| LocalDateTable_87e26680-5457-44a3-b392-ff960654eef9 | 8 | 0 | Yes |
| LocalDateTable_88b91baa-b0c5-4627-b229-9188dd486d59 | 8 | 0 | Yes |
| LocalDateTable_310a1b4b-1ce0-445e-8462-432ec7ee3792 | 8 | 0 | Yes |
| LocalDateTable_9eef63f3-dc78-4edc-9aac-192be44b09ee | 8 | 0 | Yes |
| LocalDateTable_0e515db4-907e-4fba-811a-dae635cbbf83 | 8 | 0 | Yes |
| LocalDateTable_a1f884ba-4136-4f46-bbab-7929c2f8654e | 8 | 0 | Yes |
| LocalDateTable_6f7de4f8-ce39-4aa5-a4b3-fc3a2a46d91f | 8 | 0 | Yes |
| LocalDateTable_800bf14c-e100-4064-be0c-b061a417ef67 | 8 | 0 | Yes |
| vendpackingsliptrans | 96 | 0 |  |
| LocalDateTable_896c927d-236a-42d4-ab9c-97b7dedc513c | 8 | 0 | Yes |
| LocalDateTable_86bce2c6-eeb8-4444-8a7a-9c4b6ca28030 | 8 | 0 | Yes |
| LocalDateTable_271bdd32-be18-4626-a6fb-c23b35ae2c98 | 8 | 0 | Yes |
| LocalDateTable_b1fd0ba2-883e-458d-b245-750ba5188ec2 | 8 | 0 | Yes |
| LocalDateTable_4204e042-d9ac-4400-9a91-8e2edb5b51af | 8 | 0 | Yes |
| LocalDateTable_b2d87814-aed1-45c3-a782-8565ba3d5ea2 | 8 | 0 | Yes |
| LocalDateTable_45fa4b40-c295-4107-a433-8c7e162cf5c9 | 8 | 0 | Yes |
| LocalDateTable_1c99ecf4-f9bb-4cfb-86b4-b7d8edb1bdea | 8 | 0 | Yes |
| LocalDateTable_8d1b51bb-d3c4-4872-aed8-48c5438042d1 | 8 | 0 | Yes |
| LocalDateTable_7def9d6f-1330-4645-a0c2-71e97a7bf84a | 8 | 0 | Yes |
| LocalDateTable_9da39c5f-d981-4e31-92a9-3a4d33add5e1 | 8 | 0 | Yes |
| product_dim | 87 | 0 |  |
| LocalDateTable_4cdf63e2-680c-4c3d-be61-06db7b11505d | 8 | 0 | Yes |
| LocalDateTable_eef152c8-ca4d-426f-a91f-30506096e648 | 8 | 0 | Yes |
| LocalDateTable_647c0176-1fdb-4ad8-a24b-fa7da30d873b | 8 | 0 | Yes |
| LocalDateTable_dd5c4cb9-8e95-4e48-9643-e57ea389a335 | 8 | 0 | Yes |
| LocalDateTable_f84276f5-c3b0-42a1-98cb-727a2ce69de1 | 8 | 0 | Yes |
| attribute_dim | 7 | 0 |  |
| LocalDateTable_a0a6b214-2717-42d1-9279-b27a81859e88 | 8 | 0 | Yes |
| LocalDateTable_dfd780ce-9052-4bc9-b75e-c044ded2e9dc | 8 | 0 | Yes |
| store_dim | 56 | 0 |  |
| LocalDateTable_55d5ec12-4c40-4f3b-9036-99663a3411de | 8 | 0 | Yes |
| LocalDateTable_fdd205e1-11fb-40fd-9897-1328ea401a16 | 8 | 0 | Yes |
| LocalDateTable_529789c6-0dd6-4f91-b3eb-a9d01fcac50e | 8 | 0 | Yes |
| LocalDateTable_b46ceba0-9583-4df1-915d-f0ce667e4969 | 8 | 0 | Yes |
| LocalDateTable_848f3f00-e68d-42bf-9843-bf98f0a85d2c | 8 | 0 | Yes |

## Measures

_No measures detected._

## Power Query Source (per table)

### vendtable

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_D365_Prod"),
    dbo_vendtable = Source{[Schema="dbo",Item="vendtable"]}[Data]
in
    dbo_vendtable
```

### DateTableTemplate_bd621608-5813-48a2-9dfc-9f7f8eb0b93c

```sql
Calendar(Date(2015,1,1), Date(2015,1,1))
```

### LocalDateTable_7c867e80-b28a-4699-b7fc-ce7100991356

```sql
Calendar(Date(Year(MIN('vendtable'[SinkCreatedOn])), 1, 1), Date(Year(MAX('vendtable'[SinkCreatedOn])), 12, 31))
```

### LocalDateTable_13c791e0-4f8d-4396-887f-36d72abadf53

```sql
Calendar(Date(Year(MIN('vendtable'[SinkModifiedOn])), 1, 1), Date(Year(MAX('vendtable'[SinkModifiedOn])), 12, 31))
```

### LocalDateTable_bd1a434b-1d8d-4a51-b62b-d4ab91130244

```sql
Calendar(Date(Year(MIN('vendtable'[blockedreleasedate])), 1, 1), Date(Year(MAX('vendtable'[blockedreleasedate])), 12, 31))
```

### LocalDateTable_6950c822-9189-45dc-838d-46116058dec1

```sql
Calendar(Date(Year(MIN('vendtable'[cisverificationdate])), 1, 1), Date(Year(MAX('vendtable'[cisverificationdate])), 12, 31))
```

### LocalDateTable_2a0a8ba9-927b-4e8b-8329-733acca3ef48

```sql
Calendar(Date(Year(MIN('vendtable'[birthdate])), 1, 1), Date(Year(MAX('vendtable'[birthdate])), 12, 31))
```

### LocalDateTable_e7b67ea3-d4ce-447c-a824-17416d42ed09

```sql
Calendar(Date(Year(MIN('vendtable'[modifieddatetime])), 1, 1), Date(Year(MAX('vendtable'[modifieddatetime])), 12, 31))
```

### LocalDateTable_d9b68a08-be40-4820-bad9-bef4f888decf

```sql
Calendar(Date(Year(MIN('vendtable'[createddatetime])), 1, 1), Date(Year(MAX('vendtable'[createddatetime])), 12, 31))
```

### LocalDateTable_eec567c3-09a1-4003-8763-1e7208a09dd7

```sql
Calendar(Date(Year(MIN('vendtable'[createdon])), 1, 1), Date(Year(MAX('vendtable'[createdon])), 12, 31))
```

### LocalDateTable_5fabdb19-41d2-49b3-a8be-74759e793f03

```sql
Calendar(Date(Year(MIN('vendtable'[modifiedon])), 1, 1), Date(Year(MAX('vendtable'[modifiedon])), 12, 31))
```

### vendpackingslipjour

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_D365_Prod"),
    dbo_vendpackingslipjour = Source{[Schema="dbo",Item="vendpackingslipjour"]}[Data]
in
    dbo_vendpackingslipjour
```

### LocalDateTable_8a48ef1e-66cb-457f-a9cc-1f2c2e5765c2

```sql
Calendar(Date(Year(MIN('vendpackingslipjour'[SinkCreatedOn])), 1, 1), Date(Year(MAX('vendpackingslipjour'[SinkCreatedOn])), 12, 31))
```

### LocalDateTable_f37f73d0-97fb-489d-97ad-732aa97771ff

```sql
Calendar(Date(Year(MIN('vendpackingslipjour'[SinkModifiedOn])), 1, 1), Date(Year(MAX('vendpackingslipjour'[SinkModifiedOn])), 12, 31))
```

### LocalDateTable_87e26680-5457-44a3-b392-ff960654eef9

```sql
Calendar(Date(Year(MIN('vendpackingslipjour'[deliverydate])), 1, 1), Date(Year(MAX('vendpackingslipjour'[deliverydate])), 12, 31))
```

### LocalDateTable_88b91baa-b0c5-4627-b229-9188dd486d59

```sql
Calendar(Date(Year(MIN('vendpackingslipjour'[documentdate])), 1, 1), Date(Year(MAX('vendpackingslipjour'[documentdate])), 12, 31))
```

### LocalDateTable_310a1b4b-1ce0-445e-8462-432ec7ee3792

```sql
Calendar(Date(Year(MIN('vendpackingslipjour'[intrastatfulfillmentdate_hu])), 1, 1), Date(Year(MAX('vendpackingslipjour'[intrastatfulfillmentdate_hu])), 12, 31))
```

### LocalDateTable_9eef63f3-dc78-4edc-9aac-192be44b09ee

```sql
Calendar(Date(Year(MIN('vendpackingslipjour'[invoiceissueduedate_w])), 1, 1), Date(Year(MAX('vendpackingslipjour'[invoiceissueduedate_w])), 12, 31))
```

### LocalDateTable_0e515db4-907e-4fba-811a-dae635cbbf83

```sql
Calendar(Date(Year(MIN('vendpackingslipjour'[modifieddatetime])), 1, 1), Date(Year(MAX('vendpackingslipjour'[modifieddatetime])), 12, 31))
```

### LocalDateTable_a1f884ba-4136-4f46-bbab-7929c2f8654e

```sql
Calendar(Date(Year(MIN('vendpackingslipjour'[createddatetime])), 1, 1), Date(Year(MAX('vendpackingslipjour'[createddatetime])), 12, 31))
```

### LocalDateTable_6f7de4f8-ce39-4aa5-a4b3-fc3a2a46d91f

```sql
Calendar(Date(Year(MIN('vendpackingslipjour'[createdon])), 1, 1), Date(Year(MAX('vendpackingslipjour'[createdon])), 12, 31))
```

### LocalDateTable_800bf14c-e100-4064-be0c-b061a417ef67

```sql
Calendar(Date(Year(MIN('vendpackingslipjour'[modifiedon])), 1, 1), Date(Year(MAX('vendpackingslipjour'[modifiedon])), 12, 31))
```

### vendpackingsliptrans

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_D365_Prod"),
    dbo_vendpackingsliptrans = Source{[Schema="dbo",Item="vendpackingsliptrans"]}[Data]
in
    dbo_vendpackingsliptrans
```

### LocalDateTable_896c927d-236a-42d4-ab9c-97b7dedc513c

```sql
Calendar(Date(Year(MIN('vendpackingsliptrans'[SinkCreatedOn])), 1, 1), Date(Year(MAX('vendpackingsliptrans'[SinkCreatedOn])), 12, 31))
```

### LocalDateTable_86bce2c6-eeb8-4444-8a7a-9c4b6ca28030

```sql
Calendar(Date(Year(MIN('vendpackingsliptrans'[SinkModifiedOn])), 1, 1), Date(Year(MAX('vendpackingsliptrans'[SinkModifiedOn])), 12, 31))
```

### LocalDateTable_271bdd32-be18-4626-a6fb-c23b35ae2c98

```sql
Calendar(Date(Year(MIN('vendpackingsliptrans'[accountingdate])), 1, 1), Date(Year(MAX('vendpackingsliptrans'[accountingdate])), 12, 31))
```

### LocalDateTable_b1fd0ba2-883e-458d-b245-750ba5188ec2

```sql
Calendar(Date(Year(MIN('vendpackingsliptrans'[deliverydate])), 1, 1), Date(Year(MAX('vendpackingsliptrans'[deliverydate])), 12, 31))
```

### LocalDateTable_4204e042-d9ac-4400-9a91-8e2edb5b51af

```sql
Calendar(Date(Year(MIN('vendpackingsliptrans'[intrastatfulfillmentdate_hu])), 1, 1), Date(Year(MAX('vendpackingsliptrans'[intrastatfulfillmentdate_hu])), 12, 31))
```

### LocalDateTable_b2d87814-aed1-45c3-a782-8565ba3d5ea2

```sql
Calendar(Date(Year(MIN('vendpackingsliptrans'[inventdate])), 1, 1), Date(Year(MAX('vendpackingsliptrans'[inventdate])), 12, 31))
```

### LocalDateTable_45fa4b40-c295-4107-a433-8c7e162cf5c9

```sql
Calendar(Date(Year(MIN('vendpackingsliptrans'[purchaselineexpecteddeliverydate])), 1, 1), Date(Year(MAX('vendpackingsliptrans'[purchaselineexpecteddeliverydate])), 12, 31))
```

### LocalDateTable_1c99ecf4-f9bb-4cfb-86b4-b7d8edb1bdea

```sql
Calendar(Date(Year(MIN('vendpackingsliptrans'[modifieddatetime])), 1, 1), Date(Year(MAX('vendpackingsliptrans'[modifieddatetime])), 12, 31))
```

### LocalDateTable_8d1b51bb-d3c4-4872-aed8-48c5438042d1

```sql
Calendar(Date(Year(MIN('vendpackingsliptrans'[createddatetime])), 1, 1), Date(Year(MAX('vendpackingsliptrans'[createddatetime])), 12, 31))
```

### LocalDateTable_7def9d6f-1330-4645-a0c2-71e97a7bf84a

```sql
Calendar(Date(Year(MIN('vendpackingsliptrans'[createdon])), 1, 1), Date(Year(MAX('vendpackingsliptrans'[createdon])), 12, 31))
```

### LocalDateTable_9da39c5f-d981-4e31-92a9-3a4d33add5e1

```sql
Calendar(Date(Year(MIN('vendpackingsliptrans'[modifiedon])), 1, 1), Date(Year(MAX('vendpackingsliptrans'[modifiedon])), 12, 31))
```

### product_dim

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Mart"),
    dbo_product_dim = Source{[Schema="dbo",Item="product_dim"]}[Data]
in
    dbo_product_dim
```

### LocalDateTable_4cdf63e2-680c-4c3d-be61-06db7b11505d

```sql
Calendar(Date(Year(MIN('product_dim'[activation_date])), 1, 1), Date(Year(MAX('product_dim'[activation_date])), 12, 31))
```

### LocalDateTable_eef152c8-ca4d-426f-a91f-30506096e648

```sql
Calendar(Date(Year(MIN('product_dim'[INS_DT])), 1, 1), Date(Year(MAX('product_dim'[INS_DT])), 12, 31))
```

### LocalDateTable_647c0176-1fdb-4ad8-a24b-fa7da30d873b

```sql
Calendar(Date(Year(MIN('product_dim'[UPDT_DT])), 1, 1), Date(Year(MAX('product_dim'[UPDT_DT])), 12, 31))
```

### LocalDateTable_dd5c4cb9-8e95-4e48-9643-e57ea389a335

```sql
Calendar(Date(Year(MIN('product_dim'[InDate])), 1, 1), Date(Year(MAX('product_dim'[InDate])), 12, 31))
```

### LocalDateTable_f84276f5-c3b0-42a1-98cb-727a2ce69de1

```sql
Calendar(Date(Year(MIN('product_dim'[OutDate])), 1, 1), Date(Year(MAX('product_dim'[OutDate])), 12, 31))
```

### attribute_dim

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Mart"),
    dbo_attribute_dim = Source{[Schema="dbo",Item="attribute_dim"]}[Data]
in
    dbo_attribute_dim
```

### LocalDateTable_a0a6b214-2717-42d1-9279-b27a81859e88

```sql
Calendar(Date(Year(MIN('attribute_dim'[INS_DT])), 1, 1), Date(Year(MAX('attribute_dim'[INS_DT])), 12, 31))
```

### LocalDateTable_dfd780ce-9052-4bc9-b75e-c044ded2e9dc

```sql
Calendar(Date(Year(MIN('attribute_dim'[UPDT_DT])), 1, 1), Date(Year(MAX('attribute_dim'[UPDT_DT])), 12, 31))
```

### store_dim

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Mart"),
    dbo_store_dim = Source{[Schema="dbo",Item="store_dim"]}[Data]
in
    dbo_store_dim
```

### LocalDateTable_55d5ec12-4c40-4f3b-9036-99663a3411de

```sql
Calendar(Date(Year(MIN('store_dim'[opening_date])), 1, 1), Date(Year(MAX('store_dim'[opening_date])), 12, 31))
```

### LocalDateTable_fdd205e1-11fb-40fd-9897-1328ea401a16

```sql
Calendar(Date(Year(MIN('store_dim'[closing_date])), 1, 1), Date(Year(MAX('store_dim'[closing_date])), 12, 31))
```

### LocalDateTable_529789c6-0dd6-4f91-b3eb-a9d01fcac50e

```sql
Calendar(Date(Year(MIN('store_dim'[comp_date])), 1, 1), Date(Year(MAX('store_dim'[comp_date])), 12, 31))
```

### LocalDateTable_b46ceba0-9583-4df1-915d-f0ce667e4969

```sql
Calendar(Date(Year(MIN('store_dim'[INS_DT])), 1, 1), Date(Year(MAX('store_dim'[INS_DT])), 12, 31))
```

### LocalDateTable_848f3f00-e68d-42bf-9843-bf98f0a85d2c

```sql
Calendar(Date(Year(MIN('store_dim'[UPDT_DT])), 1, 1), Date(Year(MAX('store_dim'[UPDT_DT])), 12, 31))
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com | LH_D365_Prod | [4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/LH_D365_Prod](../../../4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/DataDictionary/LH_D365_Prod/) |
| 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com | LH_Mart | [4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/LH_Mart](../../../4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/DataDictionary/LH_Mart/) |
