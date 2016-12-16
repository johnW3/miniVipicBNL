#!../../bin/linux-arm/vipic

## You may have to change vipic to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/vipic.dbd"
vipic_registerRecordDeviceDriver pdbbase

## Load record instances
dbLoadTemplate "db/user.substitutions"
dbLoadRecords "db/dbSubExample.db", "user=root"
#devA32ZedDebug = 20
dbLoadRecords("db/zedBO.db","user=vipic,LED=1,OUT=#C1 S2 @0")
dbLoadRecords("db/zedBO.db","user=vipic,LED=2,OUT=#C1 S2 @1")
dbLoadRecords("db/zedBO.db","user=vipic,LED=3,OUT=#C1 S2 @2")
dbLoadRecords("db/zedBO.db","user=vipic,LED=4,OUT=#C1 S2 @3")
dbLoadRecords("db/zedWF.db","user=vipic,WF=1,numberElements=512,IN=#C1 S0 @311,IN2=#C1 S1 @0")
dbLoadRecords("db/zedLO.db","user=vipic,WF=1")
#dbLoadRecords("db/zedWF2.db","user=vipic,WF=3,numberElements=255,IN=vipic:PixelToScan1")

## Set this to see messages from mySub
#var mySubDebug 1

## Run this to trace the stages of iocInit
#traceIocInit

devA32ZedConfig(1, 0x43c00000, 16, 0, 0)

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncExample, "user=root"
dbpf vipic:configPixelCnt1,1984
devA32ZedReport

