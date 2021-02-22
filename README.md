Import and export mysql database
================================

Importing:

```
gunzip < /path/to/outputfile.sql.gz | mysql -u USER -pPASSWORD DATABASE
```

Dumpping:

```
mysqldump -u USER -pPASSWORD DATABASE | gzip > /path/to/outputfile.sql.gz
```
