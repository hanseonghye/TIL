# form reset



- 특정 form 하나만 리셋하고 싶은 경우

  ```javascript
  $("#form_id")[0].resest();
  ```

- 모든 form 리셋

  ```javascript
  $("form").each(function() {
      this.reset();
  })
  ```

- 첫번째 form 리셋

  ```javascript
  $("form")[0].resest();
  ```

  