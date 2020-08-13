# query function inside models

`classmethod`를 사용하여 `model`안에 함수를 선언한다.



```python
class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column('restaurant_id', Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    

    @classmethod
    def exist_chk(cls, session, name):
        return session.query(cls).filter_by(name=name).scalar() is None
```





- https://stackoverflow.com/questions/57842652/flask-sqlalchemy-query-function-inside-models