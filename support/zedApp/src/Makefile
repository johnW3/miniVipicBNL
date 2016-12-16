TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#==================================================
# build a support library

LIBRARY_IOC += zed

# xxxRecord.h will be created from xxxRecord.dbd
#DBDINC += xxxRecord
# install zed.dbd into <top>/dbd
DBD += devA32Zed.dbd
DBD += zed.dbd

# specify all source files to be compiled and added to the library
#zed_SRCS += xxx
zed_SRCS += devA32Zed.c

zed_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

