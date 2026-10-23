# Azure Fundamentals — Conditional Access

## 1. What Is Conditional Access?

Microsoft Entra Conditional Access evaluates sign-in conditions to decide whether to allow access, require additional verification, or block access.

**Purpose:** Protect resources while allowing users to work securely.

## 2. How Does It Work?

Remember the three steps:

1. **Signals:** Collect information about the sign-in.
2. **Decision:** Evaluate the signals against configured policies.
3. **Enforcement:** Apply the required action.

### Common Signals
- **User:** Who is signing in?
- **Location:** Where is the sign-in coming from?
- **Device:** Is the device managed or compliant?
- **Application:** Which application is being accessed?

### Possible Enforcement Actions
- Allow access.
- Require multifactor authentication (MFA).
- Require a compliant or managed device.
- Require an approved client application.
- Block access.

## 3. Common Use Cases

| Requirement | Conditional Access policy |
|---|---|
| Protect administrator accounts | Require MFA for privileged roles. |
| Restrict email access | Require approved client applications. |
| Protect sensitive resources | Require compliant or managed devices. |
| Prevent access from untrusted sources | Block access based on configured location or other conditions. |

## 4. Exam Tips

- **Conditional Access belongs to Microsoft Entra ID.**
- Remember: **Signals → Decision → Enforcement.**
- Sign-in signals can include user, location, device, and application.
- An unusual location may trigger MFA or a block, depending on policy.
- Conditional Access can enforce MFA, device requirements, and application restrictions.
- **MFA** verifies identity with additional authentication.
- **Conditional Access** determines when MFA or other access requirements apply.

## Final Summary

Conditional Access evaluates sign-in context and applies access policies.

- **Signals:** Information about the sign-in.
- **Decision:** Evaluate the policy.
- **Enforcement:** Allow, require extra verification, or block access.
