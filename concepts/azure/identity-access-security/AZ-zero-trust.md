# Azure Fundamentals — Zero Trust Model

## 1. What Is Zero Trust?

Zero Trust is a security model based on **“Never trust automatically; always verify.”**

It assumes a security breach may already have occurred and verifies every access request, regardless of network location.

## 2. Three Guiding Principles

### Verify Explicitly
- Authenticate and authorize using all available information.
- Consider user identity, location, device state, application, and risk.
- Example: Require MFA for suspicious sign-ins.

### Use Least Privilege Access
- Grant only the permissions users need, for only as long as necessary.
- **JIT (Just-In-Time):** Grant access only when needed and for a limited time.
- **JEA (Just-Enough-Access):** Grant only the minimum required permissions.

### Assume Breach
- Assume an attacker may already be inside the network.
- Limit potential damage through network segmentation and restricted access.
- Use encryption, monitoring, analytics, and threat detection.

## 3. Traditional Security vs. Zero Trust

| Traditional Perimeter Security | Zero Trust |
|---|---|
| Trusts internal networks more readily. | Does not automatically trust internal networks. |
| Focuses on protecting the network boundary. | Verifies every access request. |
| Network location is a major trust signal. | Evaluates identity, device, and risk. |
| Internal access may be treated as trusted. | Access depends on authentication, authorization, and context. |

## 4. Example in Practice

A user signs in from an unmanaged device on public Wi-Fi.

- Low-risk application: Access might be allowed.
- Sensitive application: Additional verification, such as MFA, might be required.
- High-risk sign-in: Access might be blocked.

Access decisions are context-aware and can change as circumstances or risk change.

## 5. Key Exam Points

- **Zero Trust:** Never trust automatically; always verify.
- **Verify explicitly:** Evaluate available identity and access signals.
- **Least privilege:** Grant minimum necessary permissions.
- **Assume breach:** Limit damage, segment access, encrypt, and monitor.
- Being inside a trusted network does not automatically make a user or device trustworthy.
- Zero Trust works with Microsoft Entra ID, MFA, Conditional Access, and RBAC.

## Memory Trick

**Verify — Limit — Assume**

1. Verify every access request.
2. Limit permissions and access.
3. Assume a breach may have occurred.