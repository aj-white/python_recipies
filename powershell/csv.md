# CSV Operations

## Importing Csv
```shell
> $csvVariable = Import-Csv -Path path/to.csv
```

 ### Setting delimiter

 #### semi-colon
```shell
> $csvVariable = Import-Csv -Path path/to.csv -Delimiter ";"
```

 #### tab
 ```shell
> $csvVariable = Import-Csv -Path path/to.csv -Delimiter "`t"
```

## Searching Csv

### Single Column

```shell
> $csvVariable | Where-Object {$_.columnName -eq 'someValue'} | Select column names
```

### Multiple Columns
```shell
> $csvVariable | Where-Object {($_.columnName1 -eq 'someValue'} -or $_.columnName1 -eq 'someOtherValue') -and ($_.columnName2 -eq 'diffValue')} | Select column names
```
