from sqlalchemy import create_engine
engine = create_engine("sqlite:///identifier.sqlite")
result = engine.execute("""SELECT * FROM users""")

for row in result:
    print(row)