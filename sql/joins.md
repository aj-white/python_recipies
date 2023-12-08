# Custom Joins

### Anti join
```sql
select A.id
from A
where not exists (
  select 1 from B where A.id = B.id
)
