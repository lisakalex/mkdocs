Good choice. Here's the full setup:

## 1. Install/check SSH server

```bash
sudo apt update
sudo apt install openssh-server -y
sudo systemctl status ssh
```

If it's not running:

```bash
sudo systemctl enable ssh
sudo systemctl start ssh
```

## 2. Find your Ubuntu machine's IP

```bash
hostname -I
```

Note the local IP (e.g. `192.168.1.x`).

## 3. Firewall

```bash
sudo ufw allow OpenSSH
```

(This opens port 22/tcp.)

## 4. Test from another device (optional but good sanity check)

```bash
ssh your_username@192.168.1.x
```

If that logs in, you're set.

## 5. Connect from OwlFiles

In OwlFiles: **Add Connection → SFTP**
- **Host**: your Ubuntu machine's local IP (or public IP if connecting remotely)
- **Port**: `22`
- **Username**: your Linux username
- **Password**: your Linux password (or set up key-based auth — see below)
- Leave encryption/protocol as SFTP (default)

That's it — no vsftpd config, no passive port ranges, no separate firewall rules for a big port range. Just port 22.

## If connecting from outside your home network

You'll need to port-forward port 22 (TCP) on your router to the Ubuntu machine's local IP, using the same public-IP-lookup trick as before (`curl ifconfig.me`).

**Security note**: if you expose port 22 to the internet, consider:
- Using SSH key authentication instead of passwords (more secure, and OwlFiles supports importing/using SSH keys)
- Changing the default SSH port from 22 to something non-standard (reduces automated bot scanning, though it's security-through-obscurity, not a real fix)
- Installing `fail2ban` to block repeated failed login attempts

Want me to walk through setting up SSH key auth for OwlFiles, or is password auth fine for your setup?