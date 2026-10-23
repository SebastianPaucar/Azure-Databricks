# Authentication Methods - Key Notes

## 1. What Is Authentication?

**Authentication verifies who you are** before granting access to an application, account, or resource.

Common authentication methods include:
- Passwords
- Single sign-on (SSO)
- Multifactor authentication (MFA)
- Passwordless authentication

## 2. Single Sign-On (SSO)

**SSO allows you to sign in once and access multiple trusted applications without signing in separately to each one.**

**Example:** Sign in to your work account and access Outlook, Teams, and other authorized applications.

Benefits:
- Fewer passwords to remember.
- Fewer password resets.
- Easier user access management.

**Remember:** SSO improves convenience, but security depends on protecting the initial sign-in.

## 3. Multifactor Authentication (MFA)

**MFA requires at least two different types of authentication factors.**

There are three factor categories:

| Factor | Meaning | Example |
|---|---|---|
| Something you know | Information you know | Password or PIN |
| Something you have | A physical device | Phone or security key |
| Something you are | A biometric characteristic | Fingerprint or face |

**Example:** Enter a password and approve a sign-in using Microsoft Authenticator.

Two passwords alone do not count as MFA because they belong to the same factor category.

Microsoft Entra MFA adds an extra verification step, helping protect accounts even if a password is stolen.

## 4. Passwordless Authentication

**Passwordless authentication verifies your identity without requiring a password.**

It can use a trusted device, PIN, biometric verification, or a security key.

### Windows Hello for Business
- Uses a PIN or biometrics.
- Credentials are associated with the user's designated Windows device.
- Suitable for employees using assigned Windows computers.

### Microsoft Authenticator
- Uses a mobile phone to approve sign-ins.
- May use number matching, a PIN, or biometric verification.
- Supports sign-in without entering a password.

### FIDO2 Security Keys
- Physical security keys used to authenticate.
- May connect through USB, NFC, or Bluetooth, depending on the device.
- Use standards including WebAuthn.
- Designed to resist phishing.

## 5. Comparison of Authentication Methods

| Method | Main purpose | Key idea |
|---|---|---|
| Password | Verify identity | Enter a secret |
| SSO | Simplify access | One sign-in, multiple applications |
| MFA | Strengthen security | At least two different factor categories |
| Passwordless | Remove passwords | Authenticate using another trusted method |

These methods can work together. For example, SSO can be combined with MFA.

## 6. Azure Fundamentals Exam Tips

Remember these associations:

- **Authentication** = verifies identity.
- **SSO** = one sign-in for multiple applications.
- **MFA** = at least two different authentication factor categories.
- **Passwordless** = no password required.
- **Windows Hello for Business** = PIN or biometrics tied to a Windows device.
- **Microsoft Authenticator** = mobile-based authentication and sign-in approval.
- **FIDO2 security key** = physical key designed to resist phishing.
- **Microsoft Entra MFA** = adds an extra verification step.

## 7. Quick Self-Test

1. A user signs in once and accesses Outlook and Teams. Which method is this?  
   **Answer:** SSO.

2. A user enters a password and approves a notification on their phone. Which method is this?  
   **Answer:** MFA.

3. Does entering two different passwords count as MFA?  
   **Answer:** No. Both are something you know.

4. Which passwordless method uses a physical security key?  
   **Answer:** FIDO2 security keys.

5. Which method eliminates the need to enter a password?  
   **Answer:** Passwordless authentication.

6. Can SSO and MFA be used together?  
   **Answer:** Yes.

## Final Summary

- **SSO:** One sign-in, multiple applications.
- **MFA:** Verify identity using different factor categories.
- **Passwordless:** Authenticate without a password.
- **Windows Hello:** Device-based PIN or biometrics.
- **Authenticator:** Phone-based authentication.
- **FIDO2:** Phishing-resistant security key authentication.
