# iptables

**✅ The issue is almost certainly `iptables` on the Ubuntu server.**

Even though UFW is inactive and the Oracle Security List allows port 80, Ubuntu often still has `iptables` rules
blocking incoming traffic.

### Run these commands on your server:

```bash
# 1. Add rule for port 80
sudo iptables -I INPUT -p tcp --dport 80 -j ACCEPT

# 2. (Optional but good) Add for HTTPS too
sudo iptables -I INPUT -p tcp --dport 443 -j ACCEPT

# 3. Install the persistent tool and save rules
sudo apt install iptables-persistent -y

# When prompted, choose Yes to save current rules
sudo netfilter-persistent save

# 4. Restart Apache
sudo systemctl restart apache2
```

---

### Test again from your local machine:

```bash
curl http://141.147.71.47
```

Then try the browser again: `http://141.147.71.47`

---

Would you like me to also show you how to view current iptables rules? Just paste the output of the commands above.