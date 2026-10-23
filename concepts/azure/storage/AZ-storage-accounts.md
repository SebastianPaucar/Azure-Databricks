# Azure Storage Accounts — Key Notes

## 1. What Is an Azure Storage Account?

An Azure Storage Account provides a **unique namespace** to store and access data globally over HTTP or HTTPS.

Key characteristics:
- **Secure:** protects stored data.
- **Highly available:** designed for continued access.
- **Durable:** protects against data loss.
- **Scalable:** grows with storage requirements.

## 2. Storage Account Types

| Type | Supported Services | Main Use |
|---|---|---|
| Standard general-purpose v2 | Blobs, Data Lake Storage, Files, Queues, Tables | Recommended for most scenarios |
| Premium block blobs | Block blobs, append blobs | High transaction rates and low latency |
| Premium file shares | Azure Files | High-performance file shares; supports SMB and NFS |
| Premium page blobs | Page blobs | Specialized page blob workloads |

**Remember:** Standard general-purpose v2 is the most versatile account type.

## 3. Redundancy Options

Redundancy means maintaining copies of data to protect against failures.

| Option | Meaning |
|---|---|
| LRS | Locally redundant storage |
| ZRS | Zone-redundant storage |
| GRS | Geo-redundant storage |
| RA-GRS | GRS with read access to the secondary region |
| GZRS | ZRS in the primary region plus replication to a secondary region |
| RA-GZRS | GZRS with read access to the secondary region |

### Memory Trick

- **L** = Local
- **Z** = Zones
- **G** = Geography (regions)
- **RA** = Read Access to the secondary region

## 4. Storage Service Endpoints

The endpoint is the URL used to access a storage service.

Assume the account name is `mydatastore`.

| Service | Endpoint Suffix |
|---|---|
| Blob Storage | `.blob.core.windows.net` |
| Data Lake Storage Gen2 | `.dfs.core.windows.net` |
| Azure Files | `.file.core.windows.net` |
| Queue Storage | `.queue.core.windows.net` |
| Table Storage | `.table.core.windows.net` |

Example:

`https://mydatastore.blob.core.windows.net`

The account name remains the same; the service-specific endpoint changes.

## 5. Storage Account Naming Rules

Storage account names must:
- Contain **3–24 characters**.
- Use **lowercase letters and numbers only**.
- Be **unique across Azure**.

Examples:

- `mydata2026` — Valid
- `MyData2026` — Invalid (uppercase letters)
- `my-data` — Invalid (hyphen)

## 6. Exam Tips

1. **Default choice:** Standard general-purpose v2 is recommended for most storage scenarios.
2. **High performance:** Premium block blobs are suited to low-latency blob workloads; premium file shares are for high-performance file sharing.
3. **Availability zones:** ZRS replicates data across availability zones within a region.
4. **Disaster recovery:** GRS replicates data to a secondary region.
5. **Secondary-region reads:** Choose RA-GRS or RA-GZRS when read access to the secondary region is required.
6. **Endpoint questions:** Identify the service by its endpoint abbreviation, such as `.blob`, `.file`, or `.queue`.
7. **Naming questions:** Remember the 3–24 character limit and lowercase-alphanumeric restriction.

## 7. Key Takeaways

- A storage account is the foundation for Azure Storage services.
- Account type determines supported services and available redundancy options.
- Redundancy determines how data copies are maintained to protect against failures.
- Endpoints provide access to individual storage services.
- A storage account's name must be globally unique within Azure.

**Final exam checklist:** Know the four account types, the six redundancy options, the five service endpoints, and the storage account naming rules.
