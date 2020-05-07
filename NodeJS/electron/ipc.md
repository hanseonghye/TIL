# IPC (Inter Process Communication)

> electron에는 ipcMain, ipcRender 두가지의 ipc 모듈이 잇다.



### ipcMain

nodejs 어플리케이션에서 사용된다. `BrowserWindow` 모듈에 의해 생성된 윈도우 객체가 생성한 `renderer` 프로세스와 통신한다.  이는 `ipcRender`도 마찬가지다

```javascript
// index.js nodejs 실행 파일

const { app, BrowserWindow, ipcMain } = require('electron')

let win = null

app.on('ready', () => {
  win = new BrowserWindow({
    webPreferences: {
      nodeIntegration: true
    }
  })
  win.loadURL(`file://${__dirname}/index3.html`)
  win.webContents.openDevTools()

  ipcMain.on('async-message', (event, arg) => {
    event.sender.send('async-reply', 'async pong')
  })

  ipcMain.on('sync-message', (event, arg) => {
      event.returnValue = 'sync pong'
    })
})
```



```html
<!-- index3.html -->

<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
</head>

<body>
  <button id="async">async</button>
  <button id="sync">sync</button>
</body>

<script>
  const { ipcRenderer } = require('electron')

  document.querySelector('#async').addEventListener('click', () => {
    ipcRenderer.send('async-message', 'async ping')
  })


  ipcRenderer.on('async-reply', (event, arg) => {
    console.log(arg)
  })

  
  document.querySelector('#sync').addEventListener('click', () => {
    const reply = ipcRenderer.sendSync('sync-message', 'sync ping')
    console.log(reply)
  })
</script>

</html>
```





- https://goldenthumb.net/electron-tutorial

- https://kay0426.tistory.com/17