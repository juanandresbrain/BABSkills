# Job: _SSIS_EmailParameterFix

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** Sets the correct email / smtp server for ssis deployed with the wrong / old value.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["_SSIS_EmailParameterFix"]
    JOB --> Run_Update_1["Step 1: Run Update [TSQL]"]`n```

## Steps

### Step 1: Run Update
**Subsystem:** TSQL  

```sql
update op  set op.design_default_value='exstlhyb.buildabear.com'  from internal.object_parameters op  where 1=1   and   (    op.parameter_name='SMTP_SmtpServer'    or op.parameter_name='EmailServer'    or op.parameter_name='CM.EMAIL.SmtpServer'    or op.parameter_name='CM.SMTP Connection Manager.SmtpServer'    or op.parameter_name='CM.SMTP.SmtpServer'    or op.parameter_name='CM.SMTP_EMAIL 1.SmtpServer'    or op.parameter_name='CM.SMTP_EMAIL.SmtpServer'   )  and op.design_default_value<>'exstlhyb.buildabear.com'
```


