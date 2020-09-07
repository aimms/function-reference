#!/usr/bin/env python
import os, sys

this_script_dir = os.path.abspath(os.path.dirname(__file__))
os.chdir(this_script_dir)
sys.path.insert(0,'../..')

from buildtool.gitinfo import gitinfo

aimms_version = gitinfo().getVersion()
branchName = os.getenv('CI_COMMIT_REF_NAME', "dummyName")

print ("Going to write to AimmsVersion.FunctionReferenceVersions table the following values: (Branch: %s, Version: %s)" % (branchName, aimms_version))

#### SQL stuff 
import MySQLdb #for exception handling
from buildtool.MySQLIntraConnection import MySQLIntraConnection

strSQL = "REPLACE INTO `AimmsVersion`.`FunctionReferenceVersions` (`Branch`, `Version`) VALUES (\"%s\",\"%s\")" %(branchName, aimms_version )

mysql = MySQLIntraConnection()
mysql.connect("AimmsVersion")
try:
    mysql.execute(strSQL)
except MySQLdb.Error as e :
    print ("DB error while inserting to AimmsVersion.FunctionReferenceVersions (err: %d: %s)" % (e.args[0], e.args[1]))
except:
    print (" Error: Unknown error while inserting to AimmsVersion.FunctionReferenceVersions")
    mysql.disconnect()
    sys.exit(3)

mysql.disconnect()
sys.exit(0)
