import sqlalchemy
import ex_1

select_operation = sqlalchemy.select(
    [ex_1.users_table]
).where(ex_1.users_table.c.name == 'Lucas')

for result in select_operation.execute():
    print(result)