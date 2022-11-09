# Powershell Commands

## Create Folders

### Create multiple subdirectories inside a directory in one line

```powershell
'subdir1', 'subdir2' | % {New-Item ".\mydir\$_" -ItemType "Directory"}
```

Many thanks to [Lotpings on stackoverflow](https://superuser.com/questions/1337434/how-to-create-multiple-folders-in-powershell)
