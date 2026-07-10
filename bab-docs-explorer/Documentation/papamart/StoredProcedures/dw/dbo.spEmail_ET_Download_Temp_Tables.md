# dbo.spEmail_ET_Download_Temp_Tables

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spEmail_ET_Download_Temp_Tables"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[spEmail_ET_Download_Temp_Tables]
as

IF (Object_ID('dw.dbo.tmp_edin_bounce_import') IS NOT NULL) DROP TABLE tmp_edin_bounce_import
create table dw.dbo.tmp_edin_bounce_import
(
ClientID int,
SendID int,
SubscriberKey varchar(200),
EmailAddress varchar(200),
SubscriberID int,
ListID int,
EventDate datetime,
EventType varchar(100),
BounceCategory varchar(200),
SMTPCode varchar(50),
BounceReason varchar(1000),
BatchID int,
TriggeredSendExternalKey varchar(200)
)

IF (Object_ID('dw.dbo.tmp_edin_unsubs_import') IS NOT NULL) DROP TABLE dw.dbo.tmp_edin_unsubs_import
create table dw.dbo.tmp_edin_unsubs_import
(
ClientID int,
SendID int,
SubscriberKey varchar(200),
EmailAddress varchar(200),
SubscriberID int,
ListID int,
EventDate datetime,
EventType varchar(100),
BatchID int,
TriggeredSendExternalKey varchar(200)
)

IF (Object_ID('dw.dbo.tmp_edin_opens_import') IS NOT NULL) DROP TABLE dw.dbo.tmp_edin_opens_import
create table dw.dbo.tmp_edin_opens_import
(
ClientID int,
SendID int,
SubscriberKey varchar(200),
EmailAddress varchar(200),
SubscriberID int,
ListID int,
EventDate datetime,
EventType varchar(100),
BatchID int,
TriggeredSendExternalKey varchar(200)
)

IF (Object_ID('dw.dbo.tmp_edin_clicks_import') IS NOT NULL) DROP TABLE dw.dbo.tmp_edin_clicks_import
create table dw.dbo.tmp_edin_clicks_import
(
ClientID int,
SendID int,
SubscriberKey varchar(200),
EmailAddress varchar(200),
SubscriberID int,
ListID int,
EventDate datetime,
EventType varchar(100),
SendURLID int,
URLID int,
URL varchar(4000),
Alias varchar(200),
BatchID int,
TriggeredSendExternalKey varchar(200)
)

IF (Object_ID('dw.dbo.tmp_edin_sendjobs_import') IS NOT NULL) DROP TABLE dw.dbo.tmp_edin_sendjobs_import
create table dw.dbo.tmp_edin_sendjobs_import
(
ClientID int,
SendID int,
FromName varchar(100),
FromEmail varchar(100),
SchedTime datetime,
SentTime datetime,
[Subject] varchar(100),
EmailName varchar(500),
TriggeredSendExternalKey varchar(200),
SendDefinitionExternalKey varchar(200),
JobStatus varchar(50),
PreviewURL varchar(4000),
IsMultipart varchar(50),
Additional varchar(200)
)

IF (Object_ID('dw.dbo.tmp_edin_sent_import') IS NOT NULL) DROP TABLE dw.dbo.tmp_edin_sent_import
create table dw.dbo.tmp_edin_sent_import
(
ClientID int,
SendID int,
SubscriberKey varchar(200),
EmailAddress varchar(200),
SubscriberID int,
ListID int,
EventDate datetime,
EventType varchar(100),
BatchID int,
TriggeredSendExternalKey varchar(200)
)

IF (Object_ID('dw.dbo.tmp_edin_conversions_import') IS NOT NULL) DROP TABLE dw.dbo.tmp_edin_conversions_import
create table dw.dbo.tmp_edin_conversions_import
(
ClientID int,
SendID int,
SubscriberKey varchar(200),
EmailAddress varchar(200),
SubscriberID int,
ListID int,
EventDate datetime,
EventType varchar(100),
ReferringURL varchar(4000),
LinkAlias varchar(200),
ConversionData varchar(200),
BatchID int,
TriggeredSendExternalKey varchar(200),
URLID int
)

IF (Object_ID('dw.dbo.tmp_edin_surveys_import') IS NOT NULL) DROP TABLE dw.dbo.tmp_edin_surveys_import
create table dw.dbo.tmp_edin_surveys_import
(
ClientID int,
SendID int,
SubscriberKey varchar(200),
EmailAddress varchar(200),
SubscriberID int,
ListID int,
EventDate datetime,
EventType varchar(100),
Question varchar(2000),
Answer varchar(2000),
BatchID int,
TriggeredSendExternalKey varchar(200),
URLID int
)
```

