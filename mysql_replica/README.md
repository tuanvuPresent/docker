# Docker MySQL master-slave replication 

---
## Run

```bash
docker-compose up -d
```
- Run command master
```sql
create user 'slave_user'@'%' identified by 'password';
grant replication slave on *.* to 'slave_user'@'%' with grant option;
flush privileges;
```
- Run command slave
```sql
CHANGE MASTER TO MASTER_HOST='mysql-master',
    MASTER_USER='slave_user',
    MASTER_PASSWORD='password',
    MASTER_AUTO_POSITION=1;
START SLAVE;
```

- slave failed
```sql
reset slave;
start slave;
```