# Azure Storage Services — Key Notes

## 1. The Five Core Storage Services

| Service | Purpose | Example |
|---|---|---|
| **Azure Blob Storage** | Unstructured object data | Images, videos, backups, logs |
| **Azure Files** | Managed shared file systems | Shared folders across machines |
| **Azure Queue Storage** | Asynchronous message processing | Background tasks between application components |
| **Azure Disk Storage** | Block storage for Azure VMs | VM operating system and data disks |
| **Azure Table Storage** | Structured, non-relational NoSQL data | Device metadata and user-related records |

**Memory trick:**
- Blobs = Objects
- Files = Shared folders
- Queues = Messages
- Disks = Virtual machines
- Tables = NoSQL data

## 2. Benefits of Azure Storage

- **Durable and highly available:** redundancy protects against failures.
- **Secure:** data is encrypted, and access is controlled.
- **Scalable:** storage grows with application needs.
- **Managed:** Azure handles infrastructure maintenance.
- **Accessible:** supports HTTP/HTTPS, REST APIs, SDKs, Azure CLI, PowerShell, and the Azure portal.

## 3. Azure Blob Storage

Blob Storage stores **unstructured text and binary data**.

Common uses:
- Images, documents, audio, and video.
- Backups and disaster recovery.
- Logs and analytics datasets.
- Files accessed over HTTP/HTTPS.

### Blob Access Tiers

| Tier | Best For | Minimum Recommended Storage Duration |
|---|---|---|
| **Hot** | Frequently accessed data | No minimum |
| **Cool** | Infrequently accessed data | 30 days |
| **Cold** | Rarely accessed data | 90 days |
| **Archive** | Rarely accessed, long-term data | 180 days |

As you move from Hot to Archive:
- Storage costs generally decrease.
- Retrieval costs and latency generally increase.

Important:
- Hot, Cool, and Cold can be set at the account or blob level.
- Archive is available only at the blob level.
- Archived data must be rehydrated before normal reading; retrieval can take hours.

## 4. Azure Files

Provides fully managed shared file storage.

- **SMB:** supported by Windows, Linux, and macOS clients.
- **NFS:** supported by Linux and macOS clients.
- Multiple machines can access the same file share.
- Azure File Sync can cache SMB file shares on Windows Servers.

**Exam tip:** Shared folders accessible by multiple machines → Azure Files.

## 5. Azure Queue Storage

Stores messages for asynchronous processing.

Example:
1. An application places a task in a queue.
2. A background worker retrieves it.
3. The worker processes it when ready.

Key facts:
- Supports millions of messages.
- Maximum message size: **64 KB**.
- Commonly used for background tasks and with Azure Functions.

**Exam tip:** Messages or background processing → Queue Storage.

## 6. Azure Disk Storage

Provides block-level storage volumes for Azure virtual machines.

Examples:
- Operating system disks.
- Data disks attached to VMs.

**Exam tip:** Storage for a VM's operating system or attached disk → Disk Storage.

## 7. Azure Table Storage

A NoSQL service for large amounts of structured, non-relational data.

Example: device IDs, device status, and associated metadata.

**Exam tip:** Structured, non-relational data → Table Storage.

## 8. Exam Tips and Takeaways

1. Identify the storage service from the type of data or scenario.
2. Remember the five services: **Blobs, Files, Queues, Disks, Tables**.
3. Know the Blob tiers: Hot, Cool, Cold, Archive.
4. Archive offers low storage costs but high retrieval latency.
5. Distinguish SMB and NFS when answering Azure Files questions.
6. Remember Queue Storage's 64 KB message limit.
7. Azure Storage encrypts data and offers redundancy, scalability, and managed infrastructure.

**Final checklist:** Know what each service stores, when to use it, the four Blob access tiers, and the key exam facts about Azure Files, Queues, Disks, and Tables.