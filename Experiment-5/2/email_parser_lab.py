# -------------------------------------
# Lab 5(ii): Identify Components of an Email Address
# Run this in VS Code
# -------------------------------------

import re

# Step 1: Sample email address
email = input("Enter an email address: ").strip()

# Step 2: Define regex pattern to validate and parse email
pattern = r'^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+(\.[a-zA-Z0-9-.]+)+)$'

# Step 3: Match the pattern with the email
match = re.match(pattern, email)

# Step 4: Extract and print components
if match:
    local_part = match.group(1)
    domain = match.group(2)
    domain_parts = domain.split('.')

    print("\n=== Components of the Email Address ===")
    print("Full Email:", email)
    print("Local Part:", local_part)
    print("Domain:", domain)
    print("Domain Name:", domain_parts[0])
    
    if len(domain_parts) >= 2:
        tld = domain_parts[-1]
        print("Top-Level Domain (TLD):", tld)
    
    if len(domain_parts) > 2:
        subdomains = domain_parts[1:-1] if len(domain_parts) > 2 else domain_parts[1]
        print("Subdomain(s):", subdomains)
else:
    print("Invalid email address format.")