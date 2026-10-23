# Azure Fundamentals — Role-Based Access Control (RBAC)

## 1. What Is Azure RBAC?

Azure role-based access control (RBAC) manages **who can do what on which Azure resources**.

It assigns roles to users, groups, or other supported identities to control their permissions.

## 2. Principle of Least Privilege

Grant users **only the permissions they need** to perform their tasks.

Benefits:
- Reduces accidental changes.
- Limits damage from compromised accounts.
- Prevents unnecessary access to resources.

## 3. Three Built-in Roles

| Role | Permissions |
|---|---|
| **Owner** | Manage resources and assign Azure RBAC roles. |
| **Contributor** | Create and manage resources, but cannot assign Azure RBAC roles. |
| **Reader** | View resources without modifying them. |

**Remember:**
- Owner = manage resources + access.
- Contributor = manage resources.
- Reader = view only.

## 4. Azure RBAC Scope

Scope determines where a role assignment applies.

From broadest to narrowest:

1. **Management group** — Organizes multiple subscriptions.
2. **Subscription** — Contains resource groups and resources.
3. **Resource group** — Organizes related resources.
4. **Resource** — One specific Azure resource.

### Inheritance
Permissions assigned at a parent scope are inherited by child scopes.

**Example:** Reader assigned at subscription scope generally provides read access to the resource groups and resources within that subscription.

## 5. Role Assignment Components

Every role assignment specifies:

- **Who:** The user, group, or other supported identity.
- **What:** The role and its permissions.
- **Where:** The scope where permissions apply.

Example:

`Engineering group + Contributor + Development resource group`

The engineering group can manage resources within that resource group without automatically receiving Contributor access to the entire subscription.

Azure supports built-in roles and custom roles.

## 6. How RBAC Is Enforced

Azure RBAC controls covered Azure resource management actions through **Azure Resource Manager**.

Common management interfaces:
- Azure portal
- Azure Cloud Shell
- Azure CLI
- Azure PowerShell

**Important:** Resource management permissions do not necessarily grant access to data inside a resource. Data access may require separate permissions or data-specific roles.

## 7. Multiple Role Assignments

Azure RBAC generally combines allowed permissions from applicable role assignments.

Example:
- Reader on a resource group.
- Contributor on the same resource group.

The user generally receives the combined allowed permissions from both assignments.

Other controls, such as deny assignments, can affect the final result.

## 8. Exam Tips

- **Azure RBAC:** Who, what, and where.
- **Least privilege:** Grant only necessary permissions.
- **Owner:** Manage resources and assign roles.
- **Contributor:** Manage resources, but cannot assign roles.
- **Reader:** View resources only.
- **Scope hierarchy:** Management group → Subscription → Resource group → Resource.
- **Inheritance:** Parent-scope permissions flow to child scopes.
- **Multiple assignments:** Allowed permissions are generally combined.
- **Azure Resource Manager:** Enforces RBAC for covered resource management operations.
- **Custom roles:** Define permissions beyond built-in roles.

## Final Summary

Before assigning Azure RBAC permissions, identify:

1. **Who** needs access?
2. **What role** do they need?
3. **Where (scope)** should the role apply?

Choose the narrowest appropriate scope and follow the principle of least privilege.
