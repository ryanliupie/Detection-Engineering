### What is a Forensic Image?

A forensic image is a bit-for-bit copy of data from a source to a destination. The source can include storage media such as hard drives, USB devices, or entire systems. This process preserves all data exactly as it exists, including deleted files and hidden information. In some cases, an entire device (such as a computer or mobile device) can be imaged into a single file for analysis.

Not all imaging and backup software create forensic images. For instance, Windows backup creates image backups that aren't complete copies of the physical device.A forensic image <b>MUST</b> be a bit-for-bit copy of the source media so that all data is preserved exactly as it exists on the original device. 

Forensic imaging is used in cybersecurity to capture a complete, unaltered copy of a system so investigators can recover hidden or deleted data and analyze it safely without risking the original evidence.

Imagine: 

- A hacker deletes logs to hide activity 

`Without` forensic imaging: 
- You only see what is left, maybe even nothing

`With` forensic imaging: 
- You can recover deleted logs, and prove something happened. 
<hr>

Types of forensic images: 

- <b>Physical image:</b> This image captures a storage device's content. This includes active data, unused or unallocated space, and deleted data that might still reside in the storage unit. 
- <b>Logical image:</b> This image captures active data by scanning a storage device. 
- <b>Targeted Image:</b> This image contains specific data, such as data required for a legal examination. 
<hr>

Different types of forensic image file formats: 

- <b>Raw image (DD):</b> This image is a `"pure copy, nothing extra"`, where it is not compressed, and has no extra metadata; in its simplest format. 
- <b>EnCase image (E01):</b> This image is `"forensic friendly and court ready"`, meaning the image is compressed, includes metadata, and has built-int integrity checks (hashing)
- <b>Advanced forensic format (AFF):</b> This image is `"flexible"`, meaning it is an open source format that supports both compression and encryption, and stores data and metadata together. 
- <b>SMART:</b> This image handles `"enormous evidence"` where it supports compression and segmentation, and it used for large datasets. 
- <b>FTK (Forensic ToolKit):</b> FTK is a forensic tool that uses its `own proprietary image` format. It has hash verification, and is best suited for evidence integrity. 
<hr>

### Why is forensic imaging important? 

It helps prevent the loss of original data and the imaging tools and techniques are the only way electronic data can be submitted as evidence in a court or legal proceeding. 

### Challenges of forensic images? 

- <b>1. Preserving Authenticity:</b> If a drive is encrypted or is using anti-forensic techniques (wiping, obfuscation), you may not get a clean, readable image. 
- <b>2. Large images sizes:</b> big file sizes, especially in raw format (DD), can strain storage and transferring/sharing becomes slow. 
- <b>3. Time Constraints:</b> Imaging is slow where it can take hours or days depending on the size of a drive. This is an issue when it comes to urgent situations. 
- <b>4. Tool compatibility:</b> Not all tools support all formats. 
- <b>5. Legal Complexity:</b> `VERY important`, where chain of custody standards, integrity (hashes), and avoiding data tampering must met in legal cases.   

