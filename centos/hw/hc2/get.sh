rpm -qa > rpm.list
rpm -Va >> rpm-va.output
cat /proc/cmdline >> cmdline
systemctl list-units >> systemd.units
dracut --print-cmdline >> dracut.cmdline
dracut  --list-modules >> dracut.modules
lsinitrd  >> lsinitrd.output
ps -ef  >> ps-ef.out
lsmod >> lsmod.out
sysctl -a >> sysctl.ouot
cat /proc/mounts >> proc-mounts
tune2fs -l /dev/vda2  >> vda2.out
dumpe2fs /dev/vda2  >> vda2_dumpe2fs.out
cat /proc/meminfo >> meminfo
cat /proc/sys/vm/swappiness  >> swapiness.out
dmesg >> demsg.out
dmidecode >> dmidecode.out
cat /sys/block/vda/queue/scheduler  >> ioscheduler
ethtool -k eth0 >> ethtool.k.eth0
ethtool -i eth0 >> ethtool.i.eth0
lsblk >> lsblk.out
lspci >> lspci.out
