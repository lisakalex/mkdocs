# Character encoding error

**`â€™s`** is a common **character encoding error** (called "mojibake").

### What happened:

- The real character you wanted is: **’** (a curly/right apostrophe in "Alex’s")
- That character was saved in **UTF-8** encoding.
- But your web page is being read by the browser as **Windows-1252** (or ISO-8859-1).
- So the apostrophe gets broken and displayed as **`â€™`**

---

### How to fix it properly

Run this command on your server:

```bash
sudo nano /var/www/html/index.html
```

Then make sure your HTML file starts with this (add it at the very top if it's not there):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello from Alex's Server</title>
</head>
<body>
<h1>Hello from Alex’s Oracle Ubuntu Server</h1>
</body>
</html>
```

**Key fix:** Make sure you have this line:

```html

<meta charset="UTF-8">
```

Save the file (`Ctrl` + `O` → Enter → `Ctrl` + `X`), then refresh your browser.

---

Would you like me to show you a clean minimal `index.html` file? Just say yes.