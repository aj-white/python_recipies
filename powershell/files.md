# File Creation and Manipulation

### Creating multiple directories

```powershell
$> 1..3 | ForEach-Object {md "./filename$_}
```

creates the following structure

```bash
|- cwd
    |- filename1
    |- filename2
    |- filename3
```
