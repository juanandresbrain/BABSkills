# Usage Metrics Report

**Workspace:** Enterprise Analytics Prod  
**Dataset ID:** 650f4e05-d941-4e45-9643-73cf7ad61141  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| Report views | 16 | 0 |  |
| DateTableTemplate_d531c5a6-f782-4ea4-a755-a9747139c561 | 8 | 0 | Yes |
| Model measures | 1 | 46 |  |
| Report rank | 7 | 1 |  |
| Report page views | 17 | 0 |  |
| Report load times | 22 | 0 |  |
| LocalDateTable_3b852b25-f44a-4909-b021-a7df8cabefe6 | 8 | 0 | Yes |
| LocalDateTable_3ebb0033-50be-4e6e-8081-ee8c7cf4091f | 8 | 0 | Yes |
| LocalDateTable_dc7eb03a-ec8b-421f-b39b-107ea1f05736 | 8 | 0 | Yes |
| LocalDateTable_d27e4379-e50d-47cf-aeac-77eb5f688306 | 8 | 0 | Yes |
| Report pages | 5 | 0 |  |
| Reports | 6 | 0 |  |
| LocalDateTable_e9fae86b-d80b-4c31-9ba4-095822014411 | 8 | 0 | Yes |
| Refresh Stats | 2 | 0 | Yes |
| Dates | 5 | 0 |  |
| Workspace views | 8 | 0 |  |
| Workspace reports | 6 | 1 |  |
| LocalDateTable_bc207ece-a79c-4d33-a331-c40f45eb2725 | 8 | 0 | Yes |
| LocalDateTable_b465bb22-755a-4444-bc06-bd92af8a8952 | 8 | 0 | Yes |
| LocalDateTable_7e74b9e2-e4a5-4c05-8b29-c52b531c8abf | 8 | 0 | Yes |
| Users | 5 | 0 |  |
| Users_ReportPageView | 3 | 0 | Yes |

## Measures

### Model measures.Report views

```sql
COUNTROWS('Report views') + 0
```

### Model measures.Report viewers

```sql
DISTINCTCOUNT('Report views'[UserKey]) + 0
```

### Model measures.Page view share

```sql
DIVIDE(COUNTROWS('Report page views'), CALCULATE(COUNTROWS('Report page views'), ALL('Report pages'[SectionName])), 0)
```

### Model measures.View trend

```sql

var numberOfDays = DATEDIFF(MIN('Report views'[Date]), MAX('Report views'[Date]),DAY) + 1
var periodLength = INT(numberOfDays/2) - 1
var firstPeriod = CALCULATE([Report views], DATESBETWEEN('Report views'[Date], MIN('Report views'[Date]), MIN('Report views'[Date]) + periodLength))
var secondPeriod = CALCULATE([Report views], DATESBETWEEN('Report views'[Date], MAX('Report views'[Date]) - periodLength, MAX('Report views'[Date])))
return DIVIDE(secondPeriod - firstPeriod, firstPeriod)  + 0
```

### Model measures.P-50

```sql
PERCENTILE.INC('Report load times'[loadTime], 0.5) + 0
```

### Model measures.P-50 7d

```sql
CALCULATE([P-50], ALL(Dates), DATESINPERIOD('Report load times'[Date], max('Report load times'[Date]), -7, DAY)) + 0
```

### Model measures.P-25

```sql
PERCENTILE.INC('Report load times'[loadTime], 0.25) + 0
```

### Model measures.P-10

```sql
PERCENTILE.INC('Report load times'[loadTime], 0.1) + 0
```

### Model measures.P-90 7d

```sql
CALCULATE([P-90], ALL(Dates), DATESINPERIOD('Report load times'[Date], max('Report load times'[Date]), -7, DAY)) + 0
```

### Model measures.P-10 7d

```sql
CALCULATE([P-10], DATESINPERIOD('Report load times'[Date], max('Report load times'[Date]), -7, DAY)) + 0
```

### Model measures.Typical report opening interval

```sql
IF(ISBLANK(MAX('Report load times'[loadTime]) ), 
    "This report has no performance measurements.",
    IF(HASONEVALUE('Report load times'[loadTime]), 
        "This report only has a single performance measurement. The load time was " & MAX('Report load times'[loadTime]) & " seconds.", 
        IF([P-10] = [P-50] = [P-25], 
            "Across all measurements, this report loaded in  " & MAX('Report load times'[loadTime]) & " seconds.", 
            "For most of the users your report opens within " & INT([P-10 7d]) & " and " & INT([P-90 7d]) & " seconds." )))
```

### Model measures.Rank string

```sql
IF(HASONEVALUE(Reports[ReportGuid]), IF(ISBLANK(MAX('Report rank'[ReportRank])), "", "Rank " & MAX('Report rank'[ReportRank]) & " across "& [Total Org Report Count] & " reports in the organization"), "")
```

### Model measures.Performance trend

```sql

var numberOfDays = DATEDIFF(MIN('Report views'[Date]), MAX('Report views'[Date]),DAY) + 1
var periodLength = INT(numberOfDays/2) - 1
var firstPeriod = CALCULATE([P-50], DATESBETWEEN('Report load times'[Date], MIN('Report load times'[Date]), MIN('Report load times'[Date]) + periodLength))
var secondPeriod = CALCULATE([P-50], DATESBETWEEN('Report load times'[Date], MAX('Report load times'[Date]) - periodLength, MAX('Report load times'[Date])))
return DIVIDE(secondPeriod - firstPeriod, firstPeriod) + 0 * -1
```

### Model measures.Typical report opening time

```sql
[P-50] & " sec"
```

### Model measures.Workspace report viewers

```sql
DISTINCTCOUNT('Workspace views'[UserKey]) + 0
```

### Model measures.Workspace inactive reports

```sql
CALCULATE(DISTINCTCOUNT('Workspace reports'[ReportGuid]), 'Workspace reports'[Days with usage] = 0) + 0
```

### Model measures.Workspace views

```sql
SUM('Workspace views'[Views]) + 0
```

### Model measures.Workspace active days per report

```sql
DISTINCTCOUNT('Report views'[Date]) + 0
```

### Model measures.Workspace reports

```sql
DISTINCTCOUNT('Report views'[ReportId])
```

### Model measures.Workspace active reports

```sql
DISTINCTCOUNT('Workspace views'[ReportId]) + 0
```

### Model measures.Workspace report view %

```sql
DIVIDE([Workspace views], CALCULATE([Workspace views], ALL('Workspace views')))
```

### Model measures.Covered time display string

```sql
IF(ISBLANK(MAX('Report views'[CreationTime])), "No usage data", "Report usage based on data from " & 
DATE(
  YEAR(MIN('Report views'[CreationTime])),
  MONTH(MIN('Report views'[CreationTime])),
  DAY(MIN('Report views'[CreationTime]))
)
 & " to " & 
DATE(
  YEAR(MAX('Report views'[CreationTime])),
  MONTH(MAX('Report views'[CreationTime])),
  DAY(MAX('Report views'[CreationTime]))
))
```

### Model measures.Embedding for your organziation

```sql
CALCULATE([Report views], 'Report views'[OriginalConsumptionMethod] = "Embedding for your organization")
```

### Model measures.Embedding for your customers

```sql
CALCULATE([Report views], 'Report views'[OriginalConsumptionMethod] = "Embedding for your customers")
```

### Model measures.Simplified embedding

```sql
CALCULATE([Report views], 'Report views'[OriginalConsumptionMethod] = "Simplified embedding")
```

### Model measures.Workspace view trend

```sql

var startDate = CALCULATE(MIN('Dates'[Date]), ALL('Dates'))
var endDate = CALCULATE(MAX('Dates'[Date]), ALL('Dates'))
var numberOfDays = DATEDIFF(startDate, endDate, DAY) + 1
var periodLength = INT(numberOfDays/2) - 1
var middleDate1 =  CALCULATE(LASTDATE(DATESBETWEEN('Dates'[Date], startDate, startDate + periodLength)) , ALL('Dates'))
var middleDate2 =  CALCULATE(FIRSTDATE(DATESBETWEEN('Report views'[Date], endDate - periodLength, endDate)), ALL('Dates'))
var firstPeriod = CALCULATE([Report views], ALL('Dates'), DATESBETWEEN('Report views'[Date], startDate, middleDate1))
var secondPeriod = CALCULATE([Report views], ALL('Dates'), DATESBETWEEN('Report views'[Date], middleDate2, endDate))
//return startDate & "  " & middleDate1 & " " & middleDate2 & "  " & numberOfDays & ", " & periodLength & ": " & firstPeriod & "  " & secondPeriod
return DIVIDE(secondPeriod - firstPeriod, firstPeriod, 0)
```

### Model measures.Last refresh time display string

```sql
IF(ISBLANK(MAX('Refresh Stats'[Last Refresh])), 
	"Usage data has not been imported yet. Check the refresh history and data source credentials in the Usage Metrics Report dataset settings.", 
	IF(DATEVALUE(MAX('Refresh Stats'[Last Refresh])) < DATE(2019,11,20),
	"Usage data has not been imported yet. Check the refresh history and data source credentials in the Usage Metrics Report dataset settings.", 
	IF(DATEDIFF(MAX('Refresh Stats'[Last Refresh]), TODAY(), day ) > 4, 
		"The usage data is outdated. Check the refresh history and data source credentials in the Usage Metrics Report dataset settings.", 
		"Dataset last refreshed: " & MAX('Refresh Stats'[Last Refresh]) & " (UTC)")))
```

### Model measures.Report title

```sql
"Usage Metrics" & IF(HASONEVALUE(Reports[ReportGuid]), ": " & MAX('Reports'[ReportName]), " (Multiple reports selected)")
```

### Model measures.Report Id

```sql
IF(HASONEVALUE(Reports[ReportGuid]), MAX('Reports'[ReportGuid]), IF(DISTINCTCOUNT(Reports[ReportGuid]) = 0, "No reports selected", "Multiple reports selected"))
```

### Model measures.Covered perf time display string

```sql
IF(ISBLANK(MAX('Report load times'[Timestamp])), "No open report performance data", "Report performance based on data from " & 
DATE(
  YEAR(MIN('Report load times'[Timestamp])),
  MONTH(MIN('Report load times'[Timestamp])),
  DAY(MIN('Report load times'[Timestamp]))
)
 & " to " & 
DATE(
  YEAR(MAX('Report load times'[Timestamp])),
  MONTH(MAX('Report load times'[Timestamp])),
  DAY(MAX('Report load times'[Timestamp]))
))
```

### Model measures.P-25 7d

```sql
CALCULATE([P-25], ALL(Dates), DATESINPERIOD('Report load times'[Date], max('Report load times'[Date]), -7, DAY)) + 0
```

### Model measures.P-90

```sql
PERCENTILE.INC('Report load times'[loadTime], 0.9) + 0
```

### Model measures.P-75

```sql
PERCENTILE.INC('Report load times'[loadTime], 0.75) + 0
```

### Model measures.P-75 7d

```sql
CALCULATE([P-75], ALL(Dates), DATESINPERIOD('Report load times'[Date], max('Report load times'[Date]), -7, DAY)) + 0
```

### Model measures.Total page views

```sql
COUNTROWS('Report page views')
```

### Model measures.Total page users

```sql
DISTINCTCOUNT('Report page views'[UserKey])
```

### Model measures.Weekly Viewers

```sql

    var sop = CALCULATE(MIN('Dates'[Date]), ALL('Dates'), Dates[DoW] = 1)
    var eop = CALCULATE(MAX('Dates'[Date]), ALL('Dates'), Dates[DoW] = 7)
return
    IF(AND(MIN('Dates'[Date]) >= sop, MAX('Dates'[Date]) <= eop),
    CALCULATE(DISTINCTCOUNT('Report views'[UserKey]), DATESBETWEEN(Dates[Date], Min(Dates[fDoW]), MAX(Dates[lDoW]))),
    BLANK())
```

### Model measures.Weekly Views

```sql

    var sop = CALCULATE(MIN('Dates'[Date]), ALL('Dates'), Dates[DoW] = 1)
    var eop = CALCULATE(MAX('Dates'[Date]), ALL('Dates'), Dates[DoW] = 7)
return
    IF(AND(MIN('Dates'[Date]) >= sop, MAX('Dates'[Date]) <= eop),
    CALCULATE(COUNTROWS('Report views'), DATESBETWEEN(Dates[Date], Min(Dates[fDoW]), MAX(Dates[lDoW]))),
    BLANK())
```

### Model measures.P-10 trend

```sql

var numberOfDays = DATEDIFF(MIN('Report views'[Date]), MAX('Report views'[Date]),DAY) + 1
var periodLength = INT(numberOfDays/2) - 1
var firstPeriod = CALCULATE([P-10], DATESBETWEEN('Report load times'[Date], MIN('Report load times'[Date]), MIN('Report load times'[Date]) + periodLength))
var secondPeriod = CALCULATE([P-10], DATESBETWEEN('Report load times'[Date], MAX('Report load times'[Date]) - periodLength, MAX('Report load times'[Date])))
return DIVIDE(secondPeriod - firstPeriod, firstPeriod) + 0 * -1
```

### Model measures.P-25 trend

```sql

var numberOfDays = DATEDIFF(MIN('Report views'[Date]), MAX('Report views'[Date]),DAY) + 1
var periodLength = INT(numberOfDays/2) - 1
var firstPeriod = CALCULATE([P-25], DATESBETWEEN('Report load times'[Date], MIN('Report load times'[Date]), MIN('Report load times'[Date]) + periodLength))
var secondPeriod = CALCULATE([P-25], DATESBETWEEN('Report load times'[Date], MAX('Report load times'[Date]) - periodLength, MAX('Report load times'[Date])))
return DIVIDE(secondPeriod - firstPeriod, firstPeriod) + 0 * -1
```

### Model measures.P-75 trend

```sql

var numberOfDays = DATEDIFF(MIN('Report views'[Date]), MAX('Report views'[Date]),DAY) + 1
var periodLength = INT(numberOfDays/2) - 1
var firstPeriod = CALCULATE([P-75], DATESBETWEEN('Report load times'[Date], MIN('Report load times'[Date]), MIN('Report load times'[Date]) + periodLength))
var secondPeriod = CALCULATE([P-75], DATESBETWEEN('Report load times'[Date], MAX('Report load times'[Date]) - periodLength, MAX('Report load times'[Date])))
return DIVIDE(secondPeriod - firstPeriod, firstPeriod) + 0 * -1
```

### Model measures.P-90 trend

```sql

var numberOfDays = DATEDIFF(MIN('Report views'[Date]), MAX('Report views'[Date]),DAY) + 1
var periodLength = INT(numberOfDays/2) - 1
var firstPeriod = CALCULATE([P-90], DATESBETWEEN('Report load times'[Date], MIN('Report load times'[Date]), MIN('Report load times'[Date]) + periodLength))
var secondPeriod = CALCULATE([P-90], DATESBETWEEN('Report load times'[Date], MAX('Report load times'[Date]) - periodLength, MAX('Report load times'[Date])))
return DIVIDE(secondPeriod - firstPeriod, firstPeriod) + 0 * -1
```

### Model measures.Report view share

```sql
DIVIDE(COUNTROWS('Report views'), CALCULATE(COUNTROWS('Report views'), ALL('Report views')), 0)
```

### Model measures.Workspace report days with usage

```sql
SUM('Workspace reports'[Days with usage]) + 0
```

### Model measures.Workspace viewed reports

```sql
DISTINCTCOUNT('Workspace views'[ReportId]) + 0
```

### Model measures.Page views

```sql
COUNTROWS('Report page views') + 0
```

### Report rank.Total Org Report Count

```sql
IF(COUNTROWS('Report rank') = 0, 0, FIRSTNONBLANK('Report rank'[TotalReportCount], 0))
```

### Workspace reports.IsSelectedReport

```sql
IF(SELECTEDVALUE('Workspace reports'[ReportGuid]) = SELECTEDVALUE(Reports[ReportGuid]), 1, 0)
```

## Power Query Source (per table)

### Report views

```sql
let
    Source = UsageMetricsDataConnector.GetMetricsData(BaseUrl & "/metadata/v201906/metrics/workspace/" & WorkspaceId & "/reportviews"),
    metricsTable = Table.FromRecords(Source),
    checkForEmptyTable = if Table.IsEmpty(metricsTable) then
                        Table.FromRows
                        (
                            {
                            },
                            {
                                "ReportId", "ReportType", "ReportName", "AppName", "UserKey", "UserId", "UserAgent", "DatasetName", "DistributionMethod", "CapacityId", "CapacityName", "CreationTime", "ConsumptionMethod"
                            }
                        )
                        else
                        metricsTable,
    finalTable = Table.TransformColumnTypes(checkForEmptyTable, {{"CreationTime", type datetime}}),
    #"Renamed Columns" = Table.RenameColumns(finalTable,{{"ConsumptionMethod", "OriginalConsumptionMethod"}}),
    #"Replaced Value" = Table.ReplaceValue(#"Renamed Columns","Apps","App",Replacer.ReplaceText,{"DistributionMethod"})
in
    #"Replaced Value"
```

### DateTableTemplate_d531c5a6-f782-4ea4-a755-a9747139c561

```sql
Calendar(Date(2015,1,1), Date(2015,1,1))
```

### Model measures

```sql
let
    Source = Table.FromList({}),
    AddWorkspaceId = Table.AddColumn(Source, "WorkspaceId", each WorkspaceId),
    AddBaseUrl = Table.AddColumn(AddWorkspaceId, "BaseUrl", each BaseUrl),
    #"Removed Columns" = Table.RemoveColumns(AddBaseUrl,{"WorkspaceId", "BaseUrl"})
in
    #"Removed Columns"
```

### Report rank

```sql
let
    Source = UsageMetricsDataConnector.GetMetricsData(BaseUrl & "/metadata/v201906/metrics/workspace/" & WorkspaceId & "/reportrank"),
    metricsTable = Table.FromRecords(Source),
    checkForEmptyTable = if Table.IsEmpty(metricsTable) then
                            Table.FromRows
                            (
                                {
                                },
                                {
                                    "ReportId", "WorkspaceId", "ReportViewCount", "ReportRank", "TotalReportCount", "TenantId"
                                }
                            )
                         else
                            metricsTable,
    finalTable = Table.TransformColumnTypes(checkForEmptyTable,{{"ReportRank", Int64.Type}, {"TotalReportCount", Int64.Type}, {"ReportViewCount", Int64.Type}})
in
    finalTable
```

### Report page views

```sql
let
    Source = UsageMetricsDataConnector.GetMetricsData(BaseUrl & "/metadata/v201906/metrics/workspace/" & WorkspaceId & "/reportpagesectionviews"),
    #"metricsTable" = Table.FromRecords(Source),
    checkForEmptyTable = if Table.IsEmpty(#"metricsTable") then
                            Table.FromRows
                            (
                                {
                                },
                                {
                                    "Timestamp", "PbiCluster", "AppName", "TenantId", "UserId", "ReportId", "OriginalReportId", "GroupId", "OriginalGroupId", "AppGuid", "SectionId", "Client", "SessionSource", "DeviceOSVersion", "DeviceBrowserVersion", "UserKey"
                                }
                            )
                         else
                            #"metricsTable",
    #"Removed Columns" = Table.RemoveColumns(checkForEmptyTable,{"PbiCluster"}),
    finalTable = Table.TransformColumnTypes(#"Removed Columns", {{"Timestamp", type datetime}}),
    #"Renamed Columns" = Table.RenameColumns(finalTable,{{"GroupId", "WorkspaceId"}, {"OriginalGroupId", "OriginalWorkspaceId"}})
in
    #"Renamed Columns"
```

### Report load times

```sql
let 
    Source = UsageMetricsDataConnector.GetMetricsData(BaseUrl & "/metadata/v201906/metrics/workspace/" & WorkspaceId & "/reportloads"),
    metricsTable = Table.FromRecords(Source),
    checkForEmptyTable = if Table.IsEmpty(metricsTable) then
                            Table.FromRows
                            (
                                {
                                },
                                {
                                    "AppGuid","AppName","Client","DeviceBrowserVersion","DeviceOSVersion","EndTime","GroupId","LocationCity","LocationCountry","OriginalGroupId","OriginalReportId","PbiCluster","ReportId","StartTime","TenantId","Timestamp","UserId","SessionSource"
                                }
                            )
                         else
                            metricsTable,
    finalTable = Table.TransformColumnTypes(checkForEmptyTable, {{"Timestamp", type datetimezone}, {"StartTime", type datetimezone}, {"EndTime", type datetimezone}}),
    #"Renamed Columns" = Table.RenameColumns(finalTable,{{"LocationCountry", "Country"}})
in
    #"Renamed Columns"
```

### LocalDateTable_3b852b25-f44a-4909-b021-a7df8cabefe6

```sql
Calendar(Date(Year(MIN('Report load times'[StartTime])), 1, 1), Date(Year(MAX('Report load times'[StartTime])), 12, 31))
```

### LocalDateTable_3ebb0033-50be-4e6e-8081-ee8c7cf4091f

```sql
Calendar(Date(Year(MIN('Report load times'[EndTime])), 1, 1), Date(Year(MAX('Report load times'[EndTime])), 12, 31))
```

### LocalDateTable_dc7eb03a-ec8b-421f-b39b-107ea1f05736

```sql
Calendar(Date(Year(MIN('Report views'[CreationTime])), 1, 1), Date(Year(MAX('Report views'[CreationTime])), 12, 31))
```

### LocalDateTable_d27e4379-e50d-47cf-aeac-77eb5f688306

```sql
Calendar(Date(Year(MIN('Report load times'[Timestamp])), 1, 1), Date(Year(MAX('Report load times'[Timestamp])), 12, 31))
```

### Report pages

```sql
let
    Source = UsageMetricsDataConnector.GetMetricsData(BaseUrl & "/metadata/v201906/metrics/workspace/" & WorkspaceId & "/reportpagesectionmetadata"),
    #"metricsTable" = Table.FromRecords(Source),
    checkForEmptyTable = if Table.IsEmpty(#"metricsTable") then
                            Table.FromRows
                            (
                                {
                                },
                                {
                                    "ReportId", "SectionId", "SectionName", "WorkspaceId"
                                }
                            )
                         else
                            #"metricsTable",
    #"Filtered Rows1" = Table.SelectRows(checkForEmptyTable, each ([SectionId] <> null)),
    #"Filtered Rows" = Table.SelectRows(#"Filtered Rows1", each ([ReportId] <> null))
in
    #"Filtered Rows"
```

### Reports

```sql
let
    Source = UsageMetricsDataConnector.GetMetricsData(BaseUrl & "/metadata/v201906/metrics/workspace/" & WorkspaceId & "/reportmetadata"),
    #"metricsTable" = Table.FromRecords(Source),
    checkForEmptyTable = if Table.IsEmpty(metricsTable) then
                            Table.FromRows
                            (
                                {
                                },
                                {
                                    "OrganizationId", "ReportId", "ReportName", "WorkspaceId", "IsUsageMetricsReport"
                                }
                            )
                         else
                            metricsTable,
    #"Filtered Rows" = Table.SelectRows(checkForEmptyTable, each [ReportId] <> null and [ReportId] <> ""),
    #"Renamed Columns" = Table.RenameColumns(#"Filtered Rows",{{"ReportId", "ReportGuid"}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Renamed Columns",{{"IsUsageMetricsReport", type logical}})
in
    #"Changed Type"
```

### LocalDateTable_e9fae86b-d80b-4c31-9ba4-095822014411

```sql
Calendar(Date(Year(MIN('Report page views'[Timestamp])), 1, 1), Date(Year(MAX('Report page views'[Timestamp])), 12, 31))
```

### Refresh Stats

```sql
let
    Source = DateTime.LocalNow() // DateTime.LocalNow()
,
    #"Converted to Table" = #table(1, {{Source}}),
    #"Renamed Columns" = Table.RenameColumns(#"Converted to Table",{{"Column1", "Last Refresh"}})
in
    #"Renamed Columns"
```

### Dates

```sql

    var startDate = TODAY() - 31
    var lastRefreshDate = DATEVALUE(MAX('Refresh Stats'[Last Refresh]))
return
    CALENDAR(startDate, IF(OR(ISBLANK(lastRefreshDate), lastRefreshDate <= startDate), TODAY(), lastRefreshDate))
```

### Workspace views

```sql
SUMMARIZE('Report views', 'Report views'[ReportId], 'Report views'[UserKey], 'Report views'[UserId], 'Report views'[DistributionMethod], 'Report views'[ConsumptionMethod], "Views", [Report views])
```

### Workspace reports

```sql
ADDCOLUMNS(DISTINCT(Reports[ReportGuid]), 
                            "trend", [Workspace view trend], 
                            "active days", [Workspace active days per report])
```

### LocalDateTable_bc207ece-a79c-4d33-a331-c40f45eb2725

```sql
Calendar(Date(Year(MIN('Dates'[Date])), 1, 1), Date(Year(MAX('Dates'[Date])), 12, 31))
```

### LocalDateTable_b465bb22-755a-4444-bc06-bd92af8a8952

```sql
Calendar(Date(Year(MIN('Dates'[fDoW])), 1, 1), Date(Year(MAX('Dates'[fDoW])), 12, 31))
```

### LocalDateTable_7e74b9e2-e4a5-4c05-8b29-c52b531c8abf

```sql
Calendar(Date(Year(MIN('Dates'[lDoW])), 1, 1), Date(Year(MAX('Dates'[lDoW])), 12, 31))
```

### Users

```sql
SUMMARIZE('Report views', 'Report views'[UserId], 'Report views'[UserKey])
```

### Users_ReportPageView

```sql
SUMMARIZE('Report page views', 'Report page views'[UserId], 'Report page views'[UserKey])
```

## Shared Expressions

### WorkspaceId (0)

```sql
"ccdd9d66-24e9-48c6-a8d0-b71a2f03dff1" meta [IsParameterQuery = true, IsParameterQueryRequired = false, Type = "Text"]
```

### BaseUrl (0)

```sql
"https://WABI-US-NORTH-CENTRAL-redirect.analysis.windows.net" meta [IsParameterQuery = true, IsParameterQueryRequired = true, Type = "Text"]
```

## Data Source Cross-References

_No recognized SQL data source references detected._
