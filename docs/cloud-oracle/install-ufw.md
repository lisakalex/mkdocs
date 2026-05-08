# Install UFW

**Got it.** UFW is not installed on your server.

### Step 1: Install UFW

Run this:

```bash
sudo apt update
sudo apt install ufw -y
```

### Step 2: Configure UFW

After installation, run these commands:

```bash
# Allow SSH (important so you don't lock yourself out)
sudo ufw allow 22/tcp

# Allow Apache (HTTP + HTTPS)
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Enable UFW
sudo ufw --force enable

# Check status
sudo ufw status
```

---

### ⚠️ Important Reminder

Even after doing this, **you still need to open port 80 in Oracle Cloud Console**.

Go to Oracle Cloud → Your Instance → Subnet → Security List → Add Ingress Rule for port **80** (and **22** if not
already open).

**Source CIDR**: `0.0.0.0/0`  
**Destination Port**: `80`

---

After doing both (UFW + Oracle Security List), test again:

```bash
curl http://localhost
```

Then try `http://141.147.71.47` in your browser.

---

Let me know once you’ve done these steps, or paste the output of `sudo ufw status` after installation.