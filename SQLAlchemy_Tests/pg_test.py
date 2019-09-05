#!/usr/bin/env python

from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://learn_sqlalchemy:learn123@localhost:'\
                                                            '5432/learn_sqlalchemy')
