# -*- coding: iso-8859-15 -*-
# -*- Mode: Python; py-ident-offset: 4 -*-
# vim:ts=4:sw=4:et
'''
rpm definitions

$Id$
'''
__revision__ = '$Rev$'[6:-2]

RPM_LEAD_MAGIC_NUMBER = '\xed\xab\xee\xdb'
RPM_HEADER_MAGIC_NUMBER = '\x8e\xad\xe8'

RPMTAG_MIN_NUMBER = 1000
RPMTAG_MAX_NUMBER = 1146

#signature tags
RPMSIGTAG_SIZE     = 1000
RPMSIGTAG_LEMD5_1  = 1001
RPMSIGTAG_PGP      = 1002
RPMSIGTAG_LEMD5_2  = 1003
RPMSIGTAG_MD5      = 1004
RPMSIGTAG_GPG      = 1005
RPMSIGTAG_PGP5     = 1006


MD5_SIZE = 16 #16 bytes long
PGP_SIZE = 152 #152 bytes long


# data types definition
RPM_DATA_TYPE_NULL = 0
RPM_DATA_TYPE_CHAR = 1
RPM_DATA_TYPE_INT8 = 2
RPM_DATA_TYPE_INT16 = 3
RPM_DATA_TYPE_INT32 = 4
RPM_DATA_TYPE_INT64 = 5
RPM_DATA_TYPE_STRING = 6
RPM_DATA_TYPE_BIN = 7
RPM_DATA_TYPE_STRING_ARRAY = 8
RPM_DATA_TYPE_I18NSTRING_TYPE = 9

RPM_DATA_TYPES = (RPM_DATA_TYPE_NULL,
                  RPM_DATA_TYPE_CHAR,
                  RPM_DATA_TYPE_INT8,
                  RPM_DATA_TYPE_INT16,
                  RPM_DATA_TYPE_INT32,
                  RPM_DATA_TYPE_INT64,
                  RPM_DATA_TYPE_STRING,
                  RPM_DATA_TYPE_BIN,
                  RPM_DATA_TYPE_STRING_ARRAY,)

RPMTAG_NAME = 1000
RPMTAG_VERSION = 1001
RPMTAG_RELEASE = 1002
RPMTAG_DESCRIPTION = 1005
RPMTAG_COPYRIGHT = 1014
RPMTAG_URL = 1020
RPMTAG_ARCH = 1022


RPMTAGS = (RPMTAG_NAME,
           RPMTAG_VERSION,
           RPMTAG_RELEASE,
           RPMTAG_DESCRIPTION,
           RPMTAG_COPYRIGHT,
           RPMTAG_URL,
           RPMTAG_ARCH,)
