# Azure Fundamentals — External Identities

## 1. What Is Microsoft Entra External ID?

Enables organizations to securely provide access to people outside their Microsoft Entra tenant, such as partners, suppliers, contractors, and customers.

**Key distinction:**
- **Authentication:** Who are you?
- **Authorization:** What are you allowed to access?

## 2. Three External ID Capabilities

| Capability | Purpose | Key fact |
|---|---|---|
| **B2B collaboration** | Partners and contractors access organizational resources | External users typically appear as guest users in your directory. |
| **B2B direct connect** | Cross-tenant collaboration through supported scenarios | Supports Teams shared channels; users aren't represented as guest users in your directory. |
| **External ID for customers** | Customers sign in to your applications | Designed for customer-facing apps, such as websites and online services. |

## 3. Access Reviews

Access reviews help organizations determine whether external users still need access.

- Reviewers evaluate existing access.
- Access can be retained or removed based on the review.
- Helps prevent unnecessary guest access from continuing indefinitely.

## 4. Exam Tips

- **Invite a supplier to access files:** B2B collaboration.
- **Collaborate through a Teams shared channel without guest accounts:** B2B direct connect.
- **Allow customers to sign in to your website:** External ID for customers.
- **Check whether guests still need access:** Access reviews.
- **Authentication:** Verifies identity.
- **Authorization:** Determines permitted access.
- External users can use existing identities, depending on the supported sign-in scenario.

## Final Summary

- **B2B collaboration = guests in your directory.**
- **B2B direct connect = Teams shared channels and cross-tenant trust.**
- **External ID for customers = customer-facing applications.**
- **Access reviews = check and remove unnecessary access.**