# Create user

**✅ Got it!** Here's the cleanest way to create user **`al`**:

### Run these commands while logged in as `ubuntu`:

```bash
# 1. Create the user "al" with no extra info
sudo adduser --gecos "" al

# 2. Give "al" sudo privileges (no password needed for sudo)
sudo usermod -aG sudo al

# 3. Copy your SSH key so you can login as "al"
sudo mkdir -p /home/al/.ssh
sudo cp /home/ubuntu/.ssh/authorized_keys /home/al/.ssh/authorized_keys

# 4. Fix permissions
sudo chown -R al:al /home/al
sudo chmod 700 /home/al/.ssh
sudo chmod 600 /home/al/.ssh/authorized_keys

# 5. Verify
ls -la /home/al/.ssh
```

---

### Test the new user

From your **local machine** (not from cloud shell):

```bash
ssh al@141.147.71.47
```

---

Would you like me to also:

- Set a password for `al`?
- Make `al` the default user (remove ubuntu access)?
- Add `al` to more groups?

Just reply with the result of the commands above.