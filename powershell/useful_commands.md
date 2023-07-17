# Powershell Commands

## Create Folders

### Create multiple subdirectories inside a directory in one line

```powershell
'subdir1', 'subdir2' | % {New-Item ".\mydir\$_" -ItemType "Directory"}
```

Many thanks to [Lotpings on stackoverflow](https://superuser.com/questions/1337434/how-to-create-multiple-folders-in-powershell)


## Deleting Folders

### Delete a hidden folder (looking at you .git)

```powershell
Get-ChildItem -Hidden | Remove-Item -Force
```

## Create Aliases

### Create Alias for directory location

```powershell
function pathToPythonProjects{Set-Location -Path \path\to\python\projects}
Set-Alias -Name myprojectalias -Value pathToPythonProjects
```
## Searching

### Recursive Search By Pattern

```powershell
dir -Recurse | Select-String -pattern [SEARCH_PATTERN]
```
Thanks to [jamescoyle](https://www.jamescoyle.net/how-to/1205-how-to-use-powershell-to-recursively-search-for-text-within-files-on-windows)

### List only directories

```powershell
ls -Directory
```

### Copy Current Location to clipboard

```powershell
(pwd).Path | Set-Clipboard
```


## Powershell profile

### Find powershell profile location

```powershell
>>> $profile
```
You can open in notepad with
```powershell
>>> notepad $profile
```
