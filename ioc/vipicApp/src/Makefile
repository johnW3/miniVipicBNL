TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# xxxRecord.h will be created from xxxRecord.dbd
DBDINC += xxxRecord

# Install xxxSupport.dbd into <top>/dbd
DBD += xxxSupport.dbd

# Build an IOC support library
LIBRARY_IOC += vipicSupport

# Compile and add the code to the support library
vipicSupport_SRCS += xxxRecord.c
vipicSupport_SRCS += devXxxSoft.c

# Link locally-provided code into the support library,
# rather than directly into the IOC application.
# This is required for Windows DLL builds.
vipicSupport_SRCS += dbSubExample.c
vipicSupport_SRCS += vipicHello.c
vipicSupport_SRCS += initTrace.c

#following two commands did not get devA32ZedConfig into epics ioc??
#vipicSupport_OBJ += /root/epics/myvipic/support/zedApp/src/O.linux-arm/devA32Zed.o
#vipicSupport_LIBS += zed
vipicSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

# Build the IOC application
PROD_IOC = vipic

# vipic.dbd will be created and installed
#DBD += zed.dbd
# following commands gets devA32Zed.dbd into spot where st.cmd can download it.
# is it better to put devA32Zed.dbd into vipic.dbd????
# DBD += /root/epics/myvipic/support/dbd/devA32Zed.dbd
DBD += vipic.dbd

# vipic.dbd will include these files:
vipic_DBD += base.dbd
vipic_DBD += xxxSupport.dbd
vipic_DBD += dbSubExample.dbd
vipic_DBD += vipicHello.dbd
vipic_DBD += initTrace.dbd
# following will put devA32Zed.dbd into vipic.dbd THIS WORKS
#vipic_DBD += /root/epics/myvipic/support/dbd/devA32Zed.dbd
vipic_DBD += ../../../../support/dbd/devA32Zed.dbd

# vipic_registerRecordDeviceDriver.cpp derives from vipic.dbd
vipic_SRCS += vipic_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
#vipic_SRCS += /root/epics/myvipic/support/zedApp/src/O.linux-arm/devA32Zed
vipic_SRCS += ../../../../support/zedApp/src/O.linux-arm/devA32Zed
#vipic_SRCS += devA32Zed
vipic_SRCS_DEFAULT += vipicMain.cpp
vipic_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#vipic_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
#vipic_OBJS += /root/epics/myvipic/support/zedApp/src/O.linux-arm/devA32Zed.o
#vipic_LIBS += /root/epics/myvipic/support/lib/linux-arm/libzed
#vipic_LIBS += ZED
vipic_LIBS += vipicSupport

# To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
#ifneq ($(SNCSEQ),)
    # Build sncExample into vipicSupport
#    sncExample_SNCFLAGS += +r
#    vipic_DBD += sncExample.dbd
#    vipicSupport_SRCS += sncExample.stt
#    vipicSupport_LIBS += seq pv
#    vipic_LIBS += seq pv

    # Build sncProgram as a standalone program
#    PROD_HOST += sncProgram
#    sncProgram_SNCFLAGS += +m
#    sncProgram_SRCS += sncProgram.st
#    sncProgram_LIBS += seq pv
#    sncProgram_LIBS += $(EPICS_BASE_HOST_LIBS)
#endif

# Finally link IOC to the EPICS Base libraries
vipic_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

