# PCR-rpi-boot-sequence

The file `correct_boot.log` is the boot log generated when the Raspberry is executed correctly.

The file `wrong_boot.log` is the boot log that we manually editted the CPU device id. This file is used to represent the abnormal execution.

boot log is generated by the command `$dmesg`

To check the boot sequence, run the command `python test.py`. After extending two logs into PCR, we will find that two states are different, thus we can detect the abnormal execution.

