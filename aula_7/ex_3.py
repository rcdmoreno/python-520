import sqlalchemy
import ex_1

select_operation = sqlalchemy.select(
    [ex_1.users_table.c.name]
).where(ex_1.users_table.c.id > 0)

for result in select_operation.execute():
    print(result)