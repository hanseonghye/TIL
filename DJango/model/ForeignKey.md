# ForeignKey

## on_delete

- models.CASCADE
  - 해당 레코드가 삭제되면 그 레코드를 외래키로 참조하는 모든 레코드를 함께 삭제 된다.
- models.PROTECT
  - 외래키가 참조하고 있는 레코드를 삭제하지 못하게 한다.
- models.SET_DEFAULT
  - PROTECT와 다르게 외래키 필드의 값이 default값으로 된다.
- models.SET_NULL
  - 외래키 필드의 값이 null이 된다.
- models.SET()
  - `SET()` 함수를 통해 설정



- <https://nachwon.github.io/django-relationship/>