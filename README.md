# python-scripts
Assorted Python scripts

##### `ct-abuse.py`
- For the given domain query [Certificate Transparency](https://www.certificate-transparency.org/what-is-ct) to get a list of subdomains which have SSL/TLS certificates issued for them 
- Usage: `ct-abuse.py {target_domain}`

##### `shebang.py`
- Check if bash scripts have a shebang on line one (`#!`)
- Usgae: `./shebang.py *` or `./shebang.sh {file 1} {file ...}`

##### `haveibeenpwned.py`
- Check if your email or password has been involved in a breach indexed by [haveibeenpwned.com](https://haveibeenpwned.com/API/v2)
- Usage: 
  - `./haveibeenpwnd.py example@example.com`
  - `./haveibeenpwnd.py password`

