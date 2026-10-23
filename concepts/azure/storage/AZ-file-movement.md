# Azure File Movement Options — Key Notes

## 1. AzCopy

**Purpose:** Copy files and blobs to, from, or between Azure Storage accounts using command-line commands.

Key capabilities:
- Upload and download files.
- Copy between storage accounts.
- Synchronize files in one direction.
- Transfer files between Azure and other cloud providers.

**Exam tip:** AzCopy synchronization is **one-way**. You specify the source and destination; it does not automatically synchronize changes in both directions.

**Best for:** Scripted and automated file transfers.

## 2. Azure Storage Explorer

**Purpose:** Manage Azure Storage through a graphical user interface (GUI).

Key capabilities:
- Upload and download files.
- Browse and manage blobs and files.
- Transfer data between storage accounts.

Key facts:
- Supports Windows, macOS, and Linux.
- Uses AzCopy in the background for file and blob management tasks.

**Exam tip:** If a question asks for a visual tool to manage Azure Storage, choose **Azure Storage Explorer**.

**Best for:** Users who prefer a graphical interface over command-line commands.

## 3. Azure File Sync

**Purpose:** Keep on-premises Windows Server file shares synchronized with Azure Files.

Key capabilities:
- Bidirectional synchronization between local servers and Azure Files.
- Local access to files while centralizing storage in Azure.
- Multiple server caches.
- **Cloud tiering:** Frequently accessed files stay locally; less-used files can remain in Azure until requested.
- Server replacement and recovery by configuring a replacement server.

**Exam tip:** If a question asks for bidirectional synchronization between a Windows Server and Azure Files, choose **Azure File Sync**.

**Best for:** Hybrid environments requiring both local file-server access and cloud storage.

## 4. Main Differences

| Feature | AzCopy | Storage Explorer | Azure File Sync |
|---|---|---|---|
| Interface | Command line | Graphical interface | Background service |
| Main purpose | Copy and transfer files | Visually manage storage | Synchronize local and cloud file shares |
| Synchronization | One-way per sync operation | Manual file management and transfers | Bidirectional |
| Best use | Automation | Visual management | Hybrid cloud storage |

## 5. Exam Tips and Takeaways

- **AzCopy** = command-line file transfers and automation.
- **Storage Explorer** = graphical management of Azure Storage.
- **Azure File Sync** = bidirectional synchronization with Azure Files.
- **One-way synchronization** = AzCopy.
- **Cloud tiering** = Azure File Sync.
- **Windows, macOS, and Linux support** = Azure Storage Explorer.

**Memory trick:** AzCopy = Commands; Storage Explorer = GUI; Azure File Sync = Local + Cloud synchronization.
