TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Install databases, templates & substitutions like this
DB += dbExample1.db
DB += dbExample2.db
DB += dbSubExample.db
DB += user.substitutions
#DB += /root/epics/myvipic/support/zedApp/Db/zedBO.db
#DB += /root/epics/myvipic/support/zedApp/Db/zedWF.db
DB += ../../../../support/zedApp/Db/zedBO.db
DB += ../../../../support/zedApp/Db/zedWF.db
DB += ../../../../support/zedApp/Db/zedLO.db

# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_TEMPLATE = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

