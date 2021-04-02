# DateTime

### set

```php
$dt1 = new DateTime();

$dt2 = new DateTime("2018-07-04T11:21:35+09:00");

$dt3 = new DateTime('-1 day');
```



### format

`string`으로 반환

```php
$set_dateTime = new DateTime("2018-07-04T11:21:35+09:00");
$set_dateTime = $set_dateTime->format('Y-m-d H:i:s');
```



### timezone

```php
new DateTime("now", new DateTimeZone('Asia/Taipei'));
```



#### convert timezone

```php
$time = "2018-07-04T11:21:35+10:00";
$dt = new DateTime($time);
$dt->setTimezone(new DateTimeZone('Asia/Taipei'));
echo ($dt->format('Y-m-d H:i:s'));
// 2018-07-04 09:21:35
```

