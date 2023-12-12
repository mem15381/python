# readExample.py
from pyspark import SparkContext
from pyspark.sql import SQLContext
sc = SparkContext()
sqlc = SQLContext(sc)
data_source_format = 'org.apache.spark.sql.execution.datasources.hbase'
catalog = ''.join("""{
    "table":{"namespace":"default", "name":"firsttable"},
    "rowkey":"key",
    "columns":{
        "firstcol":{"cf":"rowkey", "col":"key", "type":"string"},
        "secondcol":{"cf":"d", "col":"colname", "type":"string"}
    }
}""".split())
df = sqlc.read\
.options(catalog=catalog)\
.format(data_source_format)\
.load()
df.select("secondcol").show()
