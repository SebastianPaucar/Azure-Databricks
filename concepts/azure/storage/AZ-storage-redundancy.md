# Azure Storage Redundancy — Key Notes

## 1. What Is Redundancy?

Redundancy means **keeping multiple copies of data** to protect against hardware failures, outages, and regional disasters.

Your choice affects:
- **Cost**
- **Availability**
- **Durability**
- **Disaster recovery**

## 2. Primary-Region Redundancy

| Option | How It Works | Key Benefit |
|---|---|---|
| **LRS** | 3 copies in one data center | Lowest cost; protects against local hardware failures |
| **ZRS** | Replicates across 3 availability zones in one region | Protects against a zone failure; read/write access can continue |

## 3. Secondary-Region Redundancy

| Option | How It Works | Key Benefit |
|---|---|---|
| **GRS** | LRS in the primary region + LRS in a secondary region | Protects against regional disasters |
| **GZRS** | ZRS in the primary region + LRS in a secondary region | Combines zone protection and regional disaster recovery |

**Important:** Replication to the secondary region is asynchronous. If the primary region fails, recent writes might not have reached the secondary region.

## 4. Read Access to the Secondary Region

| Option | Meaning |
|---|---|
| **RA-GRS** | GRS + read access to the secondary region |
| **RA-GZRS** | GZRS + read access to the secondary region |

Without `RA`, secondary-region data generally becomes accessible after failover. With `RA`, you can read secondary-region data before failover, but it might be outdated.

## 5. Synchronous vs. Asynchronous Replication

- **Synchronous:** Data is replicated within the primary region before the write operation is considered complete.
- **Asynchronous:** Data is replicated to the secondary region later, so some recent data might be lost during a regional failure.

## 6. RPO — Recovery Point Objective

RPO indicates how far back in time recoverable data might go after a failure.

- Azure Storage typically has an RPO of **less than 15 minutes** for geo-replication.
- There is no SLA for how long replication to the secondary region takes.

## 7. Exam Tips

- **Lowest cost:** LRS.
- **Availability-zone failure protection:** ZRS.
- **Regional disaster protection:** GRS.
- **Zone protection + regional disaster recovery:** GZRS.
- **Read secondary data before failover:** RA-GRS or RA-GZRS.
- **Primary region:** LRS or ZRS.
- **Secondary region:** GRS or GZRS; replication is asynchronous.
- **RPO:** measures the potential loss of recent data, not the time needed to restore service.

## 8. Key Takeaways

| Requirement | Choose |
|---|---|
| Lowest-cost redundancy | LRS |
| Protection across availability zones | ZRS |
| Protection against regional disasters | GRS |
| Zone and regional protection | GZRS |
| Secondary-region read access | RA-GRS or RA-GZRS |

**Memory trick:**
- **L** = Local
- **Z** = Zones
- **G** = Geography (secondary region)
- **RA** = Read Access to the secondary region

**Final exam checklist:** Know where the copies are stored, whether replication is synchronous or asynchronous, what `RA` means, and how RPO relates to potential data loss.