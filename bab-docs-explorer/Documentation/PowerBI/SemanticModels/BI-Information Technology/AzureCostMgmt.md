# AzureCostMgmt

**Workspace:** BI-Information Technology  
**Dataset ID:** 22b15e53-0f15-442c-ab5f-5119949a339b  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| DateTableTemplate_69e58495-c210-412c-b88a-9e24d6fc6023 | 8 | 0 | Yes |
| VMUsage | 13 | 0 |  |
| VMSizes | 6 | 0 |  |
| ManagedDisksList | 3 | 0 |  |
| Subscriptions | 4 | 0 |  |
| RI Usage Summary | 6 | 1 |  |
| AHBUsage | 16 | 0 |  |
| Pricesheet | 18 | 0 |  |
| RI Transactions | 22 | 0 |  |
| LocalDateTable_f7425414-9b4d-45e8-966e-3d22589098a2 | 8 | 0 | Yes |
| RI Recommendations | 15 | 0 |  |
| LocalDateTable_83d766ef-24f3-428a-afbc-db87de03fa4b | 8 | 0 | Yes |
| RI Usage | 14 | 0 |  |
| Usage Details | 58 | 0 |  |
| Usage Details Amortized | 40 | 0 |  |
| Calendar | 7 | 0 |  |
| LocalDateTable_ff717656-048c-4961-b672-ea2681a63862 | 8 | 0 | Yes |
| LocalDateTable_ea4e3672-4e4d-4950-acfd-c02d9f7bbbda | 8 | 0 | Yes |
| RI Recommendations (Shared) | 15 | 0 |  |
| LocalDateTable_725fea37-82ad-4886-9f14-be6cd2c89d46 | 8 | 0 | Yes |
| Resources | 10 | 0 |  |
| LocalDateTable_8aabaf90-59ce-4aa0-b83f-a079824ad3b2 | 8 | 0 | Yes |
| LocalDateTable_74f15508-f520-49c9-a78a-4908c4ec2d3d | 8 | 0 | Yes |
| LocalDateTable_d72149ad-9bec-479e-b676-0763268632ab | 8 | 0 | Yes |
| WindowsLicenses | 5 | 0 | Yes |
| Usage Meters | 8 | 0 |  |
| LocalDateTable_115c171a-914d-4c1b-ae69-13f10139ca3b | 8 | 0 | Yes |
| LocalDateTable_20ae3d31-8c42-4349-9387-b9d12dbe59dc | 8 | 0 | Yes |
| LocalDateTable_c51f6cf8-2a58-4cc1-8cd2-8db7a240c9f1 | 8 | 0 | Yes |
| LocalDateTable_5a6ed0f6-a37b-482f-89cc-264ef1da5fec | 8 | 0 | Yes |

## Measures

### RI Usage Summary.Utilisation

```sql
AVERAGEX('RI Usage Summary','RI Usage Summary'[UsedHours]/'RI Usage Summary'[ReservedHours])
```

## Power Query Source (per table)

### DateTableTemplate_69e58495-c210-412c-b88a-9e24d6fc6023

```sql
Calendar(Date(2015,1,1), Date(2015,1,1))
```

### VMUsage

```sql
SUMMARIZECOLUMNS('Usage Details'[ResourceId],FILTER('Usage Details','Usage Details'[MeterCategory] = "Virtual Machines" && 'Usage Details'[MeterName] <> "Compute Hours"),"AvgHours",AVERAGE('Usage Details'[Quantity]),"LastUsageDate",MAX('Usage Details'[Date]),"Cost",SUM('Usage Details'[Cost]),"TotalHours",SUM('Usage Details'[Quantity]),"30DaysQty",CALCULATE(SUM('Usage Details'[Quantity]),FILTER('Usage Details','Usage Details'[Date]>max('Usage Details'[Date])-30)),"VMSize",LASTNONBLANK('Usage Details'[ServiceType],1),"OS Type",LASTNONBLANK('Usage Details'[OS Type],1))
```

### VMSizes

```sql
let
    Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("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", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [name = _t, numberOfCores = _t, memoryInMB = _t, maxDataDiskCount = _t, resourceDiskSizeInMB = _t]),
    Source2 = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("nVXBitswEP2XnLegGY1G8rG4hT2VQqGXZQkBX3pwF7yl319pLCmVJQdpD3Ei/J703puZ6OXl8uPP7fdy25brl5ner3/15elC/qPRsvPfwP6hLq9PBdJFZECwMZqF0UICR6hsBBqUxVMwJgUYJMDErNwpWGMEy2tkBKJTMCXFJBtOGuGB5iVpDhZhwpiJT0TVmhMYxaR2FHMBH0sNp+UsZO2TqfFuOYuavd8aD7ycBw6IrmUhi2rkDo50Q5fOvhvxIxnb8p7NNKrQ5Hz7GdpH3AYpQOwkL3Hk7TMd8YCRIBjESVtOxjwZ0B0Z0nSYMGScNffAPBsNNw/R6ZAeWWVn98gqO7aUpRXIsqB8BcBfN08yognvO/sfVPf5jl8eELSboCr980z0CXh7D6oExYp2jWFEoJ4RYWgcZAzAfZcEH59B7V5CsoZ910bO3sJ1EQtSLCUyqThtml1YHGmupDmpp0Gn0sxZbcPqwNNe4/ofUQZ5Uv5ElUdgohB4i3kkklGGMxHIUlgeiLZ0KP8DXSdyCtFqqQDeu6FOsRoDqRVP3Mgc8255BKTTTgzw9fv2tr6NqMmMAU2Z061s7k9oHkpoHkvIw7cx3YOJzh9IdP5Qot7JMOvZxVFNRvZpUOgvxgqad+8k7Pdnce+IElTkWuh7Tr0ct0Y1GfxI/1oY6KEAr0lOGeaZhbX00EfaxmLaxnPywrZBI1uXk9d/", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type nullable text) meta [Serialized.Text = true]) in type table [name = _t, numberOfCores = _t, memoryInMB = _t, maxDataDiskCount = _t, resourceDiskSizeInMB = _t]),
    vmSizes = Table.Combine({Source, Source2}),
    #"Changed Type" = Table.TransformColumnTypes(vmSizes,{{"name", type text}, {"numberOfCores", Int64.Type}, {"memoryInMB", Int64.Type}, {"maxDataDiskCount", Int64.Type}, {"resourceDiskSizeInMB", Int64.Type}}),
    #"Replaced Value" = Table.ReplaceValue(#"Changed Type"," ","",Replacer.ReplaceText,{"name"})
in
    #"Replaced Value"
```

### ManagedDisksList

```sql
let
    Source = Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText("XdCxDcUgDATQXahTgMFABnD/pSuj7L/GB+KCo/MJn3jy84RfCVfIEt5rzHXMtXxziiMk6Z50JNH6JZlvmryV12YUL5YZJRZv6owl3upfzNjT7d22ujV3L/e4OK22lY0URgojhbHCWGGsMFbYobBDge1G2G4E0oF0IB1YB9aBdWAdDh123fsH", BinaryEncoding.Base64), Compression.Deflate)), let _t = ((type text) meta [Serialized.Text = true]) in type table [#"Disk Type" = _t, Capacity = _t]),
    #"Changed Type" = Table.TransformColumnTypes(Source,{{"Disk Type", type text}, {"Capacity", type number}})
in
    #"Changed Type"
```

### Subscriptions

```sql
SUMMARIZECOLUMNS('Usage Details'[SubscriptionId],'Usage Details'[SubscriptionName])
```

### RI Usage Summary

```sql
SUMMARIZECOLUMNS('RI Usage'[reservationOrderId],'RI Usage'[reservationId],'RI Usage'[usageDate], "ReservedHours",AVERAGE('RI Usage'[normalisedReservedHours]),"UsedHours",SUM('RI Usage'[normalisedUsedHours]))
```

### AHBUsage

```sql
SUMMARIZECOLUMNS('Usage Details'[ResourceId],'Usage Details'[Date],FILTER('Usage Details','Usage Details'[MeterCategory] = "Virtual Machines" && 'Usage Details'[Date]>max('Usage Details'[Date])-30),"Compute Hours",SUM('Usage Details'[Quantity]),"VMSize",LASTNONBLANK('Usage Details'[ServiceType],1),"OS Type",LASTNONBLANK('Usage Details'[OS Type],1),"OfferId",LASTNONBLANK('Usage Details'[OfferId],1))


```

### Pricesheet

```sql
let
    Source = AzureCostManagement.Tables(Scope, ScopeIdentifier, 1, [startDate=null, endDate=null]),
    pricesheets = Source{[Key="pricesheets"]}[Data],
    #"Renamed Columns" = Table.RenameColumns(pricesheets,{{"Unit of measure","unitOfMeasure"}, {"billingCurrency","Currency code"}, {"meterCategory", "Meter category"}, {"meterId","Meter ID"}, {"meterName","Meter name"}, {"meterRegion","Meter region"},{"meterSubCategory","Meter sub-category"}, {"productOrderName","Offer Id"}, {"unitPrice","Unit price"}, {"productId","Part number"}, {"Units","Unit"}},MissingField.Ignore),
    #"Removed Columns" = Table.RemoveColumns(#"Renamed Columns",{"Unit","tierMinimumUnits","skuId"},MissingField.Ignore),
    #"Removed Duplicates" = Table.Distinct(#"Removed Columns")
in
    #"Removed Duplicates"
```

### RI Transactions

```sql
let
    Source = AzureCostManagement.Tables(Scope, ScopeIdentifier, LookbackMonths, [startDate=null, endDate=null]),
    ritransactions = Source{[Key="ritransactions"]}[Data],
    #"Changed Type" = Table.TransformColumnTypes(ritransactions,{{"eventDate", type datetime}}),
    #"Duplicated Column" = Table.DuplicateColumn(#"Changed Type", "eventDate", "eventTime"),
    #"Extracted Date" = Table.TransformColumns(#"Duplicated Column",{{"eventDate", DateTime.Date, type date}}),
    #"Changed Type1" = Table.TransformColumnTypes(#"Extracted Date",{{"amount", type number}}),
    #"Removed Columns" = Table.RemoveColumns(#"Changed Type1",{"type", "tags", "accountName", "accountOwnerEmail","billingProfileId","billingProfileName"},MissingField.Ignore)
in
    #"Removed Columns"
```

### LocalDateTable_f7425414-9b4d-45e8-966e-3d22589098a2

```sql
Calendar(Date(Year(MIN('RI Transactions'[eventTime])), 1, 1), Date(Year(MAX('RI Transactions'[eventTime])), 12, 31))
```

### RI Recommendations

```sql
let
    Source = AzureCostManagement.Tables(Scope, ScopeIdentifier, LookbackMonths, [startDate=null, endDate=null]),
    rirecommendations = Source{[Key="rirecommendationssingle"]}[Data],
    #"Removed Columns" = Table.RemoveColumns(rirecommendations,{"type", "eTag", "lookBackPeriod", "skuProperties"}, MissingField.Ignore)
in
    #"Removed Columns"
```

### LocalDateTable_83d766ef-24f3-428a-afbc-db87de03fa4b

```sql
Calendar(Date(Year(MIN('RI Recommendations'[firstUsageDate])), 1, 1), Date(Year(MAX('RI Recommendations'[firstUsageDate])), 12, 31))
```

### RI Usage

```sql
let
    numMonths = if LookbackMonths > 2 then 2 else LookbackMonths,
    Source = AzureCostManagement.Tables(Scope, ScopeIdentifier, numMonths, [startDate = null, endDate = null]),
    riusage = Source{[Key="riusagedetails"]}[Data],
    #"Extracted Date" = Table.TransformColumns(riusage,{{"usageDate", DateTime.Date, type date}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Extracted Date",{{"reservedHours", type number}, {"usedHours", type number}})
in
    #"Changed Type"
```

### Usage Details

```sql
let
    Source = AzureCostManagement.Tables(Scope, ScopeIdentifier, LookbackMonths, [startDate=null, endDate=null]),
    usagedetails = Source{[Key="usagedetails"]}[Data],
    #"Renamed Columns" = Table.RenameColumns(usagedetails,{{"payGPrice", "PayGPrice"}, {"resourceGroupName", "ResourceGroup"}, {"resourceId", "ResourceId"}, {"subscriptionId", "SubscriptionId"}, {"subscriptionName", "SubscriptionName"}, {"quantity", "Quantity"}, {"productOrderName", "OfferId"}, {"additionalInfo", "AdditionalInfo"}, {"costInBillingCurrency", "Cost"}, {"meterId", "MeterId"}, {"publisherType", "PublisherType"}, {"publisherName", "PublisherName"}, {"chargeType","ChargeType"}, {"unitOfMeasure","UnitOfMeasure"}, {"date","Date"}, {"meterCategory","MeterCategory"}, {"meterName","MeterName"}, {"meterRegion","MeterRegion"}, {"meterSubCategory","MeterSubCategory"}},MissingField.Ignore),
    #"Changed Type" = if Scope = "Enrollment Number" then Table.TransformColumnTypes(#"Renamed Columns",{{"PayGPrice", type number}}) else Table.TransformColumnTypes(#"Renamed Columns",{{"PayGPrice", type number},{"costInUsd", type number},{"paygCostInBillingCurrency", type number},{"paygCostInUsd", type number},{"unitPrice", type number}}),
    #"Removed Columns" = Table.RemoveColumns(#"Changed Type",{"BillingAccountName", "BillingProfileName", "AccountOwnerId", "AccountName", "InvoiceSectionId", "InvoiceSection", "BillingProfileId", "billingAccountName", "billingProfileName", "billingAccountId", "invoiceSectionId", "invoiceSectionName", "billingProfileId","ResourceName"},MissingField.Ignore),
    #"Duplicated Column" = Table.DuplicateColumn(#"Removed Columns", "ResourceId", "ResourceId - Copy"),
    #"Split Column by Delimiter" = Table.SplitColumn(#"Duplicated Column", "ResourceId - Copy", Splitter.SplitTextByEachDelimiter({"/"}, QuoteStyle.Csv, true), {"ResourceId.1", "ResourceId.2"}),
    #"Removed Columns1" = Table.RemoveColumns(#"Split Column by Delimiter",{"ResourceId.1"}),
    #"Renamed Columns1" = Table.RenameColumns(#"Removed Columns1",{{"ResourceId.2", "ResourceName"}}),
    #"Added Custom" = Table.AddColumn(#"Renamed Columns1", "JsonTags", each "{"&[Tags]&"}"),
    #"Parsed JSON" = Table.TransformColumns(#"Added Custom",{{"JsonTags", Json.Document}}),
    #"Expanded JsonTags" = Table.ExpandRecordColumn(#"Parsed JSON", "JsonTags", {"App"}, {"JsonTags.App"}),
    #"Added Custom1" = Table.AddColumn(#"Expanded JsonTags", "JsonTags", each "{"&[Tags]&"}"),
    #"Parsed JSON1" = Table.TransformColumns(#"Added Custom1",{{"JsonTags", Json.Document}}),
    #"Expanded JsonTags1" = Table.ExpandRecordColumn(#"Parsed JSON1", "JsonTags", {"Env"}, {"JsonTags.Env"}),
    #"Added Custom2" = Table.AddColumn(#"Expanded JsonTags1", "JsonTags", each "{"&[Tags]&"}"),
    #"Parsed JSON2" = Table.TransformColumns(#"Added Custom2",{{"JsonTags", Json.Document}}),
    #"Expanded JsonTags2" = Table.ExpandRecordColumn(#"Parsed JSON2", "JsonTags", {"IT Dept"}, {"JsonTags.IT Dept"}),
    #"Added Custom3" = Table.AddColumn(#"Expanded JsonTags2", "JsonTags", each "{"&[Tags]&"}"),
    #"Parsed JSON3" = Table.TransformColumns(#"Added Custom3",{{"JsonTags", Json.Document}}),
    #"Expanded JsonTags3" = Table.ExpandRecordColumn(#"Parsed JSON3", "JsonTags", {"Region"}, {"JsonTags.Region"})
in
    #"Expanded JsonTags3"
```

### Usage Details Amortized

```sql
let
    Source = AzureCostManagement.Tables(Scope, ScopeIdentifier, LookbackMonths, [startDate=null, endDate=null]),
    usagedetailsamortized = Source{[Key="usagedetailsamortized"]}[Data],
    #"Renamed Columns" = Table.RenameColumns(usagedetailsamortized,{{"payGPrice", "PayGPrice"}, {"resourceGroupName", "ResourceGroup"}, {"resourceId", "ResourceId"}, {"subscriptionId", "SubscriptionId"}, {"subscriptionName", "SubscriptionName"}, {"quantity", "Quantity"}, {"productOrderName", "OfferId"}, {"additionalInfo", "AdditionalInfo"}, {"costInBillingCurrency", "Cost"}, {"meterId", "MeterId"}, {"publisherType", "PublisherType"}, {"publisherName", "PublisherName"},{"chargeType", "ChargeType"}, {"unitOfMeasure","UnitOfMeasure"}, {"date","Date"}, {"meterCategory","MeterCategory"}, {"meterName","MeterName"}, {"meterRegion","MeterRegion"}, {"meterSubCategory","MeterSubCategory"}},MissingField.Ignore),
    #"Changed Type" = Table.TransformColumnTypes(#"Renamed Columns",{{"PayGPrice", type number}}),
    #"Removed Columns" = Table.RemoveColumns(#"Changed Type",{"BillingAccountName", "BillingProfileName", "AccountOwnerId", "AccountName", "InvoiceSectionId", "InvoiceSection", "BillingProfileId", "billingAccountName", "billingProfileName", "billingAccountId", "invoiceSectionId", "invoiceSectionName", "billingProfileId", "CostCenter", "ResourceGroup", "ServiceFamily", "MeterCategory", "MeterSubCategory", "MeterRegion", "MeterName", "ResourceName", "AvailabilityZone"},MissingField.Ignore)
in
    #"Removed Columns"
```

### Calendar

```sql
CALENDAR(FIRSTDATE('Usage Details'[Date]),LASTDATE('Usage Details'[Date]))
```

### LocalDateTable_ff717656-048c-4961-b672-ea2681a63862

```sql
Calendar(Date(Year(MIN('Calendar'[Date])), 1, 1), Date(Year(MAX('Calendar'[Date])), 12, 31))
```

### LocalDateTable_ea4e3672-4e4d-4950-acfd-c02d9f7bbbda

```sql
Calendar(Date(Year(MIN('Calendar'[Month])), 1, 1), Date(Year(MAX('Calendar'[Month])), 12, 31))
```

### RI Recommendations (Shared)

```sql
let
    Source = AzureCostManagement.Tables(Scope, ScopeIdentifier, LookbackMonths, [startDate=null, endDate=null]),
    rirecommendations = Source{[Key="rirecommendationsshared"]}[Data],
    #"Removed Columns" = Table.RemoveColumns(rirecommendations,{"type", "eTag", "lookBackPeriod", "skuProperties"})
in
    #"Removed Columns"
```

### LocalDateTable_725fea37-82ad-4886-9f14-be6cd2c89d46

```sql
Calendar(Date(Year(MIN('RI Recommendations (Shared)'[firstUsageDate])), 1, 1), Date(Year(MAX('RI Recommendations (Shared)'[firstUsageDate])), 12, 31))
```

### Resources

```sql
SUMMARIZECOLUMNS('Usage Details'[SubscriptionId],'Usage Details'[ResourceGroup],'Usage Details'[ResourceId],'Usage Details'[ResourceName],FILTER('Usage Details',AND('Usage Details'[ResourceId]<>"",'Usage Details'[SubscriptionId]<>"00000000-0000-0000-0000-000000000000")),"FirstDateSeen",FIRSTDATE('Usage Details'[Date]),"Tags",LASTNONBLANK('Usage Details'[Tags],TRUE()))
```

### LocalDateTable_8aabaf90-59ce-4aa0-b83f-a079824ad3b2

```sql
Calendar(Date(Year(MIN('Calendar'[Week])), 1, 1), Date(Year(MAX('Calendar'[Week])), 12, 31))
```

### LocalDateTable_74f15508-f520-49c9-a78a-4908c4ec2d3d

```sql
Calendar(Date(Year(MIN('VMUsage'[LastUsageDate])), 1, 1), Date(Year(MAX('VMUsage'[LastUsageDate])), 12, 31))
```

### LocalDateTable_d72149ad-9bec-479e-b676-0763268632ab

```sql
Calendar(Date(Year(MIN('Resources'[FirstDateSeen])), 1, 1), Date(Year(MAX('Resources'[FirstDateSeen])), 12, 31))
```

### WindowsLicenses

```sql
SUMMARIZECOLUMNS(Pricesheet[Meter ID],Pricesheet[Meter sub-category],Pricesheet[Offer Id],filter(Pricesheet,Pricesheet[Meter category] = "Virtual Machines Licenses" && (Pricesheet[Meter sub-category] = "Windows Server Burst" || Pricesheet[Meter sub-category] = "Windows Server") && Pricesheet[Meter name] = "1 vCPU VM License"),"Unit price",MIN(Pricesheet[Per Unit price]))
```

### Usage Meters

```sql
SUMMARIZECOLUMNS('Usage Details'[OfferId],'Usage Details'[MeterId],"MeterCategory",FIRSTNONBLANK('Usage Details'[MeterCategory],1),"MeterSubCategory",FIRSTNONBLANK('Usage Details'[MeterSubCategory],1),"MeterRegion",FIRSTNONBLANK('Usage Details'[MeterRegion],1),"MeterName",FIRSTNONBLANK('Usage Details'[MeterName],1))
```

### LocalDateTable_115c171a-914d-4c1b-ae69-13f10139ca3b

```sql
Calendar(Date(Year(MIN('Usage Details'[BillingPeriodStartDate])), 1, 1), Date(Year(MAX('Usage Details'[BillingPeriodStartDate])), 12, 31))
```

### LocalDateTable_20ae3d31-8c42-4349-9387-b9d12dbe59dc

```sql
Calendar(Date(Year(MIN('Usage Details'[BillingPeriodEndDate])), 1, 1), Date(Year(MAX('Usage Details'[BillingPeriodEndDate])), 12, 31))
```

### LocalDateTable_c51f6cf8-2a58-4cc1-8cd2-8db7a240c9f1

```sql
Calendar(Date(Year(MIN('Usage Details Amortized'[BillingPeriodStartDate])), 1, 1), Date(Year(MAX('Usage Details Amortized'[BillingPeriodStartDate])), 12, 31))
```

### LocalDateTable_5a6ed0f6-a37b-482f-89cc-264ef1da5fec

```sql
Calendar(Date(Year(MIN('Usage Details Amortized'[BillingPeriodEndDate])), 1, 1), Date(Year(MAX('Usage Details Amortized'[BillingPeriodEndDate])), 12, 31))
```

## Shared Expressions

### ScopeIdentifier (0)

```sql
"62077340" meta [IsParameterQuery=true, Type="Text", IsParameterQueryRequired=true]
```

### Scope (0)

```sql
"Enrollment Number" meta [IsParameterQuery=true, List={"Enrollment Number", "Billing Profile Id", "Manually Input Scope"}, DefaultValue="Enrollment Number", Type="Text", IsParameterQueryRequired=true]
```

### LookbackMonths (0)

```sql
12 meta [IsParameterQuery=true, Type="Number", IsParameterQueryRequired=true]
```

### RIPriceSheet (0)

```sql
let
    iterations = 1000, // 100 per page, gives 100000 possibles
    skipDefault = 100,
    url = "http://prices.azure.com/",
    relPath = "api/retail/prices",
    currCode = "'AUD'",

    FnGetOnePage =
     (skipAmount) as record =>
      let
       Source = Json.Document(Web.Contents(url,[RelativePath=relPath,Query=[currencyCode=currCode,#"$skip"=Number.ToText(skipAmount),#"$filter"="priceType eq 'Reservation'"]])),
       data = try Source[Items] otherwise null,
       next = try Source[NextPageLink] otherwise null,
       skipAmt = try Source[Count] otherwise skipDefault,
       res = [Data=data, Next=next, SkipAmount = skipAmt]
      in
       res,

    GeneratedList =
     List.Generate(
      ()=>[i=0, res = FnGetOnePage(i*skipDefault)],
      each [i]<iterations and [res][Data]<>null,
      each [i=[i]+1, res = FnGetOnePage(i*[res][SkipAmount])],
      each [res][Data]),
    #"Converted to Table" = Table.FromList(GeneratedList, Splitter.SplitByNothing(), null, null, ExtraValues.Error),
    #"Expanded Column1" = Table.ExpandListColumn(#"Converted to Table", "Column1"),
    #"Expanded Column2" = Table.ExpandRecordColumn(#"Expanded Column1", "Column1", {"currencyCode", "tierMinimumUnits", "reservationTerm", "retailPrice", "unitPrice", "armRegionName", "location", "effectiveStartDate", "meterId", "meterName", "productId", "skuId", "productName", "skuName", "serviceName", "serviceId", "serviceFamily", "unitOfMeasure", "type", "isPrimaryMeterRegion", "armSkuName"}, {"currencyCode", "tierMinimumUnits", "reservationTerm", "retailPrice", "unitPrice", "armRegionName", "location", "effectiveStartDate", "meterId", "meterName", "productId", "skuId", "productName", "skuName", "serviceName", "serviceId", "serviceFamily", "unitOfMeasure", "type", "isPrimaryMeterRegion", "armSkuName"}),
    #"Removed Columns" = Table.RemoveColumns(#"Expanded Column2",{"tierMinimumUnits", "unitPrice", "skuId", "type", "isPrimaryMeterRegion", "effectiveStartDate"}),
    #"Changed Type" = Table.TransformColumnTypes(#"Removed Columns",{{"retailPrice", type number}}),
    #"Filtered Rows" = Table.SelectRows(#"Changed Type", each [reservationTerm] <> null and [reservationTerm] <> ""),
    #"Pivoted Column" = Table.Pivot(#"Filtered Rows", List.Distinct(#"Filtered Rows"[reservationTerm]), "reservationTerm", "retailPrice"),
    #"Renamed Columns" = Table.RenameColumns(#"Pivoted Column",{{"1 Year", "1Year"}, {"3 Years", "3Years"}, {"5 Years", "5Years"}})
in
    #"Renamed Columns"
```

## Data Source Cross-References

_No recognized SQL data source references detected._
