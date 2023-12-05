# Finding items with powershell

### Find most recent file in a directory
```powershell
Get-ChildItem -path | sort LastWriteTime | select -last 1
```

### Find most recent filetype in a directory (e.g. zip files)
```powershell
Get-ChildItem -path -Filter *.zip | sort LastWriteTime | select -last 1
```
