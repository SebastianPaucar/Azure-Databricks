# Directory Services - Key Notes

## 1. What Is Microsoft Entra ID?

Microsoft Entra ID is Microsoft's cloud-based **identity and access management (IAM)** service.

It helps organizations:
- Verify users' identities.
- Control access to applications and resources.
- Provide single sign-on (SSO).
- Apply security features such as multifactor authentication (MFA).
- Manage cloud identities and application access.

**Remember:** Microsoft Entra ID manages cloud identities and access. It is not simply Active Directory moved to the cloud.

## 2. Who Uses Microsoft Entra ID?

| User | Purpose |
|---|---|
| IT administrators | Manage identities, permissions, and access policies. |
| App developers | Integrate sign-in and SSO into applications. |
| Regular users | Sign in and perform actions such as self-service password resets. |
| Online service subscribers | Access services such as Microsoft 365 and Azure. |

## 3. Main Capabilities of Microsoft Entra ID

### Authentication
Verifies who you are before granting access.

Examples:
- MFA
- Self-service password reset
- Banned password lists
- Smart lockout

### Single Sign-On (SSO)
Allows one sign-in to provide access to multiple authorized applications.

### Application Management
Helps manage access to cloud and on-premises applications.

Examples:
- SaaS application integration
- Application Proxy
- My Apps portal

### Device Management and Access
Works with services such as Microsoft Intune to manage devices and support device-based access policies.

**Remember:** Microsoft Entra ID manages identity and access; Microsoft Intune focuses on device management.

## 4. Microsoft Entra Connect

Microsoft Entra Connect synchronizes identity information between on-premises Active Directory Domain Services (AD DS) and Microsoft Entra ID.

It helps organizations maintain a more consistent identity experience across on-premises and cloud environments.

Typical hybrid architecture:

`On-premises AD DS → Microsoft Entra Connect → Microsoft Entra ID`

Benefits can include:
- Synchronized identity information.
- A more consistent sign-in experience.
- Integration of on-premises identities with cloud applications.

**Important:** Synchronization does not automatically guarantee SSO. Sign-in behavior depends on configuration.

## 5. Microsoft Entra Domain Services

Microsoft Entra Domain Services provides managed, traditional domain capabilities in Azure without requiring you to manage the domain controllers yourself.

It is useful for legacy applications that require traditional Active Directory features.

### Main Features

| Feature | Purpose |
|---|---|
| Domain join | Join computers or servers to a domain. |
| Group Policy | Centrally apply settings and restrictions. |
| LDAP | Access directory information. |
| Kerberos | Traditional network authentication protocol. |
| NTLM | Traditional authentication protocol. |

### How It Works

1. You define a unique domain namespace.
2. Azure deploys two Windows Server domain controllers in the selected Azure region.
3. These domain controllers form a **replica set**.
4. Microsoft manages the domain controllers and their platform maintenance.
5. Azure VMs and compatible applications use the managed domain's features.

**Remember:** Microsoft manages the domain controllers, reducing the need for you to administer them.

## 6. Identity Synchronization

Microsoft Entra Domain Services receives synchronized identity information from Microsoft Entra ID.

In a hybrid environment:

`On-premises AD DS → Microsoft Entra Connect → Microsoft Entra ID → Microsoft Entra Domain Services`

Key rules:
- Identities and groups can synchronize from Microsoft Entra ID to Domain Services.
- Changes made directly in the managed domain do not synchronize back to Microsoft Entra ID.
- The synchronization direction into Domain Services is one-way.

**Exam tip:** Microsoft Entra ID → Domain Services, not both ways.

## 7. Compare the Services

| Service | Main purpose |
|---|---|
| Active Directory Domain Services (AD DS) | Traditional directory and domain services, commonly managed on-premises. |
| Microsoft Entra ID | Cloud identity, authentication, and access management. |
| Microsoft Entra Connect | Synchronizes identities between on-premises AD DS and Microsoft Entra ID. |
| Microsoft Entra Domain Services | Provides managed traditional domain features in Azure. |

## 8. Azure Fundamentals Exam Tips

Remember these associations:

- **Cloud identities and access:** Microsoft Entra ID.
- **Identity synchronization:** Microsoft Entra Connect.
- **Legacy applications requiring LDAP or Kerberos:** Microsoft Entra Domain Services.
- **Centralized computer settings:** Group Policy.
- **Directory access protocol:** LDAP.
- **Traditional authentication protocols:** Kerberos and NTLM.
- **Two managed domain controllers:** Replica set.
- **Domain Services synchronization:** One-way from Microsoft Entra ID to Domain Services.

## 9. Quick Self-Test

1. Which service manages cloud identities and access to Azure and Microsoft 365?  
   **Answer:** Microsoft Entra ID.

2. Which tool synchronizes identities between on-premises AD DS and Microsoft Entra ID?  
   **Answer:** Microsoft Entra Connect.

3. An older application requires LDAP, Group Policy, and Kerberos in Azure. Which service can help?  
   **Answer:** Microsoft Entra Domain Services.

4. What is a replica set in this lesson?  
   **Answer:** Two managed domain controllers deployed in an Azure region.

5. Does a change made directly in Microsoft Entra Domain Services synchronize back to Microsoft Entra ID?  
   **Answer:** No.

6. Does Microsoft Entra ID provide every traditional AD DS feature by itself?  
   **Answer:** No. Microsoft Entra Domain Services provides many traditional domain capabilities for applications that need them.

## Final Summary

- **Microsoft Entra ID:** Cloud identity and access management.
- **Microsoft Entra Connect:** Identity synchronization between on-premises AD DS and Microsoft Entra ID.
- **Microsoft Entra Domain Services:** Managed traditional domain capabilities in Azure.
- **Synchronization into Domain Services:** One-way from Microsoft Entra ID.
