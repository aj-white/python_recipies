# Finding items with powershell

### Find most recent file in a directory
```powershell
Get-ChildItem -path | sort LastWriteTime | select -last 1
```
