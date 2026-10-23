# Defense-in-Depth - Key Notes

## 1. What Is Defense-in-Depth?

Defense-in-depth is a security strategy that uses **multiple layers of protection** to protect data and prevent unauthorized access.

If one layer fails, other layers can still stop or limit an attack.

**Main objective:** Protect information and reduce the impact of security breaches.

## 2. The Seven Security Layers

Remember the layers from the outside inward:

1. **Physical Security**
   - Protect datacenters, buildings, servers, and hardware.
   - Prevent unauthorized physical access.

2. **Identity and Access**
   - Control who can sign in and what they can do.
   - Use MFA, SSO, RBAC, and auditing.
   - Azure example: Microsoft Entra ID.

3. **Perimeter**
   - Protect against external network attacks.
   - Use DDoS protection and perimeter firewalls.
   - Azure example: Azure DDoS Protection.

4. **Network**
   - Restrict communication between resources.
   - Use network segmentation and access controls.
   - Apply the principle of **deny by default**.

5. **Compute**
   - Secure virtual machines, operating systems, and endpoints.
   - Keep systems patched and use endpoint protection.

6. **Application**
   - Prevent software vulnerabilities.
   - Build security into application development.
   - Use Azure Key Vault to manage application secrets and keys.

7. **Data**
   - Protect the information itself.
   - Control access and use encryption at rest and in transit.

## 3. Important Concepts

### Encryption
- **Encryption at rest:** Protects stored data, such as files on disks and database records.
- **Encryption in transit:** Protects data while it moves between systems, typically using TLS.

### Azure Key Vault
Helps securely store and manage secrets, cryptographic keys, and certificates used by applications.

### Network Segmentation
Divides a network into smaller sections and restricts communication to help prevent attacks from spreading.

### DDoS Protection
Helps defend against distributed denial-of-service attacks, which attempt to overwhelm a service with traffic.

## 4. Exam Scenarios

| Scenario | Correct layer or service |
|---|---|
| Prevent unauthorized physical access to datacenters | Physical security |
| Require MFA and control user permissions | Identity and access |
| Defend against large-scale external traffic attacks | Perimeter / DDoS Protection |
| Restrict communication between resources | Network |
| Patch and protect virtual machines | Compute |
| Secure application code and secrets | Application / Key Vault |
| Encrypt stored information | Data |
| Encrypt information moving between systems | Data |

## 5. Key Exam Points

- Defense-in-depth means **multiple layers of security**, not relying on one control.
- Attackers must overcome several protections to reach sensitive data.
- **Physical security** protects hardware and facilities.
- **Identity and access** controls who can access resources.
- **Perimeter** protects against external attacks.
- **Network** limits communication and attack propagation.
- **Compute** secures VMs, endpoints, and operating systems.
- **Application** reduces software vulnerabilities and protects secrets.
- **Data** is the innermost layer and the ultimate asset being protected.
- Azure Key Vault manages secrets, keys, and certificates.
- Encryption at rest protects stored data; encryption in transit protects moving data.

## Memory Trick

**Physical → Identity → Perimeter → Network → Compute → Application → Data**

Think of it as protecting a valuable document: secure the building, verify people, defend the boundary, restrict internal movement, secure computers and software, and finally protect the document itself.

**Main takeaway:** If one security layer is breached, other layers should still help prevent the attacker from reaching the data.