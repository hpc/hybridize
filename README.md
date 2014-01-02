hybridize
=========

Generate an optimal rootfs hybridize list of files that should be symlinked to NFS mount and not required before NFS mount happens

Usage
-----
hybridize is called from within ppsst (createimg).  There is a requirement of only 1 kernerl installed into the rootfs so that hybridize can determine what to replace the @KVER@ varliable with in the whitelist.  The basic usage is as follows:
```
   hybridize -f /path/to/image/whitelist $HYBRID_OPTS -o /path/to/image/hybridize
```

The output file called hybridize in the example above is used to repalce those files/directories in the rootfs with symlinks to the corresponding files/directories on an NFS mount with the initramfs image.  This enables use of a (short) list of files which must remain in RAM to boot the node with any additional files added to the image defaulting to the NFS mount.

Example Whitelist Files
-----------------------
These are files that are currently used to boot RHEL/TOSS images as well as an example for a Fedora 18 image.  These are not guranteed to be as minimal as possible.  There may be additional requirements for other device drivers or other services needed before the NFS mount happens.  But these should give a good starting point.  Typical resulting image sizes are on the order of 100MB with a ill 20+GB distro available to the node once the NFS mount completes.
