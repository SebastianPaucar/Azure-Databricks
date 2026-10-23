# Encryption and Key Management - Key Notes

## 1. What Is Encryption?

Encryption converts readable data into unreadable data to protect its confidentiality. Authorized users or services can access the data using the appropriate decryption capabilities.

## 2. Types of Encryption

### Encryption at Rest
Protects data **when stored**.

Examples:
- Azure SQL databases
- Virtual machine disks
- Azure Storage accounts

### Encryption in Transit
Protects data **while moving** between users, applications, APIs, and services.

Example:
- HTTPS/TLS connections between a browser and an application.

**Exam tip:** Strong data protection generally includes both encryption at rest and encryption in transit.

## 3. Azure Key Vault

Azure Key Vault securely stores and controls access to three main items:

| Item | Purpose | Examples |
|---|---|---|
| **Secrets** | Store sensitive values | Passwords, API keys, connection strings |
| **Keys** | Support cryptographic operations | Encryption and decryption keys |
| **Certificates** | Establish identity and secure connections | TLS/SSL certificates |

**Memory trick: Key Vault = Secrets + Keys + Certificates.**

## 4. Why Key Management Matters

Key management protects keys and secrets throughout their lifecycle.

- **Access control:** Restrict who can view or use keys and secrets.
- **Key rotation:** Replace keys periodically to reduce risk.
- **Auditing:** Track key and secret usage.
- **Expiration alerts:** Notify teams before keys or certificates expire.
- **Separation of duties:** Assign different permissions for viewing, using, and rotating keys.

These practices improve security and support compliance requirements.

## 5. Managed Identities and Key Vault

Applications often need credentials to access other Azure services.

Hard-coding passwords or credentials in application code is a poor security practice.

A better approach:

1. Assign a managed identity to the application.
2. Grant the identity appropriate permissions to Key Vault.
3. Allow the application to retrieve the required secret securely at runtime.

**Benefit:** Reduces hard-coded credentials and simplifies access management.

## 6. Common Exam Scenarios

| Scenario | Correct answer |
|---|---|
| Protect data stored in a database or disk | Encryption at rest |
| Protect data transmitted over HTTPS | Encryption in transit |
| Store passwords and connection strings securely | Key Vault secrets |
| Manage cryptographic keys | Key Vault keys |
| Manage TLS/SSL certificates | Key Vault certificates |
| Replace keys periodically | Key rotation |
| Track key and secret usage | Auditing |
| Avoid hard-coded credentials | Managed identities + Key Vault |

## 7. Key Exam Takeaways

- Encryption protects **data confidentiality**.
- At rest = data is stored.
- In transit = data is moving.
- Azure Key Vault manages **secrets, keys, and certificates**.
- Key management includes access control, rotation, auditing, and expiration monitoring.
- Managed identities help applications access Azure services without hard-coded credentials.
- Encryption protects data; key management protects and controls the keys and secrets used by systems.

## Memory Trick

**Stored → Moving → Managed**

- **At rest:** Protect stored data.
- **In transit:** Protect moving data.
- **Key Vault:** Securely manage secrets, keys, and certificates.