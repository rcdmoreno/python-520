
import ex_1

connection = ex_1.engine.connect()
insert_operation = ex_1.users_table.insert()

connection.execute(
    insert_operation,
    [
        {
            'name': 'Lucas',
            'age': 26,
            'password': 'admin'
            
        } 
    ]
)
