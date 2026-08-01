# Open port 80

**✅ No problem.** Sometimes the direct "Subnet" link is not obvious or the layout varies.

### Easier way to open port 80 (Alternative navigation):

1. Go to **Oracle Cloud Console**
2. Open the **hamburger menu** (☰) on the top left
3. Go to **Networking** → **Virtual Cloud Networks**
4. Click on the **VCN** that your instance is using (it usually has a name like `vcn-...` or `Default VCN`)
5. On the left side, under **Resources**, click **Security Lists**
6. Click on the **Default Security List** (or the one associated with your instance)
7. Click the button **Add Ingress Rules**

### Fill in the rule like this:

- **Source Type**: CIDR
- **Source CIDR**: `0.0.0.0/0`
- **IP Protocol**: TCP
- **Destination Port Range**: `80`
- **Description**: `Allow HTTP`

Click **Add Ingress Rules**.

Do the same for port `443` if you want HTTPS later.

![Screenshot from 2026-05-10 15-12-53.png](img/Screenshot%20from%202026-05-10%2015-12-53.png)
![Screenshot from 2026-05-09 07-58-59.png](img/Screenshot%20from%202026-05-09%2007-58-59.png)  
![Screenshot from 2026-05-09 08-04-32.png](img/Screenshot%20from%202026-05-09%2008-04-32.png)
---

After adding the rule, go back to your server and run:

```bash
sudo ufw status
curl http://localhost
```

Then try `http://141.147.71.47` again in your browser.

---

Let me know what you see after adding the rule (or if you still can't find the Security List). I can give you
screenshots-style steps if needed.