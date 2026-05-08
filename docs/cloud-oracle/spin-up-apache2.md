# Spin up Apache2

**✅ Got it!** Let's spin up **Apache2** on your Ubuntu server.

Run these commands **as user `al`** (or `ubuntu`):

### 1. Install Apache2

```bash
sudo apt update
sudo apt install apache2 -y
```

### 2. Start and Enable Apache

```bash
sudo systemctl start apache2
sudo systemctl enable apache2
```

### 3. Check Status

```bash
sudo systemctl status apache2
```

You should see `active (running)`.

---

### 4. Test if it's working

From your browser, go to:

**http://141.147.71.47**

You should see the default Ubuntu Apache2 welcome page.

You can also test from terminal:

```bash
curl -I http://localhost
```

---

### Quick Useful Commands

```bash
# Restart Apache
sudo systemctl restart apache2

# Stop Apache
sudo systemctl stop apache2

# Check logs
sudo tail -f /var/log/apache2/error.log

# Apache configuration test
sudo apache2ctl configtest
```

---

Would you like me to also configure:

- A domain / virtual host for `al`?
- Let's Encrypt SSL (HTTPS)?
- Disable the default welcome page?

Just say what you want next.