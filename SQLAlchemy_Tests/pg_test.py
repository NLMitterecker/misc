#!/usr/bin/env python

from datetime import datetime
from sqlalchemy import (MetaData, create_engine, Table, Column, 
                        Integer, Numeric, String, ForeignKey, DateTime)

metadata = MetaData()

users = Table('cookies', metadata,
        Column('cookie_id', Integer(), primary_key=True),
        Column('cookie_name', String(50), index=True, nullable=False),
        Column('cost', Numeric(12, 2)),
        Column('added', DateTime(), default=datetime.now)
)

engine = create_engine('postgresql+psycopg2://learn_sqlalchemy:learn123@localhost:'\
                                                            '5432/learn_sqlalchemy')

metadata.create_all(engine)
