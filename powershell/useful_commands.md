# Powershell Commands

## Create Folders

### Create multiple subdirectories inside a directory in one line

```powershell
'subdir1', 'subdir2' | % {New-Item ".\mydir\$_" -ItemType "Directory"}
```

Many thanks to [Lotpings on stackoverflow](https://superuser.com/questions/1337434/how-to-create-multiple-folders-in-powershell)


## Create Aliases

### Create Alias for directory location

```powershell
function pathToPythonProjects{Set-Location -Path \path\to\python\projects}
Set-Alias -Name myprojectalias -Value pathToPythonProjects
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
