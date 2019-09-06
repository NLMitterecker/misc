#!/usr/bin/env python

import time
from datetime import datetime
from sqlalchemy import (MetaData, create_engine, Table, Column, 
                        Integer, Numeric, String, ForeignKey, DateTime,
                        insert, select)

metadata = MetaData()

cookies = Table('cookies', metadata,
        Column('cookie_id', Integer(), primary_key=True),
        Column('cookie_name', String(50), index=True, nullable=False),
        Column('cost', Numeric(12, 2)),
        Column('added', DateTime(), default=datetime.now)
)

#ins = cookies.insert().values(
#    cookie_name="chocolate chip",
#    cost="1.5"
#)

# also possible ins = insert(cookies).values( ...
#print(str(ins))

# direct DB access
#engine = create_engine('postgresql://learn_sqlalchemy:learn123@127.0.0.1:'\
#                                                            '5432/learn_sqlalchemy')
engine = create_engine('postgresql://learn_sqlalchemy:learn123@127.0.0.1:'\
                                                            '6543/learn_sqlalchemy')
metadata.create_all(engine)

connection = engine.connect()

s = select([cookies])
rp = connection.execute(s)
result = rp.fetchall()

connection.close()
